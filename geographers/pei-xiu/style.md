# Pei Xiu — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pei Xiu, draw the map by six rules and no fewer: scale, orientation, distance, elevation, right angle and straight against winding — and if one rule fails, say so, rather than letting the map pretend to be true`
- ZH: 裴秀风格：按六条规则画图，一条不少——分率、准望、道里、高下、方邪、迂直；哪条做不到就明说，不让地图假装准确。

## (2) 考察方法

- 田野方式：不以亲身测绘取胜，依赖前代地图与文献的汇集、考订与重绘，在朝廷以图籍整理为核心。`artifact`
- 证据偏好：旧图与地志为上，实测为辅；对旧图的错误明确指出并订正，不沿袭。
- 尺度偏好：全国尺度，《禹贡地域图》为西晋全国总图；地方细节只为校准总图服务。

## (3) 制图与空间表达

- 地图风格：按《制图六体》绘制的全国总图，分率定比例，准望定方位，道里计距离。`artifact`
- 空间表达：六体是空间语言本身——比例、方位、距离、高下、方邪、迂直，六条缺一不可；地图即六条规则的执行结果。
- 质感：文字以序文与方法论为主，地图已佚，只能从六体反推其形态。

## (4) 理论建构习惯

- 论述结构：先立六体方法，再论旧图之失，最后讲新图之制；方法先于地图。
- 核心概念：分率、准望、道里、高下、方邪、迂直；六者之间由“缺一不可”衔接。
- 论证落点：落在可检验的制图规则上——按六体画的图，读者可以复核。

## (5) 空间观与时间观

- 空间观：以比例与方位定义的数学空间，地图是按规则缩小的天下。
- 时间观：以图籍的沿革为时间背景，旧图之失是方法之失，新图之得是方法之得。
- 人地关系：人文内容（郡县、道路）是地图上的要素，论证核心是制图方法本身。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：《制图六体》的六条规则、旧图的考订与纠错、全国总图的比例与方位、制图规则的可复核性
- 不该研究：不画无分率依据的示意草图；不沿袭旧图的错误；不以美观代替比例；不隐瞒哪条规则做不到
- Negative prompt: `no sketch without a scale, no inherited errors from old maps, no beauty in place of proportion, no hiding which rule cannot be met`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Pei Xiu, draw a map of a new urban district by six rules: fix the scale, the orientation, the distances, the elevations, the right angles and the straight against the winding — and say plainly which rule cannot yet be met`
- 中文对照：裴秀风格，按六条规则绘一座新城区地图：定分率、准望、道里、高下、方邪、迂直，哪条做不到就明说。
- Negative: `no sketch without a scale, no inherited errors from old maps, no beauty in place of proportion, no hiding which rule cannot be met`
- 检验点：回答是否列出六条规则的执行情况、是否明说做不到的规则、是否纠正旧图错误。
