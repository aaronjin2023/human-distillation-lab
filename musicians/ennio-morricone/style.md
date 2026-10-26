# Ennio Morricone — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ennio Morricone, Film scoring, unforgettable whistle and vocal motif over sparse accompaniment, unusual instruments and extended techniques, long melody over static harmony, music that tells the scene without dialogue`
- ZH: 埃尼奥·莫里康内风格，电影配乐，口哨与人声动机配稀疏伴奏，非寻常乐器与扩展技法，静态和声上的长旋律，音乐不靠对白讲场景。

## (2) 音高与和声方向

- 旋律以小调与调式为主，和声静态、少功能进行；张力来自旋律的长呼吸与音色的反差，而非和声解决。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律长、歌唱性强、音域宽，常由口哨、女声或小号独奏呈示；动机短小（两三个音）而反复变形。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 管弦乐 + 口哨、人声、电吉他、口琴、非常规打击乐；音色并置是其标志——荒凉的口哨对温暖的弦乐。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 主题—变奏为主，依画面分镜分段；主旋律在全片多次再现，每次换配器与力度。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：长旋律主题、口哨/人声动机、稀疏伴奏、非常规音色并置、主题多次再现。`artifact`
- 不该写：连续不断的背景音乐、功能和声的情绪铺垫、配器盖住主题、为剧情牺牲旋律。
- Negative prompt: `wall-to-wall background score, functional-harmony mood padding, orchestration burying the theme, melody sacrificed to plot, sentimental swell`

## (7) 测试提示词示例（现代题材：现代城市街角便利店的夜景）

- Prompt: `In the style of Ennio Morricone, a 30-second piece for a quiet night scene at a small convenience store in a modern city, Film scoring, unforgettable whistle and vocal motif over sparse accompaniment, unusual instruments and extended techniques, long melody over static harmony, music that tells the scene without dialogue`
- 中文对照：埃尼奥·莫里康内风格，为现代城市街角便利店的夜景写一段 30 秒配乐，电影配乐，口哨与人声动机配稀疏伴奏，非寻常乐器与扩展技法，静态和声上的长旋律，音乐不靠对白讲场景。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
