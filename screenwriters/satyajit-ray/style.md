# Satyajit Ray — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Satyajit Ray: humanist observation, ordinary lives in long unhurried scenes, literary adaptation made cinematic, music as inner voice, dignity without melodrama`
- ZH: 雷伊风格：人道主义的凝视，漫长从容的日常场景，文学改编写成电影，音乐即内心，尊严而不煽情。

## (2) 结构：三幕 / 序列 / 节拍

- 结构多为生活流三幕或多段式：《大地之歌》以季节与生死为节拍；《音乐室》以一场音乐会倒叙一生；《大树之根》以家庭聚会为容器，多线并行。场次长、切换缓，时间跨度数年，闪回温和，不靠反转推进。

## (3) 对话

- 对白简洁、口语化，孟加拉日常语气；人物用闲聊、歌唱、沉默交流，情绪藏在礼节之下。动作描写细致（手势、眼神、屋内陈设），对白与动作比例均衡。旁白极少，音乐承担内心。

## (4) 人物弧光

- 主角多为普通人：乡村男孩、没落贵族、大家庭的儿子，弧光是缓慢的领悟而非剧变；人物在结尾处获得尊严或接受失去，世界照常运转。人物关系以家庭与传统为主。

## (5) 类型套路与创新

- 类型：人文剧情 / 文学改编。遵守现实主义的耐心，打破‘情节驱动’的套路：大事写小，小事写深。创新在把印度古典音乐与日常生活写进同一场戏。

## (6) 该写什么 / 不该写什么

- 该写：日常生活流、文学改编的电影化、音乐即内心、家庭与传统的对照、尊严而不煽情。
- 不该写：煽情高潮、直白说教、类型化反转、夸张表演式对白、猎奇化的异国情调。
- Negative prompt: `No sentimental climax, no direct preaching, no plot-twist gimmick, no theatrical dialogue, no exotic spectacle`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Satyajit Ray, a small Yorkshire terrier sits on a subway seat. Commuters glance and look away. A child hums a tune. Nothing big happens. The dog watches the city pass like a river.`
- 中文对照：雷伊风格：一只约克夏犬坐在地铁座位上，乘客看一眼又移开视线。一个孩子哼着小调。没有大事发生。狗看着城市像河一样流过。
- Negative: `No sentimental climax, no direct preaching, no plot-twist gimmick, no theatrical dialogue, no exotic spectacle`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
