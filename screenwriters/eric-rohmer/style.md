# Éric Rohmer — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Éric Rohmer: people talking themselves into and out of desire, a moral tale in one summer, long conversations in beautiful places, a knee or a glance as the whole plot`
- ZH: 埃里克·侯麦风格：人们用谈话把自己谈进欲望又谈出来，一个夏天的道德故事，美丽地方的长篇对话，一个膝盖或一个眼神即全部情节。

## (2) 结构：三幕 / 序列 / 节拍

- 对话即结构：‘六个道德故事’与‘喜剧与谚语’系列，每部以一句话谚语或道德困境开场；情节极简，转折是一个眼神或一次犹豫；结局是人物做出了选择，但选择本身值得怀疑。`impression`

## (3) 对话

- 对白是侯麦的本体：长篇哲学对话，人物用语言试探自己的欲望；话多，事少；潜台词是‘我想要，但我不该想要’。`impression`

## (4) 人物弧光

- 主角类型：犹豫的男人、度假的少女；弧光是‘谈出来的选择’：人物在谈话中做出决定，但决定常常是自我欺骗；结局是平静的、略带讽刺的收束。`impression`

## (5) 类型套路与创新

- 类型：道德故事 / 夏日喜剧，遵守‘谈话即剧情’套路；创新是把情节压缩到几乎为零，把道德困境写成对话。禁套路：不用大转折，不用煽情高潮，不用动作场面。`impression`

## (6) 该写什么 / 不该写什么

- 该写：长篇哲学对话、一个夏天的道德困境、眼神与犹豫作转折、谈出来的选择、平静略带讽刺的收束。
- 不该写：大转折、煽情高潮、动作场面、人物直截了当地坦白欲望。
- Negative prompt: `No big plot twist, no sentimental climax, no action set piece, no character blurting out desire plainly, no ending that confirms the choice was right`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Éric Rohmer, a man buys oden at a convenience store late at night and talks for a very long time with the clerk about whether he should call a woman he met at the beach. Nothing happens. A glance is the whole plot. The choice is doubtful.`
- 中文对照：埃里克·侯麦风格：一个男人深夜在便利店买关东煮，与店员长谈该不该给海滩上认识的女人打电话。什么都没发生。一个眼神即全部情节。选择值得怀疑。
- Negative: `No big plot twist, no sentimental climax, no action set piece, no character blurting out desire plainly, no ending that confirms the choice was right`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
