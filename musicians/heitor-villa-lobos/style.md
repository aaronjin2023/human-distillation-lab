# Heitor Villa-Lobos — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Heitor Villa-Lobos, Brazilian nationalist composition, Bach counterpoint fused with Brazilian folk melody and rhythm, choro and samba inflections, large orchestral colour, guitar idiom transferred to orchestra`
- ZH: 海托尔·维拉-洛博斯风格，巴西民族乐派作曲，巴赫对位融合巴西民间旋律与节奏，肖罗与桑巴色彩，大型管弦乐色彩，吉他语汇移植到管弦乐队。

## (2) 音高与和声方向

- 以巴西民间调式与大调—小调功能和声混合为主；和声色彩丰富，调性游移但总有民间旋律锚点。`impression`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律歌唱性强、带民间舞曲的切分与滑音，动机短小而反复；吉他式琶音常化作管弦乐旋律。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 大型管弦乐 + 吉他、巴西打击乐；音色明亮、层次多，民间乐器与管弦乐并置。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 组曲与多乐章为主，巴赫式复调结构套巴西舞曲节奏；民间主题作变奏与对位发展。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：巴西民间旋律、巴赫式对位、舞曲切分、吉他式琶音、组曲结构。`artifact`
- 不该写：脱离民间旋律的抽象和声、欧洲学院派的刻板曲式、配器盖住舞曲律动。
- Negative prompt: `folk-free abstract harmony, rigid academic form, orchestration burying the dance pulse, sentimental exoticism`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，午后晚些时候）

- Prompt: `In the style of Heitor Villa-Lobos, a 30-second piece for a cup of coffee left on a windowsill in the late afternoon, Brazilian nationalist composition, Bach counterpoint fused with Brazilian folk melody and rhythm, choro and samba inflections, large orchestral colour, guitar idiom transferred to orchestra`
- 中文对照：海托尔·维拉-洛博斯风格，为一杯放在窗台上的咖啡，午后晚些时候写一段 30 秒配乐，巴西民族乐派作曲，巴赫对位融合巴西民间旋律与节奏，肖罗与桑巴色彩，大型管弦乐色彩，吉他语汇移植到管弦乐队。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
