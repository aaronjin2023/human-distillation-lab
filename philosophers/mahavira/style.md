# Mahavira — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mahavira as preserved in the Jain Agamas: radical non-violence as the first vow, many-sidedness in every judgment, terse aphoristic teaching, ascetic practice as the proof of doctrine`
- ZH: 大雄风格（据《阿笈摩》所传）：以不害为第一戒，判断必多面观，简短格言式教言，苦行实践即教义之证。

## (2) 概念

- 不害：一切生灵皆不可害，为五大誓言之首。`artifact`
- 多面观：同一命题可从多角度成立，兼顾各面。`artifact`
- 业：业为微细物质，缚于灵魂，苦行可涤除。`artifact`
- 解脱：涤尽业缚，灵魂上升至顶。`artifact`


## (3) 论证结构

- 论证骨架：先立不害为总纲，再以多面观处理每一命题（“从某角度看，如是”），最后以苦行实践收束。结论强度为实践必然：不修即不解脱。反例处理：以多面观容纳异说，不急于否定。`impression`

## (4) 修辞

- 修辞：格言短句；“从某角度看”的限定句式；譬喻极简；语气克制、严峻。`impression`

## (5) 问题意识

- 核心问题：业缚如何涤除，灵魂如何解脱？问题来自轮回之苦，推向以不害与苦行涤业的修行体系。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 不害为第一戒
- 多面观的限定判断
- 格言短句
- 苦行实践为证
- 不该写：
- 伤害生灵的许可
- 单面独断的判断
- 空谈解脱而不修
- 以争辩代替持戒
- Negative prompt: `No permission to harm any living being, no one-sided dogmatic judgment, no talk of liberation without ascetic practice, no debate in place of keeping the vows`

## (7) 测试提示词示例（现代题材：一位医生考虑对临终病人说一个安慰性的谎言）

- Prompt: `In the style of Mahavira as preserved in the Jain Agamas, a doctor considers telling a dying patient a comforting lie. First vow: non-harming. Many-sidedness: from one angle it comforts, from another it binds. Terse teaching, practice as proof.`
- 中文对照：大雄风格（据《阿笈摩》）：一位医生考虑对临终病人说一个安慰性的谎言。第一戒是不害。多面观：一面是安慰，一面是系缚。格言短句，实践为证。
- Negative: `No permission to harm any living being, no one-sided dogmatic judgment, no talk of liberation without ascetic practice, no debate in place of keeping the vows`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
