# al-Battani — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of al-Battani, observe longer and correct Ptolemy with trigonometry: years of patient measurement at Raqqa, then tables more accurate than Copernicus would later achieve`
- ZH: 白塔尼风格：观测更久、用三角学订正托勒密：在拉卡耐心测量多年，然后是比哥白尼后来还要准确的星表。

## (2) 观测方法

仪器为浑仪、象限仪与日晷；观测策略是长期精密观测：自 877 年起在拉卡多年观测太阳、月亮与行星，测太阳年、岁差与黄道倾角。观测精度在当时极高。`artifact`

## (3) 推演与模型建构

推演是三角学订正：以三角学取代托勒密的几何方法，改进太阳与月亮的运动表；发现太阳远地点在移动。链条：长期观测 → 三角计算 → 订正托勒密 → 新表。`artifact`

## (4) 证据链

证据链：太阳年 365 日 5 时 46 分 24 秒（仅差 2 分 22 秒）→ 岁差 54.5″/年 → 黄道倾角 23°35′ → 哥白尼在《天体运行论》中引用其 23 次。关键证据强度高：数值可复核、后世引用明确。反证处理：未采用萨比特的颤动说，取均匀岁差。`artifact`

## (5) 理论语言与论证结构

语言为数表与三角论述体：《萨比天文表》以数表落实推算，以三角学论证订正。论证开头从长期观测出发，结尾给出新表。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 太阳、月亮与行星的长期精密观测
- 太阳年、岁差与黄道倾角的测定
- 以三角学订正托勒密
- 不该研究：
- 不把订正写成全盘推翻托勒密
- 不把数值写成现代精确值
- 不凭引用次数断言影响大小
- Negative prompt: `no correction presented as wholesale rejection of Ptolemy, no value presented as a modern exact value, no influence claimed from citation counts alone`

## (7) 测试提示词示例（现代题材：用白塔尼的方法，从现代多年太阳观测数据测定回归年）

- Prompt: `In the style of al-Battani, measure the tropical year from years of modern solar observations: observe patiently, compute with trigonometry, correct the standard tables, and show how far off the old tables were`
- 中文对照：白塔尼风格，从现代多年太阳观测数据测定回归年：耐心观测、用三角学计算、订正标准星表，并给出旧表偏了多少。
- Negative: `no correction presented as wholesale rejection of Ptolemy, no value presented as a modern exact value, no influence claimed from citation counts alone`
- 检验点：回答是否按该天文学家的方法走（观测 → 制表 → 校准 → 订正验证 → 成表）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
