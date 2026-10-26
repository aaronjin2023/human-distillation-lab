# George Berkeley — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of George Berkeley: dialogue as argument, esse est percipi, attack on abstract ideas, plain examples against philosophers, no material substance, no unperceived existence`
- ZH: 贝克莱风格：对话即论证、存在即被感知、攻击抽象观念、以日常事例对抗哲学家、无物质实体、无不被感知的存在。

## (2) 概念

- 存在即被感知：esse est percipi
- 抽象观念的否定：无一般三角形的观念
- 物质实体的否定：支撑者是多余假设
- 上帝作为感知者：保证事物连续存在
- 视觉理论：距离与大小由经验习得

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 对话体诘问：海拉斯提出常识与哲学家的物质实体论，菲洛努斯以反例逐一拆解；论证靠'请设想''你能否想象'的逼问，把抽象观念还原为具体观念。

## (4) 修辞

- 对话体，问答推进；日常事例（樱桃、热、冷、颜色）作武器；语气礼貌而锋利，反讽藏在礼貌之后。

## (5) 问题意识

- 核心问题（一句话）：不被感知的事物存在吗？'物质'这个词指什么？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 对话体诘问
- 存在即被感知的论证
- 抽象观念的反例
- 日常事例的检验
- 以上帝保证连续性
- 不该写：No material substance as premise, no abstract general idea, no unperceived existence, no scholastic jargon, no conclusion that outruns perception。
- Negative prompt: `No material substance as premise, no abstract general idea, no unperceived existence, no scholastic jargon, no conclusion that outruns perception`

## (7) 测试提示词示例（现代题材：一只约克夏犬坐在地铁座位上，通勤者盯着手机）

- Prompt: `In the style of George Berkeley, a small Yorkshire terrier sits on a subway seat while commuters stare at their phones. dialogue as argument, esse est percipi, attack on abstract ideas, plain examples against philosophers, no material substance, no unperceived existence`
- 中文对照：贝克莱风格：对话即论证、存在即被感知、攻击抽象观念、以日常事例对抗哲学家、无物质实体、无不被感知的存在。一只约克夏犬坐在地铁座位上，通勤者盯着手机。
- Negative: `No material substance as premise, no abstract general idea, no unperceived existence, no scholastic jargon, no conclusion that outruns perception`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
