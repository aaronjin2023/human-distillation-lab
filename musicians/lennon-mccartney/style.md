# Lennon–McCartney — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lennon–McCartney, Beatles songwriting partnership, singable diatonic melody with unexpected chromatic turns, verse-chorus craft, vocal harmony in thirds, studio arrangement as composition, short song forms stretched by coda and medley`
- ZH: 列侬—麦卡特尼（创作组合）风格，披头士创作组合，可唱的自然音阶旋律带意外的半音转折，主歌—副歌写作，三度人声和声，录音室编曲即作曲，短歌曲式靠尾声与组曲拉长。

## (2) 音高与和声方向

- 以大调—小调自然音阶为主，副歌常有半音经过与借用和弦；调性清晰，转调多在桥段发生，解决回主调。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律可唱、音域适中、级进中夹一两个大跳；列侬一路偏直陈与半音下行，麦卡特尼一路偏上行歌唱线，两路在同一首歌里可以并置。`impression`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 吉他—贝斯—鼓核心 + 钢琴、弦乐、铜管、录音室效果（双轨、变速、拼贴）；配器随专辑概念变，不固定。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 主歌—副歌—桥段的标准流行曲式；晚期以组曲（《艾比路》B 面）与长尾声（《嘿，朱迪》）拉长短曲式。`artifact`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：可唱旋律、三度和声、桥段转调、录音室拼贴、组曲式收束。`artifact`
- 不该写：无旋律的和声堆砌、独奏炫技、松散即兴、过度制作盖住人声。
- Negative prompt: `melody-free harmony, virtuoso solo showcase, loose jamming, overproduction burying the vocal, formless collage`

## (7) 测试提示词示例（现代题材：一只小约克夏犬坐在地铁座位上）

- Prompt: `In the style of Lennon–McCartney, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Beatles songwriting partnership, singable diatonic melody with unexpected chromatic turns, verse-chorus craft, vocal harmony in thirds, studio arrangement as composition, short song forms stretched by coda and medley`
- 中文对照：列侬—麦卡特尼（创作组合）风格，为一只小约克夏犬坐在地铁座位上写一段 30 秒配乐，披头士创作组合，可唱的自然音阶旋律带意外的半音转折，主歌—副歌写作，三度人声和声，录音室编曲即作曲，短歌曲式靠尾声与组曲拉长。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
