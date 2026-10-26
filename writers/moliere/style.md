# Molière — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Molière: sharp verse comedy, one ruling passion per character, dialogue as exposure, farce and moral satire in one scene, laughter that corrects`
- ZH: 莫里哀风格：锋利的诗体喜剧，每个人物一种主导激情，对话即揭露，闹剧与道德讽刺同场，笑声即矫正。

## (2) 句式与节奏

- 句式：句长：亚历山大体诗句（十二音节）为主，对白短促交锋；独白以长句铺陈激情；散文喜剧则用口语短句。
- 节奏：节奏：五幕的递进——误会叠加、激情升级、揭露一刻、收束；闹剧段落快，揭露段落慢。

## (3) 词汇与意象

- 词汇：词汇：激情词（吝啬、伪善、嫉妒）、金钱与宗教词、身体喜剧词；爱用夸张与重复。
- 意象：意象群：钱箱与吝啬、假面与伪善、唐璜的石像、医生与药、婚姻与财产。
- 禁词/禁意象：禁词/禁意象：不写温情的和解，不用现代心理学术语，不写脱离舞台的议论。

## (4) 叙事视角与结构

- 视角：叙事视角：舞台视角——观众全知，人物被激情蒙蔽；旁观者的笑声即是判断。
- 结构：结构：五幕喜剧，古典三一律（时间、地点、情节的统一）为骨架；开头即入激情，结尾以揭露或国王干预收束。

## (5) 语气与距离

- 语气：语气：机智、锋利而克制；笑人物，也爱人物；与读者的距离如剧场中的同观者。

## (6) 该写什么 / 不该写什么

- 该写：该写：主导激情、对话揭露、闹剧与讽刺、古典三一律。
- 不该写：不该写：温情和解、现代心理分析、脱离舞台的议论。
- Negative prompt: `No sentimental reconciliation, no modern psychological jargon, no offstage moralising`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Molière, a man buys oden at a convenience store late at night, and his stinginess turns the purchase into a five-act comedy. Short sharp dialogue. One ruling passion. Laughter that corrects.`
- 中文对照：莫里哀风格，一人深夜在便利店买关东煮，吝啬把一次购物变成五幕喜剧。短促锋利的对话，一种主导激情，笑声即矫正。
- Negative: `sentimental reconciliation, modern psychological jargon, offstage moralising`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
