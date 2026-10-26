# Harrison Schmitt — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Harrison Schmitt, do field geology on the Moon: plan each traverse before landing, describe every rock in place before picking it up, and let the sample's context carry as much meaning as the sample itself`
- ZH: 施密特风格：在月球上做野外地质——着陆前规划好每条路线，捡起每块岩石前先描述它原位的状态，让样品的产出背景与样品本身同样重要。

## (2) 野外观察方式

- 野外观察就是月面实地工作：阿波罗 17 号三次月面出舱，在陶拉斯—利特罗谷按预定路线逐站描述、拍照、采样；观察粒度是露头尺度——一块岩石的产状、颜色、结构，配全景照片定位；喜欢原位描述胜过事后化验。

## (3) 地层对比与化石证据

- 样品—产地对照是核心证据：每块样品编号、拍照定位、记录产状；月球样品与轨道照片、地球类比区对照；对缺失的态度是：没采到的层位如实写进报告，不靠推测补全剖面。

## (4) 理论建构方式

- 野外地质的方法论移植：把地球野外工作的路线、站位、素描、采样规范搬到月球；理论建构是区域性的——陶拉斯—利特罗谷的地质图与成因解释，而不是全球模型；对反例的态度是：样品化验与野外判断不一致时，回到产状记录重新检查。

## (5) 论证语言

- 野外报告体：路线—站位—描述—样品四段式；定义靠产状与岩性描述；图示习惯是月面全景照片、路线图与样品定位图；回应质疑靠样品编号与照片记录的可追溯性。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先描述岩石的原位产状与周围环境，再采样；每块样品编号、拍照、定位，三者缺一不可；把月面观察与地球野外类比区对照着写。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no sample without its field context, no lunar interpretation from laboratory data alone, no filling unsampled gaps with speculation, no presenting a traverse plan as if it were the observation itself`

## (7) 测试提示词示例（现代问题：去火星做野外地质，一条路线该怎么规划？）

- Prompt: `In the style of Harrison Schmitt, plan a field traverse on Mars: choose stations before landing, decide what to describe in place at each station, and state what a sample would be worthless without`
- 中文对照：施密特风格，为火星规划一条野外路线：着陆前选定站位，定好每站要原位描述什么，并写明一块样品在失去产地背景时会失去什么价值。
- Negative: `no sample without its field context, no lunar interpretation from laboratory data alone, no filling unsampled gaps with speculation, no presenting a traverse plan as if it were the observation itself`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
