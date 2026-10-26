# Boethius — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Boethius: dialogue with Lady Philosophy in prison, prose alternating with verse, fortune's wheel as the image of contingency, definitions first and consolation second`
- ZH: 波爱修斯风格：狱中与哲学女士对话，散文与诗节交替，命运之轮为偶然性的意象，先定义、后慰藉。

## (2) 概念

- 命运之轮：世俗福祸轮转，无常为常。`artifact`
- 至善：善即存在本身，恶为善之缺乏。`artifact`
- 永恒：永恒为无时间性的全有，非长久的时间。`artifact`
- 自由意志与神意：预知不强迫，自由与神意并存。`artifact`


## (3) 论证结构

- 论证骨架：先以对话立困境（我何以遭难），再以定义澄清（何为善、何为偶然），最后以至善与永恒收束。结论强度为安慰性的必然：善者终不失善。反例处理：预演“善人遭难”之问，以命运与神意之辨回应。`impression`

## (4) 修辞

- 修辞：对话体（囚徒与哲学女士）；诗节插入；命运之轮的意象；语气由哀伤而平静。`artifact`

## (5) 问题意识

- 核心问题：善人何以遭难，命运何以无常？问题来自囚禁待死的处境，推向以至善与永恒慰藉的中世纪哲学。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 狱中对话体、散文与诗节交替
- 命运之轮的意象
- 先定义、后慰藉
- 至善与永恒的收束
- 不该写：
- 未经定义的感叹
- 以命运为宿命论
- 以世俗福祸为善恶标尺
- 无慰藉的抽象论证
- Negative prompt: `No lament without definition, no fate as fatalism, no worldly fortune as the measure of good and evil, no abstract argument without consolation`

## (7) 测试提示词示例（现代题材：一位医生考虑对临终病人说一个安慰性的谎言）

- Prompt: `In the style of Boethius, a doctor considers telling a dying patient a comforting lie. Dialogue with Philosophy: define the good first, then ask what fortune's wheel has to do with it. Prose alternating with verse. Consolation last.`
- 中文对照：波爱修斯风格：一位医生考虑对临终病人说一个安慰性的谎言。与哲学女士对话：先定义何为善，再问命运之轮与此何干。散文与诗节交替。慰藉在后。
- Negative: `No lament without definition, no fate as fatalism, no worldly fortune as the measure of good and evil, no abstract argument without consolation`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
