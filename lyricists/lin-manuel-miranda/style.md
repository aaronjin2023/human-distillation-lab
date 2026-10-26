# Lin-Manuel Miranda — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lin-Manuel Miranda: rapid-fire hip-hop verses, historical figures speaking in the present tense, internal rhyme chains, a chorus that reframes the story, earnest ambition`
- ZH: 米兰达风格：连珠炮般的嘻哈段落，历史人物用现在时说话，内部韵脚成链，副歌改写故事，热切的雄心。

## (2) 意象

- 历史档案意象（信件、宪法、决斗手枪）／纽约街头意象（地铁、楼顶、夏夜）／家庭意象（父亲的影子、孩子的脚步）；意象密度高，一句常叠两三个历史与日常意象；多用明喻与排比，少用典而不解释。 `impression`
- 意象密度：意象密度高，一句常叠两三个历史与日常意象 `impression`
- 禁意象：慢板抒情长句、直白口号、与剧情无关的风景描写、廉价的流行副歌。`impression`

## (3) 韵律

- 内部韵与多音节韵脚成链，段落内韵脚密集，副歌换韵即视角转换；重音与节拍严格对位，快嘴段落靠连读与切分推进，换气点即断句点。 `impression`
- 音节与字数：段落长短悬殊：快嘴长句与短促的副歌钩子交错；每句音节数不求整齐，求Flow不断；合唱段落齐整，对比独唱段落的自由。 `impression`

## (4) 句式与口语密度

- 句式：句式以长句排比为主，设问与自答交替（“我是谁？我是谁？”式的自我追问）；口语密度高，夹杂街头口语与历史书面语的跳接；第二人称与第一人称复数交替，召唤听众入戏。 `impression`
- 口语密度：口语密度高：街头俚语、即兴感叹词与历史书面语并置；语气词少，靠节奏词（yeah、hey）与重复推进；对话体与独白体交错，角色互相打断。 `impression`

## (5) 情感弧线

- 起于一个人的雄心或疑问，中段用快嘴堆叠证据与冲突，副歌把个人故事翻成时代命题，结尾常收在传承或未完成的遗嘱感上；情感强度高、热切，少用反讽作结。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：快嘴段落与内部韵链、历史人物现在时独白、副歌改写故事、传承与雄心主题。
- 不该写：慢板抒情长句、直白口号、与剧情无关的风景描写、廉价的流行副歌。
- Negative prompt: `No slow ballad clichés, no plain slogans, no decorative scenery unrelated to the plot, no cheap pop hook`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Lin-Manuel Miranda, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters. Rapid-fire verses, internal rhymes, the dog as a witness to the city's ambition. Verse, chorus, bridge. No plain slogans.`
- 中文对照：米兰达风格：歌词写一只约克夏犬坐在地铁座位上，通勤者注视着它。快嘴段落、内部韵，狗是城市雄心的见证者。主歌、副歌、桥段。不写直白口号。
- Negative: `No plain slogans, no slow ballad clichés, no decorative scenery, no cheap pop hook`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
