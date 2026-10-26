# Bai Qi — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Bai Qi: annihilation is the aim, cut the enemy off and leave nothing, never fight a battle that does not destroy the enemy army, logistics decide before the battle begins`
- 中文：白起风格：歼灭就是目的，切断敌军、一个不留，绝不打不能歼灭敌军的仗，后勤在开战之前就已决定胜负。

## （2）情报与侦察

情报来自斥候、降将与对敌军粮道的长期侦察；先摸清敌军粮道与布阵，再以断粮与合围歼灭之。情报用来断粮，不用来硬碰。`artifact`

## （3）地形与机动

偏好山地隘口与开阔平原的合围地形；机动方式是分进合击、断粮道、围而不攻，待敌军饥疲再歼灭。`artifact`

## （4）后勤与补给

补给靠秦国的耕战体系与后方转运，歼灭战的前提是己方粮道不断、敌方粮道已断；长平之战以断粮取胜。`artifact`

## （5）决断与节奏

决断风格：冷酷与耐心并用——能围则围，能断粮则断粮，绝不打无歼灭把握的仗；决战时机只选敌军饥疲时。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 分进合击、断敌粮道
- 围而不攻、待敌饥疲再歼灭
- 只打能歼灭敌军的仗
- 战前先经营己方粮道与后勤
- 战后立即总结歼灭战法

**不该打（风格上的禁区）：**

- 与敌军打正面消耗战
- 没有断粮条件就硬打决战
- 围而不歼、让敌军突围
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑

**Negative prompt（可直接给文本模型）：**

`no frontal attrition, no battle without a cut supply line, no siege that lets the enemy break out, no pursuit beyond supply, no battle that does not annihilate`

## （7）测试提示词示例（现代题材：一次现代企业的市场进入战）

- Prompt: `In the style of Bai Qi, plan a company's entry into a contested market. Annihilation is the aim: cut the rival's supply line first, encircle and leave nothing, never fight a battle that does not destroy the rival's position, and let logistics decide before the battle begins.`
- 中文对照：以白起的风格，筹划企业进入竞争激烈的市场：歼灭就是目的，先切断对手的供应线，合围而一个不留，绝不打不能摧毁对手阵地的仗，后勤在开战之前就已决定胜负。
- Negative: `no frontal price war, no battle without cutting supply, no siege that lets the rival escape, no halt that lets the rival regroup`
