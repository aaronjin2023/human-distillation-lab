# Dmitri Shostakovich — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Ironic march and waltz, DSCH motif, stark contrasts, folk-like melody under crushing orchestral force, chamber intimacy inside symphonic scale`
- ZH: 讽刺进行曲与圆舞曲，DSCH 动机，强烈对比，压迫性管弦力道下的民间式旋律，交响规模中的室内乐亲密感。

## (2) 旋律与和声

- 旋律：DSCH（D–降 E–C–B）签名动机反复出现；民间式级进旋律常被扭曲成讽刺形态。`artifact`
- 和声：调性为底，半音与不协和制造压迫；大小调并置，解决常被推迟或落空。`artifact`

## (3) 节奏与织体

- 节奏：进行曲与圆舞曲节奏被拉长、错位；打击乐 ostinato 制造机械压迫；织体：全奏与独奏弦乐的极端对比。

## (4) 配器与音色

- 配器：大编制管弦乐，铜管与打击乐的压迫性全奏；弦乐四重奏中极简、近乎耳语的织体。

## (5) 曲式与结构

- 曲式：四乐章交响曲、弦乐四重奏；高潮常在乐章后段以全奏爆发，结尾或渐弱收束或突强收束。

## (6) 该写什么 / 不该写什么

- 该写：DSCH 签名动机、讽刺进行曲与圆舞曲、打击乐 ostinato、民间式旋律的扭曲变形、全奏与耳语的极端对比。
- 不该写：untroubled pastoral lyricism、no triumphant march without irony、no functional harmony resolving on schedule、no decorative orchestration、no single unbroken climax。
- Negative prompt: `No untroubled pastoral lyricism, no triumphant march without irony, no functional harmony resolving on schedule, no decorative orchestration, no single unbroken climax`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Dmitri Shostakovich, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, ironic march rhythm, DSCH-like motif, stark loud-soft contrasts, muted strings`
- 中文对照：肖斯塔科维奇风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，讽刺进行曲节奏，DSCH 式动机，强弱极端对比，弱音弦乐。
- Negative: `No untroubled pastoral lyricism, no triumphant march without irony, no functional harmony resolving on schedule, no decorative orchestration, no single unbroken climax`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
