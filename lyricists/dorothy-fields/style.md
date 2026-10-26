# Dorothy Fields — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dorothy Fields: witty vernacular lyrics, conversational ease, elegant understatement, romance without sentimentality, singable natural speech`
- ZH: 多萝西·菲尔兹风格：机智的口语化歌词，谈话般的从容，克制的优雅，浪漫而不滥情，像说话一样好唱。

## (2) 意象

- 意象群：(1)日常体面——晚礼服、月光、街道、阳台，体面生活的细节；(2)身体与姿态——你今晚的样子、舞步、微笑，不写抽象的爱，只写看得见的样子；(3)阳光与街道——晴朗的一面、街角、阳光，把乐观落到具体地点。意象密度中等，每句一两个具体意象，多明喻少暗喻，用典极少，几乎不用神话与宗教典故。禁意象：宏大抒情的星空与海洋、苦情自怜的意象。

## (3) 韵律

- 押韵：句尾押韵为主，韵脚干净利落，多为单音节开口韵；常以叠韵与内韵制造轻快的弹跳感；换韵多在桥段处，情绪一转即换。音节与字数：每句字数短而整齐，与摇摆乐的节拍对位，留出换气口；重音落在口语自然重音上，唱起来像说话。

## (4) 句式与口语密度

- 句式：短句为主，长短交错，平均句长短；多用对话体与直接称呼（you），设问少，排比克制。口语密度高：日常口语、俚语轻触即止，语气词少，书面语与口语比例约三七开；独白体少，多为对“你”说话。

## (5) 情感弧线

- 情感弧线：起——一个具体场景或一句恭维进场；转——一句机智的转折把情绪轻轻推开；合——副歌收在温柔的肯定上，不煽情。情感强度克制，带一点自嘲的距离；结尾常收束在一个画面上，不拖尾。

## (6) 该写什么 / 不该写什么

- 该写：机智的恭维与日常体面、对话体第二人称、短句、干净的句尾韵、阳光、街道、舞步等具体意象、副歌一句点睛。
- 不该写：滥情的宏大抒情、苦情自怜、晦涩的典故与象征、冗长的解释性句子。
- Negative prompt: `No sentimental grand lyricism, no self-pitying lament, no obscure allusion, no long explanatory lines, no forced rhyme`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Dorothy Fields, lyrics about a small Yorkshire terrier sitting on a subway seat, commuters smiling despite themselves. Witty conversational address, short singable lines, sunny street imagery, verse, chorus, bridge. No sentimentality.`
- 中文对照：多萝西·菲尔兹风格：机智的口语化歌词，谈话般的从容，克制的优雅，浪漫而不滥情，像说话一样好唱。以“一只坐在地铁里的约克夏犬”为题写歌词，见英文提示词。
- Negative: `No sentimental grand lyricism, no self-pitying lament, no obscure allusion, no long explanatory lines, no forced rhyme`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
