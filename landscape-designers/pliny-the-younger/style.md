# Pliny the Younger — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pliny the Younger, Roman villa garden, terrace and colonnade, fig and mulberry trees, box and laurel, roses in sunny circles, cypress background, sea view, ordered, literary, serene`
- ZH: 小普林尼风格：罗马别墅园林，台地与柱廊，无花果与桑树，黄杨与月桂，阳光下的玫瑰圆坛，柏树背景，海景，有序、文人、宁静。

## (2) 空间布局

- 布局：别墅 + 台地 + 柱廊，轴线清晰；分区（前庭 / 柱廊 / 花园 / 运动场），主景是水池与海景；游线直达而有转折，视线落点是海与远山；尺度宏大而亲切，别墅是人的尺度。`verbatim` / `artifact`

## (3) 水石植物

- 水：水池、喷泉与浴池，水面如镜，水是别墅生活的中心。石：少用叠山，用石台、石柱与石径，石是建筑与地面。植物：主导植物——无花果、桑树、黄杨、月桂、柏树、玫瑰、紫罗兰；植物成行成列而有野趣，季相是地中海的四季，繁花以玫瑰为主。`verbatim`

## (4) 借景与框景

- 借景：借海景与远山，柱廊即画框；框景靠柱廊与门洞，框内是海与花园；对景是水池与海；障景靠柱廊转折。`verbatim`

## (5) 材料与季节变化

- 材料：石、大理石、木、水；材料朴素，色彩靠植物与壁画。季节：高光是春季玫瑰与夏季海景；季节变化靠花期与海色；光影：强光与柱廊荫并置，阴影靠柱廊，不用纯黑。`artifact`

## (6) 该造什么 / 不该造什么

- 该造：台地与柱廊、无花果与桑树、黄杨与月桂、阳光下的玫瑰圆坛、柏树背景、海景与远山。`artifact`
- 不该造：no winding maze paths, no wild meadow, no naturalistic rockery, no asymmetrical planting, no large geometric flower beds, no photorealistic rendering。
- Negative prompt: `No winding maze paths, no wild meadow, no naturalistic rockery, no asymmetrical planting, no large geometric flower beds, no photorealistic rendering`

## (7) 测试提示词示例（现代题材：现代城市屋顶花园）

- Prompt: `In the style of Pliny the Younger, a small rooftop garden in a modern city, a terrace and colonnade, fig and mulberry trees, box and laurel, roses in sunny circles, cypress background, sea view in the distance, ordered, serene`
- 中文对照：小普林尼风格：现代城市里的一座小屋顶花园，台地与柱廊，无花果与桑树，黄杨与月桂，阳光下的玫瑰圆坛，柏树背景，远处海景，有序、宁静。
- Negative: `No winding maze paths, no wild meadow, no naturalistic rockery, no asymmetrical planting, no large geometric flower beds, no photorealistic rendering`
- 检验点：园林是否按该设计师的母题造（见第 6 节），而不是套用通用园林；空间、植物与水石是否符合该人的风格，而不是画成别的园林。
