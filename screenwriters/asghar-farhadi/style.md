# Asghar Farhadi — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Asghar Farhadi: no villains, only people with reasons, a small lie that splits a family, moral ambiguity until the last frame, the camera as a witness`
- ZH: 法哈蒂风格：没有坏人，只有人人有理；一个小谎言撕开一个家庭；道德模糊直到最后一格；镜头是证人。

## (2) 结构：三幕 / 序列 / 节拍

- 结构多为三幕式连锁反应：《一次别离》以雇佣纠纷为起点，每幕加一层谎言；《推销员》以暴力事件为中点，前后互为镜像；《英雄》以一个善举为起点，层层反转。场次中等长度，时间跨度数周，闪回极少，靠信息差推进。

## (3) 对话

- 对白日常、克制，人物用争吵、质问、沉默交锋；谎言与真相在同一句对白里并存。动作描写精确（开门、签字、打电话），对白与动作互相印证或互相拆台。旁白不用。

## (4) 人物弧光

- 主角多为中产家庭成员：父亲、教师、丈夫，弧光是道德滑坡而非成长；人物越想做好越陷越深，结尾停在未裁决处。人物关系以家庭与阶级为主，制度在门外。

## (5) 类型套路与创新

- 类型：家庭伦理 / 道德剧。遵守现实主义的因果链，打破‘善恶分明’的套路：无人全错，无人全对。创新在把一个谎言写成多米诺骨牌，每倒一张都露出新的道德面。

## (6) 该写什么 / 不该写什么

- 该写：一个小谎言连锁反应、人人有理的道德模糊、家庭与阶级的对照、信息差推进情节、未裁决的结尾。
- 不该写：脸谱化坏人、直白道德说教、煽情高潮、类型化反转、全知旁白。
- Negative prompt: `No cartoon villain, no direct moralising, no sentimental climax, no plot-twist gimmick, no omniscient narration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Asghar Farhadi, a man buys oden at a convenience store late at night and tells a small lie about why he is out. His wife calls. Each answer adds one more lie. No one is a villain. The ending does not judge.`
- 中文对照：法哈蒂风格：一个男人深夜在便利店买关东煮，撒了一个小谎解释为什么出门。妻子打来电话，每答一句又多一个谎。没有坏人。结尾不作裁决。
- Negative: `No cartoon villain, no direct moralising, no sentimental climax, no plot-twist gimmick, no omniscient narration`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
