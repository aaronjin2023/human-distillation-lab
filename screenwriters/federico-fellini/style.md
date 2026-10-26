# Federico Fellini — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Federico Fellini: a parade of grotesques, dream and memory in the same street, an innocent clown among the circus, episodes that drift like a dream, a finale where everyone dances`
- ZH: 费德里科·费里尼风格：怪诞人物的游行，梦与记忆在同一条街上，天真小丑置身马戏团，如梦般漂移的插曲，所有人起舞的结尾。

## (2) 结构：三幕 / 序列 / 节拍

- 插曲式游行结构：《甜蜜生活》是七天七夜的插曲，《八部半》是梦、记忆与现实的交织，《大路》是流浪艺人的公路；转折点常是一场梦，结局是众人起舞或独自离去。`impression`

## (3) 对话

- 对白稀疏、仪式化：人物说得少，形象与场面说话；独白常是梦呓；潜台词是‘这是一场梦吗’。`impression`

## (4) 人物弧光

- 主角类型：天真的小丑、迷失的导演、流浪艺人；弧光是‘天真遭遇怪诞’：人物在怪诞世界里走一遭，结局不是成长，是接受——或独自离去。`impression`

## (5) 类型套路与创新

- 类型：现代主义 / 梦幻 / 讽刺，遵守‘游行’套路；创新是把梦写进现实结构，把马戏团写成世界。禁套路：不用线性因果，不用现实主义解释，不用道德审判。`impression`

## (6) 该写什么 / 不该写什么

- 该写：怪诞人物游行、梦与记忆交织、插曲式漂移结构、天真小丑视角、众人起舞的收束。
- 不该写：线性因果、现实主义解释、道德审判、人物靠努力改变世界。
- Negative prompt: `No linear causality, no realist explanation, no moral judgement, no hero who changes the world by effort, no dream explained away in the morning`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Federico Fellini, a small Yorkshire terrier sits on a subway seat and the whole car becomes a circus: a clown, a giantess, a priest, a starlet. Dream and memory in the same carriage. Everyone dances at the end. No explanation.`
- 中文对照：费德里科·费里尼风格：一只约克夏犬坐在地铁座位上，整节车厢变成马戏团：小丑、巨女、神父、女明星。梦与记忆在同一节车厢。结尾所有人起舞。没有解释。
- Negative: `No linear causality, no realist explanation, no moral judgement, no hero who changes the world by effort, no dream explained away in the morning`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
