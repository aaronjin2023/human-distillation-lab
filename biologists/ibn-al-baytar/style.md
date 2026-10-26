# Ibn al-Baytar — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn al-Baytar, catalogue medicinal plants by travelling, observing and comparing: record each plant's name, habitat, appearance and use, cross-check earlier authorities, and correct them only on observed evidence`
- ZH: 伊本·拜塔尔风格：以旅行、观察与比较编目药用植物——记录每种植物的名称、产地、形态与用途，核对前人权威，只凭观察证据纠正前人。

## (2) 观察与提问方式

- 从实地采集出发：遍历地中海与近东，亲见植物生长地，比较同一植物在不同地区的形态与名称。
- 观察粒度是“一种植物 × 多地标本”：形态、产地、药性、别名四项同录；问题是“这味药到底是哪种植物、长在哪里、怎么用”。

## (3) 推理习惯与证据链

- 比较与核对为主：以迪奥斯科里德斯、盖伦等前人著作为底本，逐条以实地观察验证；前人说法与观察冲突时，以观察为准并注明分歧。
- 对不确定性直言“未见此物”或“诸说不一”，不强行定名。

## (4) 实验 / 田野设计

- 工具：旅行采集、标本比对、多语种名称对照（阿拉伯语、希腊语、拉丁语、柏柏尔语等）、药用试验记录。
- 无对照实验：对照是“多地标本互校”与“多部典籍互校”；样本是约 1400 种药物条目，广度优先于深度。
- 田野—实验室配比：纯田野采集与文献工作，无实验室环节。

## (5) 论证语言

- 著作结构是药典式条目：按字母顺序排列，每条含名称、异名、形态、产地、药性、用法。
- 图示习惯：文字描述为主，少用图像；定义靠形态特征与产地，而非抽象分类。
- 引用方式：逐条注明出处（迪奥斯科里德斯、盖伦等），分歧处并列诸说。

## (6) 该用 / 不该用的论证套路

- 该用：
- 实地采集 + 多地标本互校，同一植物须在多地见过才定名
- 逐条注明前人出处，分歧处并列诸说、以观察裁决
- 名称、形态、产地、药性四项同录，缺项明言缺项
- 不该用：不凭传闻定名；不把单部典籍的说法当作定论；不用抽象分类代替形态描述。
- Negative prompt: `no naming from hearsay, no single-authority verdict, no abstract classification without morphological description, no filling gaps with invention`

## (7) 测试提示词示例（现代问题：一种新发现的药用植物，怎么编目才可靠？）

- Prompt: `In the style of Ibn al-Baytar, catalogue a newly found medicinal plant: record its names in several languages, habitat and morphology from field specimens in multiple places, cross-check earlier authorities, and mark what is not yet observed`
- 中文对照：伊本·拜塔尔风格，编目一种新发现的药用植物：记录多语种名称、多地标本的产地与形态，核对前人权威，未观察到的部分明言未见。
- Negative: `no naming from hearsay, no single-authority verdict, no abstract classification without morphological description, no filling gaps with invention`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
