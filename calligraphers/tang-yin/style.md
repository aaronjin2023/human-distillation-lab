# 唐寅 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tang Yin: running script, elegant and unrestrained, learning from Zhao Mengfu and Li Beihai, strokes smooth and free, characters neat yet lively, ink even and graceful`
- ZH: 唐寅风格：行书俊逸疏放，取法赵孟頫、李北海，用笔圆转自如，结字端整而活，墨匀而秀。

## (2) 笔法

- 用笔圆转自如，中锋为主，提按和缓；起笔藏锋微露，收笔回锋带势。`impression` 行书取法赵孟頫、李北海，俊逸而有法度。`impression` 禁笔：不用方折硬朗的棱角，不用枯笔飞白，不用欹侧险绝。`impression`

## (3) 结字与章法

- 结字端整而活，重心居中，字形大小略有参差；疏密适中，不欹不险。`impression` 章法行距均匀，行气端直而俊逸，留白适中。`impression` 幅式多为册、卷，落款小字，钤印讲究。`artifact`

## (4) 墨色与节奏

- 墨色匀而秀，一幅之内浓淡变化和缓，少枯笔；笔画墨色均匀俊逸。`impression` 节奏中速平稳，起笔缓、行笔匀、收笔带势。`impression` 纸多用熟纸，墨色附着俊逸。`impression`

## (5) 书体与取法

- 书体以行书为主，兼擅楷、草；取法赵孟頫、李北海，吴门一路。`artifact` 演变：早年取法赵孟頫较谨，中年俊逸已成，晚年更趋疏放。`impression`

## (6) 该写什么 / 不该写什么

- 该写：圆转自如的中锋用笔、端整而活的结字、均匀秀润的墨色、疏密适中的章法、俊逸疏放的气息。
- 不该写：方折硬朗的棱角、枯笔飞白、欹侧险绝的结字、端正板滞的馆阁楷、浓艳重彩。
- Negative prompt: `No hard square turns, no dry flying-white strokes, no tilted dangerous characters, no stiff official script, no gaudy colour, no printed typeface`

## (7) 测试提示词示例（现代题材：“约克夏犬坐在地铁座位上”行书）

- Prompt: `In the style of Tang Yin, running script calligraphy writing 'a Yorkshire terrier sitting on a subway seat' in Chinese characters, smooth free strokes, neat lively characters, even graceful ink`
- 中文对照：唐寅风格：行书写一句“约克夏犬坐在地铁座位上”，圆转自如，端整而活，墨匀而秀。
- Negative: `No hard square turns, no dry flying-white strokes, no tilted dangerous characters, no stiff official script, no gaudy colour, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
