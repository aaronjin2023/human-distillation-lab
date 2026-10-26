# Kukai — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kukai: Tang-style running and cursive script, vigorous and varied, powerful turns, scholarly and dynamic, one of Japan's Three Brushes`
- ZH: 空海风格：唐风行草，笔力雄健，转折多变，气格宏大，为日本三笔之一。

## (2) 笔法

- 行草用笔取法唐人，提按分明，线条雄健；转折方圆并用，起笔藏锋，收笔回锋，少轻滑浮笔。`impression`

## (3) 结字与章法

- 结字大小参差，欹正相生；章法行距宽绰，行气连绵，通幅如唐人手札，气势宏大。`impression`

## (4) 墨色与节奏

- 墨色浓润，浓淡有度；节奏雄健顿挫，快慢交替，行气如论辩般起伏。`impression`

## (5) 书体与取法

- 主导行草，取法唐人（颜真卿、王羲之一路），兼习梵文悉昙体；为日本三笔之一，唐风书法传入日本的代表一路。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：唐风行草的雄健线条。
- 该写：大小参差的结字。
- 该写：浓润有度的墨色。
- 该写：雄健顿挫的节奏。
- 该写：手札幅式的连绵章法。
- 不该写：和样假名的纤柔。
- 不该写：匀整端正的馆阁体。
- 不该写：轻滑浮薄的线条。
- 不该写：一味浓墨的滞重。
- 不该写：断笔的楷书结字。
- Negative prompt: `No delicate kana softness, no uniform guange neatness, no light floating lines, no uniformly heavy ink, no disconnected regular-script structure, no Latin alphabet`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `In the style of Kukai, Tang-style running-cursive script writing 'late night convenience store' in Chinese characters and kana, vigorous varied strokes, powerful turns, scholarly dynamic rhythm`
- 中文对照：空海风格：以唐风行草写“深夜便利店”，雄健多变，气势宏大。
- Negative: `No delicate kana softness, no uniform neatness, no light floating lines, no uniformly heavy ink, no printed typeface`
- 检验点：笔法是否对位；结字章法是否成立；墨色节奏是否可辨；禁区写法是否出现。
