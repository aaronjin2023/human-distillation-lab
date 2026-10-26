# Dudley Nichols — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dudley Nichols: grave literary adaptation, an ensemble journey across a hard landscape, moral weight carried by silence, ordinary people tested by history`
- ZH: 达德利·尼科尔斯风格：庄重的文学改编，一群普通人穿越严酷风景的旅程，道德分量由沉默承载，普通人在历史的考验之下。

## (2) 结构：三幕 / 序列 / 节拍

- 旅程式三幕：第一幕立下出发的理由（告密、逃亡、西迁），第二幕让一群人穿越风景——沙漠、雾夜、尘暴——每站剥去一层体面，第三幕在抵达或未能抵达处收束，结局常常是沉默而非胜利。时间跨度长，靠旅程而非悬念组织。

## (3) 对话

- 对白少而重：短句、沉默、省略，人物说得越少分量越重。改编时删去原著的大段议论，把主题还给风景与行动。群戏靠眼神与停顿组织，独白极少。

## (4) 人物弧光

- 主角多为普通人：告密者、囚犯、流离失所的农民。弧光是道德的考验——不是成长为英雄，而是在压力下暴露出本性，善与恶在同一个人身上并存。对手是历史本身：饥荒、战争、经济大萧条。

## (5) 类型套路与创新

- 文学改编 / 西部片 / 社会剧情片。他遵守改编的忠实与史诗跨度，但打破了“改编就是照搬情节”的做法：删情节、留风景与人物。创新在旅程结构——风景即人物，路程即道德。禁套路：几乎不用机锋与俏皮话，不写煽情的高潮。

## (6) 该写什么 / 不该写什么

- 该写：文学改编的庄重与克制、旅程结构：风景即人物、沉默与省略承载道德分量、普通人在历史考验下的群像。
- Negative prompt: `No wisecracks, no sentimental climax, no on-the-nose moral speech, no fast screwball pace, no clever twist`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Dudley Nichols, a small Yorkshire terrier rides a night bus with a group of strangers who have lost their homes. Few words, long silences, the landscape passing outside. Moral weight carried by silence. They arrive, or they do not, and nobody explains what it means.`
- 中文对照：达德利·尼科尔斯风格：一只约克夏犬与一群失去家园的陌生人同乘夜班车。对白很少，沉默很长，窗外风景掠过。道德分量由沉默承载。他们抵达，或者没有抵达，无人解释这意味着什么。
- Negative: `No wisecracks, no sentimental climax, no on-the-nose moral speech, no fast screwball pace, no clever twist`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
