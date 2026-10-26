# Gan De — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gan De, watch one planet night after night until its rhythm shows: record Jupiter's place against the lodges, measure its return, and note the small red star beside it without claiming more than you saw`
- ZH: 甘德风格：夜复一夜盯住一颗行星、直到它的节律显现：记下木星在星宿间的位置、测出它的重现，看到它身旁的小赤星就记下来，不多宣称。

## (2) 观测方法

仪器为肉眼；观测策略是长期定点观测：以二十八宿为坐标，记录木星等行星的位置与会合周期。观测的极限是肉眼，但持续时间长。`artifact`

## (3) 推演与模型建构

推演是周期测定：从行星位置的长期记录中测出会合周期（木星约 400 天一说，待核对）；木星旁“小赤星”的记录被后世认为可能是木卫（木卫三）的最早肉眼记录，但存疑。链条：记录 → 周期 → 预报。`artifact`

## (4) 证据链

证据链薄弱：著作已佚，仅存后人引文；行星会合周期的数值见于引文；木卫记录一说存疑——肉眼能否看到木卫三，现代学者有争议。本次蒸馏只记录“存疑”，不作定论。`impression`

## (5) 理论语言与论证结构

语言为记录体：星宿位置、行星会合、现象描述。论证靠记录的对照，不靠理论。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 行星位置的长期记录
- 行星会合周期的测定
- 木星旁小赤星的如实记录
- 不该研究：
- 不把木卫记录写成定论
- 不把已佚著作的内容写成亲见
- 不凭引文断言精确数值
- Negative prompt: `no moon sighting presented as certain, no lost text presented as seen, no precise value claimed from quotations alone`

## (7) 测试提示词示例（现代题材：用甘德的方法，长期跟踪一颗现代行星，测定它的会合周期）

- Prompt: `In the style of Gan De, track a modern planet night after night: record its place against fixed stars, measure its synodic period from the records, note anything unusual beside it, and mark clearly what is seen and what is only guessed`
- 中文对照：甘德风格，长期跟踪一颗现代行星：记下它在恒星间的位置、从记录中测出会合周期、记下它身旁的任何异常，并标明什么是看到的、什么只是猜测。
- Negative: `no moon sighting presented as certain, no lost text presented as seen, no precise value claimed from quotations alone`
- 检验点：回答是否按该天文学家的方法走（观测 → 记录 → 推算 → 验证 → 成书）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
