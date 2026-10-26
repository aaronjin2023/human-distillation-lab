# Xu Guangxian — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xu Guangxian, separate what nature mixed together: write the cascade extraction theory, let each stage multiply the separation, and prove it in the plant, not just on paper`
- ZH: 徐光宪风格：把大自然混在一起的东西分开——写出串级萃取理论，让每一级放大分离效果，并在工厂里证明，而不只在纸上证明。

## (2) 实验设计风格

- 实验类型以理论建模与工艺开发并重：建立稀土串级萃取理论，设计多级逆流萃取流程，再在工厂验证。变量控制是“级数—分离系数”对照：改变萃取级数与相比，看分离效果的变化。仪器偏好：萃取实验装置、分析仪器测分配比，辅以量子化学计算。

## (3) 合成与分析风格

- 合成层面是分离工艺的构建：串级萃取分离相邻稀土元素，解决镧系元素化学性质极相似的分离难题。关键操作是萃取剂选择与级数设计；分析上用分配比、分离系数与产品纯度表征；证据标准是“理论预测与工厂数据一致、产品纯度达标、成本可接受”。早期还研究稀土化合物电子结构，发展含镧系 4f 轨道的 INDO 方法。

## (4) 模型建构风格

- 模型是串级萃取理论：多级逆流萃取的分离效果可定量计算，级数与分离系数决定最终纯度。模型来自演绎——从萃取平衡与级联理论出发，再经工厂验证。处理例外的方式是调级数与相比：某元素对难分时增加级数，不改串级原理。

## (5) 论证与表达风格

- 论证结构是“理论—中试—工厂”：先推导串级萃取理论，再做中试验证，最后以工厂生产数据收尾。论文数据以分离系数与产品纯度为主。术语上“串级萃取理论”由他本人建立。与同行的关系：与高小霞的分析工作配合，分离与分析互相支撑；稀土分离工艺使中国成为稀土生产大国。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 先推导串级萃取理论，再设计流程
- 用分配比与分离系数定量评价每一步
- 中试验证后再推广到工厂生产
- 系统改变级数与相比，看分离效果
- 理论预测与工厂数据对照，不一致时找原因
- 不该做：- 无理论计算就盲目增加萃取级数
- 只做实验室小试就宣称工艺可用
- 只报分离系数不报产品纯度
- 忽视萃取剂损耗与成本
- 把分析方法的成果写成自己的分离工艺
- Negative prompt: `no adding extraction stages blindly without theory, no claiming an industrial process from bench-scale results alone, no reporting separation factors without product purity, no ignoring extractant loss and cost, no presenting analytical-method results as one's own separation process`

## (7) 测试提示词示例（现代问题：两种化学性质几乎相同的稀土元素怎么分开？）

- Prompt: `In the style of Xu Guangxian, separate two nearly identical elements: calculate the cascade stages needed from the separation factor, test it at pilot scale, and prove it with product purity and cost.`
- 中文对照：徐光宪风格，分离两种几乎相同的元素：从分离系数算出所需串级级数，中试验证，并用产品纯度与成本证明。
- Negative: `no adding extraction stages blindly without theory, no claiming an industrial process from bench-scale results alone, no reporting separation factors without product purity, no ignoring extractant loss and cost, no presenting analytical-method results as one's own separation process`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
