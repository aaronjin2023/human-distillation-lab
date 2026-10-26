# Pedro Fernandes de Queirós — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pedro Fernandes de Queirós: a search for a southern continent that ends in an island, memorials written to a king as the voyage's second half, the log as a petition, the continent always one more voyage away`
- ZH: 佩德罗·费尔南德斯·德·基罗斯风格：搜寻南方大陆却止于一座岛，请愿书写给国王当作航行的下半场，日志是一份请愿书，大陆永远在下一次航行里。

## (2) 导航方法

- 定位：推测航法 + 纬度观测，南太平洋寻南方大陆，靠纬度与航向西行。`artifact`
- 定向：秘鲁出发向西偏南，寻传说中的南方大陆，抵圣埃斯皮里图岛（今瓦努阿图）。`artifact`
- 误差容忍：以岛为大陆，误差以请愿书的修辞掩盖，蒸馏记其航法不采其判断。`artifact`

## (3) 造船与帆装

- 船型：三船船队（1605），盖伦帆船，载定居者。`artifact`
- 帆装：横帆远洋，宜信风西行。`impression`
- 补给：秘鲁补给，岛屿逐岛补给；托雷斯分船后补给更紧。`artifact`

## (4) 航线规划习惯

- 路线：秘鲁卡亚俄—西行—圣埃斯皮里图岛（1606）—返航墨西哥；托雷斯分船南行发现托雷斯海峡（见 #51）。`artifact`
- 节奏：寻陆慢，岛上停留数周建定居点，风暴与分船后返航。`artifact`
- 返航：返墨西哥后赴马德里呈请愿书，余生请愿未果。`artifact`

## (5) 日志与海图语言

- 日志体例：航行见于其本人呈菲利普三世的请愿书（memorials）与同行者记述；请愿书即航行记录，修辞多于实测。`artifact`
- 海图语言：岛屿、海湾与定居点为主，南方大陆为修辞。`artifact`
- 命名习惯：圣埃斯皮里图岛以圣灵命名，湾以圣菲利普命名。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 圣埃斯皮里图岛
- 南方大陆搜寻航线
- 请愿书体航行记录
- 岛屿定居尝试
- 不该探索：
- No island claimed as a continent
- No memorial written that the log cannot support
- No settlement founded without water and food counted
- No westward run without a return latitude
- Negative prompt: `No island claimed as a continent, No memorial written that the log cannot support, No settlement founded without water and food counted, No westward run without a return latitude`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Pedro Fernandes de Queirós, an uncrewed search vessel hunts a southern continent in 2026 and ends at an island, its memorials to the mission written as petitions, the continent always one more voyage away.`
- 中文对照：佩德罗·费尔南德斯·德·基罗斯风格：一艘无人搜寻船2026年搜寻南方大陆却止于一座岛，请愿书写给任务方当作航行的下半场，大陆永远在下一次航行里。
- Negative: `No island claimed as a continent, No memorial written that the log cannot support, No settlement founded without water and food counted, No westward run without a return latitude`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
