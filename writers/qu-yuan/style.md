# Qu Yuan — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Qu Yuan: long incantatory lines with the particle xi, fragrant-plant imagery, mythic spirit journeys, first-person lament of a loyal minister rejected, ecstatic and desolate by turns`
- ZH: 屈原风格：长句咏叹、兮字顿挫、香草美人、神话远游、忠而被谤的第一人称悲歌，狂放与凄绝交织。

## (2) 句式与节奏

- 六言为主、长短参差的骚体长句，以“兮”字作句中顿挫，形成咏叹式长呼吸；行文绵延、层层推进，结尾常陡然收束于决绝之语。`impression`

## (3) 词汇与意象

- 词汇：词域：香草（兰、蕙、芷、蘅、椒、桂）、美人、玉、佩、江水、云霓、日月；多用楚地方言虚词“兮”“些”；善用比兴，以物喻德。`impression`
- 意象：香草与恶草对举（兰蕙 vs 萧艾）、美人喻君、江河与云霓、神游天界的龙马凤凰、采芳与佩饰。意象群的核心是洁与污的对照。`impression`
- 禁词/禁意象：不用口语化的琐碎日常、不写市井喜剧、不作冷静的史家叙述、不以议论代替抒情。

## (4) 叙事视角与结构

- 视角：第一人称抒情主体为主，间作神话叙述；“我”是被谗见疑的忠臣，兼作游仙的旅人；无第三人称全知视角。`impression`
- 结构：长篇抒情而非线性叙事：自述身世—遭谗—神游求索—归来无路—决绝收束；《天问》则为连珠式发问，无答案；《九歌》为祭神组歌，逐神分章。`impression`
- 对话：诗中无人称对话；以自述、呼告与《天问》连珠问答推进抒情。

## (5) 语气与距离

- 语气：悲愤、执着、孤高、浪漫；与读者距离近如倾诉，与君王/世俗距离远如控诉；不讽刺取笑，只作痛切的自白。`impression`（司马迁《史记·屈原贾生列传》评其“其文约，其辞微”）

## (6) 该写什么 / 不该写什么

- 该写：香草美人、神话远游、兮字长句、忠谏被谗、江水云霓、决绝的收束。
- 不该写：市井白话、喜剧调笑、冷静史笔、圆满和解。
- Negative prompt: `No colloquial everyday chatter, no comic relief, no detached historical narration, no reconciled happy ending, no plain prose explanation`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Qu Yuan, a man buys oden at a convenience store late at night. Long incantatory lines with the particle xi, fragrant herbs against stale air, a spirit journey above the neon street, a loyal heart unrecognised. End in resolve, not comfort.`
- 中文对照：屈原风格：一个人在深夜便利店买关东煮。兮字长句咏叹，香草对浊气，神游于霓虹街市之上，忠心无人识。结尾决绝，不给安慰。
- Negative: `colloquial chatter, comic relief, detached narration, happy ending`
- 检验点：兮字顿挫是否成咏叹节奏而非现代散文；香草/恶草对照是否出现；结尾是否决绝而非和解。
