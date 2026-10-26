# Steven Moffat — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Steven Moffat: time as a puzzle box, witty dialogue that never stops, a twist that rewrites the episode you just watched, love as the real paradox`
- ZH: 莫法特风格：时间是一只谜盒，对白机智不停，一个反转重写你刚看完的那集，爱才是真正的悖论。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧谜题驱动：《神秘博士》每季一个时间谜题，单集独立冒险、季终回收；《神探夏洛克》单集长片结构，三幕层层反转。闪回与闪前即结构，时间线常多线交织。

## (3) 对话

- 对白快、机智、密集，人物用抢白、双关、长句交锋；潜台词多，一句玩笑可藏三层信息。动作描写简洁，场景提示明确，对白密度极高。旁白极少。

## (4) 人物弧光

- 主角多为天才与同伴：博士、夏洛克，弧光是‘聪明反被聪明误’的循环；人物在反转处看清自己，结尾常是情感落点而非逻辑收束。人物关系以搭档与爱人为主。

## (5) 类型套路与创新

- 类型：科幻 / 推理。遵守‘谜题必有解’的套路，打破‘解谜靠线索堆砌’的成见：答案藏在情感里。创新在把时间悖论写成情感结构，把机智对白写成招牌。

## (6) 该写什么 / 不该写什么

- 该写：时间作谜盒、机智密集的对白、反转重写本集、爱作悖论、季弧谜题驱动。
- 不该写：慢节奏、直白说教、类型化推理桥段、无反转的平铺、煽情过头。
- Negative prompt: `No slow pacing, no direct preaching, no mystery cliché, no flat plotting without a twist, no over-sentimentality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Steven Moffat, a man buys oden at a convenience store late at night. He meets himself, ten years older, buying the same oden. They argue about which one of them is real. The twist rewrites the scene. Love is the paradox.`
- 中文对照：莫法特风格：一个男人深夜在便利店买关东煮，遇见十年后的自己，也在买同一份关东煮。两人争论谁才是真的。反转重写这一幕。爱是悖论。
- Negative: `No slow pacing, no direct preaching, no mystery cliché, no flat plotting without a twist, no over-sentimentality`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
