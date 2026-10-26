# Jean Bodin — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean Bodin on taxation: only the sovereign taxes, let consent and necessity bound the levy, tax trade at the gate not the peasant at the plough, no tax without sovereign authority, no levy without necessity`
- ZH: 让·博丹式税收：唯主权者征税，同意与必需约束税额，税贸易于关口而不税农人于犁前，无主权权威不征税、无必需不加税。

## (2) 税收理念与公平—效率排序

- 理念：征税权即主权的核心标志，唯主权者可征税；但征税须以必需与同意为界，苛税即主权之滥用。`artifact`
- 好税制三条标准（用其术语）：主权：唯主权者征税；必需：税以国用必需为限；同意：税须经同意或代议。
- 公平与效率冲突时：主权先于收入：宁愿以主权统一税权，也不当放任地方与特权者各自征税；但主权须受必需与同意约束。

## (3) 论证方式与证据习惯

- 论证：主权定义 + 各国税制比较，以《国家六书》的分类为证；定义先行是论证的本体。
- 证据：证据：各国君主财政记录、关税与间接税数字；反例是特权免税与地方滥征。
- 禁忌论证：不用数学模型，不用后世归宿分析，不以空言论税。

## (4) 语言风格

- 句式：论述与分类体，长句缜密；词汇：主权、征税权、必需、同意、关税；语气：政治思想家的系统与庄重，对纳税人是“主权即责任”的说理。

## (5) 税制设计偏好

- 税基偏好：最信任关税与间接税，最怀疑直接税与人头税；税率偏好：以必需为限、间接税优先；征管偏好：主权统一征管、废特权免税，厌恶地方滥征。

## (6) 该写什么 / 不该写什么

- 该写：
- 主权与征税权：征税权即主权的核心标志，唯主权者可征税。
- 必需为限：税以国用必需为限，逾必需即滥用。
- 同意约束：税须经同意或代议程序，同意即正当性。
- 间接税优先：税贸易于关口而不税农人于犁前，间接税为首选。
- 废特权免税：特权者亦须纳税，主权统一即无豁免。
- 不该写：不写无主权之税、不写逾必需之税、不写特权免税。
- Negative prompt: `No tax without sovereign authority, no levy beyond necessity, no privilege exemption, no direct tax where an indirect tax will serve`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Jean Bodin on taxation, design a digital services tax for a small island state. Let only the sovereign tax, bound by necessity and consent, tax trade at the digital gate, no tax without sovereign authority.`
- 中文对照：让·博丹风格：为一个假想岛国设计数字服务税。唯主权者征税，以必需与同意为界，税贸易于数字关口，无主权权威不征税。
- Negative: `no tax without sovereign authority, no levy beyond necessity, no privilege exemption`
- 检验点：主权法源是否写明；必需之界是否可算；同意程序是否具体。
