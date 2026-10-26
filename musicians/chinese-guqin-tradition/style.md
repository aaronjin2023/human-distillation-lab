# Chinese Guqin Tradition — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chinese Guqin Tradition, Chinese guqin tradition, single-line melody on seven silk strings, san yin open strings, an yin stopped notes, fan yin harmonics, yin nao chuo zhu ornament, long silence between phrases, music as meditation`
- ZH: 中国古琴传统（集体）风格，中国古琴传统，七弦单线旋律，散音、按音、泛音，吟猱绰注，句间长静默，音乐即静修。

## (2) 音高与和声方向

- 以五声音阶与调式（宫、商、角、徵、羽）为主；无和声进行，音高靠散音—按音—泛音的三种音色组织。`artifact`
- 主调式 / 主和声：见上；禁用进行：本传统几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律单线、缓慢、句间长静默；动机短小，以吟猱绰注的装饰音展开，不作对位发展。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 古琴独奏为主，七弦丝弦；音色分散音（浑厚）、按音（实）、泛音（清越）三路。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 段落式：曲分多段，每段以标题标意境，段落间以静默衔接；《广陵散》最长，完整打谱版本约 22 分钟（通说；各流派打谱版本时长不一，不绑定单一版本，见 conflicts.md）。`artifact`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：散音按音泛音三路、吟猱绰注、句间静默、段落标题意境、单线缓慢展开。`artifact`
- 不该写：和声进行、对位发展、固定节拍、密集音符、响亮高潮。
- Negative prompt: `harmonic progression, counterpoint, fixed meter, dense notes, loud climax, sentimental melody`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，午后晚些时候）

- Prompt: `In the style of Chinese Guqin Tradition, a 30-second piece for a cup of coffee left on a windowsill in the late afternoon, Chinese guqin tradition, single-line melody on seven silk strings, san yin open strings, an yin stopped notes, fan yin harmonics, yin nao chuo zhu ornament, long silence between phrases, music as meditation`
- 中文对照：中国古琴传统（集体）风格，为一杯放在窗台上的咖啡，午后晚些时候写一段 30 秒配乐，中国古琴传统，七弦单线旋律，散音、按音、泛音，吟猱绰注，句间长静默，音乐即静修。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
