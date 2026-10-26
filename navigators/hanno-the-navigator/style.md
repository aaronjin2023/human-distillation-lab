# Hanno the Navigator — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hanno the Navigator: a state periplus down the West African coast, colony by colony, river mouth by river mouth, day-counts and landmarks, no speculation beyond the shore`
- ZH: 汉诺风格：沿西非海岸逐站南下的国家航海记，一个殖民点接一个河口，记日程与地标，不写岸外臆测。

## (2) 导航方法

- 沿岸航行与日程推算：以日航程计距离，靠河口、海角、岛屿等地标定位；无纬度测定，靠白天航行、夜间近岸停泊。

## (3) 造船与帆装

- 迦太基大型船队：据《航海记》载六十艘船，载殖民者与补给；船队编组航行，分段设殖民点，船只兼作运兵与补给。

## (4) 航线规划习惯

- 自加迪斯出直布罗陀海峡，沿西非海岸南下，逐段设点；返航原路北上；不横渡大洋，不离岸远航。

## (5) 日志与海图语言

- 《航海记》体例：逐日记航程、登陆点、河流、野兽与土著遭遇；语言简洁如行政报告，地名与日程是骨架。

## (6) 该探索什么 / 不该探索什么

- 该探索：西非海岸逐段南下, 河口与海角地标定位, 沿岸殖民点选址。
- 不该探索：no open-ocean crossings, no latitude fixes, no speculation beyond the shore, no romantic adventure。
- Negative prompt: `no open-ocean crossings, no latitude fixes, no speculation beyond the shore, no romantic adventure`

## (7) 测试提示词示例（现代题材：一艘无人货轮横渡太平洋 / 一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Hanno the Navigator, an uncrewed cargo ship sails down the West African coast in 2026, logging each day's run, each river mouth and headland, anchoring at night, never guessing beyond the shore.`
- 中文对照：汉诺风格：一艘无人货轮沿西非海岸南下，逐日记录航程、每个河口与海角，夜间近岸停泊，绝不臆测岸外之事。
- Negative: `No open-ocean crossing, no latitude fixes, no romantic adventure, no speculation beyond the shore`
- 检验点：导航方法是否按第 (2) 节走；航线规划是否按第 (4) 节走；禁区写法是否出现。
