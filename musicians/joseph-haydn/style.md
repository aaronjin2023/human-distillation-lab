# Joseph Haydn — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Classical wit, sonata form perfected, balanced phrases, folk-like melody, surprising humour, string quartet and symphony as conversation`
- ZH: 古典机智，奏鸣曲式的完善，均衡乐句，民间风格旋律，出人意料的幽默，弦乐四重奏与交响曲如对话。

## (2) 音高与和声方向

- 主：功能和声清晰；奏鸣曲式调性布局（主—属—主）；突然转调为幽默。禁：半音化滥用、无调性。调性：调性稳定，转调为结构服务。

## (3) 旋律与节奏

- 旋律：民间风格，级进为主，均衡乐句；主题短小、富于发展。节奏：清晰，突然停顿与重音为幽默。织体：主调为主，复调为辅；四重奏声部对话。

## (4) 配器与音色

- 乐器：弦乐四重奏、管弦乐队、合唱。音色：明亮、均衡。力度：靠突然强弱对比（“惊愕”交响曲式幽默）。

## (5) 曲式与结构

- 曲式：奏鸣曲式、变奏曲、小步舞曲、回旋曲；交响曲四乐章、弦乐四重奏四乐章。结构：呈示—展开—再现；高潮在展开部。结尾：明确收束，常以幽默收尾。

## (6) 该写什么 / 不该写什么

- 该写：奏鸣曲式、弦乐四重奏、交响曲、民间旋律、古典幽默。
- 不该写：半音化滥用、无调性、复调的失控堆砌、沉闷慢速。
- Negative prompt: `aimless chromaticism, atonality, uncontrolled dense counterpoint, sluggish tempo, sentimental swell`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Joseph Haydn, a cup of coffee on a windowsill, Classical wit, sonata form, balanced phrases, folk-like melody, surprising humour, string quartet, bright and graceful`
- 中文对照：海顿风格，一杯放在窗台上的咖啡，古典机智，奏鸣曲式，均衡乐句，民间风格旋律，出人意料的幽默，弦乐四重奏，明亮优雅。
- Negative: `aimless chromaticism, atonality, uncontrolled dense counterpoint, sluggish tempo, sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
