# William Herschel — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Herschel, build a bigger telescope than anyone has, sweep the whole sky with it, count the stars field by field, and let the shape of the Galaxy emerge from the counts`
- ZH: 威廉·赫歇尔风格：造一台比谁都大的望远镜，用它扫遍整个天空，逐个天区数星，让银河系的形状从计数中浮现。

## (2) 观测方法

- 仪器：自制大型反射望远镜（口径不断增大，最大约 1.2 米），巡天与深空观测。
- 观测策略：系统扫掠巡天，逐天区记录恒星数目与星云形态；天王星为巡天中的偶然发现。
- 样本：全天恒星计数（683 个天区样本）、2500 个星云与星团、天王星、红外实验。

## (3) 推演与模型建构

- 推演：恒星计数法——各天区恒星数目多少反映银河系在该方向的深度，推断银河系为扁平盘状，太阳近中心（后世修正：太阳不在中心，计数法受消光影响）。
- 模型：银河系扁平盘模型；红外辐射为光谱之外的不可见辐射。
- 链条：巡天计数 → 各方向深度 → 银河系形状 → 太阳位置。

## (4) 证据链

- 证据：683 个天区的恒星计数为直接证据；天王星的多夜移动序列为发现证据。
- 关键证据：银道面方向恒星显著多于银极方向，计数差异即形状证据。
- 反证处理：天王星初见时误认为彗星，多夜跟踪后改判为行星，不坚持初判。

## (5) 理论语言与论证结构

- 语言：巡天报告体 + 计数统计；论证靠样本量与系统性。
- 论证：归纳式——从 683 个天区计数归纳银河系形状，结尾给出模型与星表。
- 图表：恒星计数表与银河系剖面图是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 大型反射望远镜的制作与巡天
- 恒星计数法与银河系结构推断
- 星云与星团的系统巡天
- 红外辐射的实验发现
- 天王星的巡天发现
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no claiming the Galaxy's shape from a few fields, no calling a moving object a planet after one night, no ignoring dust that dims the far stars, no presenting a first guess as a finished model`

## (7) 测试提示词示例（现代题材：测绘一个星系的形状）

- Prompt: `In the style of William Herschel, map a modern galaxy's shape: survey the whole sky with the largest available telescope, count stars field by field, correct for dust, and let the shape emerge from the counts before naming the model`
- 中文对照：以威廉·赫歇尔的风格测绘一个现代星系的形状：用现有最大的望远镜巡天，逐个天区数星，修正尘埃消光，让形状从计数中浮现再命名模型。
- Negative: `no claiming the Galaxy's shape from a few fields, no calling a moving object a planet after one night, no ignoring dust that dims the far stars, no presenting a first guess as a finished model`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
