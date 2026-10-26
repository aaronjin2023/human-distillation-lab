# Yasujiro Ozu — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yasujiro Ozu: everyday life in low still shots, parents and children who cannot say what matters, seasons passing in a hallway, a smile that hides a farewell`
- ZH: 小津风格：低机位静止镜头里的日常，父母与子女说不出要紧的话，季节在走廊里过去，微笑藏着告别。

## (2) 结构：三幕 / 序列 / 节拍

- 日常切片结构：几乎无大转折，全片由家庭日常场景串联；第一幕家庭聚首，第二幕一次出嫁、一次探望或一次离别慢慢逼近，中点常常是一句未说出口的话；第三幕人物各自归位，收束在空镜头（走廊、烟囱、火车）。时间跨度数日至数月，多用季节标记。

## (3) 对话

- 对白日常寒暄、客套、重复，要紧的话总被岔开；人物用“是啊”“天气不错”藏住告别；潜台词是亲情——没说出口的比说出口的重。动作描写极少，多写吃饭、喝茶、走路。

## (4) 人物弧光

- 主角多为父母与子女，弧光不是成长而是接受：女儿出嫁、父母老去，人物不反抗，只微笑接受。人物关系是家庭内部的体贴与疏离；结局人物不改变，季节变了。

## (5) 类型套路与创新

- 类型：家庭伦理剧；遵守套路——家庭、季节、告别；打破的一条是：全片没有戏剧冲突，日常即全部。创新在剧本层面：把“不说”写成结构，让空镜头承担情感。禁套路：不用大转折，不用煽情高潮，不用直白表白。

## (6) 该写什么 / 不该写什么

- 该写：家庭日常与季节、低机位与空镜头、寒暄底下的告别、父母与子女的体贴、微笑的收束。
- 不该写：大转折、煽情高潮、直白表白、类型反转、让人物说清自己的感受。
- Negative prompt: `No dramatic twist, no sentimental climax, no direct declaration, no genre twist, no character who explains their own feelings`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Yasujiro Ozu, a small Yorkshire terrier sits on a subway seat, watched by commuters who look away. No big event. Small talk, pauses, a glance. Nothing is explained.`
- 中文对照：小津风格：一只约克夏犬坐在地铁座位上，乘客们看了一眼又移开视线，没有大事件，寒暄、停顿、一个眼神，什么都不解释。
- Negative: `No dramatic twist, no sentimental climax, no direct declaration, no genre twist`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
