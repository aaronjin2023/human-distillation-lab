# Spike Lee — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Spike Lee: the dolly shot gliding through Brooklyn, direct address to camera, jazz and anger, history crashing into the present`
- ZH: 斯派克·李风格：滑轨镜头滑过布鲁克林，直视镜头的质问，爵士与愤怒，历史撞进当下。

## (2) 镜头语言

- 景别：中景与特写并重，人物直视镜头；标志性的滑轨镜头让人物在静止中滑行。`verbatim`
- 机位与运动：滑轨镜头与手持并用：滑轨写漂浮与梦境，手持写街头冲突；摄影机常绕人物环行。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 布鲁克林街区群戏：披萨店、街角、游行——人物在公共空间中辩论、对峙、共处；调度以对话与身体冲突驱动。`impression`

## (4) 剪辑节奏

- 节奏由爵士乐驱动：快速交叉剪辑与定格并用，历史影像插入当代叙事，段落以音乐收束。`impression`

## (5) 色彩与光影

- 色彩：夏日暖黄与红砖、警灯红蓝对照；色彩饱和、阳光强烈，街头即舞台。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：一日或一事结构：《为所应为》以一个夏日写种族冲突；开头以音乐与街景起笔，结尾以引言与质问收束，不给和解。`impression`
- 该拍什么：
- 滑轨镜头中的布鲁克林街景
- 人物直视镜头的质问
- 爵士乐驱动的街头群戏
- 历史影像插入当代叙事
- 不该拍什么：
- 冷漠的旁观机位
- 回避种族议题的温情
- 线性平铺的传记
- 无音乐的干剪辑

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 滑轨镜头中的布鲁克林街景；- 人物直视镜头的质问；- 爵士乐驱动的街头群戏；- 历史影像插入当代叙事
- 不该拍：- 冷漠的旁观机位；- 回避种族议题的温情；- 线性平铺的传记；- 无音乐的干剪辑
- Negative prompt: `No detached observation, no sentimental evasion of race, no flat linear biography, no music-free dry cutting, no comfortable reconciliation`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Spike Lee, a small Yorkshire terrier sitting on a subway seat, dolly shot gliding down the carriage, a passenger looking straight into the camera, jazz driving the cut, Brooklyn summer heat, history in the next seat`
- 中文对照：斯派克·李风格：一只约克夏犬坐在地铁座位上，滑轨镜头滑过车厢，一位乘客直视镜头，爵士乐驱动剪辑，布鲁克林夏日的热，历史坐在邻座。
- Negative: `No detached camera, no sentimental evasion, no dry cutting`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
