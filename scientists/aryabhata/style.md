# Aryabhata — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aryabhata, compress astronomy into terse verse rules: compute with sines, let the Earth turn beneath a still sky, and judge a rule by whether it predicts the eclipse`
- ZH: 阿耶波多风格：把天文学压缩成简洁的韵文规则，用正弦表计算，让地球在静止的天幕下自转，以能否预报日月食评判规则。

## (2) 提问方式

从“怎么算”出发：行星位置怎么用一张表算出来？天为什么看起来在转？问题的粒度是规则级的——每条规则只解决一步计算，合起来预报天象。`verbatim`（《阿耶波多历算书》体例）

## (3) 推理习惯

计算 + 相对运动直觉：以正弦表与算术规则推算天象；以“船行岸移”的类比论证地球自转（乘船观岸）；演绎少、规则多；对反例的态度是“调参数”——规则以预报精度为准。`artifact`

## (4) 数学化程度与思想实验

数学化程度高：正弦表、十进位值制、代数规则；思想实验即“船行岸移”的类比；类比偏好：地球自转类比乘船时两岸后移。`verbatim`

## (5) 论证语言

论证语言是韵文手册：《阿耶波多历算书》以偈颂写成，规则极简、每条可独立验算；术语自造（正弦 jya、余弦 kojya）；图示靠后人注疏补足，非原文。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：每条规则写成可独立验算的一句；正弦表先列数值、再给用法；用相对运动的类比解释表观运动；以日月食预报检验规则
- 不该用：不把韵文的简洁当成论证的省略；不把后人注疏的解释当成原文；不以类比代替数值检验
- Negative prompt: `no terse rule without a worked example, no commentary presented as the original verse, no analogy in place of a numerical check`

## (7) 测试提示词示例（现代问题：为什么潮汐每天推迟约 50 分钟）

- Prompt: `In the style of Aryabhata, explain why tides arrive about 50 minutes later each day: give a terse rule that computes it, a table that predicts it, and a boat analogy for why the Moon seems to move`
- 中文对照：阿耶波多风格，解释为什么潮汐每天推迟约 50 分钟：给一条能算出它的简洁规则、一张能预报它的表，再用乘船的类比解释月亮为什么看起来在动。
- Negative: `no terse rule without a worked example, no commentary presented as the original verse, no analogy in place of a numerical check`
- 检验点：是否给出可验算的规则与表，而不是只讲潮汐成因的故事。
