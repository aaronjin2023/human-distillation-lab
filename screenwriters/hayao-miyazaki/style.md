# Hayao Miyazaki — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hayao Miyazaki: a child enters a strange world and must work to survive, nature spirits and old gods, flight as freedom, growing up without losing wonder, a bittersweet farewell`
- ZH: 宫崎骏风格：孩子进入陌生世界，靠劳动活下去，自然精灵与古老的神，飞行即自由，长大而不失惊奇，微苦的告别。

## (2) 结构：三幕 / 序列 / 节拍

- 成长奇幻三幕：第一幕孩子进入陌生世界（搬家、隧道、森林），规则交代清楚；第二幕孩子靠劳动与善意在异世界立足，中点是一次失去（名字、父母、记忆）；第三幕孩子凭自己的选择归来或告别，收束微苦而温暖。时间跨度数日至数月，多用季节与劳动分段。

## (3) 对话

- 对白简洁、真诚，孩子的话直接；成人多用温和的忠告；潜台词是成长——没说出口的告别最重。动作描写多写飞行、劳动、自然。

## (4) 人物弧光

- 主角多为少女与孩子，弧光是从依赖到自立：不是打败反派，是学会劳动与告别。人物关系是孩子与精灵、神明、成人世界的互相照亮；结局人物不胜利，只长大。

## (5) 类型套路与创新

- 类型：动画奇幻与成长故事；遵守套路——异世界、劳动、告别；打破的一条是：反派不是恶人，自然与人类的冲突没有赢家。创新在剧本层面：把劳动与飞行写成结构，让异世界的规则承担道德重量。禁套路：不用说教收尾，不用善恶二元，不用煽情高潮。

## (6) 该写什么 / 不该写什么

- 该写：孩子进入异世界、劳动与飞行、自然精灵与古老的神、微苦温暖的告别、成长而不失惊奇。
- 不该写：说教式收尾、善恶二元、煽情高潮、让成人替孩子解决问题、直白的环保口号。
- Negative prompt: `No preachy ending, no good-versus-evil binary, no sentimental climax, no adult who solves it for the child, no direct environmental slogan`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Hayao Miyazaki, a small Yorkshire terrier follows a girl into a bathhouse for spirits late at night and must work to earn its name back. Flight, steam, kindness. A bittersweet farewell.`
- 中文对照：宫崎骏风格：一只约克夏犬跟着女孩深夜走进神明的澡堂，靠劳动赎回自己的名字，飞行、蒸汽、善意，一场微苦的告别。
- Negative: `No preachy ending, no good-versus-evil binary, no sentimental climax, no direct environmental slogan`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
