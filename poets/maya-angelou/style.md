# Maya Angelou — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Maya Angelou: spoken rhythm with gospel lift, still I rise as refrain, the caged bird singing of freedom, declarative lines that stand up, dignity as metre`
- ZH: 安杰卢风格：口语节奏带福音的 lift，我仍将奋起即叠句，笼中鸟歌唱自由，站立起来的宣言句，尊严即格律。

## (2) 意象

- 笼中鸟（歌唱自由）
- 奋起（《我仍将奋起》的叠句）
- 尘土与升起（从尘土中升起）
- 河流与歌（福音的歌）
- 母亲与女儿（传承）
- 禁意象：自怜的絮叨、抽象的大词、冷嘲
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 口语节奏：以朗诵的呼吸定行长，短行、叠句、呼应；《我仍将奋起》以叠句推进，节奏如福音；《笼中鸟》以对仗推进；整体节奏由口语的舒缓向宣言的坚定演变。

## (4) 语言密度与词汇

- 词汇：口语词极准（鸟、尘土、升起），福音词（歌、自由）与宣言词并置；抽象词（尊严、自由）借鸟与尘土落地；禁词：自怜絮叨词、抽象大词、冷嘲词。

## (5) 结构习惯

- 叠句体：以叠句（我仍将奋起）推进，宣言—对照—再宣言；单篇多以一景（笼中鸟）起兴，对仗推进，末句宣言收束；结尾多为站立的宣言而非抒情收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 笼中鸟、奋起、尘土的意象
- 口语节奏与福音 lift
- 叠句的宣言结构
- 站立的收束
- 不该写：
- 自怜絮叨与冷嘲
- 抽象大词
- 直白说教
- 冗长铺陈
- Negative prompt: `No self-pitying drift, no ironic sneer, no grand abstract words, no direct preaching, no long explanatory passages, no bowed-head ending`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Maya Angelou, a small Yorkshire terrier sits on a subway seat at night. Spoken rhythm with gospel lift, still I rise as refrain, the dog as a caged bird singing of freedom, declarative lines that stand up.`
- 中文对照：安杰卢风格：一只约克夏犬深夜坐在地铁座位上。口语节奏带福音的 lift，我仍将奋起即叠句，狗是歌唱自由的笼中鸟，站立起来的宣言句。
- Negative: `No self-pitying drift, no ironic sneer, no grand abstractions, no preaching, no long passages, no bowed-head ending`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
