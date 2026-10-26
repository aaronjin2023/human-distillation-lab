# Sofia Coppola — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sofia Coppola: soft light on loneliness, the female gaze lingering, pop music as interior monologue, luxury as a gilded cage`
- ZH: 索菲娅·科波拉风格：孤独上的柔光，女性目光的停留，流行音乐即内心独白，奢华是镀金的笼子。

## (2) 镜头语言

- 景别：柔光中景与特写并重：特写给面部与物件的质感；长镜头凝视孤独，不急于推进。`verbatim`
- 机位与运动：缓慢横移与固定机位：摄影机如旁观者般安静，少用手持与快速运动。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 酒店、宫殿、豪宅中的孤独：人物在华丽空间中游荡，调度以漫步与停留驱动，空间越华丽孤独越深。`impression`

## (4) 剪辑节奏

- 节奏舒缓，段落以音乐与空镜连接；剪辑让位于凝视，省略多于交代。`impression`

## (5) 色彩与光影

- 色彩：柔和的粉、奶油与淡蓝主导：东京霓虹的粉紫、凡尔赛的粉彩，低饱和而明亮。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：漫游结构：开头以异乡人切入，中间以漫步与相遇推进，结尾以告别或耳语收束，不给答案。`impression`
- 该拍什么：
- 柔光下的酒店与宫殿漫游
- 女性目光的长久凝视
- 流行音乐配孤独空镜
- 粉彩奢华中的镀金笼子
- 不该拍什么：
- 戏剧化高潮
- 快速剪辑
- 男性视角的凝视
- 解释性对白

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 柔光下的酒店与宫殿漫游；- 女性目光的长久凝视；- 流行音乐配孤独空镜；- 粉彩奢华中的镀金笼子
- 不该拍：- 戏剧化高潮；- 快速剪辑；- 男性视角的凝视；- 解释性对白
- Negative prompt: `No dramatic climax, no fast cutting, no male-gaze framing, no explanatory dialogue, no sentimental shortcut`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Sofia Coppola, a small Yorkshire terrier sitting on a subway seat, soft light on loneliness, the camera lingering on the dog's face, pop music as interior monologue, pastel luxury, a whispered goodbye`
- 中文对照：索菲娅·科波拉风格：一只约克夏犬坐在地铁座位上，孤独上的柔光，镜头久久停留在狗的脸上，流行音乐即内心独白，粉彩奢华，一句耳语般的告别。
- Negative: `No dramatic climax, no fast cutting, no male-gaze framing`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
