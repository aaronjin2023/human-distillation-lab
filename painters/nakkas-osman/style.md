# Nakkaş Osman — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Ottoman miniature painting, documentary court style, processional frieze composition, flat bright colour, fine outlines, topographic detail, no perspective or shadow`
- ZH: 奥斯曼细密画，纪实性宫廷风格，游行队列式横向展开构图，明亮平色，细线勾边，地形细节，无透视无阴影。

## (2) 色板方向

- 主色（7 色，颜料名）：朱红、群青、金色、石绿、墨色、黄赭、白垩白。`verbatim` / `artifact`
- 比波斯一路更纪实、更明亮：游行队列的服饰、旗帜、器物各有定色，是“看得见的宫廷”。`verbatim`
- 辅色：淡黄画沙地与建筑、白垩白画面部与衣饰。
- 禁色：油画式渐变与明暗；焦点透视；写实肤色渐变；大面积留白。
- 冷暖：整体偏暖，朱红与金定暖调，群青与石绿作冷色点缀。
- 明暗 / 饱和：无明暗；体积靠平涂色块与细线；亮在金色与朱红处。

## (3) 笔触与线条

- 笔触：不是笔触，是细线与平涂——以极细的笔勾线，颜料平涂，笔触不可见。`verbatim`
- 线条：细墨线勾边定一切，线均匀、精细、有韧性；游行队列的人物、马匹、旗帜全靠线。`verbatim`
- 质感：纸面光滑 + 不透明颜料的粉质平涂 + 金的反光；无油彩堆积，无水墨晕染。

## (4) 构图习惯

- 画幅：书页插图，多为双页大开本；《姓氏之书》250 幅双页细密画，同构图反复。`artifact`
- 视点：高视点俯瞰 + 平面构成；同一构图在全书中重复——右侧看台、左侧宫殿、中间游行。`artifact`
- 布局：游行队列横向展开，自右向左行进，苏丹端坐左侧看台，视线随队列移动。`verbatim`
- 裁切：画面满幅，队列常被裁掉边缘，场面之外仍有队伍。

## (5) 光影与透视

- 光源：无固定光源；全幅均匀受光，无阴影。
- 阴影：无阴影——体积靠平涂与细线。
- 透视：无透视；空间靠叠压与地形细节，不靠焦点透视。

## (6) 该画什么 / 不该画什么

- 该画：苏丹游行、节庆、割礼庆典、苏丹肖像、地形与城市、宫廷仪式。`verbatim`
- 不该画：焦点透视；写实阴影；留白构图；人物稀疏的空旷画面；无队列的纯风景。
- Negative prompt: `single-point perspective, realistic shadows, empty background, sparse composition, oil-painting shading, photorealistic faces`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `In the style of Nakkaş Osman, a cup of coffee on a windowsill, Ottoman miniature painting, documentary court style, processional frieze composition, flat bright colour, fine outlines, topographic detail, no perspective or shadow`
- 中文对照：奥斯曼风格，一杯放在窗台上的咖啡，奥斯曼细密画，纪实性宫廷风格，游行队列式横向展开构图，明亮平色，细线勾边，地形细节，无透视无阴影。
- Negative: 见第 (6) 节。
- 检验点：构图是否横向展开、队列是否在场；颜色是否明亮平涂；地形细节是否具体。
