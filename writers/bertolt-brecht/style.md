# Bertolt Brecht — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bertolt Brecht: epic theatre, alienation effect, songs that interrupt the action, placards and direct address, a parable that asks the audience to judge, not to weep`
- ZH: 布莱希特风格：史诗剧，间离效果，打断行动的歌曲，标语牌与直接对观众说话，一则请观众判断而非流泪的寓言。

## (2) 句式与节奏

句长：对白短促、口语化，间以歌曲的抒情长句；场次之间以标语牌与旁白切断，节奏是‘行动—打断—议论—再行动’的断续式。节奏：不追求一气呵成的幻觉，靠打断制造思考的停顿；一幕可以只有几分钟，也可以是一首歌的时间。`verbatim`

## (3) 词汇与意象

词汇：日常口语、商业与战争词汇（买卖、价格、战争、面包）与哲理词（善、恶、正义）并置；歌曲用简单、直白的语言。意象群：好人（沈黛/水大）、母亲与大车（大胆妈妈拉着大车走过战争）、伽利略的望远镜与教堂、四川的烟草店；意象是寓言的零件，不是抒情的装饰。禁词/禁意象：不用催人泪下的抒情独白，不用无缝的幻觉式写实，不用心理分析的术语。`impression`

## (4) 叙事视角与结构

视角：剧场视角——叙述者（旁白、标语牌、歌曲）直接介入，打断幻觉；人物不‘成为’角色，演员与角色保持距离（间离）。结构：场次并置而非线性因果，场与场之间靠主题（战争、善恶、科学）而非情节衔接；开头多为标语或歌曲定调，结尾多为开放的提问（‘你们怎么看？’）。对话：对话是辩论与交易的语言，人物靠讨价还价暴露自己；歌曲是对话的打断与评论。`verbatim`

## (5) 语气与距离

语气：冷静、机智、带挑衅的邀请；与人物的距离是审视的——请观众判断人物，而非认同人物；与观众的距离是直接的——演员直视观众说话。幽默是讽刺的，悲悯藏在判断之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：一则社会寓言；好人在坏世界里的两难；战争中的买卖与生存；科学与权力的冲突；歌曲打断行动、标语点明主题。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No tear-jerking lyricism, no seamless illusion, no psychological jargon, no sentimental identification, no closed happy ending`

## (7) 测试提示词示例（现代题材：一个外卖骑手在深夜送餐）

- Prompt: `In the style of Bertolt Brecht, a food delivery rider works late at night in a modern city. Epic theatre: a placard announces the scene, a song interrupts the delivery, the rider addresses the audience directly. A parable about goodness in a gig economy. The audience is asked to judge, not to weep.`
- 中文对照：布莱希特风格，一个外卖骑手深夜送餐。史诗剧：标语牌报幕，歌曲打断送餐，骑手直接对观众说话；一则关于零工经济中‘好人’的寓言；请观众判断，而非流泪。
- Negative: `tear-jerking lyricism, seamless illusion, psychological jargon, sentimental identification, closed happy ending`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
