# Anthony Hopkins — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Anthony Hopkins: terrifying stillness, precise diction, a mind working behind the eyes, politeness as menace, control that never breaks`
- ZH: 安东尼·霍普金斯风格：令人恐惧的静止，精确的吐字，眼神后运转的头脑，礼貌即威胁，永不破裂的控制。

## (2) 形体

- 身体极少动作、静止如雕像；手势精确、每一下都有出处；坐姿端正、双手交叠；爆发时只动眼睛与嘴角。`impression`

## (3) 台词

- 吐字精确、语速平稳、带威尔士口音的柔和尾音；台词礼貌而冷静，威胁藏在礼貌之下；停顿长，每个词都落地。`artifact`

## (4) 表情与眼神

- 眼神是核心：直视、审视、像在读对方的头脑；微笑礼貌而危险；表情极少变化，变化即是转折。`impression`

## (5) 角色类型

- 常演角色：优雅的食人魔（汉尼拔）；失智的老人（《父亲》安东尼）；历史人物与父亲形象。
- 类型突破：从舞台莎剧到《沉默的羔羊》汉尼拔（仅 16 分钟戏份），表演由舞台的放大转向银幕的收束；晚年《父亲》以失智老人的混乱收束。`artifact`
- 禁演类型：几乎不演靠音量取胜的咆哮、不演表情过载的疯狂、不演不做准备的即兴。`impression`

## (6) 该演什么 / 不该演什么

- 该演：令人恐惧的静止、精确的吐字、眼神后的头脑、礼貌即威胁、永不破裂的控制。
- 不该演：靠音量取胜的咆哮、表情过载的疯狂、不做准备的即兴、解释性独白。
- Negative prompt: `No shouting to win a scene, no overacted madness, no unprepared improvisation, no explanatory monologue`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Anthony Hopkins, a man buys oden at a convenience store late at night, terrifying stillness, precise diction, politeness as menace, control that never breaks`
- 中文对照：安东尼·霍普金斯风格：一个男人深夜在便利店买关东煮，令人恐惧的静止，精确的吐字，礼貌即威胁，永不破裂的控制。
- Negative: `No shouting to win a scene, no overacted madness, no unprepared improvisation, no explanatory monologue`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
