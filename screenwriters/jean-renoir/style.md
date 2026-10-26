# Jean Renoir — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean Renoir: an ensemble with no villains, everyone has their reasons, a country house weekend where class is a game, deep-focus humanism, a tragedy that ends in a shrug and a song`
- ZH: 让·雷诺阿风格：没有反派的群像，每个人都有自己的道理，阶级即游戏的乡间周末，深焦式的人道主义，以耸肩与歌声收尾的悲剧。

## (2) 结构：三幕 / 序列 / 节拍

- 群像结构：《游戏规则》是乡间周末的多线并行，《大幻影》是战俘营里的阶级三幕；场景长、人物多、转场靠人物走动而非剪辑提示；高潮是一场误会酿成的悲剧，结局是众人散场。`impression`

## (3) 对话

- 对白是自然主义的口语：人物边走边谈、互相打断、话里有阶级与礼貌的密码；潜台词是‘规则人人知道，但没人明说’。`impression`

## (4) 人物弧光

- 主角类型：贵族、仆人、飞行员、演员；弧光是‘没有人变坏，也没有人得救’：人物在规则里打转，悲剧来自误会而非恶意；结局是散场与歌声。`impression`

## (5) 类型套路与创新

- 类型：喜剧 / 剧情 / 战争，遵守‘乡间周末’套路；创新是把阶级写成游戏规则，把战争写成人与人之间的礼貌。禁套路：不用脸谱化的反派，不用道德审判收尾。`impression`

## (6) 该写什么 / 不该写什么

- 该写：没有反派的群像、乡间周末多线并行、阶级即游戏规则、误会酿成的悲剧、散场与歌声的收束。
- 不该写：脸谱化反派、道德审判收尾、单一主角拯救世界、直白的阶级控诉。
- Negative prompt: `No cartoon villain, no moralising verdict, no single hero who saves the day, no blunt class lecture, no ending that punishes one side only`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jean Renoir, a small Yorkshire terrier sits on a subway seat during a weekend trip, and the passengers around it — a worker, a lady, a soldier, a student — each have their reasons for wanting the seat. No villain. Everyone is polite. The tragedy is a misunderstanding.`
- 中文对照：让·雷诺阿风格：一个周末的旅途中，一只约克夏犬坐在地铁座位上，周围的乘客——工人、贵妇、士兵、学生——各有各的要座位的道理。没有反派。人人都很客气。悲剧是一场误会。
- Negative: `No cartoon villain, no moralising verdict, no single hero who saves the day, no blunt class lecture, no ending that punishes one side only`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
