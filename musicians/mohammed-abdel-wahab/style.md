# Mohammed Abdel Wahab — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mohammed Abdel Wahab, Modern Egyptian song composition, Arabic maqam melody over large Oriental orchestra, long vocal line with oud interjections, Western rhythms and instruments absorbed into tarab, refrain that builds by repetition`
- ZH: 穆罕默德·阿卜杜勒·瓦哈卜风格，现代埃及歌曲作曲，阿拉伯玛卡姆旋律配大型东方管弦乐队，长人声线条加乌德琴间奏，西方节奏与乐器吸收入塔拉布，副歌靠重复推进。

## (2) 音高与和声方向

- 以阿拉伯玛卡姆（调式 + 特征音 + 四分音装饰）为音高法则；和声以持续音与简单进行支撑旋律，不作功能和声主导。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律长、歌唱性强、带玛卡姆的装饰音与滑音；动机短小，副歌靠重复与装饰推进。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 乌德琴 + 小提琴组、管风琴、手风琴、打击乐的大型东方管弦乐队；音色温暖、层次多。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 歌曲主歌—副歌 + 长间奏为主；副歌多次重复，每次加装饰与力度，结尾以高潮收束。`artifact`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：玛卡姆旋律、长人声线、乌德间奏、大型东方乐队、副歌重复推进。`artifact`
- 不该写：西方功能和声主导、无玛卡姆的旋律、短歌曲式、配器盖住人声。
- Negative prompt: `Western functional harmony dominating, maqam-free melody, short pop form, orchestration burying the vocal, sentimental swell`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，午后晚些时候）

- Prompt: `In the style of Mohammed Abdel Wahab, a 30-second piece for a cup of coffee left on a windowsill in the late afternoon, Modern Egyptian song composition, Arabic maqam melody over large Oriental orchestra, long vocal line with oud interjections, Western rhythms and instruments absorbed into tarab, refrain that builds by repetition`
- 中文对照：穆罕默德·阿卜杜勒·瓦哈卜风格，为一杯放在窗台上的咖啡，午后晚些时候写一段 30 秒配乐，现代埃及歌曲作曲，阿拉伯玛卡姆旋律配大型东方管弦乐队，长人声线条加乌德琴间奏，西方节奏与乐器吸收入塔拉布，副歌靠重复推进。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
