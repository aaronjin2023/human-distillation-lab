# Viola Davis — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Viola Davis: raw truth without varnish, a voice that breaks open, tears that come from work not sentiment, dignity earned scene by scene`
- ZH: 维奥拉·戴维斯风格：不加粉饰的 raw 真实，声音会裂开，泪水来自劳作而非煽情，尊严是一场一场挣来的。

## (2) 形体

- 身体有分量、站姿稳固；动作朴素、从不夸张；哭戏时全身颤抖、鼻涕眼泪皆不回避；舞台功底使全身皆可调度。`impression`

## (3) 台词

- 音色浑厚、语速平稳；台词直白、少修饰；哭泣时声音裂开、仍把词说完。`artifact`

## (4) 表情与眼神

- 表情真实到不加粉饰：悲伤、愤怒、疲惫皆不回避；眼神直视、含泪而不求怜悯。`impression`

## (5) 角色类型

- 常演角色：底层黑人女性（艾比琳、罗斯）；战士/女王（纳尼斯卡）；母亲与妻子。
- 类型突破：从《帮助》的女佣到《藩篱》的罗斯（托尼奖与奥斯卡），再到《女王》的战士，表演由忍耐转向爆发；舞台出身使台词功底扎实。`artifact`
- 禁演类型：几乎不演粉饰的煽情、不演依赖外貌的轻浮主角、不演自我贬低的角色。`impression`

## (6) 该演什么 / 不该演什么

- 该演：不加粉饰的真实、裂开的声音、来自劳作的泪水、稳固的形体、一场一场挣来的尊严。
- 不该演：粉饰的煽情、依赖外貌的轻浮主角、自我贬低的表演、表情过载。
- Negative prompt: `No varnished sentimentality, no pretty-face leads, no self-degrading performance, no overacted expressions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Viola Davis, a small Yorkshire terrier sits on a subway seat, raw truth without varnish, dignity earned scene by scene, tears from work not sentiment`
- 中文对照：维奥拉·戴维斯风格：一只约克夏犬坐在地铁座位上，不加粉饰的 raw 真实，尊严是一场一场挣来的，泪水来自劳作而非煽情。
- Negative: `No varnished sentimentality, no pretty-face leads, no self-degrading performance, no overacted expressions`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
