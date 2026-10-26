# Ingmar Bergman — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ingmar Bergman: chamber drama of faces in close-up, God silent, marriage as a battlefield, dreams and memories bleeding into the present, a question asked and never answered`
- ZH: 伯格曼风格：特写面孔的室内剧，上帝沉默，婚姻即战场，梦与记忆渗进现在，问题问出口却没有答案。

## (2) 结构：三幕 / 序列 / 节拍

- 室内剧结构，常为两幕或环形：第一幕一对人物在封闭空间对峙（车厢、别墅、舞台）；中点是一段长独白或坦白，真相以回忆与梦境碎片出现；结尾不解决，只留一个凝视或一句未答的话。时间多为单日或数日，闪回以梦境与记忆呈现，不标明真假。

## (3) 对话

- 对白长句与独白并存，哲学追问直接说出口；沉默与凝视是台词的延续；人物用坦白互相伤害，也用坦白互相确认。动作描写极少，场景指示常写面孔与光线。

## (4) 人物弧光

- 主角多为艺术家、教授、夫妻，弧光是从自欺到直面：不是变好，而是终于说出真话。人物关系是夫妻、母子、父子、信仰者与上帝的对峙；结局人物不和解，只获得片刻的诚实。

## (5) 类型套路与创新

- 类型：心理剧情与室内剧；遵守套路——封闭空间、夫妻对峙；打破的一条是：把上帝缺席与死亡写成日常对话的底色。创新在剧本层面：让梦境与记忆直接进入对白结构，不加区分标记。禁套路：不用类型反转，不用煽情和解，不用外部事件救场。

## (6) 该写什么 / 不该写什么

- 该写：室内对峙与面孔特写、长独白与哲学追问、梦境与记忆碎片、夫妻与家庭的坦白、不回答的结尾。
- 不该写：类型反转、煽情和解、外部事件救场、直白的道德结论、用闪回确证真相。
- Negative prompt: `No genre twist, no sentimental reconciliation, no rescue by external event, no direct moral conclusion, no flashback that settles the truth`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Ingmar Bergman, a man buys oden at a convenience store late at night and meets his estranged wife at the same counter. Long confessions, silences, a dream intruding. No answer is given.`
- 中文对照：伯格曼风格：一个男人深夜在便利店买关东煮，在同一个柜台遇见分居的妻子，长篇坦白、沉默、梦境闯入，没有答案。
- Negative: `No genre twist, no sentimental reconciliation, no rescue by external event, no direct moral conclusion`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
