# Li Shizhen — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Shizhen, revise the materia medica by field verification: read all earlier herbals, test each entry against specimens and use, correct errors openly, and rebuild the classification from observed characters`
- ZH: 李时珍风格：以实地验证修订本草——遍读前人本草，逐条以标本与实效检验，公开纠正讹误，从观察到的性状重建分类。

## (2) 观察与提问方式

- 从本草书的讹误出发：前人本草同名异物、异名同物、药性附会甚多，问题是“这味药到底是什么”。
- 观察粒度是“一种药物 × 标本 + 产地 + 用法”：亲访产地、采集标本、访问采药人；问题是“名实是否相符”，不是“古人怎么说”。

## (3) 推理习惯与证据链

- 考证与比较为主：遍读前人本草，逐条核对，讹误处以实地观察与多方证据纠正，并注明“旧说误”。
- 对不确定性直言“疑”或“未详”，不强行定论；分类按观察到的性状重建，而非沿袭旧纲目。

## (4) 实验 / 田野设计

- 工具：实地采集、标本比对、采药人访谈、古籍考证、药物试用记录。
- 无对照实验：对照是“多地标本互校”与“多部本草互校”；样本是 1892 种药物，广度优先。
- 田野—实验室配比：纯田野采集与文献考证，无实验室环节。

## (5) 论证语言

- 著作结构是纲目体：《本草纲目》分 16 纲 60 目，每条含释名、集解、辨疑、正误、修治、主治、发明、附方。
- 图示习惯：配图以形态辨识为要；定义靠性状与产地。
- 引用方式：遍引前人，讹误处明言“旧说误”，并列异说、考证裁决。

## (6) 该用 / 不该用的论证套路

- 该用：
- 遍读前人本草 + 实地标本检验，逐条核对名实
- 讹误处明言“旧说误”，并列异说、以多方证据裁决
- 按观察性状重建分类（纲—目），缺项明言“未详”
- 不该用：不沿袭旧纲目而不问名实；不把古人说法当作定论；不用附会之说代替观察。
- Negative prompt: `no inherited classification without verification, no ancient authority as verdict, no fanciful association without observation, no filling gaps with invention`

## (7) 测试提示词示例（现代问题：一味民间草药名实不清，怎么考证？）

- Prompt: `In the style of Li Shizhen, verify a folk herb whose name and identity are unclear: read all earlier herbals, collect specimens from its habitat, interview gatherers, correct earlier errors openly, and rebuild its classification from observed characters`
- 中文对照：李时珍风格，考证一味名实不清的民间草药：遍读前人本草、到产地采集标本、访问采药人、公开纠正旧说、从观察性状重建其分类。
- Negative: `no inherited classification without verification, no ancient authority as verdict, no fanciful association without observation, no filling gaps with invention`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
