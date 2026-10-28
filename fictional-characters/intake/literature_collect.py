#!/usr/bin/env python3
"""Build a small, source-linked literature candidate set from public facts.

This script is deliberately scoped to the literature intake files. It reads
Hawes Publications' index of NYT adult hardcover fiction number-one titles,
then verifies Wikipedia novel pages and keeps attributed CC BY-SA plot/character
sections for downstream research. It does not claim character distillation.
"""
from __future__ import annotations

import html
import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "literature-candidates.jsonl"
INDEX_URL = "https://hawes.com/no1_f_d.htm"
UA = "HumanDistillationLab/0.1 (https://github.com/aaronjin2023/human-distillation-lab)"

# Candidate titles are curated after review. The Hawes page is secondary
# bestseller evidence; each source page is individually checked below.
CANDIDATES = [
    ("the-good-earth", "The Good Earth", "The_Good_Earth"),
    ("the-thin-man", "The Thin Man", "The_Thin_Man"),
    ("gone-with-the-wind", "Gone with the Wind", "Gone_with_the_Wind_(novel)"),
    ("the-grapes-of-wrath", "The Grapes of Wrath", "The_Grapes_of_Wrath"),
    ("the-client", "The Client", "The_Client_(novel)"),
    ("the-exorcist", "The Exorcist", "The_Exorcist_(novel)"),
    ("the-stand", "The Stand", "The_Stand"),
    ("the-lovely-bones", "The Lovely Bones", "The_Lovely_Bones"),
    ("the-da-vinci-code", "The Da Vinci Code", "The_Da_Vinci_Code"),
    ("where-the-crawdads-sing", "Where the Crawdads Sing", "Where_the_Crawdads_Sing"),
]

MONTH_DATE = re.compile(r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}$")
BYLINE = re.compile(r"^by\s+(.+?)\s+\([^)]*\)\s*-?$", re.I)


class TextCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.items: list[str] = []

    def handle_data(self, data: str) -> None:
        data = " ".join(data.split())
        if data:
            self.items.append(data)


class NoQualifyingPage(Exception):
    pass


class SectionCollector(HTMLParser):
    """Collect text under article h2 sections named Plot/Synopsis/Characters."""
    def __init__(self) -> None:
        super().__init__()
        self.in_heading = False
        self.current = ""
        self.capture = False
        self.sections: dict[str, list[str]] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "h2":
            self.in_heading = True
            self.capture = False
            self.current = ""

    def handle_endtag(self, tag: str) -> None:
        if tag == "h2":
            self.in_heading = False
            self.current = re.sub(r'\[?\s*edit\s*\]?', '', self.current, flags=re.I).strip()
            name = self.current.lower()
            self.capture = name in {"plot", "plot summary", "synopsis", "characters", "character list"}
            if self.capture:
                self.sections.setdefault(name, [])

    def handle_data(self, data: str) -> None:
        val = " ".join(data.split())
        if not val:
            return
        if self.in_heading:
            self.current += val + ' '
        elif self.capture:
            self.sections.setdefault(self.current.lower(), []).append(val)


def get(url: str) -> bytes:
    url=urllib.parse.quote(url,safe=":/?#[]@!$&'()*+,;=%")
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        if exc.code in (429, 503):
            retry = exc.headers.get("Retry-After")
            if retry:
                try:
                    wait = max(1, int(retry))
                except ValueError:
                    wait = 60
                time.sleep(wait)
            raise
        raise


def index_records() -> dict[tuple[str, str], tuple[str, str, str]]:
    parser = TextCollector()
    parser.feed(get(INDEX_URL).decode("latin-1", "replace"))
    items = parser.items
    result: dict[tuple[str, str], tuple[str, str, str]] = {}
    for i, value in enumerate(items):
        byline = BYLINE.match(value)
        if not byline or i == 0:
            continue
        title = items[i - 1]
        date = items[i + 1] if i + 1 < len(items) else ""
        if MONTH_DATE.match(date):
            author = byline.group(1).strip()
            result.setdefault((title.casefold(), author.casefold()), (author, date, title))
    return result


def word_count(value: str) -> int:
    return len(re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", value))


def bounded_sections(sections: dict[str, list[str]], maximum: int = 10000) -> tuple[str, bool]:
    has_plot = any(name in {"plot", "plot summary", "synopsis"} for name in sections)
    has_characters = any(name in {"characters", "character list"} for name in sections)
    if has_plot and has_characters:
        plot_budget, character_budget = 6600, 3300
    else:
        plot_budget, character_budget = maximum - 100, maximum - 100
    chunks = []
    for name, parts in sections.items():
        text = " ".join(parts)
        budget = character_budget if name in {"characters", "character list"} else plot_budget
        if len(text) > budget:
            text = text[:budget].rsplit(" ", 1)[0]
        chunks.append(f"## {name.title()}\n{text}")
    combined = "\n\n".join(chunks)
    was_truncated = any(
        len(" ".join(parts)) > (character_budget if name in {"characters", "character list"} else plot_budget)
        for name, parts in sections.items()
    )
    if len(combined) > maximum:
        combined = combined[:maximum].rsplit(" ", 1)[0]
        was_truncated = True
    return combined, was_truncated


def novel_lead_matches(raw: str, author: str = '') -> bool:
    paragraphs=re.findall(r'<p\b[^>]*>(.*?)</p>',raw,re.S)
    leads=[html.unescape(re.sub(r'<[^>]+>',' ',p)) for p in paragraphs if re.search(r'<(?:b|strong)\b',p)]
    intro=' '.join(' '.join(x.split()) for x in leads[:2])[:1200]
    verb=re.search(r'\b(?:is|was)\b',intro,re.I)
    clause=intro[verb.end():].split('.',1)[0][:250] if verb else ''
    match=re.search(r'\b(?:novel|novella|book|film|movie|television|series|collection)\b',clause,re.I)
    if not match or match.group().lower() not in {'novel','novella','book'} or re.match(r'\s+series\b',clause[match.end():],re.I):
        return False
    tokens=re.findall(r'[A-Za-zÀ-ž]+',author)
    return not author or bool(tokens) and tokens[-1].casefold() in intro.casefold()


def verify_wikipedia(title: str, author: str = '') -> tuple[str, int, str, str, str, str, bool]:
    base = title.replace(" ", "_")
    variants = [base]
    if not re.search(r"\((novel|book)\)$", base, re.I):
        variants.extend([base + "_(novel)", base + "_(book)"])
    for slug in dict.fromkeys(variants):
        url = "https://en.wikipedia.org/wiki/" + urllib.parse.quote(slug, safe="()_'")
        try:
            raw = get(url).decode("utf-8", "replace")
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                continue
            raise
        parser = SectionCollector()
        parser.feed(raw)
        full_text = "\n\n".join(f"## {name.title()}\n" + " ".join(parts) for name, parts in parser.sections.items())
        count = word_count(html.unescape(full_text))
        section_text, was_truncated = bounded_sections(parser.sections)
        canon = re.search(r'<link rel="canonical" href="([^"]+)"', raw)
        canonical_url = html.unescape(canon.group(1)) if canon else url
        oldid_match = re.search(r"oldid=(\d+)", html.unescape(raw))
        revision = oldid_match.group(1) if oldid_match else ""
        novel=novel_lead_matches(raw,author)
        if novel and count >= 150:
            page_title = urllib.parse.unquote(slug.replace("_", " "))
            return canonical_url, count, section_text, revision, page_title, "ok", was_truncated
    raise NoQualifyingPage(title)


def main() -> None:
    assert novel_lead_matches('<p><b>X</b> is a novel by Blatty, adapted into a film.</p>','Blatty')
    assert not novel_lead_matches('<p><b>X</b> is a film based on a novel by Blatty.</p>','Blatty')
    assert not novel_lead_matches('<p><b>X</b> is a film. It is based on a novel by Smith.</p>','Smith')
    assert not novel_lead_matches('<p><b>X</b> is a novel by Smith.</p>','Jones')
    assert not novel_lead_matches('<p><b>X</b> is a novel series by Smith.</p>','Smith')
    assert novel_lead_matches('<p><b>X</b> is the twenty-third book in a series written by Child.</p>','Lee Child')
    assert novel_lead_matches('<p><b>X</b> is a children\'s book by White.</p>','White')
    fixture=SectionCollector();fixture.feed('<h2>Plot <span>[edit]</span></h2><p>Evidence</p><h2>References</h2><p>Ignore</p>')
    assert fixture.sections=={'plot':['Evidence']}
    argp = argparse.ArgumentParser()
    argp.add_argument("--expand-limit", type=int, default=0, help="number of additional source pages to process in this batch")
    argp.add_argument("--start", type=int, default=0, help="offset into the selected date range, newest first")
    argp.add_argument("--year-from", type=int, default=1931)
    argp.add_argument("--year-to", type=int, default=2025)
    argp.add_argument("--target-count", type=int, default=0, help="stop once this many verified records exist")
    args = argp.parse_args()
    records = index_records()
    output = []
    misses = []
    jobs: list[tuple[str, str, str, tuple[str, str]]] = []
    if not args.expand_limit:
        for identifier, title, slug in CANDIDATES:
            matches = [(key, fact) for key, fact in records.items() if key[0] == title.casefold()]
            if matches:
                key, fact = matches[0]
                jobs.append((identifier, title, slug, fact[:2]))
            else:
                misses.append(f"not in Hawes index: {title}")
    if args.expand_limit:
        known = {key for key in records if any(key[0] == title.casefold() for _, title, _ in CANDIDATES)}
        extra = [(key, fact) for key, fact in records.items()
                 if key not in known and args.year_from <= int(fact[1][-4:]) <= args.year_to]
        extra.sort(key=lambda item: time.strptime(item[1][1], "%B %d, %Y"), reverse=True)
        spread = extra[args.start:args.start + args.expand_limit]
        for title_key, fact in spread:
            title = fact[2]
            slug = title.replace(" ", "_")
            title_id = re.sub(r"[^a-z0-9]+", "-", title_key[0]).strip("-")
            author_id = re.sub(r"[^a-z0-9]+", "-", fact[0].casefold()).strip("-")
            identifier = f"{title_id}--{author_id}"
            jobs.append((identifier, title, slug, fact[:2]))
    existing = [json.loads(line) for line in OUT.read_text(encoding="utf-8").splitlines() if line.strip()] if OUT.exists() else []
    existing_ids = {row["id"] for row in existing}
    existing_pairs = {(row["title"].casefold(), author.casefold()) for row in existing for author in row.get("authors", [])}
    existing_urls = {row.get("canonical_url", row.get("source_url")) for row in existing}
    for identifier, title, slug, (author, first_no1) in jobs:
        if identifier in existing_ids or (title.casefold(), author.casefold()) in existing_pairs:
            continue
        try:
            source_url, section_words, source_text, revision, source_page_title, is_novel, truncated = verify_wikipedia(title,author)
        except NoQualifyingPage:
            misses.append(f"no qualified single-novel page or <150 plot/character words: {title}")
            continue
        except urllib.error.HTTPError as exc:
            misses.append(f"source HTTP {exc.code}: {title}")
            continue
        if source_url in existing_urls:
            continue
        status = "candidate-verified" if is_novel == "ok" and section_words >= 150 else "needs-review"
        if args.expand_limit and status != "candidate-verified":
            continue
        revision_url = "https://en.wikipedia.org/w/index.php?" + urllib.parse.urlencode({"title": source_page_title.replace(" ", "_"), "oldid": revision}) if revision else source_url
        row = {
            "id": identifier,
            "title": title,
            "authors": [author],
            "medium": "literature",
            "popularity": {
                "basis": "Hawes Publications index records this title as reaching No. 1 on the NYT adult hardcover fiction list.",
                "url": INDEX_URL,
                "note": f"Secondary index; first date shown: {first_no1}. This is U.S. adult hardcover chart evidence, not global unit sales."
            },
            "source_url": source_url,
            "canonical_url": source_url,
            "source_page_title": source_page_title,
            "source_revision": revision,
            "source_revision_url": revision_url,
            "source_license": "Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0), as shown on the Wikipedia article page",
            "source_attribution": f'Wikipedia contributors, "{source_page_title}", {revision_url} (canonical page: {source_url}), accessed 2026-10-28; selected Plot/Characters sections, excerpted and lightly joined for research; share-alike terms apply.',
            "source_excerpt_note": "Plot/Characters sections only; source was not read as a complete novel. Text is capped at 10,000 characters." + (" This extract is truncated at the cap." if truncated else ""),
            "source_text": source_text,
            "status": status,
            "source_form_author_verified": True,
            "source_identity_check_version": 4,
        }
        with OUT.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        existing_ids.add(identifier)
        existing_pairs.add((title.casefold(), author.casefold()))
        existing_urls.add(source_url)
        output.append(row)
        print(f"{identifier}: author={author}; chart_date={first_no1}; plot_character_section_words={section_words}; status={status}")
        if args.expand_limit and args.target_count and len(existing_ids) >= args.target_count:
            print(f"reached target count {args.target_count}")
            break
    for miss in misses:
        print("MISS", miss)
    print(f"processed {len(output)} eligible rows; total output is {sum(1 for line in OUT.read_text(encoding='utf-8').splitlines() if line.strip()) if OUT.exists() else 0}: {OUT}")


if __name__ == "__main__":
    main()
