# Aki Kaurismäki — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aki Kaurismäki: deadpan minimalism, working-class Helsinki, long silences, rock and roll on a jukebox, kindness without sentimentality, a happy ending that arrives quietly`
- ZH: 考里斯马基风格：面无表情的极简，赫尔辛基工人阶级，长久的沉默，点唱机里的摇滚乐，不煽情的善意，安静到来的圆满结局。

## (2) 结构：三幕 / 序列 / 节拍

- 极简三幕：第一幕小人物丢工作、丢记忆或丢爱人，几场戏交代处境；第二幕靠陌生人的善意与偶然慢慢回升，中点常常是一顿饭或一首歌；第三幕安静收束，不靠高潮靠一句“留下来”。时间跨度数周，几乎不用闪回。

## (3) 对话

- 对白极少、极短、极干，人物惜字如金；沉默占一半篇幅；幽默来自一本正经的错位，不靠俏皮话。动作描写简洁，多写点唱机、咖啡、香烟这些静物。

## (4) 人物弧光

- 主角多为失业工人、流浪者、失忆者，弧光是从一无所有到被接纳：不是奋斗成功，而是被善意收留。人物关系是工人阶级小圈子与陌生人的善意；结局人物不“成长”，只是终于有地方可去。

## (5) 类型套路与创新

- 类型：工人阶级喜剧剧情；遵守套路——落魄、相遇、收留；打破的一条是：全片几乎没有戏剧冲突，靠沉默与善意推进。创新在剧本层面：把沉默写成结构，让静物与音乐代替对白。禁套路：不用煽情音乐铺垫，不用大段解释，不用阶级控诉的演说。

## (6) 该写什么 / 不该写什么

- 该写：工人阶级小人物、极简对白与长沉默、点唱机、咖啡与静物、陌生人的善意、安静的圆满收束。
- 不该写：煽情音乐铺垫、大段解释性对白、阶级控诉演说、戏剧化高潮、心理独白。
- Negative prompt: `No sentimental musical swell, no long explanatory dialogue, no class-indictment speech, no melodramatic climax, no interior monologue`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Aki Kaurismäki, a man who lost his job buys oden at a convenience store late at night. He says almost nothing. A stranger pays for his coffee. A song plays on the radio. He stays.`
- 中文对照：考里斯马基风格：一个失业的男人深夜在便利店买关东煮，几乎不说话，一个陌生人替他付了咖啡钱，收音机里放着一首歌，他留下来了。
- Negative: `No sentimental musical swell, no long explanatory dialogue, no class-indictment speech, no melodramatic climax`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
