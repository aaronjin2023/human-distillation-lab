# Kogo Noda — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kogo Noda: the quiet craftsman behind Ozu, everyday family life, seasons and farewells, dialogue that says little and means much, a smile that hides goodbye`
- ZH: 野田高梧风格：小津背后的安静工匠，日常家庭生活，季节与告别，话少意多，微笑藏着告别。

## (2) 结构：三幕 / 序列 / 节拍

- 日常切片结构，与小津条目同一骨架：家庭日常场景串联，无大转折；季节标记分段，空镜头收束。野田的贡献在剧本层面：家庭对话的日常质感与世代关系的分寸感。

## (3) 对话

- 对白日常寒暄、客套、重复，要紧的话总被岔开；潜台词是亲情——没说出口的比说出口的重。

## (4) 人物弧光

- 主角多为父母与子女，弧光是接受：女儿出嫁、父母老去，人物不反抗，只微笑接受。

## (5) 类型套路与创新

- 类型：家庭伦理剧；遵守套路——家庭、季节、告别；打破的一条是：全片没有戏剧冲突，日常即全部。创新在剧本层面：与小津共同确立“不说”的结构。禁套路：不用大转折，不用煽情高潮，不用直白表白。

## (6) 该写什么 / 不该写什么

- 该写：家庭日常与季节、寒暄底下的告别、父母与子女的体贴、低机位与空镜头、微笑的收束。
- 不该写：大转折、煽情高潮、直白表白、类型反转、让人物说清自己的感受。
- Negative prompt: `No dramatic twist, no sentimental climax, no direct declaration, no genre twist, no character who explains their own feelings`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Kogo Noda, an old couple buys oden at a convenience store late at night on a visit to Tokyo. Small talk, pauses. Their children are busy. They smile, and go home.`
- 中文对照：野田高梧风格：一对老夫妇到东京探望子女，深夜在便利店买关东煮，寒暄、停顿，子女很忙，他们笑笑，回家。
- Negative: `No dramatic twist, no sentimental climax, no direct declaration, no genre twist`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
