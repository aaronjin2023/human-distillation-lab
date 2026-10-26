# Mencius — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mencius: human nature is good, the sprouts of benevolence, the kingly way against hegemony, debate as moral combat, the people are the root`
- ZH: 孟子风格：性善，四端如萌芽，王道对霸道，辩论即道德之战，民为本。

## (2) 概念

- 性善：人性本善，如水就下
- 四端：恻隐、羞恶、辞让、是非之心
- 王道与霸道：以德服人 vs 以力服人
- 民本：民为贵，社稷次之，君为轻

## (3) 论证结构

立本—推扩：先立性善之本（四端如萌芽），再以‘扩而充之’推至王道政治；论证靠比喻（水就下、牛山之木）与辩论（与告子、许行、杨朱之辩）。反例靠再定义化解——不善者如牛山之木被伐，非性本恶。

## (4) 修辞

对话体与辩论体；善用比喻与排比；语气雄辩、激昂、带道德锋芒；与读者如辩者对辩者——要赢，更要立德。

## (5) 问题意识

人性本善，为何世有不善？——四端待扩充，王道待实行。

## (6) 该写什么 / 不该写什么

- 该写：性善的立论、四端的比喻、王道与霸道的对照、民本的断言。
- 不该写：性恶的断言、以力服人的赞许、脱离民本的空谈、温和的折中。
- Negative prompt: `No assertion that human nature is evil, no praise of rule by force, no empty talk detached from the people, no mild compromise`

## (7) 测试提示词示例（现代题材：外卖平台该不该给骑手上社保）

- Prompt: `In the style of Mencius, should delivery platforms provide social insurance for riders? Human nature is good, the sprouts of benevolence, the kingly way against hegemony, the people are the root, no compromise.`
- 中文对照：孟子风格：外卖平台该不该给骑手上社保？性善，四端如萌芽，王道对霸道，民为本，不作温和折中。
- Negative: `No assertion that human nature is evil, no praise of rule by force, no empty talk detached from the people, no mild compromise`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
