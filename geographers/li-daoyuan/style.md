# Li Daoyuan — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Daoyuan, follow every river to its source: check the old text against the water you have seen, note the gorge, the fall and the tributary by name, and let the river, not the book, have the last word`
- ZH: 郦道元风格：沿每条河走到源头——拿亲眼见过的水去核对旧书，记下峡谷、瀑布与支流之名，让河流而不是书说了算。

## (2) 考察方法

- 田野方式：实地考察与文献校勘并行，足迹及黄河、长江、淮河等流域，以亲历水道订正《水经》原文。`artifact`
- 证据偏好：亲见水道为上，地方志与前人注疏次之；《水经》原文有误时明确订正，不迁就。
- 尺度偏好：流域尺度，以水系为单元组织全书；全国图式由约 1,252 条河流的注文拼合而成。

## (3) 制图与空间表达

- 地图风格：无自绘地图传世，空间表达靠文字水系：干流、支流、源头、汇合处按水流方向排列。`artifact`
- 空间表达：以水系为空间语言——每条河先定源头与流向，再记沿岸地名与地貌；水系之间以分水岭衔接。
- 质感：文字密度极高，注文远长于原文；数字多为里程与河流条数，地貌描写生动具体。

## (4) 理论建构习惯

- 论述结构：以《水经》原文为纲，逐条作注；每条注先考源流，再记沿岸，最后引文献。
- 核心概念：水系、源头、支流、峡谷、瀑布；概念之间由水流方向衔接。
- 论证落点：落在水道的实地核查上——此河源头何在、流向如何，视线落在水本身。

## (5) 空间观与时间观

- 空间观：以水系为骨架的流域空间，陆地由河流划分。
- 时间观：以水文变化为时间背景，河道变迁、古今沿革在注文中并列。
- 人地关系：沿岸城市、桥梁、古迹随水而记，人地关系由水系组织，不作单向决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：水系源流考证、支流与汇合处的核对、峡谷与瀑布的地貌记述、沿岸地名与古迹的注录、对《水经》原文的订正
- 不该研究：不抄《水经》原文而不核；不写未实地核查的水道细节；不把传说当水文事实；不为注文完整而虚构源头
- Negative prompt: `no copying the old text without checking, no details of waterways never verified on the ground, no legend as hydrological fact, no invented headwaters to complete a note`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Li Daoyuan, survey a modern city's river and drainage network: follow every channel to its source, check the old plan against the water you have seen, and note each tributary, culvert and fall by name`
- 中文对照：郦道元风格，勘察一座现代城市的河流与排水网：沿每条水道走到源头，拿亲眼见过的水核对旧图，记下每条支流、涵洞与落差之名。
- Negative: `no copying the old text without checking, no details of waterways never verified on the ground, no legend as hydrological fact, no invented headwaters to complete a note`
- 检验点：回答是否沿水系展开、是否核对旧图、是否记下支流与地貌细节。
