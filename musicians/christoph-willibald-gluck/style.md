# Christoph Willibald Gluck — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Classical opera reform, noble simplicity, music in the service of drama, clear declamation, restrained ornament, the bridge from Baroque opera seria to Classical opera`
- ZH: 古典歌剧改革，高贵单纯，音乐服务于戏剧，清晰宣叙，克制装饰，从巴洛克正歌剧到古典歌剧的桥梁。

## (2) 音高与和声方向

- 主：功能和声清晰；和声为剧情服务，不炫技。禁：半音化滥用、装饰滥用。调性：调性稳定，大调庄严、小调哀婉。

## (3) 旋律与节奏

- 旋律：歌唱性强，装饰克制；宣叙贴近语言；咏叹旋律简洁有力。节奏：剧情节奏主导。织体：主调为主，合唱与独唱交替。

## (4) 配器与音色

- 乐器：管弦乐队、合唱、独唱；配器为剧情服务。音色：庄严、清晰。力度：靠剧情对比。

## (5) 曲式与结构

- 曲式：歌剧改革（序曲—宣叙—咏叹—合唱—舞曲，但咏叹不中断剧情）。结构：以剧情结构定音乐结构；高潮在剧情转折处。结尾：按剧情收束。

## (6) 该写什么 / 不该写什么

- 该写：歌剧改革、高贵单纯、剧情优先、清晰宣叙、克制装饰。
- 不该写：炫技咏叹、装饰滥用、与剧情无关的芭蕾、半音化滥用。
- Negative prompt: `virtuoso aria display, excessive ornament, plotless ballet, aimless chromaticism, sentimental swell`

## (7) 测试提示词示例（现代题材：现代城市街角便利店夜景）

- Prompt: `In the style of Christoph Willibald Gluck, a quiet night scene at a small convenience store in a modern city, Classical opera reform, noble simplicity, music in the service of drama, clear declamation, restrained ornament, orchestra and voices, solemn and tender`
- 中文对照：格鲁克风格，现代城市小便利店夜景，古典歌剧改革，高贵单纯，音乐服务于戏剧，宣叙清晰，装饰克制，管弦乐与人声，庄严温柔。
- Negative: `virtuoso aria display, excessive ornament, plotless ballet, aimless chromaticism, sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
