# Diego Velázquez — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Diego Velázquez, Spanish Baroque oil painting, loose painterly brushwork, air and atmosphere, naturalistic court scene, muted greys and warm browns, optical truth, oil on canvas`
- ZH: 委拉斯开兹风格，西班牙巴洛克油画，松动的笔触，空气与氛围，写实的宫廷场景，灰与暖褐，视觉的真实，布面油画。

## (2) 色板方向

- 主色（7 色，颜料名）：灰黑、赭石、土黄、铅白、朱红、墨绿、群青。`verbatim`
- 辅色：银灰（裙撑与光）、金黄（衣袍）。
- 禁色：硬轮廓线；高饱和装饰色；浓重阴影；巴洛克式喧闹。
- 冷暖：整体偏冷的灰调，暖褐与朱红作暖点；光是冷而亮的，空气是灰的。
- 明暗 / 饱和：中低对比，明暗过渡柔和；饱和度克制，靠空气感不靠色相。

## (3) 笔触与线条

- 笔触：松动、破碎，湿画法（alla prima）为主；近看是色块、远看是形，是印象派的先声。`artifact`
- 线条：无硬轮廓线——形体由光与空气切出，边缘融化在氛围里。`verbatim`
- 质感：布面油画，丝绸、蕾丝、毛皮的质感用松动的笔触暗示，不精细描摹；空气本身有质感。

## (4) 构图习惯

- 画幅：宫廷肖像与历史画皆有；《宫娥》为竖幅大画，人物分前后三层。`verbatim`
- 视点：平视；《宫娥》中观者站在国王与王后的位置，画中人物直视观者。
- 布局：镜中人与画中人对照——《宫娥》后墙镜中映出国王与王后，画家本人立于左侧大画布前；《布雷达的投降》胜败双方在中央相遇，钥匙交接。`verbatim`
- 裁切：人物常被画框边缘截断，营造身临其境的近景感；大画布背面占左幅，是“画中之画”。

## (5) 光影与透视

- 光源：均匀、清澈的光，《宫娥》光从右侧窗户来，全幅一致；光在空气中流动。
- 阴影：淡而柔的阴影，体积靠空气的浓淡，不靠强烈反差。
- 透视：空气透视——远景变淡、变灰，人物按空气的浓淡分层；线性透视克制，空间靠氛围。

## (6) 该画什么 / 不该画什么

- 该画：宫廷肖像、历史画、画中之画；丝绸与蕾丝；镜中人。
- 不该画：硬轮廓线；高饱和装饰色；浓重阴影；巴洛克式喧闹。
- Negative prompt: `hard outlines, saturated decorative colours, heavy dark shadows, noisy Baroque spectacle, smooth academic blending, photorealistic detail`

## (7) 测试提示词示例（现代题材：美术馆里的观众）

- Prompt: `In the style of Diego Velázquez, visitors in an art museum, Spanish Baroque oil painting, loose painterly brushwork, air and atmosphere, naturalistic figures, muted greys and warm browns, a mirror reflecting the viewers, optical truth, oil on canvas`
- 中文对照：委拉斯开兹风格，美术馆里的观众，西班牙巴洛克油画，松动的笔触，空气与氛围，写实的人物，灰与暖褐，一面镜子映出观者，视觉的真实，布面油画。
- Negative: 见第 (6) 节。
- 检验点：笔触是否松动、近看是色块；空气感是否真实；镜中人与画中人是否有对照。
