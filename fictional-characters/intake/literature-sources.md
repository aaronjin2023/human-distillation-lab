# Literature candidate source and access notes

Access date: 2026-10-28. Collections include `literature-candidates.jsonl` (NYT-index candidates), `global-literature-candidates.jsonl`, `series-literature-candidates.jsonl`, `chinese-literature-candidates.jsonl`, and corrected novel sources. Each row is a candidate source bundle, not a completed character analysis. Tail groups reuse frozen candidates rather than introduce new source criteria.

## Popularity evidence

The list source is the [Hawes Publications NYT Adult Hardcover Fiction Number Ones Listing](https://hawes.com/no1_f_d.htm). The page describes itself as listing adult fiction books that reached number one on the New York Times Best Seller List and the date each first reached number one. It is a secondary index, not an official NYT page or unit-sales dataset. The page states “Copyright (c) Hawes Publications. All rights reserved.” The intake reuses only factual title, author, and first-listed date fields; it does not copy Hawes prose or page markup. The evidence is limited to the U.S. adult hardcover fiction chart and does not represent global bestseller status or all popular literature.

## Plot and character source material

For each included candidate, the script visited the linked English Wikipedia novel page and extracted only headings labelled Plot, Plot summary, Synopsis, Characters, or Character list. A candidate is included only when the lead identifies it as a novel and the selected material contains at least 150 English words. The classifier is a conservative text heuristic; the source page and excerpt still require human review for edge cases. The script tries the exact title first, then `(novel)` and `(book)` variants after a missing or insufficient page. It makes one request at a time with a descriptive User-Agent; a 429/503 `Retry-After` value is honored.

Wikipedia text is attributed per row with the page title, canonical URL, revision number, revision URL, access date, and CC BY-SA 4.0 license notice. Excerpts are lightly reflowed, capped at 10,000 characters, and keep plot and character sections when both are available. The corresponding license is included in every row; reusers must preserve attribution and comply with ShareAlike terms. `source_text` contains the selected excerpt for downstream analysis. It is not a full article, and no original novel was read in this collection step.

Official API access guidance consulted: [MediaWiki API Etiquette](https://www.mediawiki.org/wiki/API:Etiquette) and [Wikimedia APIs rate limits](https://www.mediawiki.org/wiki/Wikimedia_APIs/Rate_limits). The collection uses no paid service, login, private conversation, or publisher marketing copy.

## Coverage limits

The NYT-index part is a U.S.-market English-language chart sample selected for accessible public plot/character text. It underrepresents Chinese-language publishing and other national markets; it also omits books that were popular without reaching number one on the selected chart. Chinese-market candidates use separate public circulation, ranking or sales evidence documented in their own source records.

## Global books and series

The [List of best-selling books](https://en.wikipedia.org/wiki/List_of_best-selling_books) supplies secondary, source-cited historical sales estimates. Standalone works retain the table's estimate and qualifiers. For series, the estimate belongs to the entire series: it is not a sales figure for each volume. The series article's bibliography identifies individual candidates; each novel page must identify a novel/book, its author, the relevant series, and sufficient narrative material. The infobox Series field must match. Legacy candidates collected before that requirement were rechecked in `verification/series-membership-checks.jsonl`: 55 of 61 passed; six unrelated series/standalone works were excluded. Individual novel and adaptation records remain separate. Historical series estimates are not updated sales claims and do not imply that later volumes contributed to an earlier estimate.

## Source identity verification

The version 4 check uses the page lead's first type assertion and the expected author, rather than accepting any later mention of a novel. This rejects a film page that merely says it is based on a novel, and same-title books by a different author. Previously collected NYT/global pages are rechecked in `verification/literature-source-checks.jsonl`; failed or pending identities never enter the final library. New series and corrected-page records retain the equivalent check version and lead evidence. This is a text heuristic with retained source evidence, not a claim of bibliographic expert certification.

The source excerpts support later review of fictional roles and their narrative behavior; they do not establish that a fictional character is a coherent real-world personality profile. The records are marked `candidate-verified` only for chart-index presence, a novel-identifying page lead, and the text-length threshold.
