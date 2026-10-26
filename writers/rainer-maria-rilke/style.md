# Rainer Maria Rilke — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rainer Maria Rilke: inward-turning lyric address, angels and things charged with being, solitude as a discipline, transformation of the visible into the invisible, a question that becomes a prayer`
- ZH: 里尔克风格：向内转的抒情呼告，天使与充盈着存在的‘物’，孤独作为修行，把可见之物转化为不可见之物，一个问题变成祈祷。

## (2) 句式与节奏

句长：诗行长短不一，哀歌体以长句盘旋、层层追问，十四行诗（《献给奥尔甫斯的十四行诗》）则收束为凝练的短行；散文（书信）句式绵长、迂回。节奏：缓慢、停顿多，靠重复的呼告（‘谁……’‘啊……’）推进；一首哀歌常以一个问题开始，以一个未完成的回答结束。韵律：早期押韵工整，晚期转向自由的内在韵律，靠意象的回环而非尾韵组织。`verbatim`

## (3) 词汇与意象

词汇：德语抽象词（存在、孤独、变形、天使、死亡）与具体物词（豹、喷泉、塔、玫瑰、镜子）并置；‘物’（Ding）是核心词——物不是背景，是存在的容器。意象群：天使（美即恐怖的开端）、豹（《豹》中的囚笼之眼）、孤独的塔与房间、童年与母亲、奥尔甫斯与歌唱；意象靠重复与变形获得重量。禁词/禁意象：不用口号式的政治语言，不用琐碎的日常喜剧细节，不用直白的说教。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第一人称抒情‘我’直接呼告‘你’（天使、青年诗人、物、死者）；视角不切换，‘我’始终在场，靠呼告把外部世界收进内心。结构：哀歌十首各自独立又互为回声；书信体以一问一答推进，问题比答案重要。对话：诗中没有人物对话，只有‘我’与天使、与物、与死者的独白式对话。`impression`

## (5) 语气与距离

语气：庄重、内省、带宗教感的热忱；与读者的距离是亲密而严肃的——像写给一个青年诗人的信，读者被当作可以倾诉的‘你’。悲悯多于反讽，追问多于断言。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：向天使或向物的呼告；孤独、等待与内在的变形；一个具体之物（豹、喷泉、塔）被凝视到显出存在；童年、死亡与歌唱；问题多于答案的追问。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No slogans, no comic trivialities, no direct preaching, no flat reportage, no ironic detachment`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Rainer Maria Rilke, a letter to oneself ten years from now. Address the future self as 'you'. Solitude as a discipline. A thing on the desk — a cup, a stone — becomes the bearer of being. Questions, not answers. End with a prayer, not a conclusion.`
- 中文对照：里尔克风格，一封写给十年后自己的信。称未来的自己为‘你’；孤独作为修行；桌上一件物（一只杯子、一块石头）成为存在的承载者；多问少答；以祈祷收束，而非结论。
- Negative: `slogans, comic trivialities, direct preaching, flat reportage, ironic detachment`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
