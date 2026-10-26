# Clara Schumann — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Virtuoso piano lyricism, songful melody, classical balance, intimate chamber scale, warm middle register`
- ZH: 炫技钢琴抒情，歌唱性旋律，古典均衡，亲密的室内乐尺度，温暖的中音区。

## (2) 旋律与和声

- 旋律：歌唱性长线条，钢琴炫技服务于歌唱；和声：浪漫功能和声，半音柔和。禁：瓦格纳式绵延。调性清晰，转调温和。

## (3) 节奏与织体

- 节奏：稳健中带切分；织体：钢琴主导加室内乐对话，声部平等。

## (4) 配器与音色

- 乐器：钢琴、钢琴三重奏、小型管弦乐；音色：中音区温暖，触键歌唱；力度：细腻层次。

## (5) 曲式与结构

- 曲式：协奏曲、三重奏、浪漫曲；结构：古典三乐章 / 三段体；结尾：明朗收束。

## (6) 该写什么 / 不该写什么

- 该写：钢琴协奏曲、钢琴三重奏、浪漫曲、歌唱性钢琴旋律、室内乐对话。
- 不该写：瓦格纳式半音绵延、无调性、空洞炫技、厚重管弦乐、过度煽情、打击性粗暴。
- Negative prompt: `no Wagnerian chromatic sprawl, no atonal wandering, no empty virtuosity, no thick orchestral mass, no sentimental excess, no percussive brutality`

## (7) 测试提示词示例（现代题材：深夜末班车窗外的雨）

- Prompt: `In the style of Clara Schumann, rain on the window of a night bus crossing the city, Virtuoso piano lyricism, songful melody, classical balance, intimate chamber scale, warm middle register`
- 中文对照：克拉拉·舒曼风格，深夜末班车窗外的雨，炫技钢琴抒情，歌唱性旋律，古典均衡，亲密的室内乐尺度，温暖的中音区。
- Negative: `no Wagnerian chromatic sprawl, no atonal wandering, no empty virtuosity, no thick orchestral mass, no sentimental excess, no percussive brutality`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
