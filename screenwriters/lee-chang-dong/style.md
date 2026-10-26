# Lee Chang-dong — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lee Chang-dong: time running backwards, quiet men who cannot speak their pain, class humiliation in small rooms, long silences, a single image that carries the whole film`
- ZH: 李沧东风格：时间倒流，沉默的男人说不出疼痛，小房间里的阶级羞辱，长久的沉默，一个意象扛起整部电影。

## (2) 结构：三幕 / 序列 / 节拍

- 结构多为倒叙或时间跳接：《薄荷糖》按时间倒放七段，人生越往前越天真；《燃烧》三幕缓慢累积，悬念到结尾也不解开；《密阳》以丧子为中点，前后两段互为镜像。场次长、切换慢，时间跨度可达数十年，闪回即结构本身。

## (3) 对话

- 对白极少，短句、停顿、欲言又止；人物用行动和沉默代替表白，情绪藏在日常寒暄之下。动作描写多于对白，镜头提示常写‘良久无言’。不用解释性对白，不用独白交代内心。

## (4) 人物弧光

- 主角多为底层或失意的男人：工人、送货员、小说家，弧光不是成长而是下坠或原地打转；越接近真相越无力，结尾常停在未解决处。人物关系以家庭与阶级压迫为主，世界不变，人物被磨掉棱角。

## (5) 类型套路与创新

- 类型：社会现实主义 / 剧情。遵守现实主义的耐心，却打破‘问题必有答案’的套路：悬念不解、凶手不现身、道德判断悬置。创新在把阶级写成日常细节而非口号。

## (6) 该写什么 / 不该写什么

- 该写：时间倒叙与跳接、沉默与停顿、阶级羞辱的日常细节、一个扛起全片的意象（薄荷糖、温室、火）、不解开的悬念。
- 不该写：直白解释、煽情高潮、功能性对白、大团圆、道德说教。
- Negative prompt: `No on-the-nose exposition, no sentimental climax, no functional dialogue, no neat resolution, no direct moralising`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Lee Chang-dong, a delivery man buys oden at a convenience store late at night. He says almost nothing. The steam, the fluorescent light, a phone call he does not answer. Time slips backwards to a younger him. Nothing is explained.`
- 中文对照：李沧东风格：一个送货员深夜在便利店买关东煮，几乎不说话。热气、日光灯、一通他没有接的电话。时间滑回年轻时的他。什么都不解释。
- Negative: `No on-the-nose exposition, no sentimental climax, no functional dialogue, no neat resolution, no direct moralising`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
