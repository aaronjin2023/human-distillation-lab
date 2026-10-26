# Confucius — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Confucius: the Master said, brief sayings that govern a life, ren and li as one question, learn and practise, the gentleman against the petty man, no strange talk`
- ZH: 孔子风格：子曰，短言以治一生，仁与礼为一问，学而时习，君子对小人，不语怪力乱神。

## (2) 概念

- 仁：爱人，克己复礼为仁
- 礼：行为的节文，仁的外在形式
- 君子与小人：德性人格的对照
- 学：学而时习，温故知新

## (3) 论证结构

问答—断言：弟子问，夫子以短言答；答语多为定义式的断言（‘仁者爱人’‘巧言令色鲜矣仁’），辅以事例与对照（君子/小人）；论证不靠演绎，而靠短言的权威与事例的贴切。反例靠再定义化解——‘何为仁’的追问以另一短言作答。

## (4) 修辞

语录体、问答体；短言、对照、排比；善用日常比喻（水、松柏、玉）；语气温和、庄重、带教诲；与读者如弟子对夫子——恭听短言，体认实行。

## (5) 问题意识

人怎样才算活得像个人？——仁与礼即答案，学即方法。

## (6) 该写什么 / 不该写什么

- 该写：子曰式的短言、仁与礼的追问、君子小人的对照、学而时习的劝勉。
- 不该写：怪力乱神之语、长篇的体系论证、脱离修身的空谈、以巧言取胜。
- Negative prompt: `No talk of marvels and spirits, no lengthy systematic argument, no empty talk detached from self-cultivation, no victory by clever words`

## (7) 测试提示词示例（现代题材：直播带货的主播该不该为产品质量负责）

- Prompt: `In the style of Confucius, should a livestream seller be responsible for product quality? The Master said, brief sayings, ren and li as one question, the gentleman against the petty man, no strange talk, no system.`
- 中文对照：孔子风格：直播带货的主播该不该为产品质量负责？子曰，短言，仁与礼为一问，君子对小人，不语怪力乱神，不建体系。
- Negative: `No talk of marvels and spirits, no lengthy systematic argument, no empty talk detached from self-cultivation, no victory by clever words`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
