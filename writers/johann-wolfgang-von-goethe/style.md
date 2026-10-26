# Johann Wolfgang von Goethe — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Goethe: striving without rest, the moment that must be held, Bildung as slow growth, lyric and aphorism side by side, the whole in the part`
- ZH: 歌德风格：永不停息的追求，必须留住的一瞬，教养小说式的缓慢成长，抒情与箴言并置，局部中见全体。

## (2) 句式与节奏

- 句式：句长：长短交错——抒情短句如歌，思辨长句绵延；箴言式短句常为一段的收束。
- 节奏：节奏：缓慢的成长节奏——《威廉·迈斯特》以岁月为单位，《浮士德》以一生为单位；高潮不在情节，在领悟的一瞬。

## (3) 词汇与意象

- 词汇：词汇：追求（streben）、瞬间（Augenblick）、教养（Bildung）、自然、爱、死；爱用箴言与格言。
- 意象：意象群：浮士德的书房与魔鬼、维特的绿衣与手枪、威廉的剧场、自然（植物、岩石、光）、瞬间与永恒。
- 禁词/禁意象：禁词/禁意象：不写快节奏的情节推进，不用廉价的激情，不写单一的讽刺。

## (4) 叙事视角与结构

- 视角：叙事视角：全知而温和的叙述者，时而贴近人物内心；书信体（《维特》）则为第一人称的直接倾诉。
- 结构：结构：《浮士德》两部（1808、1832），跨越一生；《威廉·迈斯特》为成长小说，旅程即结构；《维特》为书信体，日期即结构。

## (5) 语气与距离

- 语气：语气：庄重、温和而深邃；与人物的距离如导师——爱他们，也让他们付出代价。

## (6) 该写什么 / 不该写什么

- 该写：该写：追求与瞬间、成长与教养、抒情与箴言、局部中见全体。
- 不该写：不该写：快节奏情节、廉价激情、单一讽刺。
- Negative prompt: `No fast-paced plot, no cheap passion, no one-sided satire, no flat didacticism`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Goethe, a letter to oneself ten years from now. Long reflective sentences. Striving without rest. The moment that must be held. Lyric and aphorism side by side.`
- 中文对照：歌德风格，一封写给十年后自己的信。绵长的思辨长句，永不停息的追求，必须留住的一瞬，抒情与箴言并置。
- Negative: `fast-paced plot, cheap passion, one-sided satire, flat didacticism`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
