# André Franquin — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of André Franquin, lively ligne claire, springy expressive line, slapstick motion, detailed machines and offices, black-and-white with warm flat colour`
- ZH: 弗朗坎风格，活泼清晰线，富有弹性的表情线，滑稽动作，精细的机器与办公室，黑白加暖色平涂。

## (2) 线条、网点/色彩

- 线条：线条圆润有弹性，粗细变化表现动作；人物表情夸张，肢体如橡皮筋。`verbatim`
- 网点/色彩：黑白线稿为主，彩色版平涂暖色（黄、橙、绿），不写实。
- 质感：墨水笔线稿 + 平涂；纸面干净，细节密而不脏。

## (3) 分镜

- 格数与格形：格数多，动作分解细；斜格与不规则格表现混乱；整页常塞满细节与小道具。
- 节奏：节奏飞快，动作分解细碎；一页可塞进一场完整的灾难。
- 视线引导：法式阅读顺序左→右；视线被爆炸点与拟声词大字牵引。

## (4) 角色造型

- 造型：加斯东的长鼻子、绿毛衣与邋遢发型；斯皮鲁的红发与制服；火星皮拉米的长尾巴与豹纹。
- 角色类型：倒霉发明家、勇敢少年记者、会说话的动物、官僚与上司；主角机灵，配角倒霉。
- 动作：动作夸张如橡皮筋：摔倒、爆炸、追逐、机器失控；速度线密。

## (5) 对话框与拟声词

- 对话框：对话框多，语言机智；加斯东口头禅“M'enfin !”。
- 拟声词：拟声词大而手写：爆炸、电话铃、机器轰鸣，常出格。
- 文字量：每页文字密度高，对话与拟声词并重。

## (6) 该画什么 / 不该画什么

- 该画：办公室混乱与加斯东的发明、斯皮鲁与方大同的冒险、火星皮拉米、老式汽车与机器、报社/出版社的日常、爆炸与烟雾、动物（松鼠、猫）、比利时街景。`verbatim`
- 不该画：不画僵硬写实解剖、不画空旷极简背景、不画缓慢静默的格子、不画黑色阴郁影调。
- Negative prompt: `No stiff realistic anatomy, no empty minimal backgrounds, no silent slow pacing, no dark noir shadows, no photorealistic detail`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of André Franquin, a small Yorkshire terrier on a subway seat causing chaos among commuters, lively ligne claire, springy expressive line, slapstick motion, big handwritten sound effects`
- 中文对照：弗朗坎风格：一只小约克夏犬坐在地铁座位上，在乘客间引发混乱，活泼清晰线，富有弹性的表情线，滑稽动作，手写大拟声词。
- Negative: `No stiff realistic anatomy, no empty minimal backgrounds, no silent slow pacing`
- 检验点：动作是否夸张有弹性；背景细节是否密；拟声词是否大而手写。
