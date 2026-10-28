#!/usr/bin/env python3
"""Validate the new framework/reference layer; leave legacy expert files untouched."""

import argparse
import copy
import json
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
KINDS = {
    "trait-model", "trait-instrument", "item-bank", "type-framework",
    "behavior-framework", "strengths-framework", "values-framework",
    "interest-framework", "relationship-framework", "motivation-framework",
    "cognition-framework", "emotion-framework", "social-framework", "learning-framework",
    "culture-framework", "development-framework", "population-framework",
    "functioning-framework", "biological-rhythm-framework",
}
COLLECTIONS = ("personalities", "human-patterns")
DOMAINS = {"behavior", "cognition", "emotion-motivation", "social", "culture",
           "development", "population", "embodiment"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def local_path(root, value):
    require(isinstance(value, str) and value and not Path(value).is_absolute(),
            f"Expected relative path: {value}")
    path = (root / value).resolve()
    require(path.is_relative_to(root.resolve()) and path.exists(), f"Bad local reference: {value}")
    return path


def check_manifest(data, folder, body, extended=False):
    for key in ("id", "name", "version", "updated_at", "scope", "distillation_method"):
        require(isinstance(data.get(key), str) and data[key].strip(), f"{folder}: missing {key}")
    require(data["id"] == folder and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", folder),
            f"{folder}: invalid ID")
    require(data.get("kind") in KINDS, f"{folder}: unknown category")
    require(data.get("status") == "source-grounded-draft", f"{folder}: unsupported status")
    if extended:
        require(data.get("domain") in DOMAINS, f"{folder}: missing/unknown domain")
        require(data.get("analysis_level") in {"individual", "group", "multilevel"},
                f"{folder}: missing/unknown analysis level")
        for key in ("evidence_summary", "population_scope"):
            require(isinstance(data.get(key), str) and data[key].strip(), f"{folder}: missing {key}")
        require(all(s.get("access_note") for s in data.get("sources", [])),
                f"{folder}: source access coverage missing")
    for key in ("dimensions", "sources", "known_gaps"):
        require(isinstance(data.get(key), list) and data[key], f"{folder}: missing {key}")
    for collection, keys in (("dimensions", ("id", "name", "description")),
                             ("sources", ("id", "title", "url", "publisher", "source_type", "accessed_at"))):
        ids = []
        for row in data[collection]:
            require(all(isinstance(row.get(k), str) and row[k].strip() for k in keys),
                    f"{folder}: incomplete {collection} record")
            ids.append(row["id"])
        require(len(ids) == len(set(ids)), f"{folder}: duplicate {collection} IDs")
    source_ids = {source["id"] for source in data["sources"]}
    for source in data["sources"]:
        url = urlsplit(source["url"])
        require(url.scheme in ("http", "https") and url.hostname and not url.username,
                f"{folder}: invalid source URL")
        require(source.get("supports"), f"{folder}: source lacks supported claims")
        require(source["url"] in body, f"{folder}: source missing from framework text: {source['id']}")
    require(set(re.findall(r"\bS[1-9][0-9]*\b", body)) == source_ids,
            f"{folder}: body/manifest source IDs disagree")
    rights = data.get("rights", {})
    require(rights.get("summary") and rights.get("item_reproduction") == "not-included",
            f"{folder}: incomplete materials declaration")
    require(rights.get("source_ids") and set(rights["source_ids"]) <= source_ids,
            f"{folder}: rights refer to unknown sources")


def check_links(root, files):
    count = 0
    for file in files:
        for target in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
            target = target.strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            path = file.parent / unquote(target.split("#")[0])
            require(path.resolve().is_relative_to(root) and path.exists(),
                    f"{file.relative_to(root)}: broken or escaping link {target}")
            count += 1
    return count


def validate(root, write_catalog=False):
    folders = []
    for collection in COLLECTIONS:
        members = sorted(p for p in (root / collection / "frameworks").iterdir() if p.is_dir())
        require(members, f"No framework entries: {collection}")
        folders.extend(members)
    records = []
    source_count = 0
    for folder in folders:
        for name in ("SKILL.md", "framework.md", "manifest.json"):
            require((folder / name).is_file(), f"{folder.name}: missing {name}")
        data = read_json(folder / "manifest.json")
        extended = folder.parent.parent.name == "human-patterns"
        check_manifest(data, folder.name, (folder / "framework.md").read_text(encoding="utf-8"), extended)
        skill = (folder / "SKILL.md").read_text(encoding="utf-8")
        require(skill.startswith(f"---\nname: {folder.name}\n") and "\ndescription: " in skill,
                f"{folder.name}: skill header mismatch")
        require(len(skill.splitlines()) < 100, f"{folder.name}: skill entrypoint too long")
        source_count += len(data["sources"])
        records.append({"id": data["id"], "name": data["name"], "kind": data["kind"],
                        "path": str(folder.relative_to(root)), "version": data["version"],
                        "dimension_count": len(data["dimensions"]), "source_count": len(data["sources"])})
        if extended:
            records[-1].update(domain=data["domain"], analysis_level=data["analysis_level"])
    ids = {row["id"] for row in records}
    require(len(ids) == len(records), "Framework IDs must be unique across collections")
    people = read_json(root / "people/index.json")
    require(people["coverage"] == "reviewed-links-only", "Identity coverage must be explicit")
    person_ids, expert_paths = set(), set()
    for person in people["people"]:
        require(person["person_id"] not in person_ids, "Duplicate person ID")
        person_ids.add(person["person_id"])
        for reference in person["expert_paths"]:
            require(reference not in expert_paths, "One expert path linked to multiple identities")
            expert_paths.add(reference)
            require((local_path(root, reference) / "SKILL.md").is_file(), "Missing expert skill")
        for reference in person["personality_paths"]:
            local_path(root, reference)
    profiles = list((root / "profiles").glob("*/manifest.json"))
    for path in profiles:
        profile = read_json(path)
        require(profile["id"] == path.parent.name and profile["kind"] == "synthetic-role", "Invalid profile")
        require(set(profile["framework_refs"]) <= ids, "Profile references unknown framework")
        require(profile["measured_personality"] is None, "Synthetic example must not claim test results")
        for reference in profile["expert_refs"]:
            require((local_path(root, reference["path"]) / "SKILL.md").is_file(), "Missing expert skill")
    personality_records = [r for r in records if r["path"].startswith("personalities/")]
    human_records = [r for r in records if r["path"].startswith("human-patterns/")]
    catalog = {"schema_version": 1, "framework_count": len(personality_records), "frameworks": personality_records}
    overview = "# 人格与个体差异框架目录\n\n"
    overview += "当前收录 %d 个框架/工具。均为有来源的初稿，按问题选用；不代表等同的科学证据、授权或测量结果。\n\n" % len(personality_records)
    overview += "[选用与证据规则](README.md) · [组合示例](../profiles/research-collaborator/SKILL.md)\n\n"
    overview += "| 框架 | 类别 | 维度数 | 来源数 |\n|---|---|---:|---:|\n"
    for row in personality_records:
        overview += f"| [{row['name']}](frameworks/{row['id']}/SKILL.md) | {row['kind']} | {row['dimension_count']} | {row['source_count']} |\n"
    overview += "\n维度数依工具粒度而异，不能用于比较优劣。IPIP 的五项只是大五量表示例；EPQ 的四项含效度相关的 L 量表。具体细分项和限制以条目为准。\n"
    outputs = {root / "personalities/catalog.json": json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
               root / "personalities/CATALOG.md": overview}
    human_catalog = {"schema_version": 1, "framework_count": len(human_records), "frameworks": human_records}
    human_overview = "# 人类行为与差异框架目录\n\n"
    human_overview += f"当前收录 {len(human_records)} 个框架。均为有来源的概念初稿；构件不是统一量表，也不构成人类全部层面的穷尽分类。\n\n"
    human_overview += "[本区说明](README.md) · [跨层组合指南](../docs/composition-guide.md) · [人格区](../personalities/CATALOG.md)\n\n"
    human_overview += "| 框架 | 领域 | 分析层级 | 构件数 | 来源数 |\n|---|---|---|---:|---:|\n"
    for row in sorted(human_records, key=lambda r: (r["domain"], r["id"])):
        human_overview += f"| [{row['name']}](frameworks/{row['id']}/SKILL.md) | {row['domain']} | {row['analysis_level']} | {row['dimension_count']} | {row['source_count']} |\n"
    human_overview += "\nindividual：个人过程；group：群体比较；multilevel：多个层级。群体结论不能直接变为个人属性；来源数不代表证据强弱。实际访问范围和局限见各条元数据。\n"
    outputs[root / "human-patterns/catalog.json"] = json.dumps(human_catalog, ensure_ascii=False, indent=2) + "\n"
    outputs[root / "human-patterns/CATALOG.md"] = human_overview
    for path, expected in outputs.items():
        if write_catalog:
            path.write_text(expected, encoding="utf-8")
        else:
            require(path.is_file() and path.read_text(encoding="utf-8") == expected,
                    f"Stale catalog: {path.name}; run --write-catalog")
    files = [root / "README.md"]
    for directory in (*COLLECTIONS, "profiles", "docs"):
        files.extend((root / directory).rglob("*.md"))
    links = check_links(root, files)
    return {"frameworks": len(records), "collections": {"personalities": len(personality_records), "human-patterns": len(human_records)},
            "source_records": source_count, "reviewed_people": len(person_ids),
            "profiles": len(profiles), "local_links": links, "status": "passed"}


def self_test():
    folder = next((ROOT / "personalities/frameworks").glob("*/manifest.json"))
    original = read_json(folder)
    body = (folder.parent / "framework.md").read_text(encoding="utf-8")
    check_manifest(original, folder.parent.name, body)
    mutations = [lambda x: x["sources"].append(x["sources"][0]),
                 lambda x: x["rights"].update(source_ids=["MISSING"]),
                 lambda x: x.update(dimensions=[])]
    for mutation in mutations:
        invalid = copy.deepcopy(original)
        mutation(invalid)
        try:
            check_manifest(invalid, folder.parent.name, body)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid manifest was accepted")
    try:
        check_manifest(original, folder.parent.name, body + "\nUnsupported citation S999")
    except ValueError:
        pass
    else:
        raise AssertionError("Missing source was accepted")
    extended_path = ROOT / "human-patterns/frameworks/cultural-dimensions"
    extended = read_json(extended_path / "manifest.json")
    extended_body = (extended_path / "framework.md").read_text(encoding="utf-8")
    check_manifest(extended, extended_path.name, extended_body, True)
    for mutation in (lambda x: x.pop("analysis_level"), lambda x: x.update(domain="unknown"),
                     lambda x: x.update(evidence_summary=""), lambda x: x["sources"][0].pop("access_note")):
        invalid = copy.deepcopy(extended)
        mutation(invalid)
        try:
            check_manifest(invalid, extended_path.name, extended_body, True)
        except ValueError:
            pass
        else:
            raise AssertionError("Incomplete human-pattern manifest accepted")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "valid").touch()
        assert local_path(root, "valid") == (root / "valid").resolve()
        for value in ("../", "/etc/passwd", "missing"):
            try:
                local_path(root, value)
            except ValueError:
                pass
            else:
                raise AssertionError("Invalid reference accepted")
    with tempfile.TemporaryDirectory() as directory:
        fixture = Path(directory).resolve()
        for collection, source in (("personalities", folder.parent), ("human-patterns", extended_path)):
            shutil.copytree(source, fixture / collection / "frameworks" / source.name)
            (fixture / collection / "README.md").write_text("")
        (fixture / "README.md").write_text("")
        (fixture / "docs").mkdir()
        (fixture / "docs/composition-guide.md").write_text("")
        (fixture / "people").mkdir()
        (fixture / "people/index.json").write_text(json.dumps({"coverage": "reviewed-links-only", "people": []}))
        profile_dir = fixture / "profiles/research-collaborator"
        profile_dir.mkdir(parents=True)
        (profile_dir / "SKILL.md").write_text("")
        profile = {"id": "research-collaborator", "kind": "synthetic-role", "expert_refs": [],
                   "framework_refs": [folder.parent.name, extended_path.name], "measured_personality": None}
        profile_file = profile_dir / "manifest.json"
        profile_file.write_text(json.dumps(profile))
        assert validate(fixture, True)["frameworks"] == 2
        profile["framework_refs"].append("missing-framework")
        profile_file.write_text(json.dumps(profile))
        try:
            validate(fixture)
        except ValueError as error:
            assert "unknown framework" in str(error)
        else:
            raise AssertionError("Dangling cross-collection reference accepted")
        duplicate = fixture / "human-patterns/frameworks" / folder.parent.name
        shutil.copytree(fixture / "human-patterns/frameworks" / extended_path.name, duplicate)
        data = read_json(duplicate / "manifest.json")
        data["id"] = folder.parent.name
        (duplicate / "manifest.json").write_text(json.dumps(data))
        skill_path = duplicate / "SKILL.md"
        skill_path.write_text(skill_path.read_text().replace(f"name: {extended_path.name}", f"name: {folder.parent.name}"))
        try:
            validate(fixture)
        except ValueError as error:
            assert "unique across collections" in str(error)
        else:
            raise AssertionError("Ambiguous framework ID accepted")
    print("Self-test passed: source integrity, metadata, path boundaries, cross-collection composition, missing references and duplicate IDs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-catalog", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        print(json.dumps(validate(ROOT, args.write_catalog), ensure_ascii=False, indent=2))
