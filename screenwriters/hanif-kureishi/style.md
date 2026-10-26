# Hanif Kureishi — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hanif Kureishi: suburban London, second-generation immigrants caught between two cultures, sex and ambition as rebellion, witty unsentimental dialogue, no one is purely victim or villain`
- ZH: 库雷西风格：伦敦郊区，第二代移民夹在两种文化之间，性与野心即反叛，机智而不煽情的对白，没有纯粹的受害者或恶人。

## (2) 结构：三幕 / 序列 / 节拍

- 三幕式社会喜剧/剧情：第一幕郊区日常切入，人物被家庭与族群期待困住；第二幕一份生意、一段恋情或一次越界把人物推出原地，中点是身份认同的公开冲突；第三幕不解决身份问题，只让人物选一条自己的路。多线家庭与恋情并行，时间跨度数月。

## (3) 对话

- 对白机智、直率、带刺，短句与抢白多；移民家庭内部用英语夹杂南亚口音与家庭用语；潜台词是身份试探——谁在装英国人、谁在装巴基斯坦人。性话题直言不讳，少用隐喻遮掩。

## (4) 人物弧光

- 主角多为第二代移民青年，弧光是从被两种文化拉扯到主动拼贴自己的身份：不回归、不融入、不选边。人物关系是家庭、恋人与族群的三重拉力；结局人物不“找到根”，只是学会带着矛盾生活。

## (5) 类型套路与创新

- 类型：社会喜剧与移民剧情；遵守套路——家庭冲突、跨种族恋情；打破的一条是：拒绝受害者叙事，人物有欲望、有算计、有幽默。创新在剧本层面：把撒切尔时代的创业与阶级流动写进移民故事。禁套路：不用悲情煽情，不用文化本质主义的定论。

## (6) 该写什么 / 不该写什么

- 该写：伦敦郊区与移民家庭、身份拉扯与文化拼贴、机智带刺的对白、性与野心作为反叛、不选边的开放式收束。
- 不该写：悲情煽情的受害者叙事、文化本质主义定论、直白说教的政治对白、让人物只当符号、大团圆式身份和解。
- Negative prompt: `No sentimental victim narrative, no cultural essentialism, no preachy political dialogue, no character as mere symbol, no neat identity reconciliation`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Hanif Kureishi, a second-generation immigrant buys oden at a convenience store late at night and argues with his uncle on the phone about the family shop. Witty, unsentimental, no one is purely right. He keeps both the shop keys and his own plans.`
- 中文对照：库雷西风格：一个第二代移民深夜在便利店买关东煮，电话里和叔叔争论家里的铺子，机智不煽情，谁都不全对，他既留着铺子钥匙也留着自己的计划。
- Negative: `No sentimental victim narrative, no cultural essentialism, no preachy political dialogue, no neat identity reconciliation`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
