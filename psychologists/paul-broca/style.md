# Paul Broca — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Broca: lesion method, language is localised, one patient one lesion, anatomy before theory, careful autopsy evidence`
- ZH: 保罗·布洛卡风格：损伤法，语言有定位，一例患者一处损伤，解剖先于理论，谨慎的尸检证据。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 损伤法：以脑损伤部位与语言缺损的对应关系定位功能
- 临床—解剖对照：生前语言观察与死后脑解剖配对
- 个案积累：多例失语症患者的损伤部位比较
- 测量与绘图：脑区位置的精确解剖描述
- 统计与证据：生前语言缺损与死后损伤部位的一致性；多例患者的损伤重叠区。`artifact`
- 禁方法：['无解剖证据的功能猜测', '以单一病例推广全脑功能', '忽略右脑的语言作用']。

## (3) 核心概念与术语

- 布洛卡区：左额下回后部与言语产生相关
- 运动性失语：理解保留、表达受损的失语类型
- 语言定位：语言功能可定位于特定脑区
- 损伤法：功能定位的基本方法
- 术语风格：术语来自解剖学：脑区命名精确，定义以位置与缺损为据；造词少，多为解剖命名。`artifact`
- 禁概念：['整体脑功能论', '无证据定位', '心灵官能']。

## (4) 论证与结构习惯

- 归纳为主：从个案积累到定位结论
- 论证结构为病例—解剖—定位：每例配生前记录与死后解剖
- 善用反例：损伤他处而语言保留的病例界定边界
- 结构：论文组织为病例报告：病史、语言检查、解剖发现、结论四段式。`artifact`
- 案例：案例即全部证据：以失语症患者个案为核心，著名病例“Tan”只保留“tan”一音；案例功能为定位证据。`artifact`

## (5) 语气与距离

- 克制、解剖学式的冷静：语气像外科报告；与患者距离是临床观察者；与读者呈证据、不作夸大。`impression`

## (6) 该研究什么 / 不该研究什么

- 该研究：语言的脑定位、运动性失语的临床—解剖对照、损伤法的方法论。
- 不该研究：不localisation without anatomical evidence、不generalising from a single case、不ignoring cases that contradict localisation、不mental faculties without brain correlates、不claims about the right hemisphere from left-lesion data alone。
- Negative prompt: `no localisation without anatomical evidence, no generalising from a single case, no ignoring cases that contradict localisation, no mental faculties without brain correlates, no claims about the right hemisphere from left-lesion data alone`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Paul Broca, analyse a small Yorkshire terrier sitting on a subway seat. Lesion method: what function is lost, what is preserved, where would the lesion be. Anatomy before theory, one case at a time, no speculation without a lesion.`
- 中文对照：损伤法，语言有定位，一例患者一处损伤，解剖先于理论，谨慎的尸检证据。——以Paul Broca的理论风格分析“一只坐在地铁里的约克夏犬”。
- Negative: `no localisation without anatomical evidence, no generalising from a single case, no ignoring cases that contradict localisation, no mental faculties without brain correlates, no claims about the right hemisphere from left-lesion data alone`
- 检验点：理论概念是否被正确使用；方法禁区是否被遵守；结论是否落在该理论的适用边界内。
