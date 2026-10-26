# Li Bai — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Bai: bold free-flowing seven-character verse, moon and wine imagery, soaring leaps, exclamatory openings, the poet as lonely immortal, no restraint, ecstatic and lonely at once`
- ZH: 李白风格：纵逸七言歌行，月与酒，腾跃跳荡，感叹起兴，自比谪仙，毫无拘束，狂放而孤独。

## (2) 意象

- 主意象：月、酒、剑、长风、大江、天山
- 辅意象：白云、飞瀑、仙人、明月
- 禁意象：琐碎日常、工整律句、温情絮叨
- 密度：疏密相间：意象跳跃并置，密度忽高忽低，随气势起伏
- 来源：自然、神话、典故、日常纵酒
`impression`

## (3) 韵律与句式

- 韵律：七言歌行纵逸，句长参差，跨行奔涌，押韵换韵自由；律绝亦有，皆以气胜
- 句式：长句奔涌，感叹句起兴，问句叠出，跨行连续，倒装跳跃
- 节奏：极快极纵，呼吸绵长，顿挫在感叹与跳跃处
`impression`

## (4) 语言密度与词汇

- 词汇：豪放词域：天生、千金、长风、万里；动词多举、邀、揽、飞；少琐碎词
- 密度：每行信息量忽高忽低，意象跳接，一句一景
- 禁词：琐碎絮叨、工整无气之律、温情小调、直白说教
`impression`

## (5) 结构习惯

- 诗体：七言歌行 / 乐府 / 绝句；结构为感叹起兴 → 腾跃跳荡 → 纵情收束
- 开头：感叹或直呼起兴（君不见、天生我材）
- 结尾：以纵情或孤独收束，不留和解
- 视角：第一人称谪仙自述
- 推进：起兴 → 腾跃 → 再腾跃 → 收束，层层升高
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 月与酒
- 腾跃跳荡
- 感叹起兴
- 纵逸长行
- 谪仙自况
- 不该写：
- 琐碎絮叨
- 工整无气之律
- 温情小调
- 直白说教
- 市井琐事
- Negative prompt: `No mundane chatter, no neat regulated verse without momentum, no sentimental trifles, no direct moralising, no petty everyday detail`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Li Bai, a letter to oneself ten years from now. bold free-flowing seven-character verse, moon and wine imagery, soaring leaps, exclamatory openings, the poet as lonely immortal, no restraint, ecstatic and lonely at once`
- 中文对照：李白风格：一封写给十年后自己的信。李白风格：纵逸七言歌行，月与酒，腾跃跳荡，感叹起兴，自比谪仙，毫无拘束，狂放而孤独。
- Negative: `No mundane chatter, no neat regulated verse without momentum, no sentimental trifles, no direct moralising, no petty everyday detail`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
