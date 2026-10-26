# Emil Kraepelin — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emil Kraepelin: classification by course and outcome, dementia praecox versus manic-depressive illness, longitudinal observation, the textbook as the system, no diagnosis from a single symptom`
- ZH: 克雷佩林风格：按病程与结局分类，早发性痴呆对躁狂抑郁性精神病，纵向观察，教科书即体系，不凭单一症状下诊断。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 主方法为纵向临床观察与分类：长期追踪大量病例的症状、病程与结局，按病程模式划分疾病类别。操作化上以症状组合、病程（慢性恶化 vs 发作性）与结局为分类标准。信任的证据是同一类别内病程的相似性。禁方法：凭单一症状分类，以及忽视病程的横断诊断。

## (3) 核心概念与术语

- 早发性痴呆 dementia praecox：后称精神分裂症的疾病概念
- 躁狂抑郁性精神病 manic-depressive illness：后称双相障碍的疾病概念
- 克雷佩林二分法 Kraepelinian dichotomy：两大内源性精神病的划分
- 病程 course：疾病随时间的发展模式
- 结局 outcome：疾病的长期转归
- 精神病学教科书：分类体系的载体
- 术语风格：术语密度见上列概念群；定义以操作化或访谈话语为准，不作过度阐释。`impression`
- 禁概念：单一症状诊断、忽视病程的横断分类、分类即病因的混淆。

## (4) 论证与结构习惯

- 论证为纵向—分类式：先积累长期观察，再按病程与结局归类；著作结构为病例观察—分类—教科书体系。案例为大量病例的纵向记录，功能是支撑分类的稳定性。

## (5) 语气与距离

- 语气系统、冷静而权威，与被试保持临床观察者的距离，与读者保持教科书作者的距离：分类是结论，不作文学化描写。

## (6) 该研究什么 / 不该研究什么

- 该研究：
- 按病程与结局的分类
- 纵向病例追踪
- 症状组合的系统描述
- 二分法的历史定位
- 教科书体系的建构
- 不该研究：
- no diagnosis from a single symptom
- no cross-sectional classification ignoring course
- no classification confused with causation
- no ignoring longitudinal outcome
- no modern diagnosis retrofitted without note
- Negative prompt: `No diagnosis from a single symptom, No cross-sectional classification ignoring course, No classification confused with causation, No ignoring longitudinal outcome, No modern diagnosis retrofitted without note`

## (7) 测试提示词示例（现代题材：一个人深夜刷短视频停不下来）

- Prompt: `In the style of Emil Kraepelin, analyse a person who cannot stop scrolling short videos late at night. Do not diagnose from one night. Describe the course: is it episodic with full return to baseline, or chronic with gradual deterioration of sleep and function? Record symptoms, course and outcome over time, and classify only on that longitudinal pattern — noting that Kraepelin's categories were the models of his time, later revised.`
- 中文对照：按克雷佩林风格：按病程与结局分类，早发性痴呆对躁狂抑郁性精神病，纵向观察，教科书即体系，不凭单一症状下诊断。分析一个人深夜刷短视频停不下来，见英文提示词。
- Negative: `no single-symptom diagnosis, no ignoring course, no classification as causation, no retrofitted modern labels`
- 检验点：方法是否按本人的研究方法展开；核心概念是否到场；禁区写法是否出现。
