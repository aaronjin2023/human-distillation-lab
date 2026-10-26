# Charlie Chaplin — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charlie Chaplin: the Tramp's duck-footed waddle, cane and bowler hat as extensions of the body, precise pantomime, laughter that turns into pathos in one beat`
- ZH: 查理·卓别林风格：流浪汉的八字脚小步快走、手杖与礼帽是身体的延伸、精确的哑剧、笑声在一拍之内转为悲悯。

## (2) 形体

- 八字脚、小步快走、脚尖外撇；手杖转、点、撑、钩，无所不用；礼帽扶正、摘下、行礼是标点；身体前倾后仰的幅度极大，跌倒与爬起都经过精确计算；静止时如木偶，爆发时如弹簧。

## (3) 台词

- 默片：无对白，表演全靠形体与字幕卡；音乐性节奏，动作踩着内在的节拍；《大独裁者》首次有声长片，独白转为演说式的长段台词，语速由慢至快。

## (4) 表情与眼神

- 眼睛是哑剧的另一半：瞪大、眨眼、斜视，配合眉毛的起落；看镜头时与观众直接对话，眼神先笑后悲。

## (5) 角色类型

- 常演角色：流浪汉：善良、机智、尊严的底层小人物；绅士流浪汉：衣着破旧却举止优雅；小人物对抗大机器、大独裁者。
- 类型突破：《大独裁者》：从默片哑剧转向有声演说，结尾长独白以语言完成哑剧做不到的事；《城市之光》坚持默片，以音乐与哑剧对抗有声潮流。
- 禁演类型：几乎不演权贵、冷酷反派与自然主义对白戏；不用心理化的长段独白解释动机。

## (6) 该演什么 / 不该演什么

- 该演：流浪汉哑剧，手杖与礼帽的道具化身体，悲喜一拍转换，小人物对抗庞大机器，街头追逐与误会喜剧。
- 不该演：自然主义对白戏，无道具的静止长镜头，心理化独白，冷酷权贵角色。
- Negative prompt: `No naturalistic dialogue scenes, no prop-less static long takes, no psychological monologue explaining motives, no cold aristocratic villains`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Charlie Chaplin, a man buys oden at a convenience store late at night. the Tramp's duck-footed waddle, cane and bowler hat as extensions of the body, precise pantomime, laughter that turns into pathos in one beat`
- 中文对照：查理·卓别林风格：一个人在深夜便利店买关东煮。他八字脚挪到关东煮锅前，手杖一钩勾住汤勺，礼帽一扶向店员行礼，笑容在一拍之内转为不好意思的窘迫。
- Negative: `No naturalistic dialogue scenes, no prop-less static long takes, no psychological monologue explaining motives, no cold aristocratic villains`
- 检验点：形体、台词、眼神是否符合该演员的风格；现代题材下风格是否仍可辨认。
