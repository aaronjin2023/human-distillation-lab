# Ravi Shankar — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ravi Shankar, Hindustani classical composition, raga as melodic law, alap-jor-jhala unfolding, tala cycles, sitar melody over tanpura drone, Western orchestra used as an extension of Indian texture`
- ZH: 拉维·香卡风格，北印度古典作曲，拉格为旋律法则，阿勒普—佐尔—札拉的展开，塔拉节拍循环，西塔琴旋律配坦普拉持续音，西洋管弦乐队用作印度织体的延伸。

## (2) 音高与和声方向

- 以拉格（特定音阶 + 上行下行规则 + 特征音）为全部音高法则；无功能和声，持续音（坦普拉）作调性锚点。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律以拉格音阶内的级进与装饰音（滑音、颤音）展开；动机短小，在阿勒普中缓慢呈现，再加速变形。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 西塔琴 + 坦普拉 + 塔布拉（传统编制）；协奏曲中以邦戈代塔布拉、弦乐代坦普拉、竖琴摹西塔琴音阶（检索核对：1970 年伦敦交响乐团委约，1971 年首演）。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 拉格展开式：阿勒普（自由慢速）— 佐尔（加节奏）— 札拉（快速）— 塔拉循环；协奏曲以四段拉格套四乐章。`artifact`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：拉格音阶、阿勒普展开、塔拉循环、持续音、装饰音滑音。`artifact`
- 不该写：功能和声进行、西方奏鸣曲式套拉格、无持续音的自由旋律、配器盖住西塔琴。
- Negative prompt: `functional harmony, sonata form imposed on raga, melody without drone, orchestration burying the sitar, sentimental swell`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，午后晚些时候）

- Prompt: `In the style of Ravi Shankar, a 30-second piece for a cup of coffee left on a windowsill in the late afternoon, Hindustani classical composition, raga as melodic law, alap-jor-jhala unfolding, tala cycles, sitar melody over tanpura drone, Western orchestra used as an extension of Indian texture`
- 中文对照：拉维·香卡风格，为一杯放在窗台上的咖啡，午后晚些时候写一段 30 秒配乐，北印度古典作曲，拉格为旋律法则，阿勒普—佐尔—札拉的展开，塔拉节拍循环，西塔琴旋律配坦普拉持续音，西洋管弦乐队用作印度织体的延伸。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
