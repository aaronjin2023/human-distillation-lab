# Guillermo del Toro — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guillermo del Toro: a fairy tale with teeth, monsters kinder than men, a child who sees what adults cannot, Catholic imagery in a workshop of wonders`
- ZH: 德尔·托罗风格：长着牙齿的童话，怪物比人善良，孩子看见大人看不见的东西，天主教意象藏在奇观工坊里。

## (2) 结构：三幕 / 序列 / 节拍

- 结构多为双线并行童话：《潘神的迷宫》现实线与幻想线交织，任务三段式；《水形物语》以爱情为骨架，类型翻转在中段；《匹诺曹》以木偶的旅程为结构。场次中等，靠童话任务推进。

## (3) 对话

- 对白诗化、直白，人物用童话语言与日常口语交锋；潜台词少，怪物与孩子直接说出真相。动作描写细致（怪物、机关、仪式），对白与动作互相印证。旁白在《潘神的迷宫》中是结构的一部分。

## (4) 人物弧光

- 主角多为孩子与边缘人：奥菲莉娅、哑女清洁工、木偶，弧光是勇气而非成长；人物在结尾处付出代价，童话不保证幸福。人物关系以怪物与孩子的对照为主。

## (5) 类型套路与创新

- 类型：奇幻 / 童话 / 恐怖。遵守童话的任务结构，打破‘童话必有幸福结局’的套路：童话长着牙齿。创新在把怪物写成道德中心，把天主教意象写进奇观。

## (6) 该写什么 / 不该写什么

- 该写：童话作任务结构、怪物比人善良、孩子看见真相、双线并行、天主教意象。
- 不该写：脸谱化怪物、直白说教、类型化惊吓桥段、大团圆、无代价的胜利。
- Negative prompt: `No cartoon monster, no direct preaching, no horror cliché, no happy ending, no cost-free victory`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Guillermo del Toro, a small Yorkshire terrier sits on a subway seat. A girl sees the dog is really a small guardian with clockwork inside. The adults see only a pet. The fairy tale has teeth.`
- 中文对照：德尔·托罗风格：一只约克夏犬坐在地铁座位上。一个女孩看出狗其实是一只体内有发条的小守护者。大人只看见一只宠物。童话长着牙齿。
- Negative: `No cartoon monster, no direct preaching, no horror cliché, no happy ending, no cost-free victory`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
