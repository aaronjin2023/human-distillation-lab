# Frida Kahlo — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frida Kahlo, Mexican modernist oil painting, flat vivid folk colour, self-portrait with joined eyebrows and flowers in hair, exposed body with broken Ionic column, thorns and monkeys, symbolic and direct`
- ZH: 弗里达·卡罗风格，墨西哥现代主义油画，扁平鲜明的民间色彩，连眉、花环发髻的自画像，断裂的爱奥尼柱撑开的身体，荆棘与猴子，象征而直接。

## (2) 色板方向

- 主色（7 色，颜料名）：深红、翠绿、钴蓝、金黄、白色、黑色、赭石。`verbatim`
- 主色深红 + 翠绿 + 钴蓝的墨西哥民间色，高饱和、扁平。禁：灰调、平滑学院渐变、写实透视、模糊梦境。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：平滑、细腻，几乎无笔触，如民间画；线条：清晰、均匀的轮廓线。质感：平面、光滑，无厚涂。

## (4) 构图习惯

- 画幅：中小幅自画像为主；视点：正面、平视；布局：人物居中、正面直视观者，背景是天、植物或室内；对称构图（《两个弗里达》双人对称）。裁切：人物完整、不顶边。

## (5) 光影与透视

- 光源：均匀、明亮的日光，无戏剧阴影；阴影轻而平。透视：扁平、无焦点透视，空间靠前后并置。

## (6) 该画什么 / 不该画什么

- 该画：自画像、断柱、荆棘项链、猴子、蜂鸟、特瓦纳服饰、墨西哥植物。
- 不该画：见下 Negative prompt。
- Negative prompt: `no smooth academic shading, no grey muted palette, no photographic realism, no single-point perspective, no blurred dreamy atmosphere`

## (7) 测试提示词示例（现代题材：一辆停在街边的共享单车）

- Prompt: `In the style of Frida Kahlo, a shared bicycle parked on a city street, Mexican modernist oil painting, flat vivid folk colour, self-portrait with joined eyebrows and flowers in hair, exposed body with broken Ionic column, thorns and monkeys, symbolic and direct`
- 中文对照：弗里达·卡罗风格，一辆停在街边的共享单车，墨西哥现代主义油画，扁平鲜明的民间色彩，连眉、花环发髻的自画像，断裂的爱奥尼柱撑开的身体，荆棘与猴子，象征而直接。
- Negative: 见第 (6) 节。
- 检验点：题材是否被弗里达·卡罗的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
