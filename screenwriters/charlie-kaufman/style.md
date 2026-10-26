# Charlie Kaufman — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charlie Kaufman: nested consciousness, memory as a maze, a writer writing himself into the script, identity that slips, no clean resolution, the joke that turns sad`
- ZH: 查理·考夫曼风格：意识嵌套，记忆如迷宫，编剧把自己写进剧本，身份不断滑脱，没有干净的结局，笑话到最后变悲伤。

## (2) 结构：三幕 / 序列 / 节拍

- 结构即主题：嵌套、循环、倒叙与自我指涉；《改编剧本》把‘写剧本’本身写成剧情；《美丽心灵的永恒阳光》用倒放的记忆作时间线；转折点不是事件，而是主角意识到自己在做梦。`impression`

## (3) 对话

- 对白是焦虑的内心独白外化：自我怀疑、哲学追问、重复与自我纠正；人物常在说话中途推翻自己上一句；潜台词比台词更长。`impression`

## (4) 人物弧光

- 主角类型：被困在自己脑子里的男人（编剧、木偶师、失忆者）；弧光是‘原地打转的顿悟’：他看清了自己的困境，但困境没有消失；结尾不是胜利，是接受。`impression`

## (5) 类型套路与创新

- 类型：奇幻 / 爱情 / 元电影，遵守类型外壳（钻进别人脑子、删除记忆），打破的恰是类型承诺——不给答案、不给救赎。禁套路：不用线性因果，不用功能性对白交代情节。`impression`

## (6) 该写什么 / 不该写什么

- 该写：意识嵌套与自我指涉、记忆倒放与循环、身份滑脱（你是我，我是你）、焦虑的内心独白、笑话变悲伤的收束。
- 不该写：线性因果、功能性交代情节的对白、干净利落的大团圆、主角彻底战胜心魔。
- Negative prompt: `No linear causality, no functional expository dialogue, no clean happy ending, no hero who conquers his own mind, no joke without sadness underneath`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Charlie Kaufman, a small Yorkshire terrier sits on a subway seat, and a screenwriter realises he is writing this scene, and the dog is watching him write it. Memory rewinds. Who is watching whom? Dialogue that contradicts itself. No resolution.`
- 中文对照：查理·考夫曼风格：一只约克夏犬坐在地铁座位上，一位编剧意识到自己正在写这一幕，而狗正看着他写。记忆倒放。谁在看谁？对白自我矛盾。没有结局。
- Negative: `No linear causality, no functional expository dialogue, no clean happy ending, no hero who conquers his own mind, no joke without sadness underneath`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
