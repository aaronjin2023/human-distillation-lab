# Noah Baumbach — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Noah Baumbach: literate New York intellectuals arguing until the argument becomes the marriage, long scenes that refuse to cut, a divorce or a family dinner as a chamber play`
- ZH: 诺亚·鲍姆巴赫风格：博学的纽约知识分子吵到争吵本身成了婚姻，长镜头般不肯切断的场景，一场离婚或一顿家宴即室内剧。

## (2) 结构：三幕 / 序列 / 节拍

- 室内剧结构：长场景、少转场；《婚姻故事》是双面结构，夫妻各执一面；《鱿鱼和鲸》是家庭分裂的两条线；高潮是一场吵到失控、又吵回温情的长戏。`impression`

## (3) 对话

- 对白是博学的、重叠的、互相打断的争论：文学、电影、育儿、房租都能吵起来；人物用聪明话掩饰脆弱；潜台词是‘我还爱你，但我不知道怎么说’。`impression`

## (4) 人物弧光

- 主角类型：离婚的知识分子、想当艺术家的年轻人、家庭里的孩子；弧光是‘争吵后的和解不是复合，是承认’：人物没有赢回婚姻，但赢回了诚实。`impression`

## (5) 类型套路与创新

- 类型：家庭伦理 / 成长喜剧，遵守‘知识分子家庭剧’套路；创新是把离婚写成双面体，不站队、不审判。禁套路：不用善恶分明的离婚官司，不用煽情和解。`impression`

## (6) 该写什么 / 不该写什么

- 该写：重叠打断的长争论、双面结构（夫妻各执一面）、室内剧式长场景、聪明话之下的脆弱、承认代替复合的收束。
- 不该写：善恶分明的离婚官司、煽情和解、一方全错一方全对、旁白解释人物动机。
- Negative prompt: `No good-versus-evil divorce, no sentimental reconciliation, no one side entirely right, no voiceover explaining motive, no shouting without vulnerability underneath`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Noah Baumbach, a divorced couple meet by accident at a convenience store late at night buying oden, and argue about the custody schedule, the apartment, and a book one of them never finished. Long scene, overlapping dialogue, it ends in honesty, not reunion.`
- 中文对照：诺亚·鲍姆巴赫风格：一对离异夫妻深夜在便利店买关东煮偶遇，争论探视时间、公寓和一本对方从没读完的书。长场景、重叠对白，收在诚实，而不是复合。
- Negative: `No good-versus-evil divorce, no sentimental reconciliation, no one side entirely right, no voiceover explaining motive, no shouting without vulnerability underneath`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
