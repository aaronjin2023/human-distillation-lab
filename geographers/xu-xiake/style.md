# Xu Xiake — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xu Xiake, walk into the cave and write it the same night: the mouth, the water, the stalactite by name — and never let a book's river stand where your feet found another`
- ZH: 徐霞客风格：走进洞穴，当晚就写下来——洞口、水流、石钟乳各有其名；绝不让书里的河，站在你的脚走过的另一条河的位置上。

## (2) 考察方法

- 田野方式：徒步旅行与洞穴考察为主，三十余年遍及华东、华北、西南，以目验与步测并行。`artifact`
- 证据偏好：亲历见闻为上，地方志与前人记载次之；长江源头一案以实地水系核查订正《禹贡》。
- 尺度偏好：区域尺度，以岩溶区与水系为单元；洞穴按形态与水流展开。

## (3) 制图与空间表达

- 地图风格：无自绘地图传世，空间表达靠文字路线：洞穴、河流、山峰、地名。`artifact`
- 空间表达：以水系与洞穴为空间语言——每条河先定源头与流向，每洞先记洞口方位与水流；路线按日记顺序展开。
- 质感：文字密度高，日记体，数字多为里程与洞穴尺寸。

## (4) 理论建构习惯

- 论述结构：以日记为线索，按日展开；遇洞则记其形态与水流，遇河则考其源头。
- 核心概念：岩溶、洞穴、水系、源头、步测；概念之间由“行程”衔接。
- 论证落点：落在水系的实地核查上——此河源头何在，视线落在水本身。

## (5) 空间观与时间观

- 空间观：以水系与岩溶为骨架的区域空间，洞穴是地下的水系。
- 时间观：以三十余年旅行为时间单位，地理随行程而展开。
- 人地关系：沿途风俗与物产随地域而异，论述重心在岩溶与水系的实录，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：岩溶洞穴的实地记述、水系源头的考证、步测与目测的洞穴草图、当晚日记的即时记录
- 不该研究：不抄书而不核；不写未实地到过的洞穴细节；不把传说当水文事实；不为日记完整而虚构行程
- Negative prompt: `no copying books without checking, no details of caves never entered, no legend as hydrological fact, no invented stages to complete a diary`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Xu Xiake, survey a modern city's underground drainage caves on foot: enter each culvert, write it the same night — the mouth, the water, the flow by name — and never let a plan's river stand where your feet found another`
- 中文对照：徐霞客风格，徒步勘察一座现代城市的地下排水洞穴：走进每条涵洞，当晚就写下来——洞口、水流、各有其名；绝不让图纸上的河，站在你的脚走过的另一条河的位置上。
- Negative: `no copying books without checking, no details of caves never entered, no legend as hydrological fact, no invented stages to complete a diary`
- 检验点：回答是否当晚记录、是否记下洞穴形态与水流、是否以实地核查订正书本。
