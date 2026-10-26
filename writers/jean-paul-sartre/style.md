# Jean-Paul Sartre — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean-Paul Sartre: philosophical fiction, nausea before the sheer existence of things, freedom as a burden, bad faith named and refused, dialogue as confrontation, no essence before existence`
- ZH: 萨特风格：哲理小说，面对事物赤裸存在时的恶心，自由作为重负，‘自欺’被点名、被拒绝，对话即 confrontation，存在先于本质。

## (2) 句式与节奏

句长：长短交错——哲理独白绵长、层层追问，日常对话短促、针锋相对；《恶心》以日记体逐日推进，节奏是‘记录—恶心—记录’的循环。节奏：缓慢、沉思，靠独白与辩论推进，情节极少；《禁闭》三个人物一间房，全靠对话推进。`verbatim`

## (3) 词汇与意象

词汇：哲学术语（存在、虚无、自由、自欺、他人）与日常物词（栗子树根、啤酒杯、公园长椅）并置；‘恶心’（la nausée）是核心词。意象群：栗子树根（存在的赤裸）、他人的目光（地狱）、房间（禁闭的处境）、手与黏腻；意象是哲学的肉身，不是装饰。禁词/禁意象：不用抒情的升华，不用命运式的宿命论，不用温情的和解。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第一人称日记（《恶心》的罗冈丹）、戏剧的封闭空间（《禁闭》三人对峙）、第三人称的哲理叙述；视角不切换，人物始终在自己的意识里。结构：日记体逐日记录、戏剧的三一律、哲理的论证式推进；开头多为一个日常场景（公园、房间），结尾多为一个哲理的收束（‘存在先于本质’）。对话：对话是 confrontation，人物靠辩论暴露自欺。`verbatim`

## (5) 语气与距离

语气：冷峻、思辨、带挑衅的严肃；与人物的距离是审视的——请读者判断人物是否自欺；与读者的距离是直接的——哲学命题直接抛给读者。幽默是苦涩的，悲悯藏在判断之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：面对事物赤裸存在时的恶心；自由作为重负；自欺的点名与拒绝；他人的目光即地狱；存在先于本质的抉择。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No lyrical uplift, no fatalism, no sentimental reconciliation, no psychological jargon, no closed happy ending`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Jean-Paul Sartre, a letter to oneself ten years from now. No essence before existence. The letter accuses the future self of bad faith — of pretending the past chose for him. Freedom as a burden. Dialogue with oneself as confrontation. End with a choice, not a comfort.`
- 中文对照：萨特风格，一封写给十年后自己的信。不存在先于本质；信指控未来的自己自欺——假装过去替他做了选择；自由作为重负；与自己的对话即 confrontation；以抉择收束，而非安慰。
- Negative: `lyrical uplift, fatalism, sentimental reconciliation, psychological jargon, closed happy ending`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
