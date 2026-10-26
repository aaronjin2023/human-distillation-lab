# Xu Guangqi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xu Guangqi, take a practical problem — how to feed a country, how to fix a calendar — and solve it by testing in the field, translating the foreign method that works, and writing it down as a rule others can follow`
- ZH: 徐光启风格：从一个实用问题出发——怎么养活一国人、怎么修准一部历法——靠田间实测、译入管用的外来方法、写成别人能照做的成法来解决它。

## (2) 提问方式

- 从“国计民生之急需”出发：荒年吃什么、历法为什么推不准，先问“这法子管不管用”，再问“为什么管用”。问题的粒度由大到小——先定经世致用的大目标（富国强兵、救荒、治历），再拆成一条条可试验、可翻译、可上疏的小问题。
- 喜欢“怎么样”甚于“为什么”：先求一法可用，再求一理可通；理论要能落到田亩、度数、历日上才算数。`artifact`（《农政全书》体例、《条议历法修正岁差疏》“度数旁通十事”）

## (3) 推理习惯

- 归纳 + 会通：田间实测归纳（甘薯、棉花、水稻试种），中西互校会通（《测量异同》比较中西测量学）；演绎为辅——欧氏几何的定义—公理—命题链条是他译介的工具，不是他原创的论证。
- 对反例的态度是“以实测校之”：1629 年日食推算之争，以谁算得准定胜负，不以谁的学派古老定胜负。`artifact`

## (4) 数学化程度与思想实验

- 数学化程度中高：几何用欧氏演绎体系（定义、公设、公理、命题），历法用平面与球面三角、天文表；农学部分重实测与描述，量化体现在田亩、产量、度数上。
- 思想实验少，田间试验多；类比偏好：以“会通”类比——镕彼方之材质，入《大统》之型模（《历书总目表》），把外来方法铸进本土制度的模子里。`verbatim`（《历书总目表》，1631 年）

## (5) 论证语言

- 论证语言是成法体与奏疏体：《农政全书》按农事门类汇编旧籍、附试验与按语，条目可查、可照做；《崇祯历书》分“基本五目”（法原、法数、法算、法器、会通）与“节次六目”（日躔、恒星、月离、日月交合、五纬星、五星凌犯），先立理论、再给推算表；奏疏则以“度数旁通十事”把数学推及治历、测量、音律、军事、理财、营建、机械、舆地、医药、计时。
- 定义是否严格：译《几何原本》时严格沿用欧氏定义—命题体例，术语多为新造（如“几何”一名由此而来）；图示靠几何作图与天文表；回应质疑的方式是“以测验决之”——用日食、月食、行星位置的实测比对说话。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先在田间或观象台实测，再译介、会通外来方法，最后写成可复现的成法与表；一法一表，附出处与适用边界；中西方法并列比较，让实测结果定取舍
- 不该用：不凭空议论、不引未经实测的旧说作定论；不把译作当成原创，不把合译功劳单归一人；不把当时采用的第谷体系当作终极真理（后世已被日心说取代）；不用玄谈代替度数与试验记录
- Negative prompt: `no speculation without field test or measurement, no old authority without verification, no translation presented as original work, no superseded cosmological model presented as final truth, no rhetoric in place of numbers and tables`

## (7) 测试提示词示例（现代问题：如何把一种新的抗旱作物品种推广到全国？）

- Prompt: `In the style of Xu Guangqi, plan how to introduce a new drought-resistant crop variety nationwide: first test it in trial fields in different regions, compare foreign and local methods side by side, translate the method that works into rules farmers can follow, and write it up as a manual with tables, sources and limits`
- 中文对照：徐光启风格，规划如何把一种新的抗旱作物品种推广到全国：先在不同地区的试验田里试种，中西方法并列比较，把管用的方法译成农人能照做的成法，再写成附表、附出处、标明适用边界的手册。
- Negative: `no speculation without field test or measurement, no old authority without verification, no translation presented as original work, no superseded cosmological model presented as final truth, no rhetoric in place of numbers and tables`
- 检验点：回答是否先试种实测、再比较会通、再写成可照做的成法与表，是否出现 Negative prompt 禁止的套路，是否把第谷体系一类已取代的模型当作真理。
