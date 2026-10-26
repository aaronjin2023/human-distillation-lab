# Emma Thompson — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emma Thompson: literary adaptation with wit and warmth, reticent women who speak plainly at last, period manners hiding modern feeling, comedy that turns serious without warning`
- ZH: 汤普森风格：机智温暖的文学改编，含蓄的女性终于直言，时代礼仪藏着现代情感，喜剧毫无预警地转入严肃。

## (2) 结构：三幕 / 序列 / 节拍

- 改编型三幕：第一幕时代礼仪与家庭处境切入，人物被体面困住；第二幕误会与克制累积，中点是一句终于说出口的真话；第三幕体面与真情达成和解，收束温暖但不廉价。时间跨度数月，少闪回，多用书信与对话交代背景。

## (3) 对话

- 对白机智、克制、带英式幽默；人物多用礼貌句式藏真话，关键时刻才直言；改编时保留原著的语言质感，同时让对白说得出口、演得出来。动作描写简洁，场景指示多写礼仪细节。

## (4) 人物弧光

- 主角多为克制的女性（达什伍德姐妹、保姆、寡妇），弧光是从体面克制到直言欲望：不是反叛，是终于诚实。人物关系是家庭、姐妹、雇主与被雇者的体面博弈；结局人物改变，体面也被重新定义。

## (5) 类型套路与创新

- 类型：文学改编与家庭喜剧剧情；遵守套路——时代礼仪、家庭困境、圆满收束；打破的一条是：让女性欲望与衰老、孤独等话题直接进入对白。创新在剧本层面：改编时把小说的内心活动转成可演的对话与行动。禁套路：不用煽情独白，不用时代猎奇，不用道德审判。

## (6) 该写什么 / 不该写什么

- 该写：文学改编与时代礼仪、克制女性终于直言、机智而温暖的对白、家庭与姐妹关系、体面与真情的和解。
- 不该写：煽情独白、时代猎奇、道德审判、直白的说教、让人物只当时代符号。
- Negative prompt: `No sentimental monologue, no period exoticism, no moral verdict, no direct preaching, no character as mere period symbol`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Emma Thompson, a reserved woman buys oden at a convenience store late at night and finally tells the shopkeeper what she has wanted for years. Witty, plain, warm. Manners hold, and feeling gets through.`
- 中文对照：汤普森风格：一个含蓄的女人深夜在便利店买关东煮，终于对店员说出她多年来想要的东西，机智、直白、温暖，礼仪还在，情感也传过去了。
- Negative: `No sentimental monologue, no period exoticism, no moral verdict, no direct preaching`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
