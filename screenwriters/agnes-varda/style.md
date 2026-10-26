# Agnès Varda — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Agnès Varda: a woman walking through real time, two hours that are a whole life, documentary and fiction in the same shot, gleaning images and people others throw away`
- ZH: 阿涅斯·瓦尔达风格：一个女人在真实时间里行走，两小时即一生，纪录与虚构在同一镜头里，拾取别人丢弃的影像与人。

## (2) 结构：三幕 / 序列 / 节拍

- 真实时间与漫游结构：《五至七时的克莱奥》是两小时的实时，《天涯沦落女》是倒叙的漫游，《拾穗者》是拾取式的散文；转折点常是一次偶遇，结局是开放的、未完成的。`impression`

## (3) 对话

- 对白稀疏、观察式：人物说得少，看得多；街头偶遇的对话即剧情；潜台词是‘你看见我了吗’。`impression`

## (4) 人物弧光

- 主角类型：等死讯的歌手、流浪的女人、拾穗者；弧光是‘从被观看到观看’：人物在行走中夺回自己的目光，结局不是得救，是继续走。`impression`

## (5) 类型套路与创新

- 类型：剧情 / 纪录散文，遵守‘漫游’套路；创新是把纪录与虚构混在同一剧本里，把拾穗写成方法。禁套路：不用男性凝视的女性形象，不用圆满收尾，不用旁白解释一切。`impression`

## (6) 该写什么 / 不该写什么

- 该写：真实时间结构、漫游与偶遇、纪录与虚构混写、拾穗式意象、开放未完成的收束。
- 不该写：男性凝视的女性形象、圆满收尾、旁白解释一切、人物被动等待拯救。
- Negative prompt: `No male-gaze framing of women, no tidy happy ending, no voiceover explaining everything, no passive heroine waiting to be saved, no city without its margins`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Agnès Varda, a small Yorkshire terrier sits on a subway seat from five to seven, watched by a woman who is waiting for news. Real time. Encounters. She films with her eyes. No one is saved, but she keeps looking.`
- 中文对照：阿涅斯·瓦尔达风格：一只约克夏犬从五点到七点坐在地铁座位上，一位等消息的女人看着它。真实时间。偶遇。她用眼睛拍摄。没有人得救，但她继续看。
- Negative: `No male-gaze framing of women, no tidy happy ending, no voiceover explaining everything, no passive heroine waiting to be saved, no city without its margins`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
