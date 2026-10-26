# Joseph L. Mankiewicz — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joseph L. Mankiewicz: literate theatrical dialogue, flashback confession, women who speak better than the men around them, wit as a weapon and a wound`
- ZH: 约瑟夫·L·曼凯维奇风格：文雅的舞台式对白，闪回式自白，女性比身边的男人更会说话，机智既是武器也是伤口。

## (2) 结构：三幕 / 序列 / 节拍

- 闪回与自白结构：《彗星美人》以颁奖开场，多位人物轮流闪回，真相在各自的版本之间浮现；《三妻艳史》以三封信开场，三位妻子各自回忆。时间被打散，靠自白的顺序组织。其他作品亦多用倒叙与画外音。

## (3) 对话

- 对白是全片的本体：长句、机智、文学典故，女性角色尤其能言善辩，一句台词常常同时完成讽刺、揭露与自我辩护。独白与画外音是标志——人物在讲述中暴露自己。动作描写极简，把舞台让给语言。

## (4) 人物弧光

- 主角多为女性：野心勃勃的女演员、妻子、舞女。弧光是野心的代价——从天真到得手，再到得手之后的空虚。对手是另一个更会说话的人，胜负取决于谁的台词更锋利。

## (5) 类型套路与创新

- 剧情片 / 讽刺喜剧 / 文学改编。他遵守文学改编的体面与跨度，但打破了“女性只是被观看者”的写法：女性是全片最会说话、最清醒的人。创新在闪回自白结构——剧本本身就是一场审判。禁套路：几乎不用动作场面，不写直白的煽情。

## (6) 该写什么 / 不该写什么

- 该写：闪回自白与多版本真相、文雅机智的长句对白、能言善辩的女性主角、机智既是武器也是伤口。
- Negative prompt: `No action spectacle, no sentimental outburst, no on-the-nose exposition, no silent suffering, no simple hero`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Joseph L. Mankiewicz, a small Yorkshire terrier sits on a subway seat while three commuters each tell a different version of how it got there. Literate theatrical dialogue, flashback confession, wit as a weapon and a wound. Nobody is innocent, and the best line wins.`
- 中文对照：约瑟夫·L·曼凯维奇风格：一只约克夏犬坐在地铁座位上，三位乘客各自讲述它如何来到这里的不同版本。对白文雅如舞台剧，闪回式自白，机智既是武器也是伤口。无人无辜，最漂亮的一句台词获胜。
- Negative: `No action spectacle, no sentimental outburst, no on-the-nose exposition, no silent suffering, no simple hero`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
