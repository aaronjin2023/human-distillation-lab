# Nearchus — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nearchus: an admiral's fleet crawling from the Indus to the Persian Gulf, waiting out the monsoon, watering at strange coasts, reporting whales and fish-eaters as a soldier would`
- ZH: 尼阿库斯风格：舰队统帅率船自印度河爬行至波斯湾，等季风，在陌生海岸取水，以军人笔法写鲸与食鱼者。

## (2) 导航方法

- 季风等待与沿岸爬行：印度河口等西南季风转东北季风再出航，沿阿拉伯海北岸逐段西行，靠海角与河口定位。

## (3) 造船与帆装

- 亚历山大舰队：多船编组，载士兵与补给；船只在印度河口建造，适于沿岸航行而非远洋横渡。

## (4) 航线规划习惯

- 自印度河口出发，沿今巴基斯坦、伊朗海岸西行，经霍尔木兹海峡入波斯湾，与亚历山大在苏萨会合。

## (5) 日志与海图语言

- 航海记原文佚失，事迹经阿里安《印度志》转述；鲸群、食鱼者、海怪皆按行军报告写。

## (6) 该探索什么 / 不该探索什么

- 该探索：印度河—波斯湾全程, 季风等待航法, 阿拉伯海北岸逐段测绘。
- 不该探索：no monsoon-defying sailing, no open-ocean crossing, no claims beyond the coast sailed, no civilian travelogue tone。
- Negative prompt: `no monsoon-defying sailing, no open-ocean crossing, no claims beyond the coast sailed, no civilian travelogue tone`

## (7) 测试提示词示例（现代题材：一艘无人货轮横渡太平洋 / 一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Nearchus, a fleet of uncrewed survey ships waits out the monsoon at a river mouth in 2026, then crawls along a strange coast to the Gulf, logging whales and watering places like a military report.`
- 中文对照：尼阿库斯风格：一支无人勘测船队在河口等季风转向，沿陌生海岸爬行至海湾，以军人报告笔法记录鲸群与取水点。
- Negative: `No monsoon-defying sailing, no open-ocean crossing, no claims beyond the coast, no civilian travelogue tone`
- 检验点：导航方法是否按第 (2) 节走；航线规划是否按第 (4) 节走；禁区写法是否出现。
