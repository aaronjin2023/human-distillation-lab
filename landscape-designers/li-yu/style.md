# Li Yu — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Yu, Ming-Qing garden theory, the garden of leisure, small and clever, a mustard seed holds a mountain, windows as paintings, pavilions for pleasure, witty and practical`
- ZH: 李渔风格，明清造园理论，闲情之园，小而巧，芥子纳须弥，窗即画，亭为乐，机智而实用。

## (2) 空间布局

- 自然不对称，小中见大；窗、廊、亭为布局之眼，一景一窗；游线短曲，视线落在窗中山水；尺度极小，园如芥子，人在园中如在画中。`artifact`（《闲情偶寄》）

## (3) 水石植物

- 水：小池、清溪，水面小而曲；石：湖石小品，叠山小而精；植物：花木四季，梅兰竹菊，季相以四季花事为高光。`artifact`（《闲情偶寄》）

## (4) 借景与框景

- 借景：借窗为框，窗即画框，框内取山水；对景以窗与窗相望；障景以屏风、曲廊为法。`artifact`（《闲情偶寄》）

## (5) 材料与季节变化

- 材料：木、竹、砖、瓦、湖石，取材家常；季节：四季花事皆为高光，园无淡季；光影：窗光为主，日光透窗成画。`artifact`（《闲情偶寄》）

## (6) 该造什么 / 不该造什么

- 该造：芥子纳须弥、窗即画框、一景一窗、小中见大、四季花事、半亩之园。`artifact`
- 不该造：no symmetrical axis, no grand rockery, no large water surface, no bright heavy colour blocks, no crowded pavilions。
- Negative prompt: `No symmetrical axis, no grand rockery, no large water surface, no bright heavy colour blocks, no crowded pavilions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Li Yu, a tiny balcony garden in a modern apartment, windows as paintings framing a potted pine and a miniature rockery, a small water bowl, seasonal flowers in turn, witty and practical, a mustard seed holds a mountain`
- 中文对照：李渔风格：现代公寓里的一座小小阳台园，窗即画框，框内盆松与微型假山，一钵清水，四季花事轮换，机智实用，芥子纳须弥。
- Negative: `No symmetrical axis, no grand rockery, no large water surface, no bright heavy colour blocks, no crowded pavilions`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
