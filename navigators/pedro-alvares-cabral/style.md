# Pedro Álvares Cabral — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pedro Álvares Cabral: a great fleet on a wide Atlantic arc that overshoots into a new coast, a landing logged and claimed, then the monsoon run to India, the voyage as a fleet operation with losses counted plainly`
- ZH: 佩德罗·阿尔瓦雷斯·卡布拉尔风格：大船队走宽阔大西洋弧线， 偏航撞见新海岸，登陆记入日志并宣称，再乘季风去印度，航行是船队行动，损失直记不讳。

## (2) 导航方法

- 定位：推测航法 + 纬度观测，大西洋大弧向西偏航，靠纬度判断已到巴西海岸。`artifact`
- 定向：离岸大弧借信风南下，向西偏航是刻意取道还是风漂，学界有争议，见 conflicts。`impression`
- 误差容忍：船队分散后各自按纬度与季风重聚，失散船只不等待。`impression`

## (3) 造船与帆装

- 船型：13 艘大船队，卡拉克帆船，载货、武装与殖民并重。`artifact`
- 帆装：横帆远洋，宜大弧顺风航行。`impression`
- 补给：巴西登陆补给淡水，莫桑比克—马林迪—卡利卡特逐站补给；好望角风暴失 4 船。`artifact`

## (4) 航线规划习惯

- 路线：里斯本—大西洋大弧—巴西（1500）—好望角—莫桑比克—卡利卡特。`artifact`
- 节奏：大弧段快，巴西停留 10 日立标宣称，印度段乘季风。`artifact`
- 返航：卡利卡特冲突后返航，船队损失近半。`artifact`

## (5) 日志与海图语言

- 日志体例：无亲笔日志传世，航路见于编年史与船员佩罗·瓦斯·德·卡米尼亚致国王信（巴西登陆首份记录）。`artifact`
- 海图语言：登陆点与海岸走向为主，巴西海岸为新绘一段。`artifact`
- 命名习惯：巴西初名“真十字架地”，后改名；以圣人名命名登陆日。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 巴西海岸与登陆点
- 大西洋大弧向西偏航法
- 巴西—好望角—印度航线
- 大船队远洋组织
- 不该探索：
- No fleet sailed without a rendezvous latitude
- No coast claimed without a landing and a written record
- No storm sailed through at the Cape without dispersing the fleet
- No return without counting the ships lost
- Negative prompt: `No fleet sailed without a rendezvous latitude, No coast claimed without a landing and a written record, No storm sailed through at the Cape without dispersing the fleet, No return without counting the ships lost`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Pedro Álvares Cabral, a fleet of uncrewed cargo ships takes a wide Atlantic arc in 2026 and overshoots into a new coast, a landing logged and claimed, then the monsoon run onward.`
- 中文对照：佩德罗·阿尔瓦雷斯·卡布拉尔风格：一支无人货运船队2026年走宽阔大西洋弧线，偏航撞见新海岸，登陆记入日志并宣称，再乘季风继续前行。
- Negative: `No fleet sailed without a rendezvous latitude, No coast claimed without a landing and a written record, No storm sailed through at the Cape without dispersing the fleet, No return without counting the ships lost`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
