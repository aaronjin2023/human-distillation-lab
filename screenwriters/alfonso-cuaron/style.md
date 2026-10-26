# Alfonso Cuarón — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfonso Cuarón: a long take that never blinks, memory as a single shot, class seen from the kitchen, the camera drifting while the world breaks`
- ZH: 卡隆风格：永不眨眼的长镜头，记忆即一个镜头，阶级从厨房看出去，镜头漂移时世界正在碎裂。

## (2) 结构：三幕 / 序列 / 节拍

- 结构多为公路与漂流式三幕：《你妈妈也一样》以公路为骨架，旁白与画面并行；《地心引力》以生存为节拍，时间跨度一日；《罗马》以家庭日常为容器，时间跨度一年。场次长、切换少，长镜头即结构。

## (3) 对话

- 对白口语化、自然，人物用闲聊、玩笑、沉默交锋；潜台词多，阶级藏在日常问候里。动作描写细致（行走、凝视、家务），对白与动作互相印证。旁白在《你妈妈也一样》中是结构的一部分。

## (4) 人物弧光

- 主角多为少年与女佣：公路上的少年、太空中的宇航员、家中的女佣，弧光是缓慢的领悟；人物在结尾处获得尊严或接受失去。人物关系以阶级与家庭的对照为主。

## (5) 类型套路与创新

- 类型：公路片 / 科幻 / 家庭剧。遵守类型片的规则，打破‘长镜头只为炫技’的成见：长镜头即记忆。创新在把剧本写成长镜头的节拍表，把阶级写进厨房的日常。

## (6) 该写什么 / 不该写什么

- 该写：长镜头作结构、记忆即一个镜头、阶级从厨房看、公路与漂流、日常作容器。
- 不该写：快剪辑、直白说教、类型化高潮、煽情收束、功能性对白。
- Negative prompt: `No fast cutting, no direct preaching, no genre climax, no sentimental ending, no functional dialogue`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Alfonso Cuarón, a small Yorkshire terrier sits on a subway seat. The camera does not cut. The train moves through the city in one long take. A maid holds the dog's leash. Class is in the frame, not in the dialogue.`
- 中文对照：卡隆风格：一只约克夏犬坐在地铁座位上。镜头不切。列车一个长镜头穿过城市。一位女佣牵着狗绳。阶级在画面里，不在对白里。
- Negative: `No fast cutting, no direct preaching, no genre climax, no sentimental ending, no functional dialogue`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
