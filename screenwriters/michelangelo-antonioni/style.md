# Michelangelo Antonioni — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michelangelo Antonioni: a disappearance that is never explained, alienation in beautiful empty spaces, long silences where dialogue used to be, a couple drifting apart, an ending that refuses to say what happened`
- ZH: 米开朗基罗·安东尼奥尼风格：从不解释的失踪，美丽空旷空间里的疏离，对白曾经在的地方只剩长久的沉默，渐行渐远的一对，拒绝交代发生了什么的结局。

## (2) 结构：三幕 / 序列 / 节拍

- 消解结构：《奇遇》是失踪后情节的消解，《放大》是照片放大后的不确定，《蚀》是人物消失、只剩空镜头；转折点常是‘什么都没发生’的一刻；结局是空镜头或沉默。`impression`

## (3) 对话

- 对白极简、疏离：人物说得少，沉默即对白；《放大》的英语对白由爱德华·邦德执笔；潜台词是‘我们之间已经没什么可说的了’。`impression`

## (4) 人物弧光

- 主角类型：失踪的女人、摄影师、疏离的恋人；弧光是‘渐行渐远’：人物没有成长，只是漂远；结局不是分手，是空镜头。`impression`

## (5) 类型套路与创新

- 类型：现代主义 / 心理剧情，遵守‘疏离’套路；创新是把情节的消解本身写成结构，把空镜头写成结局。禁套路：不用解释失踪，不用煽情和解，不用情节填满沉默。`impression`

## (6) 该写什么 / 不该写什么

- 该写：从不解释的失踪、空旷空间与长久沉默、情节的消解、渐行渐远的恋人、空镜头式收束。
- 不该写：解释失踪、煽情和解、情节填满沉默、人物坦白心意。
- Negative prompt: `No explaining the disappearance, no sentimental reconciliation, no plot filling the silence, no character confessing feelings plainly, no ending that says what happened`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Michelangelo Antonioni, a man writes a letter to himself ten years from now, then leaves it unsent. A woman disappears from the subway car. The camera stays on the empty seat. Long silence. No explanation.`
- 中文对照：米开朗基罗·安东尼奥尼风格：一个男人给十年后的自己写信，然后没有寄出。一个女人从地铁车厢里消失了。镜头停在空座位上。长久的沉默。没有解释。
- Negative: `No explaining the disappearance, no sentimental reconciliation, no plot filling the silence, no character confessing feelings plainly, no ending that says what happened`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
