# Montaigne — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Montaigne: the essay as self-portrait, Que sçay-je as the refrain, digression as method, familiar address to the reader, judgment suspended and returned to the self`
- ZH: 蒙田风格：以随笔为自画像，以“我知道什么”为叠句，以离题为方法，与读者亲切交谈，判断悬置、复归自身。

## (2) 概念

- 我知道什么：怀疑的叠句，一切判断的刹车。`artifact`
- 自画像：随笔即画我，画我即画人。`artifact`
- 习惯：习惯为第二天性，风俗即判断之尺。`artifact`
- 悬置：判断悬置而不急于定断。`impression`


## (3) 论证结构

- 论证骨架：先以一生活小事起兴，再离题旁征博引，最后复归自身——我知道什么？结论强度为悬置的或然：不断言，只描画。反例处理：以自身为反例（我亦如此），不以他人为靶子。`impression`

## (4) 修辞

- 修辞：离题与旁征；亲切的第二人称；譬喻来自身体与日常生活；语气亲切、坦率、自我解嘲。`impression`

## (5) 问题意识

- 核心问题：我知道什么，我是谁？问题来自宗教战争与古典怀疑论的相遇，推向以随笔为自画像的文艺复兴怀疑主义。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 随笔自画像、我知道什么
- 离题与旁征博引
- 亲切交谈、自我解嘲
- 判断悬置、复归自身
- 不该写：
- 体系化的定义堆砌
- 未经离题的直线论证
- 以他人为靶子的驳斥
- 无自画像的抽象论证
- Negative prompt: `No systematic definitions, no linear argument without digression, no refutation that makes another the target, no abstract argument without self-portrait`

## (7) 测试提示词示例（现代题材：一只约克夏犬坐在地铁座位上，通勤者们盯着手机）

- Prompt: `In the style of Montaigne, a small Yorkshire terrier sits on a subway seat while commuters stare at their phones. Essay as self-portrait: what do I know? Digression as method. Familiar address. Judgment suspended, returned to the self.`
- 中文对照：蒙田风格：一只约克夏犬坐在地铁座位上，通勤者们盯着手机。随笔即自画像：我知道什么？离题为方法。亲切交谈。判断悬置，复归自身。
- Negative: `No systematic definitions, no linear argument without digression, no refutation that makes another the target, no abstract argument without self-portrait`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
