# Douglas MacArthur — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of MacArthur: bold amphibious envelopment, strike the enemy rear, island-hopping, bypass strongpoints, audacity backed by logistics`
- ZH: 麦克阿瑟风格：大胆两栖包抄，打敌人后方，跳岛作战，绕过坚固据点，胆略以后勤为后盾。

## (2) 情报与侦察

- 情报来源：空中与海上侦察、潮汐与水文测绘、密码情报；仁川的关键是潮汐与航道情报。`artifact`

## (3) 地形与机动

- 地形与机动：跳岛、两栖包抄、切断敌退路；绕过坚固据点，不逐岛争夺。`artifact`

## (4) 后勤与补给

- 后勤与补给：两栖登陆的命脉是舰队与滩头补给；潮汐窗口决定一切。`artifact`

## (5) 决断与节奏

- 决断与节奏：大胆、冒险、但算过潮汐与补给；别人说不可能的地方，恰是包抄的缺口。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 两栖包抄打敌人后方
- 跳岛、绕过坚固据点
- 算准潮汐与登陆窗口
- 登陆后直插纵深、切断退路
- 不该打：
- 逐岛争夺坚固据点
- 没有潮汐与水文情报就登陆
- 登陆后停在滩头不动
- 只打正面、不抄后路
- Negative prompt: `No island-by-island attrition against strongpoints, no landing without tide and hydrographic intelligence, no halt on the beachhead, no frontal attack without envelopment`

## (7) 测试提示词示例（现代题材：台风后海岛救援行动）

- Prompt: `In the style of MacArthur, plan a modern island relief operation after a typhoon. Bypass the blocked main port, land at an unexpected cove at high tide, cut straight to the isolated towns inland.`
- 中文对照：麦克阿瑟风格：筹划一次台风后海岛救援。绕过被堵主港，趁涨潮在意外港湾登陆，直插内陆孤立城镇。
- Negative: `No island-by-island attrition against strongpoints, no landing without tide and hydrographic intelligence, no halt on the beachhead, no frontal attack without envelopment`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
