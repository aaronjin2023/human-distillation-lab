# Alexander Pushkin — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pushkin: clarity and lightness, the Onegin stanza, irony tender and exact, the superfluous man, history through a personal fate, no word wasted`
- ZH: 普希金风格：清晰与轻盈，奥涅金诗节，温柔而精确的反讽，多余人，个人命运中的历史，一词不虚掷。

## (2) 句式与节奏

- 句式：句长：诗节工整（奥涅金诗节十四行），句式清晰；散文则短句为主，节奏明快；长句只用在抒情段落。
- 节奏：节奏：轻盈而精确——诗节如舞步，散文如对话；抒情段落放缓，叙事段落加快。

## (3) 词汇与意象

- 词汇：词汇：俄语口语与法语借词并置，日常词与历史词交错；爱用轻快的形容词与动词。
- 意象：意象群：冬夜与雪、决斗与手枪、彼得堡的雾、乡村与庄园、卡片与命运、达吉雅娜的信。
- 禁词/禁意象：禁词/禁意象：不写沉重的说教，不用华丽的堆砌，不写脱离人物的议论。

## (4) 叙事视角与结构

- 视角：叙事视角：第一人称叙述者（《奥涅金》）时而现身、时而退后；散文多为第三人称，叙述者温和而全知。
- 结构：结构：《奥涅金》为诗体小说，八章 + 抒情插叙，结尾开放；短篇以一次事件为核，结尾常为一句翻转。

## (5) 语气与距离

- 语气：语气：轻盈、温柔而精确；与人物的距离如朋友——爱他们，也笑他们。

## (6) 该写什么 / 不该写什么

- 该写：该写：奥涅金诗节、轻盈的反讽、多余人、个人命运中的历史。
- 不该写：不该写：沉重说教、华丽堆砌、脱离人物的议论。
- Negative prompt: `No heavy moralising, no ornate excess, no off-character digression, no ponderous gloom`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Pushkin, a small Yorkshire terrier sits on a subway seat. Clear light sentences. The Onegin stanza's ease. Tender irony. No word wasted.`
- 中文对照：普希金风格，一只小约克夏犬坐在地铁座位上。清晰轻盈的句子，奥涅金诗节的从容，温柔的反讽，一词不虚掷。
- Negative: `heavy moralising, ornate excess, off-character digression, ponderous gloom`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
