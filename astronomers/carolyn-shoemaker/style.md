# Carolyn Shoemaker — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carolyn Shoemaker, scan Schmidt plates night after night through a stereoscope, trust a trained eye over a quick look, and let the count of discoveries be the record of the method`
- ZH: 卡罗琳·舒梅克风格：夜复一夜用体视镜扫施密特底片，相信训练有素的眼睛胜过匆匆一瞥，让发现的数量本身成为方法的记录。

## (2) 观测方法

以帕洛玛 18 英寸施密特相机底片扫查为主：每夜拍摄多张底片，用体视镜（stereoscope）成对比较，靠人眼识别移动的彗星与小行星。巡天持续十余年，底片量以千计；发现靠系统扫查，不靠偶然。`artifact`

## (3) 推演与模型建构

目视识别 + 轨道确认：底片上移动的弥散像先判为彗星候选，点状移动像判为小行星候选，再由后续观测定轨确认。模型是开普勒轨道拟合，边界是短弧段定轨需后续跟踪。`artifact`

## (4) 证据链

证据链：底片对 → 体视镜识别 → 后续观测复现 → 定轨编号。决定性证据是 1993 年 3 月底片上 SL9 的一串彗核碎片像。反证处理：把底片缺陷、已知天体、恒星像逐一排除，候选清单逐项复核。`artifact`

## (5) 理论语言与论证结构

巡天日志体的论证语言：论文与报告以发现清单、底片编号与复核记录为核心；术语偏好：底片、体视镜、候选体、复核。开头从巡天计划出发，结尾给出发现清单与待跟踪目标。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 施密特底片的系统体视镜扫查
- 彗星与小行星候选的逐一复核
- 发现清单与后续跟踪的完整记录
- 不该研究：
- 凭单张底片的亮点宣称彗星
- 跳过复核直接上报候选
- 把巡天发现写成偶然所得
- Negative prompt: `no claiming a comet from one plate, no reporting a candidate without rechecking, no presenting survey discoveries as luck`

## (7) 测试提示词示例（现代题材：怎样系统巡天才能稳定发现近地小行星？）

- Prompt: `In the style of Carolyn Shoemaker, design a plate-scanning survey for near-Earth asteroids: set a nightly plate plan, scan each pair through a stereoscope, and recheck every moving candidate before reporting it`
- 中文对照：用卡罗琳·舒梅克的方法设计近地小行星底片巡天：定每夜拍摄计划，用体视镜逐对扫查，每个移动候选都复核后才上报。
- Negative: `no claiming a comet from one plate, no reporting a candidate without rechecking, no presenting survey discoveries as luck`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
