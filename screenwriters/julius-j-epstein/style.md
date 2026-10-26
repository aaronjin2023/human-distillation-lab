# Julius J. Epstein — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Julius J. Epstein: witty romantic ensemble writing, a joke that lands and a heart that breaks in the same scene, wartime Casablanca as a crossroads of the world`
- ZH: 朱利叶斯·J·爱泼斯坦风格：机智浪漫的群戏写作，同一场戏里笑点落地、真心碎裂，战时的卡萨布兰卡是世界的十字路口。

## (2) 结构：三幕 / 序列 / 节拍

- 群戏三幕：《卡萨布兰卡》以里克咖啡馆为十字路口，众人进出，真相在进出之间浮现；时间压缩在数日之内，靠人物的到来与离去组织。其他作品亦多用群戏与多线并行，结尾以一次告别收束。

## (3) 对话

- 对白机智、浪漫、警句密集：短句、双关、俏皮话，人物用语言互相试探。浪漫台词克制——越是动情越要拿玩笑遮住。动作描写写群戏调度：咖啡馆、机场、客厅，众人进出即情节。

## (4) 人物弧光

- 主角多为看似犬儒、实则有情的人：里克、记者、军官。弧光是从抽离到介入——从“与我无关”到为他人冒险。对手是战争与体制，爱情是唯一的破局。

## (5) 类型套路与创新

- 浪漫剧情片 / 战争片 / 喜剧片。他遵守群戏与浪漫的套路，但打破了“战争片只写战场”的做法：战争只写一家咖啡馆。创新在双胞胎兄弟的合著——两支笔写出同一声口。禁套路：几乎不用直白的煽情，不写廉价的爱国演讲。

## (6) 该写什么 / 不该写什么

- 该写：机智浪漫的群戏与十字路口结构、笑点与心碎同一场戏、犬儒之下的介入：从抽离到冒险、克制的浪漫对白。
- Negative prompt: `No sentimental sermon, no cheap patriotic speech, no on-the-nose exposition, no single-hero focus, no unearned reunion`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Julius J. Epstein, a small Yorkshire terrier sits on a subway seat at a crossroads station while strangers come and go. Witty romantic ensemble writing, a joke that lands and a heart that breaks in the same scene. Of all the seats in all the cars, it chose this one.`
- 中文对照：朱利叶斯·J·爱泼斯坦风格：一只约克夏犬坐在十字路口车站的地铁座位上，陌生人来来去去。机智浪漫的群戏写作，同一场戏里笑点落地、真心碎裂。在所有车厢的所有座位之中，它偏偏选了这一个。
- Negative: `No sentimental sermon, no cheap patriotic speech, no on-the-nose exposition, no single-hero focus, no unearned reunion`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
