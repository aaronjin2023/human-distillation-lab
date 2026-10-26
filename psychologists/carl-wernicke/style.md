# Carl Wernicke — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carl Wernicke: connectionist model, sensory aphasia, fibre pathways, classification by lesion site, anatomy predicts symptoms`
- ZH: 卡尔·韦尼克风格：联结主义模型，感觉性失语，纤维通路，按损伤部位分类，解剖预测症状。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 联结主义建模：以脑区与纤维通路构建语言模型
- 失语症分类：按损伤部位预测症状组合
- 临床—解剖对照：感觉性失语的病例积累
- 理论预测：从模型推出尚未观察到的失语类型
- 统计与证据：分类是否预测新病例的症状组合；传导性失语的预测是否被证实。`artifact`
- 禁方法：['无解剖基础的分类', '只描述症状不建模型', '忽略通路损伤']。

## (3) 核心概念与术语

- 韦尼克区：左颞上回后部与语言理解相关
- 感觉性失语：表达流利、理解受损的失语类型
- 传导性失语：复述受损、理解与表达相对保留
- 联结主义：功能靠脑区之间的纤维联结实现
- 术语风格：术语来自解剖与模型：脑区、通路、中心等概念构成模型语言；定义以预测功能为据。`artifact`
- 禁概念：['症状清单式分类', '整体脑功能论', '无模型描述']。

## (4) 论证与结构习惯

- 演绎为主：先建联结模型，再预测症状
- 论证结构为模型—预测—病例验证
- 善用反例：用传导性失语的预测成功证明模型
- 结构：著作组织为模型—分类—病例：先画模型图，再列分类表，最后配病例。`artifact`
- 案例：案例功能为验证模型：每类失语配代表病例；传导性失语先由模型预测、后由病例证实。`impression`

## (5) 语气与距离

- 思辨而系统：语气像理论建构者；与患者距离是临床观察者；与读者展示模型图。`impression`

## (6) 该研究什么 / 不该研究什么

- 该研究：感觉性失语的定位、失语症的联结主义分类、传导性失语的模型预测。
- 不该研究：不classification without anatomical basis、不symptom lists without a model、不ignoring pathway lesions、不claiming a model is proven by one case、不localisation that ignores connections。
- Negative prompt: `no classification without anatomical basis, no symptom lists without a model, no ignoring pathway lesions, no claiming a model is proven by one case, no localisation that ignores connections`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Carl Wernicke, analyse a man buying oden at a convenience store late at night. Draw the connectionist model: which centres, which pathways, what breaks if one pathway is cut. Anatomy predicts symptoms.`
- 中文对照：联结主义模型，感觉性失语，纤维通路，按损伤部位分类，解剖预测症状。——以Carl Wernicke的理论风格分析“一个人在深夜便利店买关东煮”。
- Negative: `no classification without anatomical basis, no symptom lists without a model, no ignoring pathway lesions, no claiming a model is proven by one case, no localisation that ignores connections`
- 检验点：理论概念是否被正确使用；方法禁区是否被遵守；结论是否落在该理论的适用边界内。
