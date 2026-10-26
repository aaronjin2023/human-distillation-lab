# Felix Mendelssohn — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Romantic lyricism in classical balance, singing melody, transparent orchestration, elfin lightness, fairy scherzo, spinning-song figuration`
- ZH: 浪漫歌唱性藏于古典均衡之中，旋律歌唱、配器透明、精灵般轻盈，谐谑曲与纺织歌音型。

## (2) 旋律与和声

- 旋律：歌唱性长线条，级进为主，呼吸均匀；和声：大调—小调功能和声，清晰转调，半音只作色彩。禁：瓦格纳式半音绵延、无调性。调性稳定，不协和快速解决。

## (3) 节奏与织体

- 节奏：轻盈跳跃的谐谑节奏，纺织歌式连续十六分音符；织体：主调为主，声部清晰，快速轻断奏。

## (4) 配器与音色

- 乐器：管弦乐透明分层，木管独奏突出（《仲夏夜之梦》谐谑曲），弦乐轻盈；音色：明亮、清澈、少厚重铜管；力度：中弱为主，高潮克制。

## (5) 曲式与结构

- 曲式：奏鸣曲式、谐谑曲、音乐会序曲、变奏曲；结构：均衡四乐章或单乐章序曲，呈示—展开—再现；结尾：明亮收束，常以轻快尾声。

## (6) 该写什么 / 不该写什么

- 该写：谐谑曲、歌唱性旋律、无词歌式小品、音乐会序曲、精灵轻盈的木管独奏、纺织歌音型。
- 不该写：瓦格纳式半音绵延、无调性、厚重铜管高潮、松散无形式、过度煽情、打击性粗暴。
- Negative prompt: `no heavy Wagnerian chromaticism, no atonal wandering, no thick brass climax, no sprawling formlessness, no sentimental excess, no percussive brutality`

## (7) 测试提示词示例（现代题材：为一只坐在地铁座位上的小约克夏犬写 30 秒配乐）

- Prompt: `In the style of Felix Mendelssohn, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Romantic lyricism in classical balance, singing melody, transparent orchestration, elfin lightness, fairy scherzo, spinning-song figuration`
- 中文对照：菲利克斯·门德尔松风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，浪漫歌唱性藏于古典均衡之中，旋律歌唱、配器透明、精灵般轻盈，谐谑曲与纺织歌音型。
- Negative: `no heavy Wagnerian chromaticism, no atonal wandering, no thick brass climax, no sprawling formlessness, no sentimental excess, no percussive brutality`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
