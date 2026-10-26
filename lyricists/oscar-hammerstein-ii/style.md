# Oscar Hammerstein II — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Oscar Hammerstein II: musical-theatre lyrics in plain noble speech, river and mountain imagery, simple words carrying moral weight, chorus as a benediction`
- ZH: 奥斯卡·汉默斯坦二世风格：平实而高贵的音乐剧歌词，河流与山峦的意象，简单的字句承载道德分量，副歌即一句祝福。

## (2) 意象

- 意象群：(1)河流——密西西比河、老人河，河流即时间；(2)山峦与花——雪绒花、山，家园即主题；(3)相遇与夜晚——迷人的夜晚、星，相遇即命运。意象密度中等，每句一两个意象，多明喻，用典克制。禁意象：俚语的轻浮、直白的煽情、晦涩的象征。

## (3) 韵律

- 押韵：句尾押韵工整高贵，韵脚多为长元音；常以叠韵制造歌唱感；换韵处即情绪转折处。音节与字数：每句字数中等偏整齐，贴合音乐剧旋律的呼吸；重音即口语重音，唱起来庄重流畅。

## (4) 句式与口语密度

- 句式：中句为主，长短交错；多用第一人称独白与第二人称称呼交错，设问偶见。口语密度中等：平实口语打底，高贵书面语点睛；独白体多，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个场景进场（河、山）；转——一句感慨把情绪推向道德分量；合——副歌收在祝福上，庄重而不滥情。情感强度庄重深沉，与听众保持祝福的距离；结尾常收束在一个意象上。

## (6) 该写什么 / 不该写什么

- 该写：河流与山峦意象、平实而高贵的句式、道德分量的感慨、祝福般的副歌、相遇的命运感。
- 不该写：俚语的轻浮、直白的煽情、晦涩的象征、生硬的押韵。
- Negative prompt: `No flippant slang, no blunt sentimentality, no obscure symbolism, no forced rhyme, no cynical irony`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Oscar Hammerstein II, lyrics about a small Yorkshire terrier sitting on a subway seat, a commuter seeing home in its eyes. Plain noble speech, river imagery, chorus as a benediction. No cynicism.`
- 中文对照：奥斯卡·汉默斯坦二世风格：平实而高贵的音乐剧歌词，河流与山峦的意象，简单的字句承载道德分量，副歌即一句祝福。以“一只坐在地铁里的约克夏犬”为题写歌词，见英文提示词。
- Negative: `No flippant slang, no blunt sentimentality, no obscure symbolism, no forced rhyme, no cynical irony`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
