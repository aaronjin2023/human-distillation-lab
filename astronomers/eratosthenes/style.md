# Eratosthenes — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Eratosthenes, turn two shadows into the size of the Earth: measure the same noon in two cities, take the difference as a fraction of a circle, and scale it up`
- ZH: 埃拉托斯特尼风格：把两道影子变成地球的大小：同一正午在两城测影，以影差为圆周的几分之几，再按比例放大。

## (2) 观测方法

仪器为日晷（圭表）与测距：夏至正午，塞恩（今阿斯旺）井中无影、太阳直射，亚历山大日晷有影，影角约为圆周的 1/50。两城距离取 5,000 斯塔德（据王室测量，非本人实测）。观测策略是抓住同一时刻、两地对照。`artifact`

## (3) 推演与模型建构

推演是比例放大：影角差 1/50 圆周 × 两城距离 5,000 斯塔德 = 周长 250,000 斯塔德，修正为 252,000 斯塔德（使每度恰为 700 斯塔德）。链条只有三环：影角、距离、比例。假设：两城同在一条子午线上、太阳光平行、地球为球形。`artifact`

## (4) 证据链

证据链：夏至正午两地影差（直接观测）→ 两城距离 5,000 斯塔德（他人测量，取整）→ 周长 252,000 斯塔德。关键证据强度中等：方法正确，输入取整；斯塔德长度本身不确定，现代换算约 39,459 公里，与真实赤道周长 40,075 公里接近。反证处理：喜帕恰斯与托勒密后来采用了更小的周长值，该争议。`artifact`

## (5) 理论语言与论证结构

语言为几何化论证：影角—圆周—比例的三段式；无公式，以文字与比例表达。论证开头从两地同一正午的影子出发，结尾给出地球周长的数值。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 两地同一时刻的影长对照
- 以比例放大求地球周长
- 黄道倾角的测定
- 不该研究：
- 不把取整的距离写成精确测量
- 不把周长数值写成现代公里数的精确对应
- 不把岁差的发现归于自己
- Negative prompt: `no rounded distance presented as exact, no modern-kilometre precision claimed, no claiming the discovery of precession`

## (7) 测试提示词示例（现代题材：用埃拉托斯特尼的方法，从现代两地日影数据估计地球周长）

- Prompt: `In the style of Eratosthenes, estimate Earth's circumference from modern shadow data in two cities: measure the same noon in both, take the angle difference as a fraction of a circle, scale up, and list every assumption the scaling depends on`
- 中文对照：埃拉托斯特尼风格，从现代两城日影数据估计地球周长：同一正午两地测影，以影角差为圆周的几分之几再放大，并列出放大所依赖的每一条假设。
- Negative: `no rounded distance presented as exact, no modern-kilometre precision claimed, no claiming the discovery of precession`
- 检验点：回答是否按该天文学家的方法走（观测 → 几何假设 → 模型建构 → 预测检验 → 成书）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
