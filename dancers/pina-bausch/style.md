# Pina Bausch — 舞蹈风格规格 style.md（给视频模型）

> 只描述舞蹈，不描述人生。引用演出录像时注明作品名。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pina Bausch: everyday gestures repeated until they break, chairs and tables as obstacles, men and women asking each other questions, tenderness and cruelty side by side, dance theatre, no ballet line`
- ZH: 皮娜·鲍什风格：日常动作重复到崩裂，椅子与桌子作障碍，男女互相提问，温柔与残酷并置，舞蹈剧场，没有芭蕾线条。

## (2) 动作语汇

- 核心动作：日常动作的重复与错位：走路、坐下、拥抱、抚摸头发、点烟、脱衣服；同一动作由不同舞者以不同速度重复，重复到意义翻转。`verbatim`（《穆勒咖啡馆》演出录像中直接可见）
- 动作来源：动作从日常生活中来，也从舞者本人的回答里来：鲍什向舞者提问（“你害怕什么？”），舞者的回答与即兴变成动作素材。`impression`（舞蹈剧场研究通说）
- 身体部位偏好：以全身为主导，尤其手臂与手势、躯干的弯折；腿脚不追求芭蕾式伸展，动作常起于肩、肘、手的细小颤动，再蔓延到全身。

## (3) 身体线条与空间调度

- 身体线条：身体线条曲折、断裂、不对称；重心低，贴地，舞者常蜷缩、跌倒、被拖拽；长线条只在短暂的双人舞托举中出现，随即被日常动作打断。
- 空间调度：舞台满台使用，椅子桌子布满全场，成为舞者必须绕过、撞上、搬动的障碍；队形是人群的聚散而非几何图案；进出场频繁，舞者从侧幕走入又走出，像街头来往的人。
- 视点：观众看正面全景为主，视线落点在人与人之间的关系上；近景特写只在手势与面部表情处停留，情绪靠重复的动作传达，不靠情节说明。

## (4) 节奏与音乐关系

- 节奏：节奏缓慢而执拗：同一动作重复数十次，速度几乎不变，突然插入一次加速或骤停；呼吸与动作不同步，动作像被外力推动。
- 与音乐的关系：音乐与舞蹈各自独立又互相映照：流行歌曲、歌剧选段与日常动作并置，音乐不指挥动作，动作也不图解音乐；常在音乐骤停时只剩脚步声与呼吸声。
- 速度感：速度感是断点的、滞重的：动作连绵不起来，每一下都被打断、被重复、被拖长；爆发只在极短的瞬间出现，随即回到缓慢的重复。

## (5) 情绪表达

- 情绪：情绪：焦虑、温柔、残酷、荒诞；情绪靠日常动作的重复与错位传达，而不是靠情节说明；男女之间的试探与伤害是反复的情绪核心。`impression`

## (6) 该编什么 / 不该编什么

- 该编：日常动作的重复与变奏、椅子桌子等道具障碍、男女互相提问的双人舞段落、流行歌曲与歌剧选段并置、群舞的聚散而非几何队形、水与土等自然元素的舞台使用（《春之祭》的泥土）。
- 不该编：不编芭蕾式轻盈跳跃、不编情节连贯的叙事哑剧、不编无张力的圆润流畅动作、不编纯技巧展示的炫技段落、不编皆大欢喜的团圆结尾。
- Negative prompt: `No ballet pointe work, no smooth lyrical flow, no literal mime storytelling, no virtuoso showpiece jumps, no sentimental happy ending tableau`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Pina Bausch, a small Yorkshire terrier sits on a subway seat while commuters repeat the same small gestures, chairs rearranged, everyday movements looped and displaced, tender and unsettling, dance theatre, no ballet line`
- 中文对照：皮娜·鲍什风格：一只约克夏犬坐在地铁座位上，通勤者重复着同样的细小动作，椅子被反复搬动，日常动作循环错位，温柔又不安，舞蹈剧场，没有芭蕾线条。
- Negative: `No ballet pointe work, no smooth lyrical flow, no cute pet acting, no literal mime, no happy ending tableau`
- 检验点：日常动作是否重复到意义翻转；椅子是否成为障碍而非装饰；情绪是否靠重复而非情节传达。
