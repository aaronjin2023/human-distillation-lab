# Hirokazu Kore-eda — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hirokazu Kore-eda: families that are not blood but choice, everyday life observed without judgment, children who see clearly, a gentle ending that does not forgive everything`
- ZH: 是枝裕和风格：不是血缘而是选择的家庭，日常被不带评判地注视，看得清楚的孩子，温柔但不原谅一切的结尾。

## (2) 结构：三幕 / 序列 / 节拍

- 日常家庭三幕：第一幕一个非典型家庭（寄养、偷窃、留守）切入，日常细节累积；第二幕一次离开、一次坦白或一次死亡把家庭推到边缘，中点是人物发现“家人”是可以选择的；第三幕不靠圆满收束，靠人物的各自前行收束。时间跨度数周至数月，多用季节与食事分段。

## (3) 对话

- 对白日常、克制，孩子的话直接而锋利；成人多用寒暄藏住真相；潜台词是家庭——没说出口的爱最重。动作描写多写吃饭、洗澡、走路。

## (4) 人物弧光

- 主角多为孩子与非典型家长，弧光是从依赖到看清：孩子比成人更早看清真相，成人学会放手。人物关系是选择构成的家庭；结局人物不团圆，只各自前行。

## (5) 类型套路与创新

- 类型：家庭伦理剧；遵守套路——家庭、日常、离别；打破的一条是：血缘不是家庭的定义，选择才是。创新在剧本层面：把“偷来的家人”写成结构，让日常细节承担道德重量。禁套路：不用煽情高潮，不用道德审判，不用大团圆。

## (6) 该写什么 / 不该写什么

- 该写：非血缘的选择式家庭、日常细节与食事、看得清楚的孩子、温柔克制的对白、各自前行的收束。
- 不该写：煽情高潮、道德审判、大团圆、直白的说教、让孩子说成人式台词。
- Negative prompt: `No sentimental climax, no moral verdict, no happy reunion, no direct preaching, no child speaking adult lines`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Hirokazu Kore-eda, a family that is not blood buys oden at a convenience store late at night and shares it on the curb. The children see clearly. No one says thank you out loud.`
- 中文对照：是枝裕和风格：一个不是血缘的一家人在便利店深夜买关东煮，坐在路边分着吃，孩子看得清楚，谁都没有大声说谢谢。
- Negative: `No sentimental climax, no moral verdict, no happy reunion, no direct preaching`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
