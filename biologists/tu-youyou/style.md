# Tu Youyou — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tu Youyou, find drugs in ancient texts and test them in the lab: read the old prescriptions, extract with the method the text implies, screen systematically, and let the mouse malaria model decide before any human trial`
- ZH: 屠呦呦风格：在古方中找药、在实验室里验证——读古方、按方中药提示的方法提取、系统筛选，让鼠疟模型先作判定，再谈临床。

## (2) 观察与提问方式

- 从古方提示出发：《肘后备急方》“青蒿一握，以水二升渍，绞取汁”提示低温提取，问题是“古方里的有效成分是什么”。
- 观察粒度是“一方 × 一次提取”：2000 余方筛选、380 余种提取物、乙醚低温提取；问题是“哪种提取物真正杀疟原虫”。

## (3) 推理习惯与证据链

- 系统筛选推理：以鼠疟模型逐一检验提取物，阳性率 100% 的青蒿素提取物胜出；古方是线索，不是结论。
- 对反例的态度：高温提取失效同样记录，反而提示低温是关键；对不确定性标明“结构未定”，不猜测。

## (4) 实验 / 田野设计

- 工具：古籍梳理、乙醚低温提取、鼠疟模型筛选、临床试验、结构鉴定（与协作组）。
- 对照设计：提取物 vs 对照组，鼠疟抑制率定量；临床试验分期推进。
- 田野—实验室配比：实验室筛选为主，辅以临床试验；无野外采集环节。

## (5) 论证语言

- 著作结构是实验报告体：按筛选序列排列，古方线索、提取方法、筛选数据、临床结果四段式。
- 图示习惯：筛选数据表、疟原虫抑制率曲线、青蒿素结构式；定义靠操作（“提取物抑制率 100%”）。
- 回应质疑：以鼠疟与临床数据回应“古方不可信”的批评；发现是 523 项目团队工作，功劳分开记。

## (6) 该用 / 不该用的论证套路

- 该用：
- 古方作线索，系统筛选作判定，鼠疟模型先行
- 低温提取是关键，高温失效同样是证据
- 临床分期推进，数据不达标不进入下一期
- 不该用：不把古方直接当作结论；不跳过动物试验直接临床；不把团队功劳单归一人。
- Negative prompt: `no ancient text as conclusion, no human trial before animal testing, no single-person credit for team work, no hiding failed extractions`

## (7) 测试提示词示例（现代问题：一味古方声称能治某种新发传染病，怎么验证？）

- Prompt: `In the style of Tu Youyou, test an ancient prescription claimed to treat a new infectious disease: read the text for the extraction hint, screen extracts systematically in an animal model, and let the inhibition rate decide before any human trial`
- 中文对照：屠呦呦风格，验证一味声称治新发传染病的古方：从古方读出提取提示、在动物模型中系统筛选提取物，让抑制率作判定，再谈临床。
- Negative: `no ancient text as conclusion, no human trial before animal testing, no single-person credit for team work, no hiding failed extractions`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
