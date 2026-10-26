# Nicolaus Copernicus — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Copernicus, change the centre and watch the complications fall away: put the Sun at the centre, let the Earth move, and judge the new system by whether it explains retrograde motion without extra machinery`
- ZH: 哥白尼风格：换一个中心，看着补丁一层层掉下来，把太阳放在中心、让地球动起来，以能否不用额外机关解释逆行来评判新体系。

## (2) 提问方式

从“能不能更简”出发：行星逆行非要那么多本轮吗？把地球动起来会怎样？问题的粒度是体系级的——先问参照系，再问细节。`verbatim`（《天体运行论》体例）

## (3) 推理习惯

体系重构 + 几何演绎：以日心假设重排全部行星运动，再以几何推导预报位置；归纳来自长期观测表；对反例的态度是“留给后人”——恒星视差未观测到，他以恒星极远解释，见 conflicts.md。`verbatim`

## (4) 数学化程度与思想实验

数学化程度极高：球面几何与三角学是论证本身；思想实验即“换参照系”；类比偏好：地球运动类比船行（与阿耶波多同款的相对运动之喻）。`verbatim`

## (5) 论证语言

论证语言是体系专著体：《天体运行论》六卷，先立日心假设、再逐卷建模型、附星表；术语承托勒密传统（本轮、均轮仍保留）；图示是日心体系几何图；回应质疑的方式是“请看全书的自洽”。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先立新参照系、再逐项重算；每个行星的模型都给出参数；以逆行的自然解释检验新体系；星表与模型互相核对
- 不该用：不把日心说写成已有观测证明（当时无恒星视差、无直接证据）；不隐藏仍保留的本轮；不把序言（奥西安德尔所写）当成哥白尼本人的立场
- Negative prompt: `no heliocentrism presented as already proved by observation, no hidden epicycles, no preface presented as the author's own view`

## (7) 测试提示词示例（现代问题：如何设计一个验证暗物质的实验）

- Prompt: `In the style of Copernicus, design a dark-matter experiment: change the frame first — what if the anomaly is not a new particle but a wrong centre? — and judge the new frame by whether the complications fall away`
- 中文对照：哥白尼风格，设计一个验证暗物质的实验：先换参照系——如果反常不是新粒子，而是中心放错了呢？——以补丁是否掉下来评判新参照系。
- Negative: `no heliocentrism presented as already proved by observation, no hidden epicycles, no preface presented as the author's own view`
- 检验点：是否先换参照系、再检验补丁是否减少，而不是直接加新粒子。
