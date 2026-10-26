# Federico Fellini — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Federico Fellini: dreamlike carnival, memory and fantasy fused, grotesque processions, faces as landscapes, camera that dances with the crowd`
- ZH: 费里尼风格：梦幻嘉年华，记忆与幻想融合，怪诞游行，面孔即风景，与人群共舞的镜头。

## (2) 镜头语言

- 景别：全景群戏与面孔特写交替，特写如风景般凝视。`verbatim`
- 机位：推轨与横移跟随游行，机位如舞者般移动；少用固定机位。`impression`
- 镜头：广角夸张面孔与空间，景深大，前景人物巨大。`impression`

## (3) 场面调度

- 场面调度：游行式群戏，人物如嘉年华队伍般进出画面；小丑、巨人、妓女同框。`verbatim`
- 演员：职业与素人混用，面孔优先于演技，选角看脸。`artifact`
- 空间：罗马街头、片场、海滩，现实与梦境同一空间。`impression`

## (4) 剪辑节奏

- 剪辑：段落式拼贴，场景如梦境跳接；节奏忽快忽慢，如嘉年华。`verbatim`
- 转场：硬切与叠化并用，梦境转场不加标记。`impression`
- 声音：尼诺·罗塔的音乐， Circus 般的旋律，环境音夸张。`artifact`

## (5) 色彩与光影

- 色彩：黑白时期灰调温润；彩色时期浓烈饱和，红、金、蓝如马戏团。`verbatim`
- 光影：影棚光，戏剧性明暗，面孔被照亮如舞台。`impression`
- 画幅：宽银幕，横向游行构图。`impression`

## (6) 叙事结构

- 结构：环形与拼贴（《八部半》梦与现实交织），开头常为梦境或游行。`verbatim`
- 视点：导演化身（圭多）的主观视角，记忆即叙事。`impression`
- 时间：记忆时间，过去与现在并置，不分先后。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：嘉年华游行、马戏与小丑、罗马街头、梦境与记忆、面孔特写、导演化身。
- 该拍：海滩、片场、妓院、巨人般的女性形象。
- 不该拍：不拍冷峻纪实、不拍克制留白、不拍线性因果、不拍去音乐化。
- Negative prompt: `No cold documentary realism, no restrained minimalism, no linear causality, no music-free scenes, no flat lighting, no naturalistic acting`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Federico Fellini, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat in a carnival of commuters, grotesque faces, a marching band in the carriage, dreamlike procession, camera dancing with the crowd`
- 中文对照：费里尼风格：一只约克夏犬坐在地铁座位上，车厢里是一场乘客的嘉年华，怪诞面孔，一支行进乐队，梦幻游行，与人群共舞的镜头。
- Negative: `No cold documentary realism, no restrained minimalism, no linear causality, no music-free scenes`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
