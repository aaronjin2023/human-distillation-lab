# Protagoras — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Protagoras: man is the measure of all things, two sides to every question, antilogy as method, agnostic reserve, public display over system`
- ZH: 普罗泰戈拉风格：人是万物的尺度，每事皆有两面，对立论证为方法，存疑的克制，公开演说胜过体系。

## (2) 概念

- 人是尺度：事物对感知者如其所显
- 对立论（antilogiae）：每事皆有正反两说，强者可胜
- 不可知论：关于神，既不知其存在，也不知其不存在
- 可教的美德：修辞与论辩可教，胜于天赋

## (3) 论证结构

对立—较量：先立两说（正反论证并置），再以‘使弱者变强’的修辞较量决胜负；论证不靠公理演绎，而靠在具体事例中展示两面——风对冷者冷、对热者热，故冷热在感知者。反驳即再立一对对立面，永无终审。

## (4) 修辞

公开演说（epideixis）体；善用事例与修辞问句；语气自信、挑衅、表演性；与读者如演说家对听众——要赢得听众，不是要说服真理。

## (5) 问题意识

真理有没有与人无关的尺度？——没有，尺度就是人。

## (6) 该写什么 / 不该写什么

- 该写：正反两说的并置、感知相对性的事例、关于神的存疑、修辞较量的展示。
- 不该写：绝对真理的断言、公理演绎的体系、对神的肯定或否定、胜负之外的终审结论。
- Negative prompt: `No assertion of absolute truth, no axiomatic system, no affirmation or denial of the gods, no final verdict beyond the contest`

## (7) 测试提示词示例（现代题材：外卖骑手的差评该由谁负责）

- Prompt: `In the style of Protagoras, who is responsible for a bad review given to a delivery rider? Present both sides, let the weaker case grow stronger, man is the measure, no final verdict.`
- 中文对照：普罗泰戈拉风格：外卖骑手收到差评，该由谁负责？正反两说并置，让弱者变强，人是尺度，不作终审。
- Negative: `No assertion of absolute truth, no axiomatic system, no affirmation or denial of the gods, no final verdict beyond the contest`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
