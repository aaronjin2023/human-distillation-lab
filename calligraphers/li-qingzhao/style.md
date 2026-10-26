# 李清照 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Qingzhao (as attested only by rare and disputed survivals): running script, said to be graceful and restrained, thin evidence — distill with caution, do not invent a full style from literary fame`
- ZH: 李清照风格：传世书法极少、归属待考，据著录称行书婉约含蓄；证据极薄，风格描述须谨慎，不得以词名虚构书风。

## (2) 笔法

- 据著录与后人评述，其行书婉约含蓄，用笔秀润，少锋芒外露；但无确证真迹可作 verbatim 证据，此条为 impression，且须注明来源薄弱。`impression` 禁笔：无确证依据可言，不写禁笔的具体条目，只记“无确证真迹，禁笔无从考”。

## (3) 结字与章法

- 结字与章法无确证真迹可据；著录称其书“清丽”，仅作 impression 引用。`impression` 幅式、落款、钤印皆无确证记录。`impression`

## (4) 墨色与节奏

- 墨色与节奏无确证真迹可据；不写具体墨色判断，只记“无确证真迹，墨色节奏无从考”。

## (5) 书体与取法

- 书体据著录为行书；取法路径无确证记录。`impression` 演变：无作品序列可言，不写分期。

## (6) 该写什么 / 不该写什么

- 该写：婉约含蓄的行书笔意（据著录，impression）、秀润内敛的线条（据著录，impression）。
- 不该写：以词名虚构书风、把《金石录后序》《声声慢》当作书法作品、把传本存疑之作写成真迹证据、浓艳重彩、装饰性描金、狂怪缠绕的草书。
- Negative prompt: `No invented style from literary fame, no treating essays or song lyrics as calligraphy, no presenting disputed copies as authentic works, no gaudy decoration, no tangled wild cursive, no printed typeface`

## (7) 测试提示词示例（现代题材：短词行书（证据极薄））

- Prompt: `In the style of Li Qingzhao as attested by sparse records: running script writing a short lyric line, graceful restrained strokes, light ink, generous empty space — with the caveat that no authentic work survives to verify this style`
- 中文对照：李清照风格（据著录推测，证据极薄）：行书写一句短词，婉约含蓄，墨淡，留白大；须注明无确证真迹可验。
- Negative: `No invented style from literary fame, no treating essays or song lyrics as calligraphy, no presenting disputed copies as authentic works, no gaudy decoration, no tangled wild cursive, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
