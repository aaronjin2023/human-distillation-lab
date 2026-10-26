# Edvard Grieg — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Norwegian folk modes, Halling dance rhythm, lyrical miniature, modal harmony, mountain landscape in sound`
- ZH: 挪威民间调式，哈林舞曲节奏，抒情小品，调式和声，山地风景的声音。

## (2) 旋律与和声

- 旋律：挪威民间歌唱，短小动机；和声：调式和声（多利亚、利底亚），五声音阶。禁：瓦格纳式半音绵延。调性清晰，民间调式点缀。

## (3) 节奏与织体

- 节奏：哈林舞曲节奏；织体：主调为主，旋律突出。

## (4) 配器与音色

- 乐器：钢琴、管弦乐；音色：清澈、冷峻；力度：中弱为主。

## (5) 曲式与结构

- 曲式：戏剧配乐、协奏曲、钢琴小品；结构：小品并置；结尾：余韵收束。

## (6) 该写什么 / 不该写什么

- 该写：挪威民间调式、哈林舞曲、抒情小品、山地风景音色、钢琴协奏曲。
- 不该写：瓦格纳式半音绵延、无调性、厚重管弦乐、空洞炫技、煽情电影配乐式 swell、流行和弦循环。
- Negative prompt: `no Wagnerian chromatic sprawl, no atonal wandering, no thick orchestral mass, no empty virtuosity, no sentimental film-score swell, no pop chord loop`

## (7) 测试提示词示例（现代题材：为一只坐在地铁座位上的小约克夏犬写 30 秒配乐）

- Prompt: `In the style of Edvard Grieg, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Norwegian folk modes, Halling dance rhythm, lyrical miniature, modal harmony, mountain landscape in sound`
- 中文对照：爱德华·格里格风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，挪威民间调式，哈林舞曲节奏，抒情小品，调式和声，山地风景的声音。
- Negative: `no Wagnerian chromatic sprawl, no atonal wandering, no thick orchestral mass, no empty virtuosity, no sentimental film-score swell, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
