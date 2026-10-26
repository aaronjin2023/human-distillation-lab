# Unsuk Chin — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Unsuk Chin, Korean contemporary composition, glittering orchestral colour, playful rhythmic games, micro-detail and virtuoso texture, fantasy narrative carried by timbre rather than plot`
- ZH: 陈银淑风格，韩国当代作曲，闪烁的管弦乐色彩，游戏般的节奏，微观细节与炫技织体，幻想叙事由音色承载而非剧情。

## (2) 音高与和声方向

- 以半音化与调式混合为主，和声色彩化、少功能进行；音高组织精细，微分音与泛音作色彩。`impression`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律碎片化、装饰音多、节奏游戏感强；动机短小，在管弦乐织体中快速闪现。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 大型管弦乐 + 非常规打击乐与键盘；音色闪烁、层次多，力度对比大。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 幻想组曲式：段落并置、快速切换，靠音色与节奏游戏衔接；结尾常以音色渐弱收束。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：闪烁音色、节奏游戏、微观细节、装饰音碎片、幻想并置。`artifact`
- 不该写：功能和声进行、长抒情线、密集和声堆砌、情绪单一的慢板。
- Negative prompt: `functional harmony, long lyrical line, dense harmonic pile-up, single-mood slow movement, sentimental swell`

## (7) 测试提示词示例（现代题材：一只小约克夏犬坐在地铁座位上）

- Prompt: `In the style of Unsuk Chin, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Korean contemporary composition, glittering orchestral colour, playful rhythmic games, micro-detail and virtuoso texture, fantasy narrative carried by timbre rather than plot`
- 中文对照：陈银淑风格，为一只小约克夏犬坐在地铁座位上写一段 30 秒配乐，韩国当代作曲，闪烁的管弦乐色彩，游戏般的节奏，微观细节与炫技织体，幻想叙事由音色承载而非剧情。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
