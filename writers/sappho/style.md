# Sappho — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sappho: brief lyric fragments, direct address to gods and lovers, the body speaking, sweet-bitter love, plain words charged with feeling, silence as part of the poem`
- ZH: 萨福风格：短促的抒情残篇，直接呼告神与爱人，身体在说话，甜苦交织的爱，素朴的词承载强烈的情，沉默也是诗的一部分。

## (2) 句式与节奏

- 句式：句长：短句为主，行短而密；萨福体（Sapphic stanza）四行一节，前三行十一音节、末行五音节，行内停顿如呼吸。
- 节奏：节奏：歌唱的节奏，短促、停顿、再起；残篇的断裂本身就是节奏——断掉的地方由读者的想象接上。

## (3) 词汇与意象

- 词汇：词汇：素朴而感官——甜、苦、蜜、玫瑰、月亮、身体（汗、颤抖、脸色发青）；神名直接呼告，不绕弯；不用宏大史诗词汇。
- 意象：意象群：爱神阿佛洛狄忒、月亮与星辰、玫瑰与蜜、身体的感觉（出汗、颤抖、失语）、离别与思念、少女与婚礼。
- 禁词/禁意象：禁词/禁意象：不写史诗式的战争与英雄，不用抽象议论，不写长篇叙事。

## (4) 叙事视角与结构

- 视角：叙事视角：第一人称抒情我，直接对你（爱人、神、朋友）说话；我—你结构是全部，第三人称几乎不出现。
- 结构：结构：呼告起笔（女神啊、甜蜜的母亲），再以身体感觉层层推进，结尾常为一句祈求或一句断言；残篇无完整结构，断裂即结构。

## (5) 语气与距离

- 语气：语气：亲密、炽热而坦率，既甜蜜又痛苦；与爱人零距离，与神如与朋友对话。

## (6) 该写什么 / 不该写什么

- 该写：该写：爱的甜苦、身体的感觉、呼告、离别、月亮与玫瑰、残篇的断裂。
- 不该写：不该写：史诗战争、抽象议论、长篇叙事、冷静的旁观。
- Negative prompt: `No epic warfare, no abstract philosophical digression, no long narrative, no detached observation`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Sappho, a letter to oneself ten years from now. Short lyric lines. Direct address. The body remembers what the mind forgets. Sweet-bitter. Let the fragment break off.`
- 中文对照：萨福风格，一封写给十年后自己的信。短促的抒情行，直接呼告，身体记得头脑忘记的事，甜苦交织，让残篇在断裂处停住。
- Negative: `epic warfare, abstract digression, long narrative, detached observation`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
