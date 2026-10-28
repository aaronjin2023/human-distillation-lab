**One confirmed P2 delivery defect; no P0/P1 blocker found in this bounded audit.**

1. **P2 — Export silently drops evidence supporting retained `tensions` claims.**
   [build_characters.py:136](/Users/aaron/codex_workspace/skills/references/human-distillation-lab/scripts/build_characters.py:136) collects evidence only from traits, while line 164 exports tension statements unchanged. Validation checks trait references only.

   Reproduction: *The Goldfinch*, `profile-989e39367c0b0078`, retains “已与基特西订婚，仍持续迷恋皮帕并感到困惑” in [the delivered card, line 25](/Users/aaron/codex_workspace/skills/references/human-distillation-lab/fictional-characters/works/the-goldfinch--donna-tartt.md:25). Its supporting sentence is **S24** in `batches/literature/0013.input.json`, work `the-goldfinch--donna-tartt`. S24 is absent from both the card and `evidence.jsonl`, record 206. The delivered package therefore loses the evidence for a retained psychological claim, despite passing validation. Preserve support for these statements or omit unsupported export fields; frozen source packets need no change.

**Observed snapshot:** October 28, 2026, 16:27–16:32 JST: **720 works — 343 novels and 377 films; 1,645 profiles; 1,365 identities; 7,412 trait claims.** Receipt remained unchanged, all seven root-file hashes matched, and `complete=false`. Counts below 1,000 are not a finding.

Checked:

- **Admission:** inspected v4 identity logic, popularity qualifications, deduplication and series gates. Local film-versus-novel regression passed. Latest v4 audit contained 475 passes/35 failures; legacy series audit contained 55 passes/six failures. No failed gate record appeared in the export. No demonstrably wrong admission or duplicate work was identified.
- **Identity:** inspected merge/separation decisions and automatic linking. No duplicate merge keys or identity containing multiple profiles from the same work were found. Sampled adaptations retain separate profiles; historical depictions explicitly exclude real-person psychological assessment. CMU intake uses column 12, zero-index 11.
- **Flow:** both self-tests and export validation passed. All exported evidence text matched its frozen numbered source; source hashes matched the preparation normalization. Two sampled patch-review replays exactly reproduced outputs. Staged export and last-written receipt were assessed without assuming directory-wide atomicity.
- **Evidence:** compared **12 profiles, 61 trait claims and 14 tension statements** with source support: 陈阵; 宋江、吳用; 甄嬛、玄凌; Theodore Decker、Boris Pavlikovsky; Harry Potter in two novels and one film; Oskar Schindler; and Cao Cao in *Red Cliff*. Inspected the relevant Chinese section boundaries. No additional material contradiction or direct-statement/interpretation error was demonstrated.

No files changed, external services invoked, agents spawned, extraction jobs run, or publication performed.
This was a sample audit, not review of all eventual 1,000 works; upstream synopsis accuracy and subsequent batches remain unverified.
