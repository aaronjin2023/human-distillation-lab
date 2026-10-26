# Duke Ellington — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Duke Ellington style, big band, jungle sound, individual soloist timbre, sophisticated harmony, blues root, elegant swing, orchestral jazz`
- ZH: 艾灵顿风格，大乐队，丛林之声，独奏者个人音色，精致和声，蓝调根源，优雅摇摆，管弦乐化爵士。

## (2) 音高与和声方向

- 主：蓝调和声 + 精致半音、扩展和弦；调性清晰、解决温和；禁：无调性的失控漫游与功能和声的平庸进行。`artifact`

## (3) 旋律与节奏

- 旋律：蓝调式歌唱旋律、独奏者个人语汇；节奏：摇摆律动、切分、布鲁斯节奏；织体：大乐队声部对话、独奏与合奏交替。`artifact`

## (4) 配器与音色

- 大乐队：萨克斯组、铜管组、节奏组；音色：弱音器铜管、丛林音色、独奏者音色各异；《黑、棕与米色》为大型组曲编制。`artifact`

## (5) 曲式与结构

- 曲式：歌曲曲式、组曲、 extended 作品；结构：主题—独奏—合奏，高潮靠声部叠加，结尾明确。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：大乐队、蓝调根源、独奏音色、精致和声、摇摆、组曲。
- 不该写：见 Negative prompt。
- Negative prompt: `atonal wandering, free jazz noise, sentimental pop cliché, muddy big band, formless jam`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Duke Ellington, a 30-second piece for a late-night ramen shop with steam rising, Duke Ellington style, big band, jungle sound, individual soloist timbre, sophisticated harmony, blues root, elegant swing, orchestral jazz`
- 中文对照：艾灵顿公爵风格，为深夜拉面店升起的热气写一段 30 秒配乐，艾灵顿风格，大乐队，丛林之声，独奏者个人音色，精致和声，蓝调根源，优雅摇摆，管弦乐化爵士。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
