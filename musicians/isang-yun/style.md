# Isang Yun — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Isang Yun, Korean contemporary composition, Hauptstimme single-line melody, East Asian ornament and glissando, flexible rhythm without bar-line pulse, orchestral colour as melody itself`
- ZH: 尹伊桑风格，韩国当代作曲，主声部单线旋律，东亚装饰音与滑音，无小节线脉动的自由节奏，管弦乐色彩即旋律本身。

## (2) 音高与和声方向

- 以五声音阶与十二音技法混合为主；主声部（Hauptstimme）单线旋律作核心，和声由旋律的装饰与泛音构成。`impression`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律单线、长呼吸、带装饰音与滑音；动机短小，在单线中缓慢展开，不作对位发展。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 管弦乐 + 东亚乐器色彩；音色细腻，单线旋律在不同乐器间传递。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 单线展开式：一条主旋律缓慢展开，段落靠音色与力度的变化衔接；结尾常以单线渐弱收束。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：主声部单线、装饰音滑音、自由节奏、音色传递、缓慢展开。`artifact`
- 不该写：功能和声进行、对位发展、固定节拍脉动、密集配器。
- Negative prompt: `functional harmony, contrapuntal development, fixed metrical pulse, dense orchestration, sentimental melody`

## (7) 测试提示词示例（现代题材：现代城市街角便利店的夜景）

- Prompt: `In the style of Isang Yun, a 30-second piece for a quiet night scene at a small convenience store in a modern city, Korean contemporary composition, Hauptstimme single-line melody, East Asian ornament and glissando, flexible rhythm without bar-line pulse, orchestral colour as melody itself`
- 中文对照：尹伊桑风格，为现代城市街角便利店的夜景写一段 30 秒配乐，韩国当代作曲，主声部单线旋律，东亚装饰音与滑音，无小节线脉动的自由节奏，管弦乐色彩即旋律本身。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
