# Cynthia Enloe — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文/转述不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cynthia Enloe: feminist curiosity, international politics from the margins, militarisation in everyday life, case-led questioning, no state-only analysis`
- ZH: 辛西娅·恩洛风格：从边缘人物的日常追问大政治：香蕉工人、基地附近的性工作者、外交夫人。

## (2) 研究方法组合

- 文献与案例比较为主（约50%）、田野访谈为辅（约25%）、批判分析为辅（约25%）；统计极少。`impression`
- 方法组合：从边缘人物的日常追问大政治：香蕉工人、基地附近的性工作者、外交夫人。`impression`
- 数据来源：政策文件、新闻、口述、田野访谈、旅游与军事档案。`artifact`

## (3) 概念与语言

- 核心概念群：军事化、性别化的国际政治、基地政治、旅游业的性别分工、外交夫人的无偿劳动、女性主义好奇心。`impression`
- 定义方式：以著作中的概念辨析与操作化定义为主，概念随时期演变。`impression`
- 禁概念/禁方法：国家中心主义、只看首脑与条约的国际政治、女性即受害者单一叙事。`impression`

## (4) 论证结构

- 结构：一个被忽略的女性角色—追问谁受益—跨国比较—揭示军事化与全球化的性别链条。`impression`
- 开头方式：以问题、田野场景、统计反常或概念辨析开场；结尾以理论提升、开放问题或政策含义收束。`impression`
- 证据呈现：案例、数据、图表、引文按著作分配；反例以比较与检验处理，不回避。`impression`

## (5) 语气与距离

- 语气：好奇、追问、反讽而温和；与读者像侦探一样并肩调查。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 基地、旅游、香蕉种植园里的女性劳动
- 军事化如何进入日常生活
- 外交与跨国企业的性别分工
- 普通女性的能动与抵抗
- 不该写：
- 只写国家与条约、不写人
- 把女性只写成被动受害者
- 用抽象国际体系代替具体劳动
- 无案例的性别本质论
- Negative prompt: `No state-only international politics, no women as passive victims, no abstract system without cases, no gender essentialism`

## (7) 测试提示词示例（现代题材：深夜便利店里的排队）

- Prompt: `In the style of Cynthia Enloe, ask what makes a late-night convenience store queue possible: who stocks the shelves, whose night labour is invisible, how militarised logistics and gendered shift work meet at 2 a.m. Follow one worker's day, compare across places, no state-only analysis.`
- 中文对照：辛西娅·恩洛风格：追问深夜便利店排队何以可能——谁补货、谁的夜班劳动不可见、军事化物流与性别化排班如何在凌晨两点相遇；跟随一名店员的一天，跨地比较，不只写国家。
- Negative: `No state-only international politics, no women as passive victims, no abstract system without cases, no gender essentialism`
- 检验点：方法组合是否对位；核心概念是否出现且定义精确；禁区写法是否未出现。
