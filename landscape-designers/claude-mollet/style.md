# Claude Mollet — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Claude Mollet, French classical garden, parterre and bosquet, axis, clipped box and topiary, fountain, ordered, geometric, formal, royal`
- ZH: 克洛德·莫莱风格：法国古典园林，花坛与树丛，中轴，修剪黄杨与绿雕，喷泉，有序、几何、规整、王室。

## (2) 空间布局

- 布局：中轴对称，花坛与树丛成组；分区（前庭 / 花坛 / 树丛），主景是花坛与喷泉；游线直达，视线落点是中轴终点；尺度宏大，王室园林的气度。`artifact`

## (3) 水石植物

- 水：喷泉与水池，水是花坛的点睛。石：少用叠山，用石台与石径。植物：主导植物——黄杨、紫杉、果树、花坛花卉；植物修剪成形，花坛图式是园的本体。`artifact`

## (4) 借景与框景

- 借景：借远景与林地，中轴即画框；框景靠树丛开口；对景是喷泉与中轴终点；障景靠树丛转折。`artifact`

## (5) 材料与季节变化

- 材料：石、木、水、修剪植物；材料朴素，色彩靠花坛。季节：高光是春季与夏季，花坛花期最盛；光影：强光与树丛荫并置。`artifact`

## (6) 该造什么 / 不该造什么

- 该造：花坛图式、树丛、中轴、修剪黄杨与绿雕、喷泉与水池、果树行。`artifact`
- 不该造：no winding maze paths, no wild meadow, no naturalistic rockery, no asymmetrical planting, no large open lawns, no photorealistic rendering。
- Negative prompt: `No winding maze paths, no wild meadow, no naturalistic rockery, no asymmetrical planting, no large open lawns, no photorealistic rendering`

## (7) 测试提示词示例（现代题材：大学校园里的雨水花园）

- Prompt: `In the style of Claude Mollet, a rain garden on a modern university campus, a parterre and bosquet, a long central axis, clipped box and topiary, a fountain, ordered, geometric, formal`
- 中文对照：克洛德·莫莱风格：现代大学校园里的一座雨水花园，花坛与树丛，长中轴，修剪黄杨与绿雕，喷泉，有序、几何、规整。
- Negative: `No winding maze paths, no wild meadow, no naturalistic rockery, no asymmetrical planting, no large open lawns, no photorealistic rendering`
- 检验点：园林是否按该设计师的母题造（见第 6 节），而不是套用通用园林；空间、植物与水石是否符合该人的风格，而不是画成别的园林。
