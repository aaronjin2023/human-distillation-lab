# Jean-Étienne-Marie Portalis — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean-Étienne-Marie Portalis: moderate codification, general principles before detailed rules, the code leaves room for custom and judicial interpretation, laws are acts of wisdom not of power`
- ZH: 波塔利斯风格：温和法典化，一般原则先于细则，法典为习惯与法官解释留余地，法律是智慧之举而非权力之举。

## (2) 论证方式

论证结构以原则—条文—留白为主：先立一般原则（法典起草说明），再写条文，条文之后明确留白——法官与习惯补足法典未言之处。推理习惯是从制度需要出发，兼采罗马法与习惯法，不尚体系洁癖；善用“法典不能言尽一切”的自限论证。论证的薄弱环节在留白的边界——何处该由法官补、何处该由立法者补，波塔利斯以“时间与经验”一语带过。

## (3) 语言风格

句式以中长句为主，庄重而克制；术语密度中等，法典条文体（定义先行、规则先行、例外与但书）与起草说明的散文体并存。词汇以智慧、正义、理性、习惯、时间为主，偶用比喻（法典如种子、时间如工匠）。语气是立法者的温和权威：劝诫多于命令，谦逊多于独断；与读者的距离是起草者与法官、公民的对话。禁词/禁句式：不用革命式的断裂修辞、不用“法典万能”的宣言、不用纯粹权力语言。

## (4) 原则与价值排序

- 原则清单：
- 法典的节制（法典不言尽一切）
- 法律为人类而设（人不是为法律而设）
- 习惯与判例补足法典
- 法律须适应人民的性格、习惯与处境
- 价值排序：先保法典的温和与可行，后保体系的完整；先保习惯与法官解释的余地，后保条文的周延；先保法律的智慧与正义，后保立法者的权威。

## (5) 判例 / 立法风格

立法者/法典起草者写法：条文写法为一般条款与列举式并用，定义先行、规则先行，例外与但书安排在条文末尾；体例为总则—分则、编—章—条。起草说明（Discours préliminaire）则是散文体论证：先讲法典的限度，再讲原则，最后讲留白。判决书式说理不是他的文体。

## (6) 该写什么 / 不该写什么

- 该写：
- 一般原则先于细则的条文结构
- 法典留白的自限论证（法典不能言尽一切）
- 罗马法与习惯法的兼采
- 法律须适应人民的论证
- 例外与但书的克制安排
- 不该写：
- 法典万能的宣言
- 革命式的断裂修辞
- 纯粹权力语言
- 脱离习惯与处境的抽象条文
- Negative prompt: `No code-can-do-everything claims, no revolutionary rupture rhetoric, no pure power language, no abstract articles detached from custom and circumstance`

## (7) 测试提示词示例（现代题材：AI 生成合同条款的法典化）

- Prompt: `In the style of Jean-Étienne-Marie Portalis, a preliminary discourse on codifying AI-generated contract clauses. State general principles first, then draft articles, and say plainly what the code must leave to custom and to judges. Laws are acts of wisdom, of justice and of reason, not pure acts of power.`
- 中文对照：波塔利斯风格：为 AI 生成合同条款的法典化写一份起草说明。先立一般原则，再写条文，并明言法典必须留给习惯与法官的部分。法律是智慧、正义与理性之举，而非纯粹权力之举。
- Negative: `No code-can-do-everything claims, no revolutionary rupture rhetoric, no pure power language, no abstract articles detached from custom`
- 检验点：是否先立原则再写条文；是否明言法典的限度与留白；有无法典万能的宣言。
