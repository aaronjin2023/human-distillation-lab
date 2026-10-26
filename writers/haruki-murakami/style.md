# Haruki Murakami — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Haruki Murakami: plain first-person narration, everyday detail, jazz, cats, wells and parallel worlds, surreal events told in a flat calm voice, questions left unanswered`
- ZH: 村上春树风格：平实的第一人称叙述，日常细节，爵士乐、猫、井与平行世界，超现实事件用平静的语气讲述，问题不作解答。

## (2) 句式与节奏

- 平实的中长句为主，口语化；短句作停顿；从句不多，节奏如散步。
- 节奏：中长句平实推进，短句作停顿；段落中等长度，章节切分平缓，节奏如散步。

## (3) 词汇与意象

- 常用词域：猫、井、耳朵、爵士、啤酒、厨房、火车、黑暗走廊；外来语与品牌名自然出现；形容词克制。
- 意象：井、猫、会说话的动物、黑暗走廊、两个月亮、耳朵；日常物突然变成入口。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第一人称「僕」为主；长篇常双线并行、第一与第三人称交替。
- 结构：双线并行、谜面不解；开头多为日常场景切入，结尾开放，谜不揭开。
- 对话：对话简短、留白多，常岔开话题，信息在岔开处泄露；人物常答非所问，谜面留在对话里。

## (5) 语气与距离

- 疏离、温柔、孤独；与人物同情，与读者如朋友闲谈。

## (6) 该写什么 / 不该写什么

- 该写：猫（失踪、引路、通灵）、井（深入、下坠、记忆的入口）、耳朵与黑暗走廊、两个月亮（身体与异世界的接口）、孤独的青年男性叙述者与失踪的女性（寻找即是小说的引擎）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No grand explanation, no moralising, no heroic climax, no ornate lyricism, no neat resolution`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Haruki Murakami, a small Yorkshire terrier sits on a subway seat. The narrator watches it. A cat walks past in the tunnel. Nobody explains anything. Jazz plays somewhere far away.`
- 中文对照：村上春树风格，一只小约克夏犬坐在地铁座位上。叙述者看着它。一只猫从隧道里走过。没有人解释什么。远处传来爵士乐。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
