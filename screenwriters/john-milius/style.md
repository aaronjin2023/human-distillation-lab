# John Milius — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Milius: mythic macho adventure, men tested by wilderness and war, surf and sword as a code of honour, dialogue like a war cry, history as legend`
- ZH: 约翰·米利厄斯风格：神话式的阳刚冒险，男人在荒野与战争中受考验，冲浪与剑即荣誉准则，对白像战吼，历史即传奇。

## (2) 结构：三幕 / 序列 / 节拍

- 史诗冒险三幕：第一幕立下一群男人与一次远征，第二幕让他们穿越荒野与战争——河流、沙漠、战场——每站一次考验，第三幕在决战或归来处收束。时间跨度长，靠远征而非悬念组织。

## (3) 对话

- 对白雄壮、简短、有战吼感：短句、格言、誓言，人物用语言互相激励。动作描写写冒险：冲浪、骑马、战斗，场面本身就是情节。独白少，对话多。

## (4) 人物弧光

- 主角多为战士与冒险者：军官、剑客、海盗。弧光是荣誉的考验——从莽撞到领悟荣誉的代价，或至死不悟。对手是荒野、战争与时代，荣誉是唯一的准则。

## (5) 类型套路与创新

- 战争片 / 冒险片 / 奇幻片。他遵守冒险片的远征与考验套路，但打破了“战争片要反战”的成见：战争被写成神话与考验。创新在神话写作——把历史写成传奇。禁套路：几乎不用讽刺与反战说教，不写女性主角的内心戏。

## (6) 该写什么 / 不该写什么

- 该写：神话式阳刚冒险与远征结构、荒野与战争中的荣誉考验、战吼式的格言对白、历史写成传奇。
- Negative prompt: `No ironic detachment, no anti-war sermon, no soft introspection, no cynical deconstruction, no quiet domestic drama`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of John Milius, a small Yorkshire terrier leads a band of night-shift workers up a river of neon to find the last bowl of oden. Mythic macho adventure, men tested by wilderness and war, dialogue like a war cry, history as legend. The dog does not retreat.`
- 中文对照：约翰·米利厄斯风格：一只约克夏犬率领一群夜班工人沿霓虹之河而上，寻找最后一碗关东煮。神话式阳刚冒险，男人在荒野与战争中受考验，对白像战吼，历史即传奇。狗不撤退。
- Negative: `No ironic detachment, no anti-war sermon, no soft introspection, no cynical deconstruction, no quiet domestic drama`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
