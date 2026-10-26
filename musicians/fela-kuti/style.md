# Fela Kuti — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fela Kuti, Afrobeat composition, long groove built on interlocking guitar and keyboard riffs, call-and-response horns, Yoruba rhythm and pidgin vocal chant, songs stretched over fifteen minutes by riff variation`
- ZH: 费拉·库蒂风格，非洲节拍作曲，吉他与键盘交错连复段构成的长律动，呼应式铜管，约鲁巴节奏与皮钦语人声 chant，歌曲靠连复段变奏拉长到十余分钟。

## (2) 音高与和声方向

- 以约鲁巴调式与小调五声音阶为主，和声极简（常一两个和弦循环全曲）；张力来自节奏层叠而非和声。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律以呼应式短句为主，人声 chant 与铜管齐奏交替；动机短小，反复中加装饰。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 电吉他、电键盘、贝斯、鼓组、铜管组、打击乐的大乐队；音色层叠，每层节奏型独立又咬合。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 长律动曲式：同一律动循环全曲，段落靠连复段的进入与退出划分；结尾常以律动渐弱而非终止式收束。`artifact`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：交错连复段、呼应式铜管、长律动循环、人声 chant、节奏层叠。`artifact`
- 不该写：短歌曲式、功能和声进行、独奏堆砌、配器盖住律动。
- Negative prompt: `short pop form, functional harmony, solo showcase, orchestration burying the groove, sentimental swell`

## (7) 测试提示词示例（现代题材：一只小约克夏犬坐在地铁座位上）

- Prompt: `In the style of Fela Kuti, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Afrobeat composition, long groove built on interlocking guitar and keyboard riffs, call-and-response horns, Yoruba rhythm and pidgin vocal chant, songs stretched over fifteen minutes by riff variation`
- 中文对照：费拉·库蒂风格，为一只小约克夏犬坐在地铁座位上写一段 30 秒配乐，非洲节拍作曲，吉他与键盘交错连复段构成的长律动，呼应式铜管，约鲁巴节奏与皮钦语人声 chant，歌曲靠连复段变奏拉长到十余分钟。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
