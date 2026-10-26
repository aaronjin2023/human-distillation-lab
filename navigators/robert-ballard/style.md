# Robert Ballard — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Ballard: remote vehicles over the abyss, Argo's cameras finding Titanic, hydrothermal vents in darkness, plain technical logs, the seafloor as a chart to be read`
- ZH: 巴拉德风格：遥控潜水器越深渊，阿耳戈号镜头找到泰坦尼克号，黑暗中的深海热泉，平实的技术日志，海底就是待读的海图。

## (2) 导航方法

定位：水面以 GPS 定位，水下以声呐与遥控潜水器导航；调查按海底地形网格规划。`artifact` 航向：按网格逐区搜索，海底地形即航线。`artifact`

## (3) 造船与帆装

船型：考察船（诺尔号 Knorr）+ 遥控潜水器阿耳戈（Argo）与阿尔文（Alvin）；下潜以遥控器代人。补给：考察补给按航次备足。`artifact`

## (4) 航线规划习惯

路线：深海调查航线：按网格搜索北大西洋海底，1985 年定位泰坦尼克号。节奏：搜索步占大头，航行只为抵达调查区。`artifact`

## (5) 日志与海图语言

日志体例：日期—位置—深度—声呐—影像，逐日登记；语言：技术性、平实，数据先行。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：深海遥控调查、海底网格搜索、热泉与沉船定位。
- 不该探索：不无声呐依据的海底断言；不脱离网格的随机搜索；不浪漫化的沉船叙事。
- Negative prompt: `No seafloor claims without sonar, no random searching without a grid, no romanticised wreck narrative, no staged deep-sea footage`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Robert Ballard, a small Yorkshire terrier rides the subway with a remote camera. It searches the tunnels grid by grid, finds a lost ship of commuters in the dark, and logs sonar, depth and images at every square.`
- 中文对照：巴拉德风格：一只约克夏犬带着遥控镜头乘地铁。它逐格搜索隧道，在黑暗中找到一艘失落的通勤者之船，每格记录声呐、深度与影像。
- Negative: `No seafloor claims without sonar, no random searching without a grid, no romanticised wreck narrative, no cute anthropomorphism`
- 检验点：搜索是否按网格；定位是否有声呐依据；沉船是否以数据为准。
