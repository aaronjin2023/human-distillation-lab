# 文徵明 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wen Zhengming: running and regular script of the Wu school, warm and refined, small regular script precise, running script gentle and flowing, ink light and elegant, late large characters freer`
- ZH: 文徵明风格：吴门行楷温润雅正，小楷精绝，行书温和流畅，墨淡而雅，晚年大字更放。

## (2) 笔法

- 用笔温润，中锋为主，提按和缓；小楷精绝，笔笔有法；行书温和流畅，牵丝和缓。`impression` 起笔藏锋，收笔回锋，锋芒内敛。`impression` 禁笔：不用方折硬朗的棱角，不用侧锋刷字的锋芒，不用枯笔飞白。`impression`

## (3) 结字与章法

- 结字端整雅正，重心居中，字形大小均匀而略有参差；小楷行列分明，行书行气端直而和缓。`impression` 章法行距均匀，留白适中，落款小字，钤印讲究。`artifact` 幅式多为卷、册，晚年有大字轴。`artifact`

## (4) 墨色与节奏

- 墨色淡而雅，一幅之内浓淡变化和缓，少枯笔；小楷墨浓而匀，行书墨润而活。`impression` 节奏中速平稳，起笔缓、行笔匀、收笔回。`impression` 纸多用熟纸，墨色附着温润。`impression`

## (5) 书体与取法

- 书体行书、楷书皆精，兼擅草书；取法二王、赵孟頫，吴门一路。`artifact` 演变：早年小楷精绝，中年行书温润已成，晚年大字行草更放。`impression`

## (6) 该写什么 / 不该写什么

- 该写：温润的中锋用笔、精绝的小楷、温和流畅的行书、淡而雅的墨色、吴门的雅正气息。
- 不该写：方折硬朗的棱角、侧锋刷字的锋芒、枯笔飞白、欹侧险绝的结字、浓艳重彩。
- Negative prompt: `No hard square turns, no side-brush flourish, no dry flying-white strokes, no tilted dangerous characters, no gaudy colour, no printed typeface`

## (7) 测试提示词示例（现代题材：“约克夏犬坐在地铁座位上”行书）

- Prompt: `In the style of Wen Zhengming, running script calligraphy writing 'a Yorkshire terrier sitting on a subway seat' in Chinese characters, warm gentle strokes, neat refined characters, light elegant ink`
- 中文对照：文徵明风格：行书写一句“约克夏犬坐在地铁座位上”，温润流畅，端整雅正，墨淡而雅。
- Negative: `No hard square turns, no side-brush flourish, no dry flying-white strokes, no tilted dangerous characters, no gaudy colour, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
