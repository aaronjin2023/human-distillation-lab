# Stevie Wonder — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Stevie Wonder: joy as a discipline, plain words made musical by rhythm, a chorus that lifts before it lands, love without embarrassment`
- ZH: 汪达风格：快乐是一种操练，平实的词被节奏托成音乐，副歌先托起再落下，爱而不难为情。

## (2) 意象

- 日常奇迹意象（电话、阳光、孩子的笑）／迷信意象（破碎的镜子、黑猫、十三）／爱意象（电话线、阳光、花）；意象密度中等；多用具体名词，少用抽象词。 `impression`
- 意象密度：意象密度中等 `impression`
- 禁意象：华丽辞藻、抽象口号、刻薄的讽刺、与快乐无关的沉重。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音；副歌韵脚最亮，换韵即换一段快乐；音节与节拍严丝合缝，讲究律动。 `impression`
- 音节与字数：句式以中短句为主，叙事句与抒情句交替；副歌短促上扬；断句随律动走。 `impression`

## (4) 句式与口语密度

- 句式：句式以叙事与抒情为主，陈述与呼唤交替；口语密度高，像打电话的人说话；多用第一人称倾诉与第二人称呼唤。 `impression`
- 口语密度：口语密度高：日常口语、电话用语自然入词；书面语极少；独白体与对话体交错。 `impression`

## (5) 情感弧线

- 起于一个日常的奇迹，中段沿快乐推进、越讲越亮，副歌收在爱本身上，结尾常是微笑的落点；情感浓烈而克制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：日常奇迹意象、节奏托起的平实词、副歌的托起感、爱而不难为情。
- 不该写：华丽辞藻、抽象口号、刻薄的讽刺、与快乐无关的沉重。
- Negative prompt: `No ornate diction, no abstract slogans, no cruel satire, no heaviness unrelated to joy`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Stevie Wonder, lyrics about a small Yorkshire terrier on the subway, a little miracle on an ordinary day. Plain words lifted by rhythm, chorus that lifts before it lands. Verse, chorus, bridge. No ornate diction.`
- 中文对照：汪达风格：歌词写一只约克夏犬在地铁上，平凡日子里的小奇迹。平实的词被节奏托起，副歌先托起再落下。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no cruel satire, no heaviness unrelated to joy`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
