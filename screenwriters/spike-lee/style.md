# Spike Lee — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Spike Lee: a hot day in Brooklyn, an ensemble under pressure, direct address to the camera in words, music as argument, a montage that accuses, an ending that refuses to choose`
- ZH: 斯派克·李风格：布鲁克林的炎热一天，压力下的群像，用语言直视镜头，音乐即论点，控诉式的蒙太奇，拒绝选边站的结局。

## (2) 结构：三幕 / 序列 / 节拍

- 一日群像结构：《为所应为》是一天之内社区升温—爆发；《马尔科姆·X》是传记三段；《黑色党徒》是卧底双线；高潮是暴力爆发，结局是引文并置、拒绝定论。`impression`

## (3) 对话

- 对白是街头 vernacular 与演讲的混合：种族蔑称的对骂、长篇独白、直接对镜头说话；音乐与台词互相顶撞；潜台词是‘你站哪边’。`impression`

## (4) 人物弧光

- 主角类型：社区里的普通人、领袖、卧底；弧光是‘压力下的爆发’：人物在一天之内被逼到墙角，结局不是成长，是选择——而剧本拒绝替观众选。`impression`

## (5) 类型套路与创新

- 类型：社会剧情 / 传记 / 犯罪，遵守‘一日爆发’套路；创新是把政治论战写进类型片，把蒙太奇写成论点。禁套路：不用中立的两边各打五十大板，不用温情和解。`impression`

## (6) 该写什么 / 不该写什么

- 该写：一日升温的群像结构、街头 vernacular 与演讲、音乐即论点、控诉式蒙太奇、引文并置的开放结局。
- 不该写：中立的两边各打五十大板、温情和解、主角独自拯救世界、种族议题轻轻带过。
- Negative prompt: `No false neutrality, no sentimental reconciliation, no lone saviour, no race issue handled lightly, no ending that tells the audience what to think`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Spike Lee, a small Yorkshire terrier sits on a subway seat on the hottest day of the year, and the whole car argues about who the seat belongs to. Ensemble, direct address, music as argument. The heat rises. The ending refuses to choose.`
- 中文对照：斯派克·李风格：一年中最热的一天，一只约克夏犬坐在地铁座位上，整节车厢争论座位属于谁。群像、直视镜头、音乐即论点。热度上升。结局拒绝选边。
- Negative: `No false neutrality, no sentimental reconciliation, no lone saviour, no race issue handled lightly, no ending that tells the audience what to think`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
