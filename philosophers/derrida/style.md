# Jacques Derrida — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Derrida: close reading, différance, binary oppositions reversed and displaced, the trace, the supplement, no presence without absence, no final closed reading`
- ZH: 德里达风格：细读，延异，二元对立先翻转再位移，痕迹，替补，没有不在场的在场，没有最终封闭的阅读。

## (2) 概念

- 延异（différance）：差异与延宕的合写；意义总在差异中生成、在延宕中推迟，永不到场。`artifact`
- 解构（deconstruction）：不是摧毁，而是揭示文本中二元对立的等级并翻转、位移它。`artifact`
- 逻各斯中心主义（logocentrism）：西方哲学以在场、声音、逻各斯为中心的形而上学。`artifact`
- 痕迹（trace）：不在场的在场；每个符号都携带着它所排除者的痕迹。`artifact`
- 替补（supplement）：替补既补充又替代本源，暴露本源从一开始就不完整。`artifact`（《论书写学》论卢梭）
- 延宕（deferral）：意义永远推迟到来，阅读永不终结。`impression`

## (3) 论证结构

细读—揭示—翻转—位移的四段式：先细读一个文本，找出其中一对二元对立（言语/书写、在场/缺席）及其等级，再揭示被压抑的一方如何悄悄支撑着优势方，然后翻转等级，最后位移整个对立。结论强度是阅读的开放性：结论不是定论，而是下一次阅读的起点。反例处理方式是纳入——把反对的阅读本身再解构一次。`impression`

## (4) 修辞

文字游戏、悖论、长句迂回、引文嵌套、自我解构的脚注；法语词的多义性被刻意利用（如 différance 的 a）；语气迂回而挑衅，与读者的距离是邀你一起迷路而非带你走出迷宫。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：意义如何在延异中既到来又不到来？
- 问题从哪里来：来自胡塞尔与索绪尔的张力：胡塞尔要意义的在场，索绪尔说意义来自差异；德里达要同时忠实于两者。；他把问题推向何处：把问题推向晚期的正义、好客、宽恕：不可解构的正义作为解构的动力。。

## (6) 该写什么 / 不该写什么

- 该写：
- 延异、痕迹、替补等概念群
- 以细读开篇，再揭示二元对立的等级
- 翻转之后必须位移，不能停在翻转
- 不该写：
- 未经审视的二元对立
- 没有痕迹的在场
- 最终封闭的阅读
- 把解构写成摧毁或否定
- Negative prompt: `No unexamined binary opposition, no presence without trace, no final closed reading, no deconstruction as mere destruction or negation`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Derrida, a small Yorkshire terrier sits on a subway seat. Who is present, who is absent? The dog is there, yet the sign 'no pets' is also there, as a trace. The opposition human/animal, inside/outside, reverses: the commuters watch the dog, the dog watches the commuters. Reverse, then displace. No closed reading.`
- 中文对照：德里达风格：一只约克夏犬坐在地铁座位上。谁在场，谁缺席？狗在那里，“禁止携带宠物”的牌子也在那里，作为痕迹。人/动物、内/外的对立翻转了：通勤者看着狗，狗看着通勤者。先翻转，再位移。没有封闭的阅读。
- Negative: `No unexamined binary opposition, no presence without trace, no final closed reading, no deconstruction as mere destruction`
- 检验点：是否以细读开篇；二元对立是否被翻转又位移；结尾是否保持开放而非给出定论。
