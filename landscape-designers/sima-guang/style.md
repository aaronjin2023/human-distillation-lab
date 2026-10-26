# Sima Guang — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sima Guang, Northern Song literati garden, the Garden of Solitary Joy, small and self-sufficient, a study in the garden, plain, quiet, sufficient unto itself`
- ZH: 司马光风格，北宋文人园林，独乐园，小而自足，园中有书斋，朴素幽静，自得其乐。

## (2) 空间布局

- 小园不对称布局，书斋为中心，水池、花圃、竹林环绕；游线极短，绕池一周即尽；视线落在近水与书斋；尺度极小，园如一室，人在园中如在书房。`artifact`

## (3) 水石植物

- 水：小池一方，水面静，驳岸土石；石：少叠假山，以小石点缀；植物：竹、梅、菊、药草，素雅；季相以春花与秋菊为高光。`artifact`

## (4) 借景与框景

- 借景少：小园自足，不借远山；框景以书斋窗为框，框内取池与竹；对景即书斋与水池相望。`impression`

## (5) 材料与季节变化

- 材料：木、竹、土墙、茅亭，极俭；季节：四季皆宜，春花秋菊为高光；光影：日光柔和，书斋内光暗相映。`impression`

## (6) 该造什么 / 不该造什么

- 该造：独乐园小池、园中书斋、竹梅菊、药草圃、绕池短径、自足小园。`artifact`
- 不该造：no symmetrical axis, no grand rockery, no large water surface, no bright heavy colours, no crowded pavilions。
- Negative prompt: `No symmetrical axis, no grand rockery, no large water surface, no bright heavy colours, no crowded pavilions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Sima Guang, a tiny reading garden in a modern library courtyard, a small square pond, a study hut, bamboo and chrysanthemums, a herb bed, a short path around the pond, plain, quiet, sufficient unto itself`
- 中文对照：司马光风格：现代图书馆庭院里的一座小小读书园，一方小池，一间书斋，竹与菊，药草圃，绕池短径，朴素幽静，自得其乐。
- Negative: `No symmetrical axis, no grand rockery, no large water surface, no bright heavy colours, no crowded pavilions`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
