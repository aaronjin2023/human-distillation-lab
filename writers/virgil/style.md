# Virgil — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Virgil: polished hexameter, pity and empire held together, the hero who obeys fate at great cost, pastoral calm against epic violence, tears in things`
- ZH: 维吉尔风格：精雕的六音步，悲悯与帝国并置，顺从命运而付出代价的英雄，田园的宁静对照史诗的暴力，万物有泪。

## (2) 句式与节奏

- 句式：句长：六音步长句，精雕细琢，音节与意义高度配合；半句停顿（caesura）的位置即情感的停顿。
- 节奏：节奏：庄重而缓慢，如仪仗行进；战斗段落加快，田园段落放缓；哀悼的段落最慢，一句可停半拍。

## (3) 词汇与意象

- 词汇：词汇：命运（fatum）、虔敬（pietas）、帝国、泪（lacrimae）、田野与蜂群；拉丁语的庄重与音乐性是风格本体。
- 意象：意象群：特洛伊的火焰与罗马的奠基、迦太基女王的爱与弃、冥界之旅、蜜蜂与农事、盾牌上的未来罗马。
- 禁词/禁意象：禁词/禁意象：不写荷马式的粗粝直白，不用反讽解构，不写快节奏的冒险。

## (4) 叙事视角与结构

- 视角：叙事视角：全知而悲悯的叙述者，贴近埃涅阿斯的内心又不失距离；神界与人界交替，命运高于一切。
- 结构：结构：《埃涅阿斯纪》前六卷漂泊（奥德赛式）、后六卷战争（伊利亚特式）；冥界之旅在正中，是全诗的枢纽；结尾以杀戮收束，不给和解。

## (5) 语气与距离

- 语气：语气：庄重、悲悯而克制；对罗马的赞颂与对代价的哀悼同时存在，赞颂越响，哀悼越深。

## (6) 该写什么 / 不该写什么

- 该写：该写：命运与虔敬、帝国的代价、田园与战争的对照、冥界之旅、万物有泪。
- 不该写：不该写：粗粝的直白、反讽解构、快节奏冒险、廉价的胜利欢呼。
- Negative prompt: `No rough Homeric bluntness, no irony or deconstruction, no fast-paced adventure, no cheap triumphalism`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Virgil, a letter to oneself ten years from now. Polished long sentences. Fate and duty held against private longing. Tears in things. No cheap triumph.`
- 中文对照：维吉尔风格，一封写给十年后自己的信。精雕的长句，命运与责任对照私人的渴望，万物有泪，不廉价欢呼。
- Negative: `rough bluntness, irony, fast-paced adventure, cheap triumphalism`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
