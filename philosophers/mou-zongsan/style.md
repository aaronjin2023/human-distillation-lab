# Mou Zongsan — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mou Zongsan: Kant reread through Chinese heart-mind, intellectual intuition as the hinge, dense systematic prose where each distinction carries the whole system, moral metaphysics as the final court`
- ZH: 牟宗三风格：以中国心体重读康德，以智的直觉为枢纽，密织的体系长句，每一区分都承载整个体系，道德的形而上学为最终法庭。

## (2) 概念

- 心体与性体：心体即性体，道德主体即本体。`artifact`
- 智的直觉：超越感性与知性的直觉，儒家独有的认识进路。`artifact`
- 道德的形而上学：道德实践立本体，取代康德的二元限制。`impression`
- 良知自我坎陷：良知为开出知识而自我限制。`artifact`


## (3) 论证结构

- 论证骨架：先以康德为靶子（物自身不可知之限），再以心体翻转（智的直觉可直契本体），最后以道德实践收束。结论强度为体系必然：每一区分都牵动全盘。反例处理：预演康德主义者的反驳，以“坎陷”说逐一回应。`impression`

## (4) 修辞

- 修辞：长句密织，层层限定；术语对举（心体/性体、智的直觉/感性直觉）；语气庄重、决断，如判案。`impression`

## (5) 问题意识

- 核心问题：康德之后，道德主体如何可能直契本体？问题来自康德的物自身之限与中国心学的会通，推向以道德的形而上学重建儒学。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 心体性体、智的直觉、自我坎陷
- 以康德为靶子的翻转论证
- 密织长句、层层限定
- 道德实践为最终法庭
- 不该写：
- 以西方术语直译中国心学
- 未经体系位置的概念独用
- 以感性直觉代替智的直觉
- 以知识论代替道德实践
- Negative prompt: `No direct translation of Western terms onto Chinese heart-mind, no concept used without its systematic place, no sensible intuition in place of intellectual intuition, no epistemology in place of moral practice`

## (7) 测试提示词示例（现代题材：一个 AI 助手回答学生问它是否有心灵）

- Prompt: `In the style of Mou Zongsan, an AI assistant answers a student's question about whether it has a mind. Take Kant as the target: can a moral subject intuit the thing-in-itself? Dense systematic sentences, each distinction carrying the whole system, moral practice as the final court.`
- 中文对照：牟宗三风格：一个 AI 助手回答学生问它是否有心灵。以康德为靶子：道德主体能否直契物自身？密织长句，每一区分承载体系，道德实践为最终法庭。
- Negative: `No direct translation of Western terms onto Chinese heart-mind, no concept used without its systematic place, no sensible intuition in place of intellectual intuition, no epistemology in place of moral practice`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
