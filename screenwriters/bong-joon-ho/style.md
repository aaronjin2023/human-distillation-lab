# Bong Joon-ho — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bong Joon-ho: genre that flips halfway, class upstairs and downstairs, dark comedy turning into tragedy without warning, meticulous detail that pays off, no one innocent`
- ZH: 奉俊昊风格：类型中途翻转，楼上楼下的阶级，黑色喜剧毫无预警地转入悲剧，处处伏笔的细节，没有无辜者。

## (2) 结构：三幕 / 序列 / 节拍

- 类型翻转三幕：第一幕类型片开场（喜剧、悬疑、科幻），人物与规则交代清楚；第二幕中点类型整体翻转——喜剧变悲剧、悬疑变社会批判；第三幕不靠圆满收束，靠一个细节的回收（石头、楼梯、气味）收束。时间跨度数日至数月，多用空间（楼上楼下、车厢）分段。

## (3) 对话

- 对白精确、带黑色幽默，阶级差异藏在用词与礼貌里；人物多用玩笑藏住恶意；潜台词是阶级——气味、楼梯、半地下室即语言。动作描写多写空间与细节。

## (4) 人物弧光

- 主角多为底层家庭或小人物，弧光是从钻营到崩塌：不是成长，是终于看清楼梯没有尽头。人物关系是楼上与楼下的互相渗透；结局人物不胜利，只留下气味。

## (5) 类型套路与创新

- 类型：黑色喜剧、社会惊悚、科幻；遵守套路——类型开场、翻转、回收；打破的一条是：类型在中段整体翻转，喜剧与悲剧同一具身体。创新在剧本层面：把阶级写成空间（半地下室、楼梯、车厢），让细节在结尾回收。禁套路：不用说教收尾，不用大团圆，不用善恶二元。

## (6) 该写什么 / 不该写什么

- 该写：类型中途翻转、楼上楼下的阶级空间、黑色幽默与细节回收、气味、楼梯、石头等物件、不圆满的收束。
- 不该写：说教式收尾、大团圆、善恶二元、直白的阶级控诉、让翻转只为惊奇。
- Negative prompt: `No preachy ending, no happy reunion, no good-versus-evil binary, no direct class indictment, no twist for surprise alone`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Bong Joon-ho, a poor family buys oden at a convenience store late at night and schemes to get a job upstairs. Dark comedy, then the genre flips. The smell gives them away.`
- 中文对照：奉俊昊风格：一家穷人深夜在便利店买关东煮，盘算着怎么去楼上找份工作，黑色喜剧，然后类型翻转，气味出卖了他们。
- Negative: `No preachy ending, no happy reunion, no good-versus-evil binary, no direct class indictment`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
