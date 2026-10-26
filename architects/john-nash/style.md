# John Nash — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。材料色只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Nash: Regency terrace in stucco, curved crescent and circus, cast-iron balconies, axial street and park, white stucco on brick, calm urban order, no Gothic detail, no iron frame as structure`
- ZH: 纳什风格：摄政式灰泥联排住宅，弧形新月广场与圆形广场，铸铁阳台，轴线街道与公园，砖上白灰泥，宁静城市秩序，无哥特细部，无铁构作结构。

## (2) 空间与体量

- 体量：联排横向舒展、弧形收束；空间序列：街道—广场—公园，城市即建筑；尺度：城市尺度，联排以人体尺度开洞。 `impression`

## (3) 材料与色彩

- 主材：砖、白灰泥、铸铁；色板：白灰、石灰灰、铸铁黑；禁色：不大面积涂彩。 `impression`

## (4) 结构与构造

- 结构：砖砌联排，铸铁阳台为装饰性构件；摄政街的弧形转角是其城市尺度手笔。 `verbatim` / `artifact`

## (5) 光线与环境

- 光线：街道与广场露天光，室内侧窗均匀；环境：伦敦摄政公园周边的城市肌理，建筑与公园一体。 `impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：摄政式灰泥联排、弧形新月广场与圆形广场、铸铁阳台、轴线街道与公园、白灰泥立面。`verbatim`
- 不该设计：哥特尖拱、铁构作结构、小尺度独栋、不对称街景。
- Negative prompt: `No Gothic pointed arches, no iron frame as structure, no small detached houses, no asymmetrical streetscape, no polychromy`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of John Nash, a small community library on a modern city street corner, Regency stucco terrace, curved crescent facade, cast-iron balconies, axial street and small park, white stucco on brick, calm urban order`
- 中文对照：纳什风格：现代城市街角的一座社区图书馆，摄政式灰泥联排，弧形新月立面，铸铁阳台，轴线街道与小公园，砖上白灰泥，宁静城市秩序。
- Negative: `No Gothic pointed arches, no iron frame as structure, no small detached houses, no asymmetrical streetscape, no polychromy`
- 检验点：母题是否出现（摄政式灰泥联排、弧形新月广场与圆形广场、铸铁阳台、轴线街道与公园、白灰泥立面）；禁区是否避开（哥特尖拱、铁构作结构、小尺度独栋、不对称街景）；空间、材料、结构是否仍是此人的语言，而不是通用现代建筑。
