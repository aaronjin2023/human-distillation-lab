# Charles Mingus — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Mingus, Post-bop jazz composition, gospel shout and blues roots, collective improvisation inside tightly written ensemble charts, shifting meters, vocal-like brass, bass-led counterpoint`
- ZH: 查尔斯·明格斯风格，后比波普爵士作曲，福音呼喊与蓝调根基，严密写作的乐队谱面之内的集体即兴，变拍子，人声化的铜管，贝斯主导的对位。

## (2) 音高与和声方向

- 调性以蓝调音阶与教会调式为底，和声在功能和声与半音游移之间摆动；不协和音用作呼喊与张力，不作装饰。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律歌唱性强、带哭腔的滑音与长音，动机短小而反复呼喊；节奏上 6/8 福音律动、摇摆与突然停顿并置，复节奏常见。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 中型爵士乐队：小号（弱音器）、长号、萨克斯组、低音提琴主导、鼓；音色对比强烈——低音部的轰鸣对高音木管的抒情。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 组曲式与多段式为主，主题—再现—变奏的古典式布局套在爵士曲式上；高潮多在中后段，结尾常以主题碎片收束而非整齐终止。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：蓝调主题、福音式呼喊、集体即兴段落、组曲式结构、贝斯引导的声部进入。`artifact`
- 不该写：光滑的流行和声套路、独奏堆砌而无写作骨架、节拍一成不变的摇摆、情绪单一的背景爵士。
- Negative prompt: `smooth pop chord loop, solo showcase with no written structure, constant swing feel, sentimental background jazz, no collective improvisation`

## (7) 测试提示词示例（现代题材：一只小约克夏犬坐在地铁座位上）

- Prompt: `In the style of Charles Mingus, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Post-bop jazz composition, gospel shout and blues roots, collective improvisation inside tightly written ensemble charts, shifting meters, vocal-like brass, bass-led counterpoint`
- 中文对照：查尔斯·明格斯风格，为一只小约克夏犬坐在地铁座位上写一段 30 秒配乐，后比波普爵士作曲，福音呼喊与蓝调根基，严密写作的乐队谱面之内的集体即兴，变拍子，人声化的铜管，贝斯主导的对位。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
