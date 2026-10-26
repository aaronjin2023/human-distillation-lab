# Ume Kenjiro — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ume Kenjiro: French civil law as model, prompt codification, freedom of contract, settlement as a legal institution, clear and systematic prose`
- ZH: 梅谦次郎风格：法国民法为蓝本，民法典速行，契约自由，和解即法律制度，清晰而系统的散文。

## (2) 论证方式

- 论证结构：从法国民法出发，以速行法典为大前提，推向契约自由的结论；多用比较法与体系解释，辅以对延期论的反驳；反驳预设（“法典可缓行”）以“社会需要法典”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中长句为主，清晰、系统；术语密度高（民法典、契约自由、和解、要义），喜用法国民法术语的日译；语气：立法者的果断，不拖泥带水；善用体系表格推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：法国民法传统、民法典速行、契约自由、和解制度、体系完整。`artifact`
- 价值排序：原则冲突时先保法典的速行与体系完整，后保单条的完美；先保契约自由，后保习惯的保留。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 立法者：法典起草的写法——蓝本先行、条文逐条起草、审议修改、颁布；学者：《民法要义》以要义体逐条释义。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 法国民法为蓝本：以布瓦索纳德旧民法典草案为起点，主张速行。`artifact`
- 民法典速行：反对延期，主张立即施行法典。`artifact`
- 契约自由：契约自由是民法典的核心。`impression`
- 和解论：和解是独立的法律制度，博士论文即以和解为题。`artifact`
- 演变：早期留法留德，中期民法典起草三人之一，晚期法政大学与朝鲜法典编纂。`impression`
- 不该写：No delay in codification, no custom as exemption, no piecemeal perfectionism, no rhetoric without a code, no hesitation in legislation。
- Negative prompt: `No delay in codification, no custom as exemption, no piecemeal perfectionism, no rhetoric without a code, no hesitation in legislation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ume Kenjiro, a civil-code analysis of a settlement agreement: freedom of contract, settlement as an institution, the code must be applied promptly and systematically, not delayed for perfection.`
- 中文对照：梅谦次郎风格：一份民法典分析，论和解协议：契约自由，和解是独立的法律制度，法典须及时系统地适用，不为求完美而拖延。
- Negative: `No delay in codification, no custom as exemption, no piecemeal perfectionism, no rhetoric without a code`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
