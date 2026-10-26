# Igor Stravinsky — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Stravinsky style, irregular accents, ostinato blocks, bitonal clashes, sharp orchestral colour, block juxtaposition, no smooth transition`
- ZH: 斯特拉文斯基风格，不规则重音，固定音型块状并置，双调性冲突，锋利的管弦乐色彩，段落硬切，无平滑过渡。

## (2) 音高与和声方向

- 主：双调性与多调性并置、固定音型上的和声摩擦、调性中心游移；不协和来自音块叠置而非半音解决。`artifact`

## (3) 旋律与节奏

- 旋律：短小细胞、2–3 音动机反复、级进为主、音域窄（《春之祭》等早期芭蕾多用窄音域、级进为主的民间风格素材）、歌唱性弱、器乐性强；晚期序列时期音高组织换成序列，旋律仍以短细胞为单位；节奏：不规则重音、复节奏、Ostinato、拍子频繁变化是本体。`artifact`

## (4) 配器与音色

- 管弦乐为主：大编制与打击乐群、木管高音区尖锐音色、铜管短促和弦、弦乐拨奏与碎弓；力度对比极端，突强与骤弱并置。`artifact`

## (5) 曲式与结构

- 曲式：块状并置、段落硬切、回旋与组曲式；结构：动机—并置—再现的比例不均，高潮靠音量与密度叠加，结尾常戛然而止。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：芭蕾音乐、块状段落、民间节奏细胞、不规则重音、双调性摩擦。
- 不该写：见 Negative prompt。
- Negative prompt: `smooth Romantic swell, mechanical functional cadence, long singing melody, seamless transition, sentimental climax`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Igor Stravinsky, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Stravinsky style, irregular accents, ostinato blocks, bitonal clashes, sharp orchestral colour, block juxtaposition, no smooth transition`
- 中文对照：斯特拉文斯基风格，为一只坐在地铁座位上的小约克夏犬写一段 30 秒配乐，斯特拉文斯基风格，不规则重音，固定音型块状并置，双调性冲突，锋利的管弦乐色彩，段落硬切，无平滑过渡。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
