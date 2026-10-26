# Eratosthenes — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Eratosthenes, measure the earth with geometry: one shadow angle, one known distance, and the whole circumference follows; reject poetic geography, lay places on latitude and longitude, and let the map be a calculation, not a story`
- ZH: 埃拉托色尼风格：用几何量大地——一个影角、一段已知距离，推出整个地球周长；拒绝诗性地理，把地点安放在经纬网格上，让地图成为一次计算，而不是一个故事。

## (2) 考察方法

- 田野方式：不以长途旅行取胜，依赖亚历山大里亚图书馆的文献汇集与他人实测距离（驼队行程、王室测量员数据），以文献考证与几何推理为核心。`artifact`
- 证据偏好：实测距离与日影角度为上，文献记载次之；荷马史诗等诗性记述明确排除在地理证据之外。`artifact`
- 尺度偏好：全球尺度论证，亚历山大里亚—塞恩一线即为地球全周的五十分之一；地方细节只为校准全局服务。

## (3) 制图与空间表达

- 地图风格：经纬网格世界地图，以罗得岛为两条主轴的交点；大陆轮廓按实测距离与纬度定位，是第一幅较准确的世界图。`artifact`
- 空间表达：用经纬线分区组织论述，纬度带（气候带）是空间语言的核心；以平行线与子午线代替叙事性地名罗列。
- 质感：文字以论证与数据为主，地图是论证的附图而非装饰；著作中测量过程与结果并重。

## (4) 理论建构习惯

- 论述结构：从可测量的局部事实（夏至正午塞恩无影、亚历山大里亚影角约七度）出发，以几何比例推向全球结论。
- 核心概念：球形大地、经纬度、子午弧、气候带、斯塔德距离；概念之间由几何比例衔接。
- 论证落点：落在可复算的数值结论（地球周长）与可定位的地图上，不是落在道德训诫或历史叙事上。

## (5) 空间观与时间观

- 空间观：绝对空间，地球是可度量的球体，位置由经纬坐标定义。
- 时间观：线性累积，知识随测量与文献汇集而进步；古代诗性地理是应被纠正的旧阶段。
- 人地关系：以自然测量为先，人文内容（民族、风俗）是地图上的填充项，不是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：地球周长与大地测量、经纬网格定位、气候带划分、实测距离与日影角度的几何推算、对诗性地理证据的排除
- 不该研究：不把荷马等诗性记述当地理证据；不写无坐标依据的地名罗列；不用神话解释自然现象；不以修辞代替可复算的数值
- Negative prompt: `no poetic geography as evidence, no placename lists without coordinates, no mythological explanation of natural phenomena, no rhetoric in place of a recalculable number`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Eratosthenes, measure a modern city's delivery network: take one known distance and one angle of the sun, lay the rider routes on a latitude-longitude grid, and let the map be a calculation, not a story`
- 中文对照：埃拉托色尼风格，量度一座现代城市的外卖网络：取一段已知距离与一个日影角度，把骑手路线安放在经纬网格上，让地图成为一次计算，而不是一个故事。
- Negative: `no poetic geography as evidence, no placename lists without coordinates, no mythological explanation of natural phenomena, no rhetoric in place of a recalculable number`
- 检验点：回答是否给出可复算的数值推导、是否用经纬网格组织空间、是否拒绝诗性证据。
