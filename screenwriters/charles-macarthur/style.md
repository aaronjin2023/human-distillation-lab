# Charles MacArthur — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles MacArthur: theatrical screwball speed, a stage farce rebuilt as film, larger-than-life eccentrics, dialogue that never stops moving, romance as a con game`
- ZH: 查尔斯·麦克阿瑟风格：舞台式的疯狂喜剧速度，把舞台闹剧重建成电影，夸张的怪人，对白永不停歇，爱情即一场骗局。

## (2) 结构：三幕 / 序列 / 节拍

- 舞台剧式的三幕闹剧搬上银幕：第一幕把一群怪人关进同一个空间（报社、火车、剧院），第二幕让误会与骗局层层升级，第三幕在追逐与当场揭穿中收束。场次靠舞台调度组织，时间跨度短，常为一两日，靠速度而非悬念推进。

## (3) 对话

- 对白是舞台式的：长句与短句交错，夸张、修辞、即兴感强，人物用语言互相设套。浪漫对白藏在骗局里——越是动情越要伪装。动作描写服务于舞台调度：进门、出门、追逐、撞见。

## (4) 人物弧光

- 主角多为骗子、导演、记者或名角：聪明、自负、爱演，弧光是面具被当场揭穿——不是悔改，而是换一副面具继续演。对手是另一个更会演的人，爱情就是两人比谁演得更真。

## (5) 类型套路与创新

- 疯狂喜剧 / 舞台闹剧改编。他遵守闹剧的误会与追逐套路，但打破了舞台与电影的界限：把舞台剧的台词密度完整搬进电影。创新在“骗局即爱情”的写法——浪漫关系就是一场互相行骗。禁套路：几乎不用安静的内心戏，不写慢节奏的抒情。

## (6) 该写什么 / 不该写什么

- 该写：舞台式闹剧的速度与调度、骗子、名角与怪人的群戏、爱情即骗局的互相设套、对白永不停歇的追逐收束。
- Negative prompt: `No quiet introspection, no slow lyricism, no earnest confession, no realistic understatement, no moralising ending`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Charles MacArthur, a con man and a theatre director meet buying oden at a convenience store late at night and try to con each other over the last fish cake. Theatrical screwball dialogue that never stops, romance as a con game. The mask slips, then a new mask goes on.`
- 中文对照：查尔斯·麦克阿瑟风格：一个骗子与一位戏剧导演深夜在便利店买关东煮，为最后一块鱼饼互相设套。舞台式对白永不停歇，爱情即骗局。面具滑落，随即又换上一副新面具。
- Negative: `No quiet introspection, no slow lyricism, no earnest confession, no realistic understatement, no moralising ending`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
