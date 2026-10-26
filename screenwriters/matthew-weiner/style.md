# Matthew Weiner — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Matthew Weiner: identity as a costume you cannot take off, period detail as psychology, subtext thicker than dialogue, people who lie to themselves first`
- ZH: 韦纳风格：身份是一件脱不下的戏服，时代细节即心理，潜台词比对白更厚，人先骗自己。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧多线并行：《广告狂人》以广告公司为容器，每季一个时代节点，单集以日常场景收尾；时间跨度十年，闪回揭示身份秘密。场次长、切换缓，靠细节累积推进。

## (3) 对话

- 对白克制、优雅，人物用寒暄、玩笑、沉默交锋；潜台词极重，一句日常问候可藏三层意思。动作描写细致（点烟、倒酒、眼神），对白与动作互相拆台。旁白不用。

## (4) 人物弧光

- 主角唐·德雷柏：身份造假者，弧光是原地打转——每季看似坦白，实则换一件戏服；人物不成长，时代在变。人物关系以婚姻与职场的双重伪装为主。

## (5) 类型套路与创新

- 类型：时代剧 / 家庭剧。遵守时代细节的考据，打破‘时代剧靠大事’的套路：大事在背景，小事在前景。创新在把广告写成身份隐喻，把潜台词写成主角。

## (6) 该写什么 / 不该写什么

- 该写：身份作戏服、时代细节即心理、潜台词比对白厚、日常场景收尾、原地打转的弧光。
- 不该写：直白解释身份、煽情收束、类型化时代桥段、功能性对白、人物突然坦白。
- Negative prompt: `No on-the-nose identity reveal, no sentimental ending, no period cliché, no functional dialogue, no sudden confession`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Matthew Weiner, a man buys oden at a convenience store late at night in 1962. He lights a cigarette he does not want. The clerk calls him by a name that is not his. He does not correct her.`
- 中文对照：韦纳风格：一个男人深夜在便利店买关东煮，时间是 1962 年。他点了一支并不想抽的烟。店员叫他一个不是他的名字。他没有纠正。
- Negative: `No on-the-nose identity reveal, no sentimental ending, no period cliché, no functional dialogue, no sudden confession`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
