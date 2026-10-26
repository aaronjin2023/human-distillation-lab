# Tōru Takemitsu — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tōru Takemitsu, Japanese contemporary composition, sparse notes and long silences, pentatonic fragments over delicate orchestral colour, East-West timbre, dreamlike non-linear form, sound as garden`
- ZH: 武满彻风格，日本当代作曲，稀疏音符与长静默，五声音阶碎片配细腻管弦乐色彩，东西音色交融，梦幻的非线性曲式，声音如庭园。

## (2) 音高与和声方向

- 以五声音阶碎片与调式为主，和声色彩化、少功能进行；调性游移，音高靠音色与静默组织。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律碎片化、音符稀疏、长静默间隔；动机短小（两三个音），在静默中浮现又消失。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 西洋管弦乐 + 尺八、琵琶等日本乐器；音色细腻、泛音多，力度极轻到极弱为主。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 非线性 / 庭园式：段落并置而非发展，靠音色与静默的对比衔接；结尾常以静默收束。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：稀疏音符、长静默、五声音阶碎片、东西音色并置、非线性并置。`artifact`
- 不该写：密集配器、功能和声进行、动机发展式结构、响亮高潮。
- Negative prompt: `dense orchestration, functional harmony, developmental motivic structure, loud climax, sentimental melody`

## (7) 测试提示词示例（现代题材：现代城市街角便利店的夜景）

- Prompt: `In the style of Tōru Takemitsu, a 30-second piece for a quiet night scene at a small convenience store in a modern city, Japanese contemporary composition, sparse notes and long silences, pentatonic fragments over delicate orchestral colour, East-West timbre, dreamlike non-linear form, sound as garden`
- 中文对照：武满彻风格，为现代城市街角便利店的夜景写一段 30 秒配乐，日本当代作曲，稀疏音符与长静默，五声音阶碎片配细腻管弦乐色彩，东西音色交融，梦幻的非线性曲式，声音如庭园。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
