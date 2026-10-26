# Quentin Tarantino — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Quentin Tarantino: chapters out of order, long talk before the violence, pop-culture trivia as dialogue, a needle drop written into the script, revenge served late and loud`
- ZH: 昆汀·塔伦蒂诺风格：章节打乱顺序，暴力之前先长谈，流行文化琐事即对白，配乐写进剧本，复仇来得又晚又响。

## (2) 结构：三幕 / 序列 / 节拍

- 章节式非线性结构：每章有自己的标题与高潮，时间线打乱后在结尾咬合；长对话场景后接突然的暴力；《低俗小说》三段交错，《被解救的姜戈》是复仇三幕。`impression`

## (3) 对话

- 对白是塔伦蒂诺的招牌：关于电影、音乐、食物的长篇闲聊，脏话与引经据典并存；人物在动手之前先用嘴确立风格；潜台词是‘我比你更懂这个世界’。`impression`

## (4) 人物弧光

- 主角类型：有规矩的亡命徒、复仇者、过气明星；弧光是‘守规矩的人被逼破戒’，或‘破戒的人赢回尊严’；结尾常是一场迟到的、私人化的复仇。`impression`

## (5) 类型套路与创新

- 类型：犯罪 / 西部 / 复仇，遵守 B 级片与类型片的套路；创新是把类型片的‘闲聊’写成主菜，把历史改写成复仇幻想。禁套路：不用克制的含蓄，不用‘暴力有后果’的说教收尾。`impression`

## (6) 该写什么 / 不该写什么

- 该写：章节标题与打乱的时间线、动手之前的长篇闲聊、流行文化引文与脏话、写进剧本的配乐提示、迟到的私人复仇。
- 不该写：克制含蓄的留白、暴力后的道德说教、平铺直叙的时间线、人物不说话就动手。
- Negative prompt: `No restrained understatement, no moralising after violence, no straight chronological timeline, no action without talk first, no polite dialogue`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Quentin Tarantino, two hitmen buy oden at a convenience store late at night and argue for ten minutes about the best convenience-store food, foot massages, and a movie none of them has seen. Then the violence. Chapter title first. Dialogue is the action.`
- 中文对照：昆汀·塔伦蒂诺风格：两个杀手深夜在便利店买关东煮，花十分钟争论哪家便利店的食物最好、足底按摩和一部谁都没看过的电影。然后才是暴力。先出章节标题。对白即动作。
- Negative: `No restrained understatement, no moralising after violence, no straight chronological timeline, no action without talk first, no polite dialogue`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
