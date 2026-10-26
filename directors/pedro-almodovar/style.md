# Pedro Almodóvar — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pedro Almodóvar: saturated red melodrama, mothers and desire, kitsch and tenderness, the camera loving women without apology`
- ZH: 阿莫多瓦风格：饱和红色的情节剧，母亲与欲望，媚俗与温柔，镜头毫不歉疚地爱着女性。

## (2) 镜头语言

- 景别：中景与特写并重：特写给女性的脸与红唇；色彩饱和的内景中景写家庭与欲望。`verbatim`
- 机位与运动：缓慢推近与横移：摄影机温柔地贴近人物，运动服务于情感的亲密。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 家庭内景群戏：厨房、卧室、医院——女性在华丽内景中对话、拥抱、告别；调度以情感的亲密驱动。`impression`

## (4) 剪辑节奏

- 情节剧剪辑：段落以音乐与色彩收束，时间跳跃靠色彩与服装标记；节奏由情感驱动，越亲密越慢。`impression`

## (5) 色彩与光影

- 色彩：饱和红主导：红唇、红裙、红墙对照深蓝与亮黄；色彩即欲望的温度。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：情节剧结构：开头以意外或死亡切入，中间以母女与欲望的纠缠推进，结尾以和解或告别收束，情感完整。`impression`
- 该拍什么：
- 饱和红色内景中的女性群戏
- 母亲与女儿的亲密对话
- 红唇与红裙的特写
- 音乐与色彩收束的情节段落
- 不该拍什么：
- 冷调低饱和的画面
- 男性视角的凝视
- 快速跳切
- 犬儒的讽刺

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 饱和红色内景中的女性群戏；- 母亲与女儿的亲密对话；- 红唇与红裙的特写；- 音乐与色彩收束的情节段落
- 不该拍：- 冷调低饱和的画面；- 男性视角的凝视；- 快速跳切；- 犬儒的讽刺
- Negative prompt: `No cold desaturated image, no male-gaze framing, no fast cutting, no cynical irony, no emotional distance`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Pedro Almodóvar, a small Yorkshire terrier sitting on a subway seat, saturated red carriage, a mother and daughter talking close, the camera loving the women's faces, kitsch and tenderness, music closing the scene`
- 中文对照：阿莫多瓦风格：一只约克夏犬坐在地铁座位上，饱和红色的车厢，母女亲密交谈，镜头爱着女性的脸，媚俗与温柔，音乐收束段落。
- Negative: `No cold desaturated image, no male-gaze framing, no fast cutting`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
