# E.Y. Harburg — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of E.Y. Harburg: plain words with a social conscience, a dream just over the horizon, irony that comforts rather than bites, chorus as a wish`
- ZH: 哈伯格风格：平实的词带着社会良心，梦想就在地平线那头，反讽是安慰而非刺痛，副歌是一个愿望。

## (2) 意象

- 梦想意象（彩虹、地平线、蓝天）／大萧条意象（失业者、街角、空口袋）／日常意象（雨、巴黎的四月、旧外套）；意象密度低，每句一个意象；多用明喻，少用典。 `impression`
- 意象密度：意象密度低，每句一个意象 `impression`
- 禁意象：华丽辞藻、愤怒的控诉、抽象口号、与现实无关的幻想。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音，副歌韵脚最顺；换韵处即愿望的转折处；音节与旋律贴合，讲究唱得顺、记得住。 `impression`
- 音节与字数：句式整齐，每句字数接近；主歌叙事、副歌抒情，长短句交错少。 `impression`

## (4) 句式与口语密度

- 句式：句式以中短句为主，叙事与祈愿交替；口语密度高，像街头的人说话；多用第一人称倾诉与第二人称对话。 `impression`
- 口语密度：口语密度高：日常口语、街头用语，语气词自然；书面语极少；对话体与独白体交错。 `impression`

## (5) 情感弧线

- 起于眼前的困境，中段望向远方的梦想，副歌收在愿望本身上，结尾常是温柔的坚持而非实现；情感克制而悲悯。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：平实词与社会关怀、梦想与地平线意象、温柔的反讽、副歌的愿望感。
- 不该写：华丽辞藻、愤怒的控诉、抽象口号、与现实无关的幻想。
- Negative prompt: `No ornate diction, no angry denunciation, no abstract slogans, no escapist fantasy detached from reality`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of E.Y. Harburg, lyrics about a small Yorkshire terrier sitting on a subway seat, dreaming of a home beyond the rainbow of the city lights. Plain words, gentle irony, chorus as a wish. Verse, chorus, bridge. No ornate diction.`
- 中文对照：哈伯格风格：歌词写一只约克夏犬坐在地铁座位上，梦见城市灯光彩虹那头的家。平实的词，温柔的反讽，副歌是一个愿望。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no angry denunciation, no abstract slogans, no escapist fantasy`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
