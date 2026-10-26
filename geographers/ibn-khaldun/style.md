# Ibn Khaldun — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn Khaldun, explain a civilisation by its geography first: the climate that feeds it, the desert that hardens it, the cohesion that raises it — and then watch the same cohesion rot in the city it built, in cycles, not in straight lines`
- ZH: 伊本·赫勒敦风格：先以地理讲文明——养育它的气候、磨砺它的沙漠、托起它的凝聚力；再看这凝聚力在它建起的城市里腐烂，循环往复，不走直线。

## (2) 考察方法

- 田野方式：以北非与中东的任职、旅行见闻与历史文献并行，在开罗以历史比较为核心。`artifact`
- 证据偏好：历史事例的比较为上，地理观察次之，传说最下；王朝周期以多个王朝的兴衰对照为准。
- 尺度偏好：文明尺度，以气候带与王朝为单元；区域细节只为验证周期服务。

## (3) 制图与空间表达

- 地图风格：无自绘地图传世，空间表达靠文字气候带：温带、热带、寒带与文明分布。`artifact`
- 空间表达：气候带是空间语言本身——温带宜居、极端气候不利文明；沙漠与城市是两种空间的对照。
- 质感：文字以理论论述为主，历史事例密集，数字多为王朝年限与世代数。

## (4) 理论建构习惯

- 论述结构：先立理论（阿萨比亚与王朝周期），再以历史事例验证，最后讲地理（气候带）对文明的制约。
- 核心概念：阿萨比亚、王朝周期、气候带、沙漠与城市、文明；概念之间由“循环”衔接。
- 论证落点：落在周期的判断上——王朝约三代而衰，视线落在循环本身。

## (5) 空间观与时间观

- 空间观：以气候带分区的空间，温带是文明的中心，沙漠与城市是两种对立的空间。
- 时间观：循环时间观，王朝兴衰约三代（约 120 年）为一周期，不走直线进步。
- 人地关系：气候与地理塑造群体的凝聚力与生计方式，但文明兴衰由社会机制（阿萨比亚的得失）决定，不是单纯的环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：气候带与文明分布的论述、阿萨比亚与王朝周期的历史比较、沙漠与城市的空间对照、多个王朝兴衰的对照验证
- 不该研究：不以单一王朝的兴衰立论；不把气候带写成文明的唯一决定因素；不用传说代替历史事例；不把循环写成直线进步
- Negative prompt: `no theory from a single dynasty, no climate as the sole cause of civilisation, no legend in place of a historical case, no cycles rewritten as straight progress`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ibn Khaldun, explain a modern megacity's rise and strain: the climate and hinterland that feed it, the cohesion that raised it, and how that cohesion thins in the city it built — in cycles, not in straight lines`
- 中文对照：伊本·赫勒敦风格，讲一座现代特大城市的兴起与紧张：养育它的气候与腹地、托起它的凝聚力，以及这凝聚力在它建起的城市里如何变薄——循环往复，不走直线。
- Negative: `no theory from a single dynasty, no climate as the sole cause of civilisation, no legend in place of a historical case, no cycles rewritten as straight progress`
- 检验点：回答是否以气候与凝聚力立论、是否用多个事例对照、是否落在循环判断上。
