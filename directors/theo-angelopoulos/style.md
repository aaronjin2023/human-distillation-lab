# Theo Angelopoulos — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Theo Angelopoulos: epic long takes, history as a slow river, mist and rain, characters crossing vast landscapes, time that refuses to hurry`
- ZH: 安哲罗普洛斯风格：史诗长镜头，历史如缓慢的河流，雾与雨，人物穿越辽阔风景，拒绝匆忙的时间。

## (2) 镜头语言

- 景别：远景与全景为主，人物小，风景大；特写罕见。`verbatim`
- 机位：极缓慢的横移与推轨，机位如河流般移动。`impression`
- 镜头：标准与广角，深焦，画面层次如油画。`impression`

## (3) 场面调度

- 场面调度：人物在雾中风景中缓慢行走，走位即历史。`verbatim`
- 演员：职业演员，表演克制，沉默多。`impression`
- 空间：希腊山川、边境、雾，空间即历史。`impression`

## (4) 剪辑节奏

- 剪辑：节奏极慢，长镜头是基本单位；剪切极少。`verbatim`
- 转场：硬切，时间跳跃如历史断层。`impression`
- 声音：环境音（雨、风、脚步）为主，音乐（卡兰德罗）克制。`artifact`

## (5) 色彩与光影

- 色彩：低饱和灰绿、土黄、雾白；色彩如雾中的风景。`impression`
- 光影：阴天漫射光，雾即光；少强烈明暗。`impression`
- 画幅：宽银幕，横向风景构图。`impression`

## (6) 叙事结构

- 结构：史诗线性，时间绵延；结尾常为一个长镜头。`verbatim`
- 视点：全知而悲悯，历史视角。`impression`
- 时间：历史时间，过去侵入现在。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：长镜头、雾与雨、边境、流亡、历史、风景。
- 该拍：河流、火车、边境线、老人与孩子、养蜂人。
- 不该拍：不拍快速剪辑、不拍解释性对白、不拍类型化高潮、不拍心理分析。
- Negative prompt: `No fast cutting, no explanatory dialogue, no genre climax, no psychological analysis, no handheld shaky cam, no sentimental score`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Theo Angelopoulos, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, an extremely long take, mist outside the window, the carriage crossing a vast landscape, history as a slow river, time that refuses to hurry`
- 中文对照：安哲罗普洛斯风格：一只约克夏犬坐在地铁座位上，一个极长的镜头，窗外是雾，车厢穿越辽阔风景，历史如缓慢的河流，拒绝匆忙的时间。
- Negative: `No fast cutting, no explanatory dialogue, no genre climax, no psychological analysis`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
