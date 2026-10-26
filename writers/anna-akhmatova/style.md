# Anna Akhmatova — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Anna Akhmatova: classical clarity, a plain word carrying unbearable weight, the voice of a queue outside a prison, love and history in the same quatrain, silence as testimony`
- ZH: 阿赫玛托娃风格：古典的清晰，一个平实的词承载难以承受的重量，监狱外排队者的声音，爱与历史在同一四行诗里，沉默作为证词。

## (2) 句式与节奏

句长：诗行短促、凝练，四行诗（quatrain）是基本单位；早期抒情短诗以日常口语的节奏推进，晚期《安魂曲》以长诗的段落回环。节奏：缓慢、克制，靠重复与停顿推进；一首诗常以一个日常细节开始，以一个历史的重量收束。韵律：古典格律（四音步、押韵）为主，晚期转向自由的内在韵律。`impression`

## (3) 词汇与意象

词汇：俄语日常词（手套、窗、茶、围巾）与历史词（监狱、排队、告别）并置；‘排队’‘等待’‘沉默’是核心词。意象群：手套（掉落的手套）、窗（内外边界）、监狱外的长队、母亲与儿子、彼得堡的街道；意象靠重复获得重量。禁词/禁意象：不用华丽的比喻堆砌，不用抽象的哲理议论，不用煽情的控诉。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第一人称抒情‘我’直接说话，‘我’既是恋人也是母亲、既是个人也是见证者；视角不切换，‘我’始终在场。结构：四行诗的并置、长诗的段落回环；开头多为一个日常细节，结尾多为历史的重量。对话：诗中没有人物对话，只有‘我’与‘你’（恋人、儿子、死者）的独白式对话。`impression`

## (5) 语气与距离

语气：克制、庄重、带悲怆的清晰；与读者的距离是亲密而严肃的——像对一个排队者说话，读者被当作可以倾诉的‘你’。悲悯多于反讽，见证多于抒情。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：一个平实的词承载历史的重量；监狱外排队者的声音；爱与历史在同一四行诗里；沉默作为证词；日常细节中的永恒。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No ornate metaphor, no abstract philosophising, no sentimental accusation, no flat reportage, no ironic detachment`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Anna Akhmatova, a letter to oneself ten years from now. Classical clarity. A plain word carrying unbearable weight. A glove, a window, a queue outside a prison. Love and history in the same quatrain. Silence as testimony.`
- 中文对照：阿赫玛托娃风格，一封写给十年后自己的信。古典的清晰；一个平实的词承载难以承受的重量；一只手套、一扇窗、监狱外的一支长队；爱与历史在同一四行诗里；沉默作为证词。
- Negative: `ornate metaphor, abstract philosophising, sentimental accusation, flat reportage, ironic detachment`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
