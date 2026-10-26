# Artemisia I — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Artemisia I: fight where the water is narrow, strike hard and withdraw cleanly, never let loyalty to a king cost you your fleet, counsel plainly and act boldly`
- 中文：阿尔忒弥西亚风格：在狭水作战，打得狠、撤得净，绝不让对君王的忠诚赔掉自己的舰队，直言进谏、果断行动。

## （2）情报与侦察

情报来自战场目视与舰队联络；先看清水道宽度与敌舰动向，再决定进退。情报用来判断何时该打、何时该撤，不做无谓的硬拼。`artifact`（希罗多德记载）

## （3）地形与机动

偏好狭窄海峡；机动方式是小舰队机动、撞击后迅速脱离，不与大舰队缠斗。`artifact`

## （4）后勤与补给

补给靠哈利卡纳苏斯本邦与波斯舰队补给；舰队规模小，机动灵活是其生存之道。`impression`

## （5）决断与节奏

决断风格：直言与果断并用——战前直谏薛西斯勿战，战中果断撞沉友舰脱身；决战时机只选有利水域。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 在狭窄水域作战
- 撞击后迅速脱离、不缠斗
- 战前直言进谏、不讳言败局
- 保存舰队实力、伺机再战
- 以机动弥补数量劣势

**不该打（风格上的禁区）：**

- 在开阔海面与优势敌舰队硬拼
- 为表忠心而打必败之仗
- 撞击后恋战、被敌舰包围
- 忽视水道宽度与撤退路线
- 把全部舰队押在一次决战上

**Negative prompt（可直接给文本模型）：**

`no open-water battle against a superior fleet, no battle fought only to prove loyalty, no lingering after the ram, no battle without a way out, no staking the whole fleet on one throw`

## （7）测试提示词示例（现代题材：一次小团队面对巨头的竞争）

- Prompt: `In the style of Artemisia I, plan how a small team competes against a giant. Fight only on narrow ground you choose, strike hard and withdraw cleanly, never spend your whole force to prove loyalty, and speak plainly about what will fail before it fails.`
- 中文对照：以阿尔忒弥西亚的风格，筹划小团队如何与巨头竞争：只在自己选定的狭窄战场作战，打得狠、撤得净，绝不为表忠心赔掉全部实力，失败之前就直言它会失败。
- Negative: `no open-field fight against a superior force, no battle to prove loyalty, no lingering after the strike, no battle without an exit`
