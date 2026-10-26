# Julian Corbett — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Corbett: sea power serves policy, command of the sea is relative and local, limited war at sea, fleet in being, blockade and joint operations over decisive battle alone`
- ZH: 科贝特风格：海权服务于政治，制海权是相对而局部的，有限战争，存在舰队，封锁与联合作战重于单一决战。

## (2) 情报与侦察

- 情报来源：敌舰队动向、贸易航线、港口与封锁线情报；核心判断是制海权在何时何地、为哪个政治目标服务。`artifact`

## (3) 地形与机动

- 地形与机动：海洋分战区，制海权可局部、可有时限；存在舰队（fleet in being）牵制敌军而不必决战。`artifact`

## (4) 后勤与补给

- 后勤与补给：封锁线、护航与商船保护是海权的日常工作；补给安全重于决战光环。`artifact`

## (5) 决断与节奏

- 决断与节奏：有限战争可以只打有限目标；不必每战都求歼灭，牵制、封锁、登陆配合陆军同样达成政治目标。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 先定政治目标，再定海上任务
- 把制海权当作相对、局部的状态来经营
- 用存在舰队牵制强敌
- 封锁、护航、登陆配合陆军
- 不该打：
- 把决战当作海战的唯一目的
- 假设制海权一旦夺取就永久有效
- 为决战而决战、不顾政治目标
- 忽视商船与补给线的日常保护
- Negative prompt: `No decisive battle as the sole object, no assumption of permanent command of the sea, no naval action without a political object, no neglect of convoy and blockade`

## (7) 测试提示词示例（现代题材：争议海域多国商船护航筹划）

- Prompt: `In the style of Corbett, plan a modern multinational escort operation for merchant shipping in a contested sea. Command of the sea is local and temporary: protect convoys, keep a fleet in being, serve the political object.`
- 中文对照：科贝特风格：筹划一次现代多国商船护航行动。制海权是局部而暂时的：护航为先，存在舰队牵制，服务政治目标。
- Negative: `No decisive battle as the sole object, no assumption of permanent command of the sea, no naval action without a political object, no neglect of convoy and blockade`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
