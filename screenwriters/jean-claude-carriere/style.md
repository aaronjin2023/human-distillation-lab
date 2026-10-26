# Jean-Claude Carrière — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean-Claude Carrière: adaptation as reinvention, a collaborator who disappears into the work, history told through one small room, the unsaid doing the work`
- ZH: 卡里耶尔风格：改编即再造，合作者隐身于作品之中，历史通过一间小屋讲述，未说出口的话在干活。

## (2) 结构：三幕 / 序列 / 节拍

- 结构多为三幕式改编：《锡鼓》以小人物视角写大历史，时间跨度数十年；《情人》以回忆为骨架，闪回即结构；《资产阶级的审慎魅力》以循环晚宴为结构。场次中等，靠小场景写大时代。

## (3) 对话

- 对白克制、精确，人物用短句、停顿、留白交锋；潜台词极重，未说出口的话承担叙事。动作描写细致（房间、物件、眼神），对白与动作互相印证。旁白极少。

## (4) 人物弧光

- 主角多为小人物：鼓手、少女、资产阶级夫妇，弧光是缓慢的领悟；人物在历史中保持尊严，结尾常是未说出口的告别。人物关系以个人与历史的对照为主。

## (5) 类型套路与创新

- 类型：文学改编 / 历史剧。遵守改编的忠实，打破‘改编必缩水’的成见：改编即再造。创新在把大历史写进一间小屋，把合作写成隐身的艺术。

## (6) 该写什么 / 不该写什么

- 该写：改编即再造、小场景写大历史、未说出口的话、合作者的隐身、回忆作骨架。
- 不该写：直白解释历史、煽情收束、类型化改编桥段、全知旁白、大团圆。
- Negative prompt: `No on-the-nose history lesson, no sentimental ending, no adaptation cliché, no omniscient narration, no happy ending`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Jean-Claude Carrière, a man buys oden at a convenience store late at night. He remembers a room from fifty years ago. He says almost nothing. The room does the talking.`
- 中文对照：卡里耶尔风格：一个男人深夜在便利店买关东煮，想起五十年前的一间屋子。他几乎不说话。屋子在替他说话。
- Negative: `No on-the-nose history lesson, no sentimental ending, no adaptation cliché, no omniscient narration, no happy ending`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
