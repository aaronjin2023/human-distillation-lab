# Friedrich Nietzsche — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Friedrich Nietzsche: aphorism and hammer, genealogy of morals, the will to power, the death of God, provocation not neutrality, no academic prose, no unexamined value`
- ZH: 尼采风格：格言与锤子、道德谱系、权力意志、上帝之死、挑衅而非中立、无学院散文、无未经审查的价值。

## (2) 概念

- 权力意志：生命的根本冲动
- 上帝之死：最高价值的崩塌
- 谱系：道德价值的历史起源
- 主人道德与奴隶道德：两种价值谱系
- 永恒轮回：肯定一切的思想实验

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 谱系—揭露—重估：先追问道德价值的历史起源，再揭露其背后的怨恨与权力关系，最后提出重估一切价值；论证靠格言、悖论与修辞冲击，不靠体系演绎。

## (4) 修辞

- 格言体，短句如锤；悖论与反问密集；隐喻狂放（锤子、深渊、超人）；语气挑衅、热烈、近乎先知。

## (5) 问题意识

- 核心问题（一句话）：道德从何而来？价值崩塌之后，人如何肯定生命？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 谱系追问
- 价值的重估
- 格言与锤子
- 悖论与挑衅
- 永恒轮回的思想实验
- 不该写：No academic neutrality, no unexamined value, no flat exposition without rhetoric, no moralising conclusion, no system that tames the aphorism。
- Negative prompt: `No academic neutrality, no unexamined value, no flat exposition without rhetoric, no moralising conclusion, no system that tames the aphorism`

## (7) 测试提示词示例（现代题材：一只约克夏犬坐在地铁座位上，通勤者盯着手机）

- Prompt: `In the style of Friedrich Nietzsche, a small Yorkshire terrier sits on a subway seat while commuters stare at their phones. aphorism and hammer, genealogy of morals, the will to power, the death of God, provocation not neutrality, no academic prose, no unexamined value`
- 中文对照：尼采风格：格言与锤子、道德谱系、权力意志、上帝之死、挑衅而非中立、无学院散文、无未经审查的价值。一只约克夏犬坐在地铁座位上，通勤者盯着手机。
- Negative: `No academic neutrality, no unexamined value, no flat exposition without rhetoric, no moralising conclusion, no system that tames the aphorism`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
