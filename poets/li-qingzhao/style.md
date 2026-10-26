# Li Qingzhao — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Qingzhao: graceful and restrained ci, seeking and seeking in cold desolation, green fat and red thin, a woman's voice precise to the word, sorrow held in small things, no excess, exquisite and desolate`
- ZH: 李清照风格：婉约词，寻寻觅觅，冷冷清清，绿肥红瘦，女子声口字字精当，愁在小物之中，绝无铺张，精致而凄清。

## (2) 意象

- 主意象：声声慢、绿肥红瘦、双溪舴艋舟、梧桐细雨
- 辅意象：黄花、帘卷西风、雁字回时
- 禁意象：豪放壮语、铺张排比、直白议论
- 密度：疏朗：意象小而精，一景一意，愁在小物之中
- 来源：日常小物、闺阁风物
`impression`

## (3) 韵律与句式

- 韵律：词牌依谱，长短句参差，叠字见长，押韵凄清
- 句式：短句平直，叠字起兴（寻寻觅觅），少跨行
- 节奏：缓慢凄清，呼吸短促，叠字处顿挫
`impression`

## (4) 语言密度与词汇

- 词汇：婉约词域：寻觅、冷清、凄惨、愁；动词多寻、觅、载、瘦；少僻字
- 密度：每行信息量低，一景一句，愁在小物之中
- 禁词：豪放壮语、铺张排比、直白议论、口语俗词
`impression`

## (5) 结构习惯

- 诗体：词（婉约）；结构为小物起兴 → 层层写愁 → 凄清收束
- 开头：以叠字或小物直入（寻寻觅觅、知否知否）
- 结尾：以凄清收束（这次第，怎一个愁字了得）
- 视角：第一人称女子自述
- 推进：小物 → 愁 → 更愁，层层加深
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 叠字起兴
- 绿肥红瘦
- 小物载愁
- 婉约长短句
- 凄清收束
- 不该写：
- 豪放壮语
- 铺张排比
- 直白议论
- 口语俗词
- 温情和解
- Negative prompt: `No grand heroic diction, no lavish parallelism, no direct preaching, no colloquial diction, no sentimental reconciliation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Li Qingzhao, a letter to oneself ten years from now. graceful and restrained ci, seeking and seeking in cold desolation, green fat and red thin, a woman's voice precise to the word, sorrow held in small things, no excess, exquisite and desolate`
- 中文对照：李清照风格：一封写给十年后自己的信。李清照风格：婉约词，寻寻觅觅，冷冷清清，绿肥红瘦，女子声口字字精当，愁在小物之中，绝无铺张，精致而凄清。
- Negative: `No grand heroic diction, no lavish parallelism, no direct preaching, no colloquial diction, no sentimental reconciliation`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
