# Issey Miyake — 时装风格规格 style.md（给图像模型）

> 只描述时装，不描述人生。引用系列时只写系列名与廓形 / 面料特征，不编造发布年份。色彩只写色名，不编造实测 HEX 值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Issey Miyake, pleated fabric, one-piece construction, no waistline, fluid sculptural silhouette, muted colours, technology and body in harmony`
- ZH: 三宅一生风格：褶皱面料，一块布成衣，无腰线，流动雕塑廓形，低调色彩，科技与身体合一。

## (2) 廓形方向

主廓形 2 种：一是一块布廓形——整件衣服由一块布构成，无腰线、无省道，靠褶皱与身体互动立形；二是褶皱直筒廓形，宽松流动。`artifact`
- 比例：无腰线，上下等分，视觉落点在褶皱的纵线而非腰线；长度多及膝以下。`impression`

## (3) 面料与色彩

面料：主面料为聚酯褶皱布、棉、真丝，配技术面料；织法重热压褶皱，厚度薄—中，垂感流动。`artifact`
- 色彩：主色为黑、白、灰、米等低调色，辅色为单色亮色点缀；禁艳色大面积印花与繁复图案。冷暖偏冷，饱和度低，明暗对比弱。`impression`

## (4) 剪裁与结构

剪裁：无剪裁即剪裁——一块布热压褶皱成衣，剪裁让位于面料工艺；省道取消，接缝极少。`artifact`
- 结构：单层为主，褶皱本身即结构；内衬无；穿脱简洁，身体活动度极高。`impression`

## (5) 细节与配饰

细节：领以无领、圆领为主；袖为宽袖、落肩袖；扣多用无扣、系带；褶皱是核心细节。`artifact`
- 配饰：只写与时装一体设计的配饰——Bao Bao 包、褶皱围巾；不写纯珠宝线。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：热压褶皱面料、一块布成衣、无腰线流动廓形、黑白灰米的低调色盘、科技面料与身体合一、褶皱纵线。`verbatim` / `artifact`
- 不该设计：合体收腰、艳色大面积印花、繁复装饰、硬挺建筑廓形、传统剪裁省道。
- Negative prompt: `No body-con fit, no bright all-over print, no heavy ornament, no stiff architectural silhouette, no traditional darted tailoring`

## (7) 测试提示词示例（现代题材：现代城市街角便利店店员的工作服）

- Prompt: `In the style of Issey Miyake, a convenience store uniform in a modern city, pleated fabric, one-piece construction, no waistline, fluid movement, muted colours, functional and sculptural`
- 中文对照：三宅一生风格：现代城市便利店店员的工作服，褶皱面料，一块布成衣，无腰线，流动感，低调色彩，功能与雕塑并存。
- Negative: `No tailored suit, no tight fit, no bright print, no heavy ornament, no symmetrical perfect silhouette`
- 检验点：褶皱是否流动而不是死板；廓形是否无腰线而不是收腰；面料是否轻盈而不是厚重。
