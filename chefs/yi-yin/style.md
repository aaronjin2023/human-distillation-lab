# Yi Yin — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yi Yin: five flavours in harmony, water as the root of all taste, the cauldron as the measure, balance over intensity, ancient bronze ritual, no single flavour dominating`
- ZH: 伊尹风格：五味调和，水为味本，鼎鼐为度，平衡胜过浓烈，青铜礼器的肃穆，没有一味独大。

## (2) 味型方向

- 主味：五味调和——甘、酸、苦、辛、咸五味皆备，无一味独大。`verbatim`
- 辅味：水之清鲜，清水为味之本，淡中见厚。`verbatim`
- 禁味：单味独大、过咸、过辣、重酱掩盖本味。
- 味型层次：多层复合而归于平和，先后多少，其齐甚微。`verbatim`
- 浓淡对比度：淡而不薄，厚而不腻；酸度与辣度均低，辣几近于无。

## (3) 刀工与火候

- 刀工：鼎鼐之烹，整料入鼎，刀工隐于鼎中；切法以整块、大块为主，少见细丝薄片。`impression`
- 火候：文火久炖，鼎中之变，精妙微纤；火力小、时间长，靠时间出味。`verbatim`
- 质感：酥烂、软糯、汤清味醇；酥烂靠久炖，汤清靠水为本、少油少酱。

## (4) 调味

- 调味料：水为本，甘、酸、苦、辛、咸五味为调；调料极简，无后世酱料体系。`verbatim`
- 调味顺序：先水后味，五味先后入鼎，多少之间，齐甚微。`verbatim`
- 禁调味：重酱、重油、辛辣刺激之味；不用浓味压过食材本味。

## (5) 摆盘与食材选择

- 摆盘：鼎鼐为器，青铜礼器上桌，肃穆简朴，留白即礼制。`impression`
- 食材选择：五谷、禽兽、鱼鳖、菜蔬，取其时令本味；不求珍稀，但求合时。
- 上菜节奏：祭祀与宴飨之序，先汤后实，先淡后厚。

## (6) 该做什么菜 / 不该做什么菜

- 该做：五味调和、鼎鼐烹制、清水为本、甘酸苦辛咸均衡、青铜礼器、整料久炖、汤清味醇。
- 不该做：`No single dominant flavour, no heavy sauce masking the ingredient, no chilli heat, no greasy richness, no rustic casual plating, no modern garnish`
- Negative prompt: `No single dominant flavour, no heavy sauce masking the ingredient, no chilli heat, no greasy richness, no rustic casual plating, no modern garnish`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Yi Yin, a modern bowl of ramen reimagined as five-flavour harmony: clear broth as the root of taste, five seasonings in perfect balance, whole ingredients simmered slowly in a bronze cauldron, ritual simplicity, no single flavour dominating`
- 中文对照：伊尹风格：一碗现代拉面，按五味调和重做：清汤为味之本，五味均衡，整料在青铜鼎中文火久炖，肃穆简朴，没有一味独大。
- Negative: `No single dominant flavour, no heavy sauce, no chilli heat, no greasy richness, no modern garnish`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
