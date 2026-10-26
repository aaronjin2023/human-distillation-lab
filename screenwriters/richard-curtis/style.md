# Richard Curtis — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Curtis: warm romantic comedy, bumbling British understatement, love declared sideways through jokes, an ensemble of friends orbiting one hesitant hero, a happy ending earned by a public confession`
- ZH: 柯蒂斯风格：温暖浪漫喜剧，笨拙的英式含蓄，爱意借玩笑斜着说出口，一群朋友围着一个犹豫的主角，公开表白换来圆满结局。

## (2) 结构：三幕 / 序列 / 节拍

- 三幕式浪漫喜剧，常带多线并行与群像：第一幕婚礼/葬礼/书店相遇等社交场合切入；第二幕误会与错过层层累积，中点是几乎要成的表白被打断；第三幕公开场合的表白或追赶收束。多线在结尾交叉，多用蒙太奇收束。时间跨度数周至数月，少闪回。

## (3) 对话

- 对白轻快、机智、自嘲，短句与抢白并存；英式含蓄——真心话总藏在玩笑与道歉后面；配角负责插科打诨，主角负责结巴。动作描写简洁，多用场景提示而非心理描写；旁白极少。

## (4) 人物弧光

- 主角多为善良但犹豫的普通人（书店老板、葬礼致辞者、首相），弧光是从逃避到公开表白：不是变强，而是敢说了。人物关系以朋友群与家庭为底，爱情线之外总有一条友情或亲情线同步收束；结尾人物改变，世界也变暖。

## (5) 类型套路与创新

- 类型：浪漫喜剧；遵守套路——相遇、误会、追赶、圆满；打破的一条是：主角不靠魅力靠笨拙与真诚取胜。创新在剧本层面：把葬礼、婚礼等社交仪式写成结构骨架，多线群像一次收束。禁套路：不用冷峻反讽收尾，不用开放式悲剧结局。

## (6) 该写什么 / 不该写什么

- 该写：婚礼、葬礼等社交仪式开场、英式自嘲与含蓄表白、朋友群像与多线并行、公开场合的表白或追赶、温暖圆满的收束。
- 不该写：冷峻反讽收尾、开放式悲剧结局、直白肉麻的情话、让主角靠魅力而非真诚取胜、冗长的心理独白。
- Negative prompt: `No cynical ironic ending, no open-ended tragic close, no mawkish direct love declaration, no hero who wins by charm alone, no long interior monologue`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Richard Curtis, a shy man buys oden at a convenience store late at night and keeps bumping into the same woman at the same shelf. Jokes, apologies, friends egging him on. He finally declares himself in public, badly and sincerely.`
- 中文对照：柯蒂斯风格：一个害羞的男人在便利店深夜总在同一个货架撞见同一个女人，玩笑道歉朋友起哄，最后在公开场合笨拙而真诚地表白。
- Negative: `No cynical ironic ending, no tragic open ending, no mawkish love declaration, no long interior monologue`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
