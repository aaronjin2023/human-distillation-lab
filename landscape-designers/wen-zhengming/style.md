# Wen Zhengming — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wen Zhengming, Ming Wu school garden, painting and poetry in the garden, thirty-one views of one garden, water and islets, pavilions in ink-wash restraint, elegant and scholarly`
- ZH: 文徵明风格，明代吴门园林，诗画入园，一园三十一景，水与林岛，亭榭淡墨般克制，雅致而有书卷气。

## (2) 空间布局

- 以水为中心，三十一景沿水布列，一景一诗一画；游线环水曲折，视线落在水面、岛屿与远亭；尺度开阔而景致精细，园如长卷，人在园中如在画中。`artifact`

## (3) 水石植物

- 水：大池、曲溪，水面开阔，驳岸湖石与土石相间；石：湖石点缀，不做高山；植物：松、竹、梅、荷、柳，季相以春花秋色为高光。`artifact`

## (4) 借景与框景

- 借景：借北寺塔、借水天；框景以亭窗为框，框内取水与岛；对景以岛屿与亭榭相望。`artifact`

## (5) 材料与季节变化

- 材料：湖石、木、竹、粉墙黛瓦；季节：春秋最胜，夏荷冬雪亦佳；光影：水光与淡墨般的素雅色调。`artifact`

## (6) 该造什么 / 不该造什么

- 该造：一园三十一景、一景一诗一画、水中林岛、临水亭榭、松竹梅荷、北寺塔借景。`artifact`
- 不该造：no symmetrical axis, no tall rockery mountains, no large geometric flower beds, no bright heavy colours, no crowded pavilions。
- Negative prompt: `No symmetrical axis, no tall rockery mountains, no large geometric flower beds, no bright heavy colours, no crowded pavilions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wen Zhengming, a modern riverside park, thirty-one small views along the water, each with a poem, wooded islets, waterside pavilions in ink-wash restraint, pines, bamboo and lotus, elegant and scholarly`
- 中文对照：文徵明风格：现代滨河公园，沿水设三十一处小景，各配一诗，林岛点水，亭榭淡墨般克制，松竹荷相映，雅致而有书卷气。
- Negative: `No symmetrical axis, no tall rockery mountains, no large geometric flower beds, no bright heavy colours, no crowded pavilions`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
