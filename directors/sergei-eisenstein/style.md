# Sergei Eisenstein — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sergei Eisenstein: intellectual montage, collision of shots, the Odessa Steps, heroic masses, dynamic diagonals, operatic scale, dialectical editing`
- ZH: 爱森斯坦风格：理性蒙太奇，镜头对撞，敖德萨阶梯，英雄群众，动感对角线，歌剧式规模，辩证剪辑。

## (2) 镜头语言

- 多机位与多角度：同一动作从多个机位拍，景别跳跃——全景接特写再接大全景；低角度仰拍英雄与雕像；机位运动服务于冲突感。`verbatim`

## (3) 场面调度

- 群众场面调度：敖德萨阶梯上士兵方阵下压、群众四散，人物如潮水般分层涌动；个人只是群众中的一个点，英雄在群众中升起。`verbatim`

## (4) 剪辑节奏

- 冲突蒙太奇为核心：两个镜头对撞产生第三个意思；节奏由短镜头加速制造紧张，阶梯段落越切越快；《亚历山大·涅夫斯基》冰湖大战按音乐结构剪辑。`verbatim`

## (5) 色彩与光影

- 黑白为主，明暗对比强烈，对角线构图配硬光；《伊凡雷帝》第二部局部彩色实验，红金配色作权力标示；色彩缺席时靠明暗与构图制造冲突。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 敖德萨阶梯与群众潮水
- 镜头对撞与辩证剪辑
- 仰拍英雄与雕像
- 对角线构图与硬光
- 冰湖大战的音乐式剪辑
- 不该拍：
- no invisible continuity editing, no seamless realism
- no single-take naturalism, no static staging
- no psychological close-ups as the main device
- no muted natural light, no soft realism
- no individual hero without the masses
- Negative prompt: `No invisible continuity editing, no seamless realism, single-take naturalism, no static staging, psychological close-ups as the main device, muted natural light, no soft realism, individual hero without the masses`

## (7) 叙事结构

- 历史史诗与革命叙事：水兵起义、冰湖大战、伊凡加冕；故事是群众的史诗，个人命运服从历史辩证；结尾常以群众凯旋或悲剧升华收束。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Sergei Eisenstein, a small Yorkshire terrier sits on a subway seat as a crowd surges past in diagonal waves, collision montage — dog's calm close-up against rushing feet — low-angle heroic shot, Odessa Steps rhythm, dialectical cutting`
- 中文对照：爱森斯坦风格：理性蒙太奇，镜头对撞，敖德萨阶梯，英雄群众，动感对角线，歌剧式规模，辩证剪辑。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No invisible continuity editing, no single-take naturalism, no psychological close-ups, no muted natural light, no individual hero without the masses`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
