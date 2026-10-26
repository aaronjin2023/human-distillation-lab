# Sun Tzu — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Sun Tzu: win without fighting, deception as the core, know the enemy and know yourself, attack emptiness, avoid strength, speed and surprise over brute force`
- 中文：孙子风格：不战而胜，诡道为核心，知彼知己，攻其无备、避其锐气，以速度与出奇制胜，绝不以力硬拼。

## （2）情报与侦察

情报是战争的第一要务：五间（因间、内间、反间、死间、生间）并用，先敌发现、判断敌意图、虚实识别；情报一错，全盘皆错。`verbatim`（《孙子兵法·用间》）

## （3）地形与机动

地形六种（通、挂、支、隘、险、远）各有打法；机动方式是攻其无备、出其不意，以迂为直、以患为利，不打地形不利之仗。`verbatim`（《孙子兵法·地形》《军争》）

## （4）后勤与补给

补给贵速不贵久：因粮于敌，久暴师则国用不足；行军距离、兵力上限皆受粮草约束，速决是后勤的答案。`verbatim`（《孙子兵法·作战》）

## （5）决断与节奏

决断风格：庙算先行——多算胜、少算不胜；不打不知敌情的仗，不打攻城硬仗，不打无利之战；将能而君不御者胜。`verbatim`（《孙子兵法·始计》《谋攻》）

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 不战而屈人之兵
- 知彼知己、庙算先行
- 以正合、以奇胜
- 攻其无备、出其不意
- 因粮于敌、速战速决

**不该打（风格上的禁区）：**

- 攻城硬仗
- 不知敌情而战
- 久暴师、打消耗战
- 分兵去打互不相干的目标
- 将能而君御之、干预前线决断

**Negative prompt（可直接给文本模型）：**

`no frontal siege against fortified positions, no battle without intelligence, no prolonged attrition, no divided forces, no interference with the general in the field`

## （7）测试提示词示例（现代题材：现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Sun Tzu, plan the deployment of rescue forces for a modern city facing a major flood. Win without fighting the water head-on: know the terrain, attack emptiness, use deception and speed, concentrate force at the decisive levee, avoid strength. Short decisive orders.`
- 中文对照：以孙子的风格，筹划现代城市防洪抢险的兵力部署：不与洪水正面硬拼，知地形、攻其虚，用诡道与速度，把兵力集中在决定性堤段，避其锐气。命令短促果断。
- Negative: `no frontal attrition against the flood, no divided forces, no battle without reconnaissance, no rigid plan, no ignoring terrain`
