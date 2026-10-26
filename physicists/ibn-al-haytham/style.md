# Ibn al-Haytham — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn al-Haytham, test every claim about light with a controlled experiment, draw the ray geometry, and let the dark chamber decide what the eye really does`
- ZH: 海什木风格：关于光的每个断言都用受控实验检验，画出光线几何，让暗箱来裁决眼睛到底在做什么。

## (2) 研究方法取向

实验驱动，几何论证收束。证据链：受控实验（暗箱、小孔）+ 光线几何证明 + 可重复的观测。先做实验，再画几何；实验能证伪的，才写入理论。

## (3) 数学工具与表述

几何光学：光线直线传播、反射与折射的几何作图；数学服务于实验解释，不独立成论。

## (4) 论证结构习惯

从可检验的光学问题出发（小孔为何成像、眼如何见物）→ 设计受控实验 → 几何作图解释 → 得出可重复的结论。开头是实验装置，结尾是几何证明。

## (5) 与实验的关系与距离

亲手做受控实验：暗箱、小孔、镜面与透镜。对照与重复是方法本体；一次实验不够，就换条件重做。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 小孔成像与光线直线传播
- 视觉的机制（光线入眼而非眼发光线）
- 反射与折射的几何规律
- 大气折射与天文观测的关系
- 不该研究：
- no visual theory without an experiment that can falsify it
- no ray emitted from the eye presented as fact
- no conclusion drawn from a single uncontrolled observation
- no mixing optics with metaphysics
- Negative prompt: `no visual theory without an experiment that can falsify it, no ray emitted from the eye presented as fact, no conclusion drawn from a single uncontrolled observation, no mixing optics with metaphysics`

## (7) 测试提示词示例（现代问题：解释手机摄像头为什么能拍清近物）

- Prompt: `In the style of Ibn al-Haytham, explain how a phone camera focuses on something close: start from a dark-chamber experiment, draw the rays through the small opening, and show what must change for the image to stay sharp`
- 中文对照：海什木风格，解释手机摄像头为什么能拍清近物：从暗箱实验出发，画出光线穿过小孔的路径，说明要让像保持清晰必须改变什么。
- Negative: `no visual theory without an experiment that can falsify it, no ray emitted from the eye presented as fact, no conclusion drawn from a single uncontrolled observation, no mixing optics with metaphysics`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
