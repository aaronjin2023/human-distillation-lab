# Sylvia Chang — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sylvia Chang: women's lives at different ages, Taipei and Hong Kong as emotional maps, love that arrives late or leaves early, tenderness without sentimentality`
- ZH: 张艾嘉风格：不同年龄的女性人生，台北与香港是情感地图，迟到或早退的爱，温柔而不煽情。

## (2) 结构：三幕 / 序列 / 节拍

- 女性群像三幕：第一幕一位或几位女性在城市日常切入，被爱情与家庭困住；第二幕一次相遇或一次离开把人物推出原地，中点是人物终于为自己做一个决定；第三幕不靠圆满收束，靠人物的自处收束。多线并行（《20 30 40》三位女性三条线），时间跨度数月。

## (3) 对话

- 对白温柔、克制，带台北与香港口语；女性之间的对话多、直白而体贴；潜台词是年龄与处境——没说出口的遗憾最重。动作描写多写城市街道、咖啡馆、家庭。

## (4) 人物弧光

- 主角多为不同年龄的女性，弧光是从为别人活到为自己做决定：不是反叛，是终于自处。人物关系是女性之间、母女、恋人的互相照亮；结局人物不胜利，只自处。

## (5) 类型套路与创新

- 类型：女性剧情与都市爱情；遵守套路——相遇、错过、自处；打破的一条是：拒绝男性拯救与大团圆，女性互相照亮。创新在剧本层面：把不同年龄的女性写成同一主题的三条线，一次收束。禁套路：不用煽情独白，不用说教，不用大团圆。

## (6) 该写什么 / 不该写什么

- 该写：不同年龄的女性、台北与香港的城市地图、温柔克制的对白、女性互相照亮、自处的收束。
- 不该写：煽情独白、说教、大团圆、男性拯救、让女性只当爱情符号。
- Negative prompt: `No sentimental monologue, no preaching, no happy reunion, no male rescue, no woman as mere love symbol`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Sylvia Chang, three women of different ages buy oden at the same convenience store late at night, each alone, each thinking of someone. Tender, restrained. They leave separately, a little less alone.`
- 中文对照：张艾嘉风格：三个不同年龄的女人深夜各自在同一家便利店买关东煮，各自想着一个人，温柔克制，各自离开，稍微不那么孤单。
- Negative: `No sentimental monologue, no preaching, no happy reunion, no male rescue`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
