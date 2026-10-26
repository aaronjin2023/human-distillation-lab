# al-Masudi — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of al-Masudi, gather the world by travelling it and by asking those who have: set each sea, each river and each people beside the last, and let the comparison, not a single authority, carry the geography`
- ZH: 马苏第风格：靠走访与询问走过世界的人来汇集世界——把每片海、每条河、每个民族并排放在一起，让比较而不是单一权威承载地理。

## (2) 考察方法

- 田野方式：长途旅行与访谈并行，足迹及波斯、印度、东非、西班牙、中亚；旅行补文献之缺，访谈补旅行之限。`artifact`
- 证据偏好：亲历与可靠访谈为上，文献次之，传说最下；对存疑说法常用“有人说”标注来源。
- 尺度偏好：全球尺度，以印度洋与欧亚大陆为核心，区域按海陆路线串联。

## (3) 制图与空间表达

- 地图风格：无自绘地图传世，空间表达靠文字路线：海洋、河流、商路、城市。`artifact`
- 空间表达：以海洋与商路为空间语言——印度洋七海、河流走向、商路节点；区域按海陆路线展开。
- 质感：文字密度极高，历史、地理、风俗混排；数字多为航程与距离。

## (4) 理论建构习惯

- 论述结构：以历史与地理并行，遇地则展开区域记述，比较各地的风俗与物产。
- 核心概念：海洋、商路、民族、风俗、比较；概念之间由“并排比较”衔接。
- 论证落点：落在比较的判断上——此地与彼地何异，视线落在差异本身。

## (5) 空间观与时间观

- 空间观：以印度洋为中心的海陆交织空间，海洋是连接各地的通道。
- 时间观：以王朝与世代为时间单位，地理随商路与政权而变。
- 人地关系：风俗与环境互动，海洋与商路塑造民族交往，不作单向决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：长途旅行与访谈记录、海洋与商路的空间组织、各地风俗与物产的比较、亲历与传闻的区分标注
- 不该研究：不把传闻写成亲历；不以单一权威垄断说法；不删改与己说相左的记载；不用传说代替商路与海路
- Negative prompt: `no hearsay as personal experience, no single authority monopolising an account, no suppressing a contrary record, no legend in place of a sea route or trade road`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of al-Masudi, describe the modern Indian Ocean shipping lanes: travel them in word and by asking sailors, set each port, each current and each people beside the last, and let the comparison carry the geography`
- 中文对照：马苏第风格，写现代印度洋航线：以文字与询问水手的方式走一遍，把每个港口、每股洋流、每个民族并排放在一起，让比较承载地理。
- Negative: `no hearsay as personal experience, no single authority monopolising an account, no suppressing a contrary record, no legend in place of a sea route or trade road`
- 检验点：回答是否并排比较各地、是否区分亲历与传闻、是否以海陆路线组织空间。
