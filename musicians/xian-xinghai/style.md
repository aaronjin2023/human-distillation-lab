# Xian Xinghai — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xian Xinghai, Chinese modern composition, pentatonic folk melody over Western choral and orchestral forms, march rhythm and call-and-response chorus, theme that a crowd can sing`
- ZH: 冼星海风格，中国近现代作曲，五声音阶民间旋律配西方合唱与管弦乐曲式，进行曲节奏与呼应式合唱，主题能让群众齐唱。

## (2) 音高与和声方向

- 以五声音阶与大调—小调功能和声混合为主；调性清晰，和声支撑旋律，不作实验。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律歌唱性强、级进为主、音域适中，民间歌腔的滑音；动机短小，副歌一句可记。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 合唱 + 管弦乐为主，间加中国打击乐；音色明亮、层次清，合唱占前景。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 大合唱组曲式：多乐章连缀，朗诵—独唱—合唱交替；高潮在末乐章，结尾以合唱齐唱收束。`artifact`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：五声民间旋律、呼应式合唱、进行曲节奏、大合唱组曲、群众可唱的主题。`artifact`
- 不该写：复杂和声、半音化旋律、密集配器盖住合唱、个人化抒情长线。
- Negative prompt: `complex harmony, chromatic melody, dense orchestration burying the chorus, private lyricism, sentimental swell`

## (7) 测试提示词示例（现代题材：一只小约克夏犬坐在地铁座位上）

- Prompt: `In the style of Xian Xinghai, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Chinese modern composition, pentatonic folk melody over Western choral and orchestral forms, march rhythm and call-and-response chorus, theme that a crowd can sing`
- 中文对照：冼星海风格，为一只小约克夏犬坐在地铁座位上写一段 30 秒配乐，中国近现代作曲，五声音阶民间旋律配西方合唱与管弦乐曲式，进行曲节奏与呼应式合唱，主题能让群众齐唱。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
