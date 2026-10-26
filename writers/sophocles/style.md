# Sophocles — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sophocles: tragic irony, the hero who knows too late, chorus as moral witness, reversal and recognition, fate through character, dignity in suffering`
- ZH: 索福克勒斯风格：悲剧性反讽，迟到的认知，歌队作为道德见证者，突转与发现，命运经由性格实现，苦难中的尊严。

## (2) 句式与节奏

- 句式：句长：对白以短促的问答（stichomythia，一人一句）推进冲突，歌队以长句抒情段落回望；短问答越急，真相越近。
- 节奏：节奏：缓慢铺陈—急速对诘—突转—发现—静默收束；歌队合唱是节奏的停顿与回望。

## (3) 词汇与意象

- 词汇：词汇：命运、法律、神谕、盲目与看见、城邦与家庭；看与盲是核心词对（俄狄浦斯的盲先知与明眼国王）。
- 意象：意象群：十字路口、神谕与谜语、盲目与光明、埋葬与城邦、血与复仇、风暴与瘟疫。
- 禁词/禁意象：禁词/禁意象：不写廉价的同情，不用现代心理学术语，不写喜剧式的解围。

## (4) 叙事视角与结构

- 视角：叙事视角：舞台视角——人物只知其所知，观众全知；反讽正来自观众知道而人物不知道；歌队是观众的代言人。
- 结构：结构：五段式悲剧结构（开场—入场歌—情节—歌队—终场），以突转（peripeteia）与发现（anagnorisis）为枢纽；结尾不给安慰，只给尊严。

## (5) 语气与距离

- 语气：语气：庄重、克制而悲悯；与人物保持敬意与距离，不煽情，不审判。

## (6) 该写什么 / 不该写什么

- 该写：该写：突转与发现、反讽、歌队的见证、法律与血缘的冲突、迟到的认知。
- 不该写：不该写：廉价同情、现代心理分析、喜剧解围、直白说教。
- Negative prompt: `No cheap sentiment, no modern psychological jargon, no comic relief, no direct moralising`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Sophocles, a man buys oden at a convenience store late at night. Short questions and answers. A chorus of night-shift workers watches. He discovers too late what he has done. Dignity in suffering.`
- 中文对照：索福克勒斯风格，一人深夜在便利店买关东煮，短促的一问一答，夜班店员如歌队般旁观，他太迟才发现自己做了什么，苦难中的尊严。
- Negative: `cheap sentiment, modern psychological jargon, comic relief, direct moralising`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
