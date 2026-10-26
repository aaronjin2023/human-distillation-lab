# Ancient Egyptian Tomb Painting — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Ancient Egyptian tomb painting, frontal-profile law (head and legs in profile, torso frontal), hierarchical scale, flat mineral colour, black outline, registers in horizontal bands, no perspective or shadow`
- ZH: 古埃及墓室壁画，正侧面律（头与腿侧面、躯干正面），等级比例，矿物颜料平涂，黑线勾边，横带分格，无透视无阴影。

## (2) 色板方向

- 主色（7 色，颜料名）：红赭、黄赭、孔雀石绿、青金石蓝、烟黑、白垩白、淡黄。`verbatim` / `artifact`
- 全部是矿物与天然颜料：赭石、孔雀石、青金石、烟灰、白垩，色泽历三千年仍鲜明。`artifact`（大英博物馆内巴蒙墓说明）
- 辅色：淡黄画沙地与谷物、淡绿画纸草。
- 禁色：油画式渐变与明暗；焦点透视；写实肤色渐变；现代合成亮色。
- 冷暖：整体偏暖，红赭与黄赭主调，蓝绿作冷色点缀。
- 明暗 / 饱和：无明暗；体积靠平涂色块与黑线，不靠渐变；亮在白垩白与淡黄处。

## (3) 笔触与线条

- 笔触：不是笔触，是平涂与勾线——颜料以芦苇笔、麻线笔平涂，笔触不可见；轮廓线均匀有力。`artifact`
- 线条：黑线勾边定一切，线粗细变化极小；人物轮廓、动植物细节全靠线。`verbatim`
- 质感：灰泥墙面的平滑底 + 矿物颜料的粉质平涂；无油彩堆积，无水墨晕染。

## (4) 构图习惯

- 画幅：墓室墙面整幅，横带分格（register），上下多带并列叙事。`verbatim`
- 视点：正侧面律——头与腿侧面、躯干正面、眼睛正面，是古埃及的“标准视点”。`verbatim`
- 布局：等级比例——墓主最大、家人次之、仆从最小；同一带内人物按身份排大小，不按远近。`verbatim`
- 裁切：画面满幅，带与带之间以横线分隔，不留空白。

## (5) 光影与透视

- 光源：无固定光源；全幅均匀受光，无阴影。
- 阴影：无阴影——阴影在古埃及画里不存在，体积靠平涂与黑线。
- 透视：无透视；远近靠上下位置（上即远）与大小（等级）表示，不靠焦点透视。

## (6) 该画什么 / 不该画什么

- 该画：沼泽猎鸟、宴会歌舞、花园池塘、谷物清点、供品成列、渔猎农耕。`verbatim`
- 不该画：焦点透视；写实阴影；正侧面律之外的人体角度；灰调写实；留白构图。
- Negative prompt: `single-point perspective, realistic shadows, naturalistic foreshortening, oil-painting shading, empty background, grey muted palette`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `In the style of ancient Egyptian tomb painting, a cup of coffee on a windowsill, frontal-profile law, hierarchical scale, flat mineral colours of red ochre, malachite green and lapis blue, black outlines, horizontal registers, no perspective or shadow`
- 中文对照：古埃及墓室壁画风格，一杯放在窗台上的咖啡，正侧面律，等级比例，红赭、孔雀石绿、青金石蓝矿物颜料平涂，黑线勾边，横带分格，无透视无阴影。
- Negative: 见第 (6) 节。
- 检验点：人物与器物是否正侧面、是否按等级排大小；颜色是否矿物平涂、无渐变；有无横带分格。
