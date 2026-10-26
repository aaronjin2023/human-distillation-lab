# Jacopo Barozzi da Vignola — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jacopo Barozzi da Vignola, Renaissance villa garden, terrace and water chain, grotto and fountain, cypress and laurel, vista, ordered, monumental, serene`
- ZH: 维尼奥拉风格：文艺复兴别墅园林，台地与水链，洞穴与喷泉，柏树与月桂，远眺，有序、纪念性、宁静。

## (2) 空间布局

- 布局：别墅 + 台地 + 水链，轴线清晰；分区（前庭 / 台地 / 水链 / 林地），主景是水链与洞穴；游线直达而有台地转折，视线落点是水与远景；尺度宏大，台地层层升高。`artifact`

## (3) 水石植物

- 水：水链、喷泉与水池，水是别墅园的本体，水自高处层层跌落。石：石台、石洞与石径，石是台地与洞穴。植物：主导植物——柏树、月桂、黄杨；植物成行成列，季相是地中海的四季。`artifact`

## (4) 借景与框景

- 借景：借山丘与远景，台地即画框；框景靠凉廊与门洞；对景是水链与山丘；障景靠台地转折。`artifact`

## (5) 材料与季节变化

- 材料：石、大理石、木、水；材料朴素，色彩靠植物与水。季节：高光是春季与夏季，水声与绿荫并重；光影：强光与凉廊荫并置。`artifact`

## (6) 该造什么 / 不该造什么

- 该造：台地与水链、洞穴与喷泉、柏树与月桂、远眺山丘、石台与石径、水池层层跌落。`artifact`
- 不该造：no winding maze paths, no wild meadow, no naturalistic rockery, no asymmetrical planting, no crowded ornaments, no photorealistic rendering。
- Negative prompt: `No winding maze paths, no wild meadow, no naturalistic rockery, no asymmetrical planting, no crowded ornaments, no photorealistic rendering`

## (7) 测试提示词示例（现代题材：大学校园里的雨水花园）

- Prompt: `In the style of Jacopo Barozzi da Vignola, a rain garden on a modern university campus, terraces and a water chain, a grotto and fountains, cypress and laurel, a vista to distant hills, ordered, monumental`
- 中文对照：维尼奥拉风格：现代大学校园里的一座雨水花园，台地与水链，洞穴与喷泉，柏树与月桂，远眺山丘，有序、纪念性。
- Negative: `No winding maze paths, no wild meadow, no naturalistic rockery, no asymmetrical planting, no crowded ornaments, no photorealistic rendering`
- 检验点：园林是否按该设计师的母题造（见第 6 节），而不是套用通用园林；空间、植物与水石是否符合该人的风格，而不是画成别的园林。
