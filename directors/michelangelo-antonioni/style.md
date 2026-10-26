# Michelangelo Antonioni — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michelangelo Antonioni: modernist alienation, architecture over people, long empty takes, characters lost in space, time that will not resolve`
- ZH: 安东尼奥尼风格：现代主义疏离，建筑压过人物，空旷的长镜头，人物在空间中迷失，时间拒绝收束。

## (2) 镜头语言

- 景别：远景与全景为主，人物常被建筑与风景吞没；特写罕见。`verbatim`
- 机位：缓慢横移与推轨，机位常在人物离场后继续停留，拍空镜头。`verbatim`
- 镜头：长焦压缩空间，景深浅，人物与背景分离。`impression`

## (3) 场面调度

- 场面调度：人物在现代建筑、荒原、空旷广场中游荡，走位无目的。`verbatim`
- 演员：职业演员，表演克制、疏离，台词少，沉默多。`impression`
- 空间：现代主义建筑、工业区、荒原，空间即异化本身。`impression`

## (4) 剪辑节奏

- 剪辑：节奏极慢，长镜头后接空镜头；剪切制造时间断裂而非连续。`verbatim`
- 转场：硬切，场景之间留白，省略不作交代。`impression`
- 声音：环境音（风、脚步、机器）为主，对白稀疏，音乐克制。`impression`

## (5) 色彩与光影

- 色彩：黑白时期灰调冷峻；彩色时期（《红色沙漠》）人工色彩，工业灰绿与赭红。`verbatim`
- 光影：阴天漫射光，少强烈明暗；色彩本身即情绪。`impression`
- 画幅：宽银幕，横向构图强调空旷。`impression`

## (6) 叙事结构

- 结构：去情节化，事件（失踪、谋杀）不解决，结尾开放。`verbatim`
- 视点：限知视角，观众与人物同样迷失。`impression`
- 时间：绵延的时间，等待与游荡即内容。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：现代建筑与荒原、人物离场后的空镜头、失踪与不解决的事件、疏离的情侣。
- 该拍：工业区、空旷广场、雾中的风景、漫长的等待。
- 不该拍：不拍情节反转、不拍心理独白、不拍煽情特写、不拍闭合结局。
- Negative prompt: `No plot twists, no psychological monologue, no sentimental close-ups, no closed ending, no fast cutting, no explanatory dialogue`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Michelangelo Antonioni, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, the camera lingers after the passengers leave, empty carriage, modern architecture, alienation, long empty take, time that will not resolve`
- 中文对照：安东尼奥尼风格：一只约克夏犬坐在地铁座位上，乘客离场后镜头继续停留，空荡的车厢，现代建筑，疏离，空旷的长镜头，拒绝收束的时间。
- Negative: `No plot twists, no psychological monologue, no sentimental close-ups, no closed ending`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
