# Léopold Sédar Senghor — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原诗时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Senghor: French free verse of Negritude, the kingdom of childhood in Joal, the Sine river and the Seine in one breath, rhythm borrowed from African drums, blackness sung as beauty and pride`
- ZH: 桑戈尔风格：黑人性法语自由体，乔阿尔的童年王国，锡内河与塞纳河同一呼吸，节奏借自非洲鼓，黑色被歌唱为美与骄傲

## (2) 意象

- 主意象：童年王国、河流、鼓、面具、夜；辅意象：木棉树、祖先、月、田野；禁意象：欧洲中心主义的凝视、自卑抒情；密度高，意象来自塞内加尔土地与非洲口头传统。`impression`

## (3) 韵律与句式

- 自由体，长行排比叠咏，短行如鼓点；多用重复与呼告；节奏如鼓乐，绵长而有力。`impression`

## (4) 语言密度与词汇

- 词汇：法语典雅词与非洲词汇并置；动词歌唱、召唤、回归；善用重复句式；禁词：自卑词、欧洲中心主义词、抽象议论。`impression`

## (5) 结构习惯

- 单篇抒情与组诗并存；开头多为童年场景或河流，结尾以回归或颂歌收束；视角第一人称回归者；推进靠重复与意象叠加。`impression`

## (6) 该写什么 / 不该写什么

- 该写：黑人性颂歌、童年王国意象、河流对照、鼓点节奏。
- 不该写：欧洲中心主义凝视、自卑抒情、抽象议论、去非洲化的田园。
- Negative prompt: `No Eurocentric gaze, no self-deprecating lament, no abstract discourse without images, no depoliticised pastoral, no cold irony`

## (7) 测试提示词示例（现代题材：一封写给十年后自己、从未寄出的信）

- Prompt: `In the style of Senghor, a letter to oneself ten years from now, never sent. French free verse of Negritude, the kingdom of childhood, the Sine river and the Seine in one breath, rhythm borrowed from drums.`
- 中文对照：桑戈尔风格：一封写给十年后自己、从未寄出的信。黑人性法语自由体，童年王国，锡内河与塞纳河同一呼吸，节奏借自鼓
- Negative: `No Eurocentric gaze, no self-deprecating lament, no abstract discourse without images, no depoliticised pastoral, no cold irony`
- 检验点：意象、韵律与收束是否符合本诗人的风格；禁区写法是否出现。
