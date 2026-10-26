# Hippalus — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hippalus: a name attached to a wind, a single discovery that turned coastal crawling into a straight crossing, known only from one book's mention`
- ZH: 希帕罗斯风格：一个名字系于一阵风，一次发现把沿岸爬行变成直航，全凭一部书的一提而知。

## (2) 导航方法

- 季风直航：发现（或命名）西南季风，利用季风自红海口横渡至印度西海岸；返航候东北季风。

## (3) 造船与帆装

- 红海—印度商船：适于横渡的远洋船，不再逐站沿岸补给。

## (4) 航线规划习惯

- 自红海口直航印度西海岸，返航亦直航；航线即季风本身。

## (5) 日志与海图语言

- 其人仅见于《厄立特里亚海航行记》一提，是否真实存在有争议；季风航法或为多代水手积累，归名于一人。

## (6) 该探索什么 / 不该探索什么

- 该探索：季风横渡, 红海—印度直航, 季风历的利用。
- 不该探索：no coastal crawling, no sailing against the monsoon, no biography beyond the single mention, no claims of sole discovery。
- Negative prompt: `no coastal crawling, no sailing against the monsoon, no biography beyond the single mention, no claims of sole discovery`

## (7) 测试提示词示例（现代题材：一艘无人货轮横渡太平洋 / 一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Hippalus, an uncrewed cargo ship in 2026 rides one seasonal wind straight across an ocean, its whole method named after the wind itself, its captain known only from a single mention.`
- 中文对照：希帕罗斯风格：一艘无人货轮乘一季风直航大洋，整套航法以风命名，船长其人仅见于一部书的一提。
- Negative: `No coastal crawling, no sailing against the monsoon, no biography beyond the single mention, no claims of sole discovery`
- 检验点：导航方法是否按第 (2) 节走；航线规划是否按第 (4) 节走；禁区写法是否出现。
