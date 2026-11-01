#!/usr/bin/env python3
"""Static regressions for the six legacy audit repairs, not semantic or model-effect validation."""

import argparse
import json
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
K = "landscape-designers/kobori-enshu"
L = "geologists/inge-lehmann"
N = "materials-scientists/konstantin-novoselov"
Q = "writers/li-qingzhao"
W = "managers/karl-weick"
Y = "calligraphers/ni-yuanlu"
PACKAGES = (K, L, N, Q, W, Y)
FILES = ("SKILL.md", "process.md", "style.md", "technique.md", "language.md",
         "motifs.md", "decisions.md", "conflicts.md", "manifest.json")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check(root):
    def read(package, name):
        return (root / package / name).read_text(encoding="utf-8")

    for package in PACKAGES:
        require("[基本资料](biography.md)" in read(package, "SKILL.md"),
                f"{package}: biography entrypoint missing")
    manifests = {package: json.loads(read(package, "manifest.json")) for package in PACKAGES}
    require("枯山水靠每日" not in read(K, "process.md"), "Kobori: dry-garden template returned")
    require("编者迁移练习" in read(K, "process.md"), "Kobori: migration boundary missing")
    for term in ("野外记录本、剖面图、标本清单", "鉴定结果、年龄数据", "古地理复原", "地质锤", "野外考察结束"):
        require(term not in read(L, "process.md"), f"Lehmann: unrelated template returned: {term}")
    for term in ("按人物习惯", "电镜一缺", "病毒模板/VLS", "器件集成/专利/标准"):
        require(term not in read(N, "process.md"), f"Novoselov: unrelated requirement returned: {term}")
    for name in FILES[:-2]:
        require("《夏日绝句》" in read(Q, name), f"Li Qingzhao: branch missing in {name}")
    require("不得禁止议论" in read(Q, "style.md"), "Li Qingzhao: argumentative branch blocked")
    samples = manifests[W]["language_samples"]
    require(samples and all(sample["level"] == "artifact" for sample in samples),
            "Weick: unverified samples must remain artifact summaries")
    require("`verbatim`" not in read(W, "technique.md"), "Weick: unverified direct quotation returned")
    for name in FILES[:-1]:
        body = read(Y, name)
        require("来源不足" in body and "不能作为倪元璐本人风格预设" in body,
                f"Ni Yuanlu: source gate missing in {name}")
    require("In the style of Ni Yuanlu" not in read(Y, "style.md"), "Ni Yuanlu: unsupported author prompt returned")
    works = manifests[Y]["source_works"]
    require(works and all("不得作为蒸馏源" in work["transmission"] for work in works),
            "Ni Yuanlu: generic titles accepted as usable sources")


def self_test():
    # Copy only the nine inputs per assigned package; never mutate the source library.
    with tempfile.TemporaryDirectory() as directory:
        fixture = Path(directory)
        for package in PACKAGES:
            target = fixture / package
            target.mkdir(parents=True)
            for name in FILES:
                shutil.copyfile(ROOT / package / name, target / name)
        check(fixture)
        mutations = (
            (W, "manifest.json", '"level": "artifact"', '"level": "verbatim"', "Weick:"),
            (Q, "style.md", "不得禁止议论", "必须禁止议论", "Li Qingzhao:"),
            (Y, "style.md", "不能作为倪元璐本人风格预设", "可作为倪元璐本人风格预设", "Ni Yuanlu:"),
        )
        for package, name, old, new, expected in mutations:
            path = fixture / package / name
            original = path.read_text(encoding="utf-8")
            require(old in original, f"Mutation target missing: {package}/{name}")
            try:
                path.write_text(original.replace(old, new, 1), encoding="utf-8")
                try:
                    check(fixture)
                except ValueError as error:
                    require(str(error).startswith(expected), f"Unexpected rejection: {error}")
                else:
                    raise AssertionError(f"Audit regression accepted: {package}/{name}")
            finally:
                path.write_text(original, encoding="utf-8")
        check(fixture)
    print("PASS: 3 injected regressions rejected; source packages untouched. Static checks only.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        check(ROOT)
        print("PASS: 6 packages; process, branch, evidence and source gates present. Static checks only.")
