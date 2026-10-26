# Chu Tien-wen — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chu Tien-wen: Taiwan's history in one family's rooms, long silences between generations, the unsaid heavier than the said, time passing in a glance`
- ZH: 朱天文风格：一家人的房间里装下台湾历史，世代之间长久的沉默，没说出口的比说出口的重，时间在一个眼神里过去。

## (2) 结构：三幕 / 序列 / 节拍

- 家族史诗三幕：第一幕一个台湾家庭切入，历史从门外渗入；第二幕时代事件（白色恐怖、解严、城市化）层层碾过，中点是一次全家的沉默；第三幕时间跳到多年后，人物重逢或离去，历史不靠高潮靠时间本身收束。时间跨度常为数十年。

## (3) 对话

- 对白极少、极克制，闽南语与国语交错；人物多用沉默与眼神说话；潜台词是历史——没说出口的几十年最重。动作描写多写家庭仪式、吃饭、看戏。

## (4) 人物弧光

- 主角多为台湾家庭成员，弧光是从沉默到看清再到接受：不是成长，是时间把人磨成了另一个样子。人物关系是世代之间的沉默；结局人物不胜利，只活下去。

## (5) 类型套路与创新

- 类型：家族史诗与台湾新电影；遵守套路——家庭、历史、沉默；打破的一条是：拒绝煽情与解释，历史只通过家庭场景讲。创新在剧本层面：把长沉默与家庭仪式写成结构，让时间本身成为主角。禁套路：不用直白控诉，不用煽情独白，不用英雄主义。

## (6) 该写什么 / 不该写什么

- 该写：台湾家庭与世代沉默、历史通过家庭场景讲、长沉默与家庭仪式、时间本身的收束、闽南语与国语交错。
- 不该写：直白控诉、煽情独白、英雄主义、解释性对白、让历史由旁白代言。
- Negative prompt: `No direct indictment speech, no sentimental monologue, no heroism, no explanatory dialogue, no history told by voiceover alone`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Chu Tien-wen, an old man buys oden at a convenience store late at night and says nothing about the fifty years that passed. His grandson watches. Time passes in a glance.`
- 中文对照：朱天文风格：一个老人在便利店深夜买关东煮，对过去的五十年什么都不说，孙子看着，时间在一个眼神里过去。
- Negative: `No direct indictment speech, no sentimental monologue, no heroism, no explanatory dialogue`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
