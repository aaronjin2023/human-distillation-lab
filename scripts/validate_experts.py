#!/usr/bin/env python3
"""Check domain entrypoints and new expert packages; preserve legacy content."""

import argparse
import copy
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

from validate_library import check_links, local_path, read_json, require

ROOT = Path(__file__).resolve().parents[1]
FILES = ("SKILL.md", "style.md", "process.md", "technique.md", "language.md",
         "motifs.md", "decisions.md", "conflicts.md", "manifest.json")
NAME_KEYS = ("scientist", "biologist", "geographer", "thinker", "writer", "educator", "person", "jurist", "tax_figure", "name")


def check_expert(data, slug, domain, body):
    require(data.get("id") == slug and data.get("domain") == domain, "Expert identity/domain mismatch")
    require(data.get("kind") == "expert-method" and data.get("status") == "source-grounded-draft",
            "New expert status/kind mismatch")
    if domain == "politics":
        require(isinstance(data.get("living_person"), bool), "Missing political expert living status")
    for key in ("name", "name_zh", "scope", "version", "updated_at", "distillation_method"):
        require(isinstance(data.get(key), str) and data[key].strip(), f"Missing expert field: {key}")
    for key in ("sources", "source_works", "known_gaps"):
        require(isinstance(data.get(key), list) and data[key], f"Missing expert list: {key}")
    require(isinstance(data.get("legacy_refs"), list), "Missing explicit legacy references")
    ids = [s["id"] for s in data["sources"]]
    require(len(ids) == len(set(ids)), "Duplicate expert source ID")
    require(set(re.findall(r"\bS[1-9][0-9]*\b", body)) == set(ids), "Expert source citations disagree")
    for source in data["sources"]:
        for key in ("id", "title", "url", "publisher", "source_type", "accessed_at", "access_note"):
            require(isinstance(source.get(key), str) and source[key].strip(), f"Incomplete source: {key}")
        url = urlsplit(source["url"])
        require(url.scheme in ("http", "https") and url.hostname and not url.username, "Invalid expert source URL")
        require(source.get("supports") and source["url"] in body, f"{slug}/{source['id']}: source support/link missing")
    rights = data.get("rights", {})
    require(rights.get("summary") and rights.get("item_reproduction") == "not-included", "Missing materials scope")
    require(rights.get("source_ids") and set(rights["source_ids"]) <= set(ids), "Invalid rights source reference")


def validate(root, write_catalog=False):
    index = read_json(root / "domains/index.json")
    require(index.get("coverage") == "curated-domain-entrypoints", "Domain coverage must be explicit")
    require({d["id"] for d in index["domains"]} == {"medicine", "history", "education", "politics"}, "Unexpected domains")
    require(len(index["domains"]) == 4, "Duplicate domains")
    counts, added_paths, source_count = {}, set(), 0
    for domain in index["domains"]:
        entries, seen = [], set()
        for category in ("existing_paths", "new_paths"):
            for relative in domain[category]:
                require(relative not in seen, f"Duplicate domain entry: {relative}")
                seen.add(relative)
                folder = local_path(root, relative)
                require(all((folder / f).is_file() and (folder / f).stat().st_size for f in FILES),
                        f"Incomplete nine-file expert package: {relative}")
                data = read_json(folder / "manifest.json")
                if category == "new_paths":
                    require(relative not in added_paths, "New package indexed twice")
                    added_paths.add(relative)
                    body = "\n".join((folder / f).read_text() for f in FILES if f.endswith(".md"))
                    check_expert(data, folder.name, domain["id"], body)
                    for reference in data["legacy_refs"]:
                        require((local_path(root, reference) / "SKILL.md").is_file(), "Missing related legacy expert")
                    skill = (folder / "SKILL.md").read_text()
                    require(skill.startswith(f"---\nname: {folder.name}\n") and "\ndescription: " in skill,
                            "Invalid new expert skill header")
                    source_count += len(data["sources"])
                    name = data["name_zh"]
                    topic = data["source_works"][0]
                else:
                    name = next((data[k + "_zh"] for k in NAME_KEYS if data.get(k + "_zh")), None)
                    require(name, f"Unknown legacy name field: {relative}")
                    topic = data.get("field") or data.get("school") or data.get("genre") or "见原条目"
                entries.append((relative, name, topic, "新增方法草稿" if category == "new_paths" else "复用既有草稿"))
        counts[domain["id"]] = {"existing": len(domain["existing_paths"]), "new": len(domain["new_paths"]), "total": len(entries)}
        content = f"# {domain['name']}专家入口\n\n{domain['baseline']}\n\n{domain['scope']}\n\n"
        content += "[领域总览](README.md) · [机器索引](index.json)\n\n"
        content += "旧条目本轮检查文件完整性并建立入口，没有全面重新核验其引文与效果；新增条目的具体访问范围和缺口见各自manifest。原有分类与专业面向保留。\n\n"
        content += "| 专家 | 状态 | 原条目侧重 / 新条目代表作 |\n|---|---|---|\n"
        for relative, name, topic, status in entries:
            content += f"| [{name}](../{relative}/SKILL.md) | {status} | {str(topic).replace('|', '／')} |\n"
        target = root / "domains" / f"{domain['id']}.md"
        if write_catalog:
            target.write_text(content)
        else:
            require(target.is_file() and target.read_text() == content, f"Stale domain catalog: {target.name}")
    actual = {p.parent.relative_to(root).as_posix() for collection in ("medical-experts", "historians", "politicians")
              for p in (root / collection).glob("*/manifest.json")}
    require(actual == added_paths, "New expert packages and index disagree")
    files = list((root / "domains").glob("*.md"))
    for relative in added_paths:
        files.extend((root / relative).glob("*.md"))
    return {"domains": counts, "new_experts": len(added_paths), "new_source_records": source_count,
            "local_links": check_links(root, files), "status": "passed"}


def self_test():
    folder = ROOT / "medical-experts/david-sackett"
    original = read_json(folder / "manifest.json")
    body = "\n".join((folder / f).read_text() for f in FILES if f.endswith(".md"))
    check_expert(original, folder.name, "medicine", body)
    for mutation in (lambda x: x["sources"].append(x["sources"][0]),
                     lambda x: x["rights"].update(source_ids=["S999"]),
                     lambda x: x["sources"][0].update(url="javascript:invalid"),
                     lambda x: x["sources"][0].pop("access_note"),
                     lambda x: x.update(domain="history")):
        invalid = copy.deepcopy(original)
        mutation(invalid)
        try:
            check_expert(invalid, folder.name, "medicine", body)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid expert metadata accepted")
    print("Expert self-test passed: duplicate sources, rights, unsafe URLs, access coverage and domain mismatch")
    political = copy.deepcopy(original)
    political.update(domain="politics", living_person=False)
    check_expert(political, folder.name, "politics", body)
    for missing_status in (None, "false", 0):
        political["living_person"] = missing_status
        try:
            check_expert(political, folder.name, "politics", body)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid political expert living status accepted")
    print("Political expert self-test passed: living status requires a boolean")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-catalog", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        print(json.dumps(validate(ROOT, args.write_catalog), ensure_ascii=False, indent=2))
