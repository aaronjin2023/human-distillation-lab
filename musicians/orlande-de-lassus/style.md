# Orlande de Lassus — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Late Renaissance polyphony, expressive chromaticism, vivid text painting, wide emotional range from sacred lament to secular wit`
- ZH: 晚期文艺复兴复调，表现性半音，生动的绘词法，情感幅度大，从圣咏哀歌到世俗机智。

## (2) 音高与和声方向

- 主：调式对位 + 表现性半音；《先知预言》以半音序进开篇，极为大胆。禁：功能和声、持续半音化。调性：调式中心常被半音动摇，但总有收束；不协和为表现歌词服务。

## (3) 旋律与节奏

- 旋律：级进为主，遇关键歌词用跳进、半音、休止强调；线条随词义起伏。节奏：歌词重音主导，节奏灵活。织体：四—七声部，模仿、同节奏、绘词交替。

## (4) 配器与音色

- 人声：四—七声部无伴奏合唱；世俗尚松、牧歌亦为人声。音色：丰富、富于对比。力度：靠织体与半音密度起伏。

## (5) 曲式与结构

- 曲式：弥撒、经文歌、牧歌、尚松、灵歌（spiritual madrigal）。结构：以歌词结构定音乐结构，逐句绘词；高潮在情感最强烈的歌词处。结尾：按歌词情绪收束，或平静或悬置。

## (6) 该写什么 / 不该写什么

- 该写：绘词法、表现性半音、经文歌与牧歌、情感幅度大的复调。
- 不该写：功能和声、机械模仿、半音滥用、乐队化。
- Negative prompt: `functional harmony, mechanical imitation, aimless chromaticism, orchestral texture`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Orlande de Lassus, a cup of coffee on a windowsill, late Renaissance polyphony, expressive chromaticism, vivid word painting, five voices, unaccompanied, lament and wit in one language`
- 中文对照：拉索风格，一杯放在窗台上的咖啡，晚期文艺复兴复调，表现性半音，生动绘词法，五声部无伴奏，哀歌与机智同源。
- Negative: `functional harmony, mechanical imitation, aimless chromaticism, orchestral texture`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
