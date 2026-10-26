# Qi Jiguang — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Qi Jiguang: train the soldier before the battle, the mandarin duck formation is the answer, discipline and drill beat courage alone, write the manual as you fight`
- 中文：戚继光风格：战前先练兵，鸳鸯阵就是答案，纪律与操练胜过单凭勇气，边打仗边写操典。

## （2）情报与侦察

情报来自斥候、降倭与对倭寇战法的精通；先摸清倭寇部署与战法，再以鸳鸯阵破之。情报用来选阵法，不做硬碰。`artifact`

## （3）地形与机动

偏好东南沿海与北方边地的练兵作战；机动方式是鸳鸯阵协同、步骑配合，辅以火器。`artifact`

## （4）后勤与补给

补给靠明朝财政与沿途屯田，练兵先行、军饷先行；行军距离受辎重与季节约束。`artifact`

## （5）决断与节奏

决断风格：练兵与严法并用——先练成戚家军，再打仗；决战时机只选己方占优时，不打无把握的仗。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 先练兵、后打仗
- 鸳鸯阵协同、步骑配合
- 严法与操练并用
- 边打边写操典
- 只打己方占优的仗

**不该打（风格上的禁区）：**

- 没有练兵就打仗
- 没有阵法就硬打倭寇
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑
- 把操典与实战割裂

**Negative prompt（可直接给文本模型）：**

`no battle without training, no battle without formation, no pursuit beyond supply, no halt that lets the enemy regroup, no manual without practice`

## （7）测试提示词示例（现代题材：一次现代企业的组织改革）

- Prompt: `In the style of Qi Jiguang, plan a company's reorganisation. Train the soldier before the battle: the formation is the answer, discipline and drill beat courage alone, and write the manual as you fight.`
- 中文对照：以戚继光的风格，筹划一家企业的组织改革：战前先练兵，阵法就是答案，纪律与操练胜过单凭勇气，边打仗边写操典。
- Negative: `no battle without training, no battle without formation, no frontal price war, no manual without practice`
