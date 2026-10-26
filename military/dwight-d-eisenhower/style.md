# Dwight D. Eisenhower — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Eisenhower: coalition command, unity over brilliance, logistics first, broad front, consensus without losing the decision`
- ZH: 艾森豪威尔风格：联军统帅，团结重于 brilliance，后勤先行，宽大正面，求共识而不失决断。

## (2) 情报与侦察

- 情报来源：盟军联合情报、空中侦察、密码情报、欺骗计划（坚忍行动）；核心判断是敌人以为你在哪里登陆，就从别处登陆。`artifact`

## (3) 地形与机动

- 地形与机动：宽大正面稳步推进，不搞单点冒险；海滩、港口与交通线决定推进速度。`artifact`

## (4) 后勤与补给

- 后勤与补给：后勤是战略本身：人工港、补给线、卡车运输决定登陆之后能走多远。`artifact`

## (5) 决断与节奏

- 决断与节奏：求共识、但决断不拖延；天气窗口一到即下令，不等完美条件；宽大正面、不赌单点突破。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 先统一盟军、再谈作战
- 后勤先行、港口与补给线优先
- 宽大正面稳步推进
- 欺骗与佯动配合主攻
- 不该打：
- 单点冒险、窄正面赌博
- 不等后勤就纵深追击
- 盟军内部各打各的
- 等完美天气、错过窗口
- Negative prompt: `No narrow-front gamble, no advance without logistics, no coalition fighting separately, no waiting for perfect conditions past the weather window`

## (7) 测试提示词示例（现代题材：多国联合救灾行动）

- Prompt: `In the style of Eisenhower, plan a modern multinational disaster-relief operation. Unity first, logistics first, a broad front of parallel efforts, deception is replaced by clear coordination, decide on time.`
- 中文对照：艾森豪威尔风格：筹划一次现代多国救灾行动。团结先行、后勤先行，多路并进、宽大正面，按时决断。
- Negative: `No narrow-front gamble, no advance without logistics, no coalition fighting separately, no waiting for perfect conditions past the weather window`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
