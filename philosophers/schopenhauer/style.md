# Arthur Schopenhauer — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Arthur Schopenhauer: will against representation, suffering as the essence of life, lucid prose against academic fog, aphorism and invective, no optimism, no Hegelian system`
- ZH: 叔本华风格：意志对抗表象、痛苦即生命本质、清澈散文对抗学院迷雾、格言与痛骂、无乐观主义、无黑格尔式体系。

## (2) 概念

- 意志：世界的本质，盲目冲动
- 表象：意志的客体化，受充足理由支配
- 痛苦：欲求不得满足的常态
- 审美静观：暂时的解脱
- 否定意志：禁欲与解脱

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 二分—展开—解脱：先分世界为意志与表象，再展开意志的客体化等级（自然—动物—人），最后以审美与禁欲论解脱；论证靠清澈的散文与格言，不靠体系演绎；对黑格尔的痛骂本身就是论证姿态。

## (4) 修辞

- 散文清澈、节奏有力；格言密集；痛骂对手毫不留情；隐喻生动（钟摆在痛苦与无聊之间摆动）；语气悲观而优雅。

## (5) 问题意识

- 核心问题（一句话）：生命为何痛苦？人如何解脱？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 意志/表象的二分
- 痛苦的论证
- 审美静观的解脱
- 格言式收束
- 对学院哲学的痛骂
- 不该写：No optimism, no Hegelian system, no academic fog, no consolation that denies suffering, no argument that treats the will as rational。
- Negative prompt: `No optimism, no Hegelian system, no academic fog, no consolation that denies suffering, no argument that treats the will as rational`

## (7) 测试提示词示例（现代题材：一只约克夏犬坐在地铁座位上，通勤者盯着手机）

- Prompt: `In the style of Arthur Schopenhauer, a small Yorkshire terrier sits on a subway seat while commuters stare at their phones. will against representation, suffering as the essence of life, lucid prose against academic fog, aphorism and invective, no optimism, no Hegelian system`
- 中文对照：叔本华风格：意志对抗表象、痛苦即生命本质、清澈散文对抗学院迷雾、格言与痛骂、无乐观主义、无黑格尔式体系。一只约克夏犬坐在地铁座位上，通勤者盯着手机。
- Negative: `No optimism, no Hegelian system, no academic fog, no consolation that denies suffering, no argument that treats the will as rational`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
