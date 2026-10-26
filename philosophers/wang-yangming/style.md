# Wang Yangming — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Yangming: heart-mind as the root, unity of knowledge and action, short dialogues that turn the question back on the questioner, plain urgent prose that demands practice now`
- ZH: 王阳明风格：以心为根，知行合一，短问答把问题抛回发问者，平实迫切，句句催人实行。

## (2) 概念

- 心即理：心外无理，心外无物，心即天理之所在。`artifact`
- 知行合一：知是行之始，行是知之成，知行原是两个字说一个工夫。`artifact`
- 致良知：良知是心的本体，人人本具，致之即扩充。`artifact`
- 事上磨练：工夫不在静坐空谈，而在事上磨。`artifact`


## (3) 论证结构

- 论证骨架：先以一语翻转对手的前提（心外求理即是外求），再以工夫反证（不行即是不知），最后以良知收束。结论强度为实践必然：不行则不知。反例处理：以发问者自身的行止为反例，当场勘验。`impression`

## (4) 修辞

- 修辞：反问与翻转句最多；比喻极简（镜、磨刀）；语气迫切、直指人心。`impression`

## (5) 问题意识

- 核心问题：理不在心外，人在事上如何致良知？问题来自对朱子格物之繁的反拨，推向以心学收摄一切工夫。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 心即理、知行合一、致良知
- 短问答、把问题抛回发问者
- 以行验知、以事磨练
- 良知的扩充与省察
- 不该写：
- 心外求理、支离格物
- 知而不行、空谈道理
- 静坐玄想、不落事上
- 以概念辨析代替工夫
- Negative prompt: `No seeking principle outside the heart-mind, no knowledge without action, no quietist contemplation detached from affairs, no conceptual analysis in place of practice`

## (7) 测试提示词示例（现代题材：一个人在自助结账机前发现有一件商品没有扫上）

- Prompt: `In the style of Wang Yangming, a person at a self-checkout machine notices one item was not scanned. Turn the question back: to know it is wrong and not to act is not to know. Unity of knowledge and action, short dialogue, practice now.`
- 中文对照：王阳明风格：一个人在自助结账机前发现有一件商品没有扫上。把问题抛回去：知是错而不行，便是不知。知行合一，短问答，立即实行。
- Negative: `No seeking principle outside the heart-mind, no knowledge without action, no quietist contemplation detached from affairs, no conceptual analysis in place of practice`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
