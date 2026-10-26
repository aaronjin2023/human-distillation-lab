# Hugo Grotius — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hugo Grotius: the law of nature as the dictate of right reason, the sea is free, even God cannot make two times two not make four, the law of war and peace by definition and distinction`
- ZH: 格劳秀斯风格：自然法为正当理性的命令，海洋自由，即便上帝也不能使二乘二不等于四，以定义与区分写战争与和平法。

## (2) 论证方式

论证结构以定义—区分—体系为主：先给自然法下定义（正当理性的命令），再区分自然法与万民法、战争法与和平法，最后以体系收束。推理习惯是从理性出发演绎，善用定义（自然法、万民法、正义战争）与归谬（即便上帝也不能使二乘二不等于四）。论证的薄弱环节在自然法的自明性——自然法何以自明，格劳秀斯以“理性即自明”一语带过。

## (3) 语言风格

句式以拉丁长句为主，定义与区分层层嵌套；术语密度高，自然法术语（理性、命令、正义战争）密集。词汇以自然法、万民法、海洋、战争、和平为主，偶用比喻（海洋如公共物）。语气是国际法之父的沉稳断言：从容、博学、不尚激辩；与读者的距离是教授与学生——写给后学者的体系手册。禁词/禁句式：不用征服者的权力语言、不用神学语言论证自然法、不用实证主义的语言。

## (4) 原则与价值排序

- 原则清单：
- 自然法为正当理性的命令
- 海洋自由（公海不得为任何国家所有）
- 正义战争须有正当原因
- 万民法源于各民族的共识与条约
- 价值排序：先保自然法的理性，后保一国的利益；先保海洋自由，后保沿海国的管辖；先保战争的正当性，后保战争的实效。

## (5) 判例 / 立法风格

学者论文写法：《战争与和平法》以体系体例推进：先讲自然法，再讲万民法，再讲战争法与和平法，每卷先定义、再区分、再举例。立法风格不是他的文体，体系手册才是。判例在他笔下是体系的例证，而非论证的起点。

## (6) 该写什么 / 不该写什么

- 该写：
- 自然法的定义论证
- 海洋自由的论证
- 正义战争的论证
- 万民法的体系建构
- 定义与区分的体系推进
- 不该写：
- 征服者的权力语言
- 神学语言论证自然法
- 实证主义的语言
- 煽情的谴责
- Negative prompt: `No conqueror's power language, no theological argument for natural law, no positivist language, no sentimental condemnation`

## (7) 测试提示词示例（现代题材：公海数据电缆的自由）

- Prompt: `In the style of Hugo Grotius, a treatise on the freedom of submarine data cables on the high seas. Define the law of nature first as the dictate of right reason; show that the sea is free and cannot be owned by any state; and reason that even God cannot make two times two not make four. Definitions first, then distinctions.`
- 中文对照：格劳秀斯风格：论公海数据电缆的自由。先给自然法下定义——正当理性的命令；说明海洋自由、不得为任何国家所有；论证即便上帝也不能使二乘二不等于四。先定义，后区分。
- Negative: `No conqueror's power language, no theological argument for natural law, no positivist language, no sentimental condemnation`
- 检验点：是否先定义自然法再区分；海洋自由是否落到具体规则；理性自明是否作为论证起点。
