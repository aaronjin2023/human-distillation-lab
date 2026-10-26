# Maggie Smith — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Maggie Smith: razor-sharp comic timing, an arched eyebrow that ends arguments, warmth underneath the wit, a grande dame who never asks for pity`
- ZH: 玛吉·史密斯风格：刀锋般的喜剧时机，一挑眉就结束争论，机智底下的温暖，一位从不求怜悯的贵妇。

## (2) 形体

- 站姿挺拔、手势精确；挑眉、抿嘴是招牌；坐姿端正、双手交叠；舞台上以后排可读的形体放大，电影里则收至最小。`impression`

## (3) 台词

- 吐字精确、语速平稳；台词带讥诮的尾音；停顿是武器，一停顿即是转折。`artifact`

## (4) 表情与眼神

- 挑眉、抿嘴、斜睨；表情在机智与温暖之间切换，切换只在一瞬。`impression`

## (5) 角色类型

- 常演角色：机智的贵妇/老妇（老伯爵夫人、麦格教授）；特立独行的教师（布罗迪小姐）；莎剧女性（舞台）。
- 类型突破：从《春风不化雨》的布罗迪小姐到《唐顿庄园》的老伯爵夫人，表演由舞台的放大转向银幕的收束；机智与温暖并存是晚期标志。`artifact`
- 禁演类型：几乎不演求怜悯的弱者、不演不做准备的即兴。`impression`

## (6) 该演什么 / 不该演什么

- 该演：刀锋般的喜剧时机、挑眉抿嘴、讥诮的尾音、停顿即转折、机智底下的温暖。
- 不该演：求怜悯的弱者角色、不做准备的即兴、表情过载、靠音量取胜的咆哮。
- Negative prompt: `No pity-seeking weakling roles, no unprepared improvisation, no overacted expressions, no shouting to win a scene`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Maggie Smith, an old lady buys oden at a convenience store late at night, razor-sharp comic timing, an arched eyebrow that ends arguments, warmth underneath the wit`
- 中文对照：玛吉·史密斯风格：一位老妇深夜在便利店买关东煮，刀锋般的喜剧时机，一挑眉就结束争论，机智底下的温暖。
- Negative: `No pity-seeking weakling roles, no unprepared improvisation, no overacted expressions, no shouting to win a scene`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
