# Antônio Carlos Jobim — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Antônio Carlos Jobim, Bossa nova songwriting, gentle syncopated guitar rhythm, jazz-extended harmony over diatonic melody, whispered vocal line, sea and breeze imagery carried by harmony rather than words`
- ZH: 安东尼奥·卡洛斯·若比姆风格，巴西波萨诺瓦歌曲写作，轻柔切分的吉他节奏，自然音阶旋律上的爵士扩展和声，低语式人声线条，海与风的意象由和声承载而非歌词。

## (2) 音高与和声方向

- 以大调自然音阶旋律 + 爵士扩展和弦（大七、九、十一和弦）为主；和声色彩丰富但解决温和，调性游移而不失落。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律轻柔、级进为主、音域窄，近乎低语；动机短小，反复中加半音装饰。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 尼龙弦吉他 + 钢琴、贝斯、轻打击乐；音色柔和、空间感大，配器不抢旋律。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 歌曲主歌—副歌为主，段落短；和声进行本身即结构，结尾常以和声循环渐弱收束。`artifact`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：轻柔切分、爵士扩展和声、低语旋律、吉他节奏型、和声循环结构。`artifact`
- 不该写：强烈的节奏驱动、功能和声的硬解决、华丽配器、喊唱式人声。
- Negative prompt: `driving beat, hard functional cadence, lush orchestration, belting vocal, sentimental swell`

## (7) 测试提示词示例（现代题材：现代城市街角便利店的夜景）

- Prompt: `In the style of Antônio Carlos Jobim, a 30-second piece for a quiet night scene at a small convenience store in a modern city, Bossa nova songwriting, gentle syncopated guitar rhythm, jazz-extended harmony over diatonic melody, whispered vocal line, sea and breeze imagery carried by harmony rather than words`
- 中文对照：安东尼奥·卡洛斯·若比姆风格，为现代城市街角便利店的夜景写一段 30 秒配乐，巴西波萨诺瓦歌曲写作，轻柔切分的吉他节奏，自然音阶旋律上的爵士扩展和声，低语式人声线条，海与风的意象由和声承载而非歌词。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
