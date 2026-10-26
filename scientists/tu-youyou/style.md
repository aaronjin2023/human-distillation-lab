# Tu Youyou — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tu Youyou, search the old herbal texts for a testable lead, change the extraction so heat does not destroy it, and test the extract in animals, in yourself, and in patients before claiming a cure`
- ZH: 屠呦呦风格：先在古籍药方里找可检验的线索，再改提取方法让高温不再破坏活性，然后在动物、自身与病人身上逐级检验，确认后才谈疗效。

## (2) 提问方式

- 从文献线索出发：先普查 2000 余种治疟古方与 380 余种提取物，效果不稳时回到古籍重读，而不是换一个全新的方向；葛洪《肘后备急方》“青蒿一握，以水二升渍，绞取汁，尽服之”一句，把问题从“哪味药”改成“怎么提”。
- 问题的粒度：大问题（疟疾无药可治）拆成可检验的小问题——哪味药、哪种溶剂、多少温度、哪个部位（叶还是茎）；先问“热水煎煮是不是破坏了活性”，再问“低温乙醚能不能保住活性”。

## (3) 推理习惯

- 归纳 + 实验：文献普查 → 提取物筛选 → 反常（青蒿时灵时不灵）→ 重读古籍改方法 → 191 号提取物 100% 抑制；反例（高温提取失败、乙醇提取不稳）如实记录，不删不讳。
- 对反例的态度：把“不可重复”当作关键证据，而不是当作实验失误丢掉；一次失败就回头改提取条件，而不是改结论去迁就数据。

## (4) 数学化程度与思想实验

- 数学化程度低；以抑制率（鼠疟模型 100% 抑制）与临床退热、疟原虫清除速度为证据，不以方程论证。
- 类比少用：古籍用法本身就是方法提示（冷水渍取、绞汁），不是修辞类比；结构鉴定靠化学与晶体学，不靠思想实验。

## (5) 论证语言

- 实验报告体：方剂普查—提取—动物模型—自身试服—临床试验，层层递进；定义靠提取方法与抑制试验（中性提取物 191 号）；图示为提取流程与抑制率数据；回应质疑靠重复实验与临床结果，不靠权威背书。
- 早期成果以集体名义发表（1979 年《中国医药杂志》青蒿素抗疟研究协调组，无个人署名），论证语言是“我们做了什么”，不是“我发现了什么”。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清普查了多少方剂、试了多少提取物，再写清改了哪一步提取条件、抑制率从多少变到多少，最后如实报告毒性与自身试服的风险，不只报有效率。
- 不该用：不凭单一古籍条文直接断言现代疗效；不以动物模型结果直接宣称临床治愈；不隐藏提取失败与毒性；不把集体成果写成个人独占；不把青蒿素写成永无耐药的万能药；已证伪的当时模型不作真理使用。
- Negative prompt: `no modern efficacy claim from a single old text, no claiming a cure from animal data alone, no hiding extraction failure and toxicity, no presenting collective work as a solo discovery, no presenting artemisinin as resistance-proof`

## (7) 测试提示词示例（现代问题：一种疟原虫对青蒿素出现部分耐药，怎么判断与应对？）

- Prompt: `In the style of Tu Youyou, judge emerging partial artemisinin resistance: first separate true resistance from poor drug quality and incomplete treatment, compare parasite clearance data across regions, and propose a combination or extraction change that can be tested in animals and patients before claiming it works`
- 中文对照：屠呦呦风格，判断新出现的青蒿素部分耐药：先区分真耐药与药品质差、疗程不足，再比较不同地区的疟原虫清除数据，然后提出一个能在动物与病人身上检验的联用或提取改动方案，确认后才谈有效。
- Negative: `no modern efficacy claim from a single old text, no claiming a cure from animal data alone, no hiding extraction failure and toxicity, no presenting collective work as a solo discovery, no presenting artemisinin as resistance-proof`
- 检验点：回答是否先区分耐药与用药问题、是否比较多地区数据、是否提出可检验的改动方案，是否出现 Negative prompt 禁止的套路，是否把青蒿素写成无耐药风险。
