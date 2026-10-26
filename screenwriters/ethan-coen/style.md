# Ethan Coen — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ethan Coen (with Joel Coen): vernacular absurdism, a stoner philosopher who is right by accident, polite people saying terrible things, the joke that stays deadpan while the world burns`
- ZH: 伊桑·科恩风格（与乔尔·科恩合著）：方言荒诞主义，误打误撞说对的瘾君子哲学家，客气人说可怕的话，世界着火时笑话依然面无表情。

## (2) 结构：三幕 / 序列 / 节拍

- 与乔尔·科恩文件夹相同的犯罪几何学：小计划连锁失控；本文件夹更强调‘误会链’——人物各说各话，情节靠听错、会错意推进；结局同样拒绝救赎。`impression`

## (3) 对话

- 对白是伊桑侧重的核心：方言、重复、纠正、哲学化的胡话；‘督爷’式的慵懒独白与明尼苏达客气话并置；人物越是一本正经，台词越荒诞；潜台词是‘没人真的在听对方说话’。`impression`

## (4) 人物弧光

- 主角类型：误打误撞的局外人、说胡话的先知、倒霉的普通人；弧光是‘原地打转的清醒’：人物在结尾看清了荒诞，但什么都没改变。`impression`

## (5) 类型套路与创新

- 类型：犯罪 / 黑色喜剧 / 西部；创新是把方言喜剧写进犯罪片，把哲学写进瘾君子的胡话。禁套路：不用煽情救赎，不用聪明人翻盘，不用直白说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：方言与重复纠正式对白、各说各话的误会链、慵懒的哲学胡话、客气话之下的威胁、面无表情的荒诞。
- 不该写：煽情救赎、聪明人翻盘、直白说教、人物突然变得机智。
- Negative prompt: `No sentimental redemption, no clever hero who outsmarts fate, no direct moralising, no character who suddenly becomes witty, no warm reassurance`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Ethan Coen (with Joel Coen), a man writes a letter to himself ten years from now, but keeps getting interrupted by a neighbour who wants to talk about his rug, his bowling league, and a briefcase that is definitely not his. Polite, deadpan, nothing is resolved.`
- 中文对照：伊桑·科恩风格（与乔尔·科恩合著）：一个男人给十年后的自己写信，却不断被邻居打断，邻居要谈他的地毯、保龄球队和一只肯定不是他的公文包。客气、面无表情、什么都没解决。
- Negative: `No sentimental redemption, no clever hero who outsmarts fate, no direct moralising, no character who suddenly becomes witty, no warm reassurance`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
