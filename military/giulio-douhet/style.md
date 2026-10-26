# Giulio Douhet — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Douhet: command of the air decides war, bomb the enemy heartland, strike population and industry, air power needs no permission from land or sea`
- ZH: 杜黑风格：制空权决定战争，轰炸敌方腹地，打击人口与工业，空军不需要陆海军批准。

## (2) 情报与侦察

- 情报来源：敌方工业中心、人口密集区、机场与防空部署的空中侦察；核心判断是哪些目标一炸就动摇敌方抵抗意志。`artifact`

## (3) 地形与机动

- 地形与机动：天空无战线，飞机直抵腹地；地面防线对空袭无效，机动即航程与载弹量的函数。`artifact`

## (4) 后勤与补给

- 后勤与补给：机场、前沿基地、燃油与弹药决定出动率；制空权的前提是持续出动，不是单次突袭。`artifact`

## (5) 决断与节奏

- 决断与节奏：开战即大规模轰炸，不搞渐进升级；打击敌方意志重于歼灭敌方军队；陆海军转为辅助。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 开战即集中轰炸敌方腹地
- 打击工业、交通与人口中心
- 先夺制空权再谈地面推进
- 建独立空军，不隶属陆海军
- 不该打：
- 把飞机只当作陆军的侦察与支援工具
- 零敲碎打的小规模空袭
- 只炸前线、不碰腹地
- 等陆军推进再使用空军
- Negative prompt: `No air power as mere army support, no piecemeal small raids, no front-line-only bombing, no waiting for ground advance before using air power`

## (7) 测试提示词示例（现代题材：针对后勤网络的无人机作战筹划）

- Prompt: `In the style of Douhet, plan a modern drone campaign against an enemy logistics network. Strike the heartland nodes first, in mass, to paralyse the whole system rather than duelling over the front line.`
- 中文对照：杜黑风格：筹划一场针对敌方后勤网络的现代无人机作战。首批大规模打击腹地节点，瘫痪全系统，不在前线缠斗。
- Negative: `No air power as mere army support, no piecemeal small raids, no front-line-only bombing, no waiting for ground advance before using air power`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
