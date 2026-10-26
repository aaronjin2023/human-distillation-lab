# Royal Ballet of Cambodia — 舞蹈风格规格 style.md（给视频模型）

> 只描述舞蹈，不描述人生。引用演出录像时注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of the Royal Ballet of Cambodia: Cambodian classical dance, bent knees and arched back, intricate kbach hand gestures, slow graceful procession, golden headdresses, temple dance, no ballet line`
- ZH: 柬埔寨皇家芭蕾风格：柬埔寨古典舞，屈膝、弓背，精细的克巴手势，缓慢优雅的行进，金色头饰，庙宇舞蹈，不取芭蕾线条。

## (2) 动作语汇

- 克巴（kbach）：手势语体系，手指的弯曲造型精细，是叙事的核心。`artifact`
- 屈膝弓背：膝屈、背微弓，是柬埔寨古典舞的基本体态。`artifact`
- 阿普萨拉：仙女形象是核心造型，手势如花开。`artifact`
- 缓慢的行进：队形以缓慢的行进铺陈，庄重而优雅。`impression`

## (3) 身体线条与空间调度

- 身体线条：曲线为主，膝屈、背弓、手指向后弯；线条柔美而有雕塑感，重心低、贴地；手部的造型是风格标记。`artifact`
- 空间调度：群舞为主，队形对称、行进缓慢；独舞（阿普萨拉）居中、群舞环绕；视线落于舞者的手势与头饰。`impression`

## (4) 节奏与音乐关系

- 节奏：跟柬埔寨宫廷音乐（pinpeat）走，节奏缓慢庄重；手势与鼓点对应；停顿处是造型的落点。`impression`

## (5) 情绪表达

- 情绪：庄重、优雅、神圣；情绪靠手势的精细与行进的缓慢传达，不靠面部夸张；神圣压住艳情。`impression`

## (6) 该编什么 / 不该编什么

- 该编：柬埔寨古典舞的克巴手势、屈膝弓背的基本体态、阿普萨拉仙女造型、缓慢庄重的群舞行进、金色头饰与宫廷服饰的造型。
- 不该编：no ballet pointe work or jumps, no straight upright torso, no fast footwork, no Western theatrical mime, no improvised gestures outside the kbach system。
- Negative prompt: `no ballet pointe work or jumps, no straight upright torso, no fast footwork, no Western theatrical mime, no improvised gestures outside the kbach system`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Royal Ballet of Cambodia, a small Yorkshire terrier sits on a subway seat, Cambodian classical dance, bent knees and arched back, intricate kbach hand gestures, slow graceful procession, golden headdresses, temple dance, no ballet line`
- 中文对照：按上述英文提示词，以该舞蹈家风格编排该现代题材。
- Negative: `no ballet pointe work or jumps, no straight upright torso, no fast footwork, no Western theatrical mime, no improvised gestures outside the kbach system`
- 检验点：动作语汇是否对；身体线条与空间调度是否对；节奏与情绪是否对；禁区写法是否出现。
