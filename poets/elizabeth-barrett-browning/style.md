# Elizabeth Barrett Browning — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Elizabeth Barrett Browning: elevated sonnet sequence, love as spiritual argument, biblical and classical allusion, long periodic sentences breaking into exclamation, earnest and ardent`
- ZH: 巴雷特·勃朗宁风格：崇高的十四行诗组，以爱为精神论证，圣经与古典典故，长句层层推进后迸为感叹，真挚而热烈。

## (2) 意象

- 爱与灵魂（主意象，爱的神学化）
- 眉额与面容（凝视与被凝视）
- 锁链与自由（政治诗中的解放）
- 意大利（流亡与新生之地）
- 孩子与母亲（《给孩子的哭泣》式哀怜）
- 禁意象：轻浮调情、世俗应酬的意象
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 十四行诗为主（莎士比亚体与彼特拉克体混用），五音步抑扬格；长句多从句嵌套，行末跨行推进，感叹句收束；《奥罗拉·利》为九卷空白体长诗，句长参差、议论与叙事交织。

## (4) 语言密度与词汇

- 词汇典雅而高密度：圣经语言、古典神话、抽象名词（灵魂、永恒、真理）与具体身体意象并置；多用典故压缩意义，一典抵一节；禁词：口语俚语、轻佻双关。

## (5) 结构习惯

- 单篇十四行诗以命题—转折（volta 多在第 9 行或末联）—收束为骨架；诗组按情感进程编排（从怀疑到确信）；长诗《奥罗拉·利》以书信体叙事推进，议论段落插入叙事。

## (6) 该写什么 / 不该写什么

- 该写：
- 十四行诗组的爱之论证
- 灵魂与永恒的崇高意象
- 以政治诗写解放与同情
- 长句推进后的感叹收束
- 不该写：
- 轻浮的调情小调
- 无典故支撑的直白抒情
- 冷嘲与反讽的疏离语气
- 琐碎日常的絮叨
- Negative prompt: `No flippant flirtation, no flat plainspoken confession, no ironic detachment, no trivial daily chatter, no love poem without spiritual argument`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Elizabeth Barrett Browning, a small Yorkshire terrier sits on a subway seat at night. A sonnet sequence of love and soul, long periodic sentences, biblical allusion, the dog as a small soul watched by strangers, exclamatory close.`
- 中文对照：巴雷特·勃朗宁风格：一只约克夏犬深夜坐在地铁座位上。以十四行诗组写爱与灵魂，长句推进、圣经典故，狗是一个被陌生人注视的小灵魂，感叹收束。
- Negative: `No flippant tone, no plainspoken flatness, no ironic detachment, no trivial chatter`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
