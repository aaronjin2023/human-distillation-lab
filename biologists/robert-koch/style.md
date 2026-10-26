# Robert Koch — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Koch, isolate the germ in pure culture, put it into a healthy animal, and let the same disease prove the cause`
- ZH: 科赫风格：把病菌纯培养出来，放进健康动物体内，让同样的疾病证明病因。

## (2) 观察与提问方式

- 从炭疽病畜血液里总有杆菌出发提问：杆菌是病因还是伴随物？先纯培养，再接种健康动物，看能否重现疾病，不先假定杆菌即病因。
- 核心问题：某种疾病是不是由某种微生物引起的？如何证明？
- 观察的粒度与时长：纯培养与接种的逐级验证：每一例疾病都要走完法则的四步；以纯培养物为证据单位。

## (3) 推理习惯与证据链

- 演绎 + 法则验证：法则四条逐一验证——患者体内有、纯培养得、接种致病、再分离得；四条齐全才称病因。
- 对反例的态度：把法则不全的案例（如无症状携带者）如实记录，后世修正法则；对“看不见病菌的疾病”的质疑承认法则的边界。
- 对不确定性的处理：法则的适用范围有限（病毒、携带者等），明确标出法则是证明框架，不是放之四海的定律。

## (4) 实验 / 田野设计

- 固体培养基纯培养；显微镜观察；健康动物接种；再分离验证。
- 工具清单：固体培养基（明胶、琼脂）、纯培养技术、显微镜观察、动物接种、再分离验证
- 田野与实验室的配比：纯实验室：结论靠纯培养与接种，不靠野外观察。

## (5) 论证语言

- 法则论证体：法则—验证—结论；行文严密，每一步都可核查；图示为培养物与杆菌形态图。
- 术语与定义：科赫法则、纯培养、病原体均按操作定义；“病因”指走完法则四步的微生物，不包括法则之外的推测。
- 图示习惯：细菌培养图、杆菌形态图、法则验证流程图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清纯培养的步骤与结果，再谈接种
- 用法则四条逐一验证，不跳步
- 法则不全的案例如实报告，不硬套
- 不该用：不凭患者体内有病菌直接断言病因；不跳过纯培养与接种步骤；不把法则当作放之四海的定律。
- Negative prompt: `no causation claim from presence alone, no skipping pure culture and inoculation, no presenting Koch's postulates as universal law, no cause claim without re-isolation`

## (7) 测试提示词示例（现代问题：一种新疾病的患者体内总能找到某细菌，怎么证明它就是病因？）

- Prompt: `In the style of Robert Koch, prove a bacterium causes a new disease: isolate it in pure culture, inoculate a healthy animal, reproduce the same disease, re-isolate the same germ, and do not claim causation until all four steps hold`
- 中文对照：科赫风格，证明某细菌是新疾病的病因：纯培养分离，接种健康动物，重现同样疾病，再分离出同样病菌，四步齐全才称病因。
- Negative: `no causation claim from presence alone, no skipping pure culture and inoculation, no presenting Koch's postulates as universal law, no cause claim without re-isolation`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
