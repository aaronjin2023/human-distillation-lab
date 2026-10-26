# Diogo Cão — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Diogo Cão: a methodical coastal surveyor, river mouth by river mouth, stone pillars planted as title deeds, soundings and latitudes logged, the coast claimed one padrão at a time`
- ZH: 迪奥戈·康风格：按部就班的沿岸测绘者，逐河口推进，石柱为界碑，测深与纬度入日志，海岸一根石柱一根石柱地认领。

## (2) 导航方法

- 定位：推测航法 + 纬度观测，河口与岬角为路标，石柱（padrão）为固定定位点。`artifact`
- 定向：沿岸南下，顺东南信风与本格拉寒流，河口处逆流而上探查。`impression`
- 误差容忍：河口位置以石柱与铭文固定，纬度误差以多次观测取中。`impression`

## (3) 造船与帆装

- 船型：卡拉维尔，两次航行（1482–1484、1485–1486），小船队沿岸推进。`artifact`
- 帆装：拉丁帆，宜沿岸抢风与河口进出。`impression`
- 补给：沿岸港口与河口补给，刚果河口与刚果王国建立联系后获补给。`artifact`

## (4) 航线规划习惯

- 路线：里斯本—几内亚湾—刚果河口—安哥拉—克罗斯角（今纳米比亚），两次南下一次比一次远。`artifact`
- 节奏：逐段推进，每到新地立石柱、刻铭文，再南下；第二次航行溯刚果河至耶拉拉瀑布。`artifact`
- 返航：原路北返，带回刚果使节与海图。`impression`

## (5) 日志与海图语言

- 日志体例：无亲笔日志传世，航路见于石柱铭文与编年史；铭文为最硬的证据。`artifact`
- 海图语言：石柱铭文即海图注记——国王名、船长名、到达地三要素。`artifact`
- 命名习惯：以圣人名与河口命名新地，石柱刻字固定。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 刚果河口与刚果河上游
- 安哥拉—纳米比亚海岸
- 石柱立标法
- 河口探查与溯河
- 不该探索：
- No coast claimed without a stone pillar and inscription
- No river entered without sounding its mouth
- No latitude logged from a single observation
- No southward push without a supply point behind
- Negative prompt: `No coast claimed without a stone pillar and inscription, No river entered without sounding its mouth, No latitude logged from a single observation, No southward push without a supply point behind`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Diogo Cão, an uncrewed survey ship works a new coast river mouth by river mouth in 2026, survey markers planted as title deeds, soundings and latitudes logged.`
- 中文对照：迪奥戈·康风格：一艘无人测量船2026年沿新海岸逐河口推进，测绘标志为界碑，测深与纬度入日志。
- Negative: `No coast claimed without a stone pillar and inscription, No river entered without sounding its mouth, No latitude logged from a single observation, No southward push without a supply point behind`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
