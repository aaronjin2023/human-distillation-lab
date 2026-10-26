# Mahmoud Darwish — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原诗时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mahmoud Darwish: free verse of exile and return, the olive tree and the lost house, identity carried in a poem like a passport, lyrical and political in one breath, the homeland as a woman and a wound`
- ZH: 达尔维什风格：流亡与归来的自由体，橄榄树与失落的家园，身份如护照般装进诗里，抒情与政治同一呼吸，故乡是女人亦是伤口

## (2) 意象

- 主意象：橄榄树、家园、钥匙、海、咖啡；辅意象：鸽子、风、伤口、护照；禁意象：抽象无根的抒情、廉价的口号；密度高，意象来自巴勒斯坦土地与流亡日常。`impression`

## (3) 韵律与句式

- 自由体，长行排比叠咏，短行如哽咽；多用重复与呼告；节奏如潮汐，去而复来。`impression`

## (4) 语言密度与词汇

- 词汇：土地、家园、身份等词域，日常词（咖啡、钥匙、面包）承载政治重量；善用重复句式；禁词：空洞口号、抽象大词、廉价煽情。`impression`

## (5) 结构习惯

- 单篇抒情与长诗并存；开头多为故乡场景或身份宣告，结尾以归来或守望收束；视角第一人称流亡者，时而代集体言；推进靠重复与意象叠加。`impression`

## (6) 该写什么 / 不该写什么

- 该写：流亡与归来主题、橄榄树与家园意象、身份宣告、重复叠咏。
- 不该写：抽象无根抒情、廉价口号、煽情滥情、去政治化的田园。
- Negative prompt: `No rootless abstract lyricism, no cheap slogans, no sentimental melodrama, no depoliticised pastoral, no hollow grand words`

## (7) 测试提示词示例（现代题材：一只约克夏犬深夜坐在地铁座位上，乘客们看着它）

- Prompt: `In the style of Mahmoud Darwish, a small Yorkshire terrier sits on a subway seat at night. Free verse of exile, the dog carrying its home like a passport, the olive tree in a paper cup, lyrical and political in one breath.`
- 中文对照：达尔维什风格：一只约克夏犬深夜坐在地铁座位上。流亡自由体，犬把家园当护照揣着，纸杯里的橄榄树，抒情与政治同一呼吸
- Negative: `No rootless abstract lyricism, no cheap slogans, no sentimental melodrama, no depoliticised pastoral, no hollow grand words`
- 检验点：意象、韵律与收束是否符合本诗人的风格；禁区写法是否出现。
