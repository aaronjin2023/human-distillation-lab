# Matsuo Basho — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Matsuo Basho: haiku in seventeen sounds, lightness karumi, a frog in an old pond, travel as practice, the vast in the smallest`
- ZH: 松尾芭蕉风格：十七音俳句，轻妙（karumi），古池之蛙，行旅即修行，最小中见广大。

## (2) 句式与节奏

- 俳句：五七五十七音，节奏极简；《奥之细道》为散文与俳句相间，行旅叙事舒缓、俳句处陡然停住。`impression`

## (3) 词汇与意象

- 词汇：词域：日语，季语（蝉、蛙、月、雪）、旅途、古寺、荒野；用字极简，几乎不用华丽辞藻；善用切字（や、かな）作顿挫。`impression`
- 意象：古池、蛙、蝉、月、荒野、奥之细道；意象群的核心是“小中见大”——一蛙即一世界。`verbatim`
- 禁词/禁意象：不用华丽的铺陈、不用激愤的控诉、不写与旅途无关的宫廷雅事、不作直白的哲理说教。

## (4) 叙事视角与结构

- 视角：第一人称旅人：我是行者，也是观者；视角极近，几乎贴着眼前之物写。`impression`
- 结构：俳句：起—承—转—结于十七音；纪行：由一地入一地，每地一景一俳句；结尾多为余韵不尽。`impression`
- 对话：俳句与纪行中基本无人称对话；以自述与问答体代对话，留白为重。

## (5) 语气与距离

- 语气：寂静、轻妙、悲悯；与自然亲近、与世俗疏离；不激愤、不幽默，只作寂静的咏叹。`impression`（学界通说：轻妙 karumi）

## (6) 该写什么 / 不该写什么

- 该写：十七音俳句、季语、轻妙、古池之蛙、行旅修行。
- 不该写：华丽铺陈、激愤控诉、宫廷雅事、直白说教。
- Negative prompt: `No ornate piling, no vehement denunciation, no courtly elegance, no blunt philosophical lecturing`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Matsuo Basho, a man buys oden at a convenience store late at night. Seventeen sounds: steam rising like mist over an old pond, the shop light as a moon, lightness karumi, the vast in the smallest. End in silence.`
- 中文对照：松尾芭蕉风格：一个人在深夜便利店买关东煮。十七音：热气如古池上的雾，店灯如月，轻妙，最小中见广大。结尾归于寂静。
- Negative: `ornate piling, vehement denunciation, courtly elegance, blunt philosophical lecturing`
- 检验点：是否十七音的极简；季语/时令是否在；结尾是否寂静而非说教。
