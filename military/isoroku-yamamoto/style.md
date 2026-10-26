# Isoroku Yamamoto — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yamamoto: carrier air power first, surprise at the outset, bold opening blow, gamble on a short war, never fight a long attrition the nation cannot sustain`
- ZH: 山本风格：航母航空先行，开局奇袭，大胆首击，赌短期战争，绝不打国家耗不起的长期消耗战。

## (2) 情报与侦察

- 情报来源：空中侦察、密码情报、外交与舰队动向；核心判断是敌舰队主力何时何地最脆弱。`artifact`

## (3) 地形与机动

- 地形与机动：太平洋广阔海域、航母机动、长途奔袭；机动即航程，奇袭即生命。`artifact`

## (4) 后勤与补给

- 后勤与补给：日本国力与油料的短板决定战争不能拖长；补给线一断，机动即停。`artifact`

## (5) 决断与节奏

- 决断与节奏：开局奇袭、一击定局；赌的是短期决战，不是长期消耗；中途岛一失，赌局即崩。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 航母航空集中、开局奇袭
- 打敌舰队主力于不备
- 算准航程与返航油料
- 速决、不拖长
- 不该打：
- 把航母当作战列舰的附庸
- 没有奇袭就打正面决战
- 打国家耗不起的长期消耗战
- 忽视油料与国力短板
- Negative prompt: `No carriers as battleship auxiliaries, no frontal battle without surprise, no long attrition the nation cannot sustain, no operation ignoring fuel and national capacity`

## (7) 测试提示词示例（现代题材：向孤岛的突击空运救援）

- Prompt: `In the style of Yamamoto, plan a modern surprise disaster-relief airlift to an isolated island. Concentrate airlift at the outset, strike before weather closes, keep the operation short and decisive.`
- 中文对照：山本风格：筹划一次向孤岛的现代突击空运救援。开局集中空运力量，抢在天气恶化前行动，短促决断、不拖长。
- Negative: `No carriers as battleship auxiliaries, no frontal battle without surprise, no long attrition the nation cannot sustain, no operation ignoring fuel and national capacity`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
