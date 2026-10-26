# Rembrandt van Rijn — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rembrandt van Rijn, Dutch Golden Age oil painting, chiaroscuro, golden light in darkness, thick impasto highlights, loose late brushwork, deep human feeling, group portrait as drama`
- ZH: 伦勃朗风格，荷兰黄金时代油画，明暗法，黑暗中的金光，厚涂高光，晚期自由的笔触，深沉的人情，群像即戏剧。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、土黄、暗褐、铅白、朱红、群青、墨绿。`verbatim`
- 辅色：金黄（光与织物）、灰黑（暗部）。
- 禁色：明朗的均匀光；高饱和的装饰色；纤细苍白的人体；巴洛克式的喧闹。
- 冷暖：暗部冷黑、亮部暖金，光是暖的、暗是冷的，冷暖对撞而深沉。
- 明暗 / 饱和：高对比，亮部极亮、暗部极暗，中间调由罩染构成；饱和度在亮部高、在暗部几近于无。

## (3) 笔触与线条

- 笔触：早期笔触精细，中期肯定，晚期自由、厚重——厚涂（impasto）高光如雕塑，刮刀与笔并用。`artifact`
- 线条：无硬轮廓线——形体由光切出，亮与暗的交界即轮廓。
- 质感：布面油画，皮肤、织物、金属的质感在金光下极致真实，暗部则沉入黑暗；晚期笔触的肌理本身即是内容。

## (4) 构图习惯

- 画幅：群像与大幅叙事皆有；《夜巡》为横幅巨幅（363×437 厘米），人物横向展开如行军。`verbatim`
- 视点：平视略仰；《夜巡》中队长与副队长居中，民兵分列左右，光束照亮中央。
- 布局：对角线光束构图——光从左侧斜射，照亮焦点、其余沉入黑暗；《浪子回头》为金字塔构图，父亲居中、浪子跪于膝前。`verbatim`
- 裁切：《夜巡》后世被裁切过（现存面貌非原作全貌），见 conflicts.md；人物常被画框边缘截断，营造近景感。

## (5) 光影与透视

- 光源：单一、温暖的光源，光从画面外斜射，是画面的主角；光照亮内心，不止照亮形体。`verbatim`
- 阴影：暗部极暗、近乎纯黑，体积靠亮部的厚涂，不靠中间调。
- 透视：浅空间——人物贴近画面，背景沉入黑暗，空间压缩而非深远；透视克制，戏剧靠光影与情感。

## (6) 该画什么 / 不该画什么

- 该画：群像、圣经叙事、自画像；黑暗中的金光；厚涂的皮肤与织物。
- 不该画：明朗的均匀光；高饱和装饰色；纤细苍白的人体；巴洛克式喧闹。
- Negative prompt: `bright even daylight, saturated decorative colours, slender pale figures, noisy Baroque spectacle, smooth academic blending, flat vector illustration`

## (7) 测试提示词示例（现代题材：深夜的书房与台灯）

- Prompt: `In the style of Rembrandt van Rijn, a study room with a desk lamp late at night, Dutch Golden Age oil painting, chiaroscuro, golden light in darkness, thick impasto highlights, loose brushwork, deep quiet feeling, a reader in warm light, oil on canvas`
- 中文对照：伦勃朗风格，深夜书房里的一盏台灯，荷兰黄金时代油画，明暗法，黑暗中的金光，厚涂高光，自由的笔触，深沉安静的情感，暖光中的读者，布面油画。
- Negative: 见第 (6) 节。
- 检验点：光是否温暖而集中；暗部是否沉入黑暗；读者面部是否有内心的深度而不是表面光亮。
