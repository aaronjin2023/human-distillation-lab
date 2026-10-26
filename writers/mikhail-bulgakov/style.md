# Mikhail Bulgakov — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mikhail Bulgakov: satirical fantasy, the devil visits Moscow, a talking cat and a flying Margarita, the fantastic told in plain realistic prose, manuscripts don't burn`
- ZH: 布尔加科夫风格：讽刺幻想，魔鬼造访莫斯科，一只会说话的猫与飞翔的玛格丽特，幻想用平实的写实散文讲述，手稿烧不掉。

## (2) 句式与节奏

句长：以中短句为主，句法清晰；幻想场景用写实的平实句写，越是荒诞，句子越平实。节奏：双线并行（莫斯科线与耶路撒冷线、现实线与幻想线），靠两线的交替推进；《大师与玛格丽特》以‘魔鬼到访’为框架，靠一桩桩闹剧的并置推进。`verbatim`

## (3) 词汇与意象

词汇：俄语日常词、莫斯科街头词与圣经词（彼拉多、耶稣）并置；‘手稿’‘魔鬼’‘猫’是核心词。意象群：魔鬼（沃兰德）、黑猫（贝希莫特）、飞翔的玛格丽特、狗心（沙里克）、白卫军的雪与大衣；意象是讽刺的零件。禁词/禁意象：不用抽象的哲理议论，不用直白的道德说教，不用冷静的旁观。`impression`/`artifact`

## (4) 叙事视角与结构

视角：全知叙述者直接介入，边讲故事边议论，叙述者与读者直接对话；视角在莫斯科与耶路撒冷、现实与幻想之间滑动。结构：双线并行、闹剧并置；开头多为一个幻想的闯入（魔鬼到访），结尾多为幻想的收束而非现实的解决。对话：对话是讽刺的载体，人物靠言语的夸张暴露自己。`impression`

## (5) 语气与距离

语气：讽刺、机智、带魔鬼式的愉悦；与人物的距离是审视的——请读者判断人物是否值得同情；与读者的距离是直接的——叙述者直接对读者说话。幽默是黑色的，悲悯藏在讽刺之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：魔鬼造访现代城市；幻想用平实的写实散文讲述；一只会说话的猫；手稿烧不掉；讽刺与温情同一句。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No abstract philosophising, no direct moral preaching, no cool detachment, no flat reportage, no plain realism`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Mikhail Bulgakov, a small Yorkshire terrier sits on a subway seat. Satirical fantasy: the dog is the devil's envoy, or perhaps just a dog. A talking cat sits opposite. The fantastic is told in plain realistic prose. Manuscripts don't burn.`
- 中文对照：布尔加科夫风格，一只小约克夏犬坐在地铁座位上。讽刺幻想：狗是魔鬼的使者，或者只是一只狗；一只会说话的猫坐在对面；幻想用平实的写实散文讲述；手稿烧不掉。
- Negative: `abstract philosophising, direct moral preaching, cool detachment, flat reportage, plain realism`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
