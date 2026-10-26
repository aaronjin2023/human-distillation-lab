# Pearl Primus — 舞蹈风格规格 style.md（给视频模型）

> 只描述舞蹈，不描述人生。引用演出录像时注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pearl Primus: African American modern dance, high leaps with grounded landings, African ritual rhythms, protest as movement, the body as testimony, no ballet line`
- ZH: 珀尔·普里默斯风格：非裔现代舞，高跳而落地的跳跃，非洲仪式节奏，抗议即动作，身体即证言，不取芭蕾线条。

## (2) 动作语汇

- 高跳：腾空高、落地沉，跳跃的落点是风格标记。`artifact`
- 非洲仪式节奏：以非洲仪式舞蹈的节奏为动作来源。`artifact`
- 抗议即动作：以身体直接表达抗议，动作即证言。`impression`
- 《芳加》：以西非欢迎舞为题材的标志作品。`artifact`

## (3) 身体线条与空间调度

- 身体线条：线条有力，跳跃时身体舒展、落地时重心极沉；躯干的扭动富弹性；重心可高可低，腾空与贴地对照强烈。`impression`
- 空间调度：独舞与群舞并重，跳跃铺满舞台；队形随仪式节奏聚散；视线随跳跃的抛物线移动。`impression`

## (4) 节奏与音乐关系

- 节奏：跟非洲鼓乐走，节奏强烈而切分；跳跃的腾空与落地即节奏的句读；停顿处是证言的落点。`impression`

## (5) 情绪表达

- 情绪：抗议、庄严、狂喜同体；情绪靠跳跃的力度与节奏的密度传达，不靠面部夸张；证言中有力量。`impression`

## (6) 该编什么 / 不该编什么

- 该编：非裔现代舞的高跳与沉落地、非洲仪式节奏、抗议即动作的独舞、《芳加》的欢迎舞队形、身体即证言的直视。
- 不该编：no ballet pointe work or soft landings, no literal mime, no restrained minimalism, no decorative movement without testimony, no single-rhythm unison。
- Negative prompt: `no ballet pointe work or soft landings, no literal mime, no restrained minimalism, no decorative movement without testimony, no single-rhythm unison`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Pearl Primus, a person buys oden at a convenience store late at night, African American modern dance, high leaps with grounded landings, African ritual rhythms, protest as movement, the body as testimony, no ballet line`
- 中文对照：按上述英文提示词，以该舞蹈家风格编排该现代题材。
- Negative: `no ballet pointe work or soft landings, no literal mime, no restrained minimalism, no decorative movement without testimony, no single-rhythm unison`
- 检验点：动作语汇是否对；身体线条与空间调度是否对；节奏与情绪是否对；禁区写法是否出现。
