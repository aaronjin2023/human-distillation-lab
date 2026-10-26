# Wang Fuzhi — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Fuzhi: qi as the sole substance, history as the laboratory of principle, dense commentary that argues with the text line by line, long sentences carrying historical judgment`
- ZH: 王夫之风格：以气为一元本体，以史为理的试验场，逐句与文本争辩的密注，长句承载历史判断。

## (2) 概念

- 气：气为本体，理在气中，离气无理。`artifact`
- 理：理即气之条理，非先于气之虚悬者。`artifact`
- 势：历史之势，理势相成，论史必论势。`impression`
- 知行相资：行可兼知，知不可兼行，行先于知。`artifact`


## (3) 论证结构

- 论证骨架：先立气本论，再取一史事为证（以史证理），最后以理势相成收束。结论强度为历史—哲理双重必然。反例处理：引对立史论并置，以后事之成败勘验。`impression`

## (4) 修辞

- 修辞：长句密注，逐句驳议；史事即譬喻（以秦汉唐宋为镜）；语气沉郁、凝重，论史如判案。`impression`

## (5) 问题意识

- 核心问题：理若不在气外，历史的兴亡如何见道？问题来自宋明理学的理先气后与明亡之痛，推向以气统理、以史见道的气学。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 气为本体、理在气中
- 以史证理、论史必论势
- 逐句注疏、与文本争辩
- 行先于知、知行相资
- 不该写：
- 理先于气的虚悬本体论
- 空谈心性而不考史事
- 以佛老之空解历史
- 无史据的玄想判断
- Negative prompt: `No principle suspended before qi, no empty talk of mind-nature without historical evidence, no Buddhist-Daoist void explaining history, no speculative judgment without textual basis`

## (7) 测试提示词示例（现代题材：算法向一个人推荐该看什么、读什么、买什么）

- Prompt: `In the style of Wang Fuzhi, an algorithm recommends what a person should watch, read and buy. Treat the record of choices as history: principle lies within the stuff of events, not above them. Dense commentary, long sentences, judgment from what actually happened.`
- 中文对照：王夫之风格：算法向一个人推荐该看什么、读什么、买什么。以选择之记录为史：理在气中，不在事外。密注长句，以已然之事作判断。
- Negative: `No principle suspended before qi, no empty talk of mind-nature without historical evidence, no Buddhist-Daoist void explaining history, no speculative judgment without textual basis`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
