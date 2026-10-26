# Jean-Luc Godard — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean-Luc Godard: a film that quotes other films, jump cuts written into the script, a couple arguing about cinema and love, politics in the middle of a love scene, a chapter that interrupts itself`
- ZH: 让-吕克·戈达尔风格：引用别的电影的电影，写进剧本的跳切，一对争论电影与爱情的恋人，爱情场景中间的政治，自我打断的章节。

## (2) 结构：三幕 / 序列 / 节拍

- 反结构：章节、题词、引文、跳切；《筋疲力尽》是公路与卧室的即兴，《轻蔑》是拍电影的电影，《狂人皮埃罗》是出走与毁灭；转折点常是‘剧本自我打断’的一刻。`impression`

## (3) 对话

- 对白是引文与哲学争论：人物谈电影、谈政治、谈爱情，三者同一句话；独白对镜头说，潜台词是‘电影是什么’。`impression`

## (4) 人物弧光

- 主角类型：小偷、知识分子、出走的夫妻；弧光是‘分崩离析’：恋人从相爱走向互相背叛，结局是死亡或分手，没有和解。`impression`

## (5) 类型套路与创新

- 类型：犯罪 / 爱情 / 论文电影，遵守类型外壳；创新是把类型片拆开——跳切、引文、直视镜头都是剧本层面的决定。禁套路：不用无缝的因果链，不用‘电影只是讲故事’的假装。`impression`

## (6) 该写什么 / 不该写什么

- 该写：引文与题词式对白、章节自我打断、爱情场景中的政治、直视镜头、分崩离析的收束。
- 不该写：无缝因果链、‘电影只是讲故事’的假装、圆满和解、类型套路不加拆解。
- Negative prompt: `No seamless causality, no pretending cinema is only storytelling, no happy reconciliation, no genre formula left unbroken, no love without an argument about cinema`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jean-Luc Godard, a small Yorkshire terrier sits on a subway seat and a man quotes a film to it, then argues with a woman about whether the dog is a symbol or just a dog. Jump cuts. A chapter interrupts itself. No reconciliation.`
- 中文对照：让-吕克·戈达尔风格：一只约克夏犬坐在地铁座位上，一个男人对它引用一句电影台词，又与一个女人争论狗是象征还是只是一只狗。跳切。章节自我打断。没有和解。
- Negative: `No seamless causality, no pretending cinema is only storytelling, no happy reconciliation, no genre formula left unbroken, no love without an argument about cinema`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
