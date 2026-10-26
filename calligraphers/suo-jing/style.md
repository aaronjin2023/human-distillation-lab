# Suo Jing — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Suo Jing: zhangcao cursive, silver hooks and iron strokes, each character separate yet brisk, the Western Jin bridge of cursive`
- ZH: 索靖风格：章草银钩铁画，字字独立而疾书，为西晋草书之桥。

## (2) 笔法

- 章草用笔：隶意未脱，波磔犹存而省减；笔画劲利如银钩铁画，起收分明。`impression`（摹本与章草通说）
- 禁笔：他几乎不用的笔法——今草的连绵缠绕、楷书的方折。

## (3) 结字与章法

- 结字扁阔近隶，字字独立不连绵；笔画省减后仍可辨，章法行列整齐。`impression`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 摹本墨色不可据为原墨；节奏疾速而字字分明，一字一顿而笔势相连。`artifact`

## (5) 书体与取法

- 书体：章草。西晋章草代表，与张芝并称；“银钩虿尾”之说见后世著录。`impression`
- 演变：真迹已佚，无分期。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 章草的字字独立
- 隶意未脱的省减笔画
- 银钩铁画般的劲利线条
- 疾速而分明的节奏
- 扁阔近隶的结字
- 不该写：
- 今草的连绵缠绕
- 楷书的方折
- 小篆的圆转匀线
- 狂草的放纵
- 浓艳装饰
- Negative prompt: `No continuous cursive connections, no regular-script square turns, no seal-script rounded curves, no wild-cursive flourishes, no ornate decoration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Suo Jing, zhangcao cursive writing modern Tokyo subway station names, silver-hook iron strokes, each character separate yet brisk, flat wide forms, ink on paper`
- 中文对照：索靖风格：以章草写现代东京地铁站名，银钩铁画，字字独立而疾书，结字扁阔。
- Negative: `No continuous cursive connections, no regular-script square turns, no seal-script rounded curves, no wild-cursive flourishes, no ornate decoration`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
