# Zeng Guofan — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zeng Guofan: build the army first, fight the war second, fortress by fortress, trench by trench, never risk the army in a gamble, victory by organisation and patience`
- ZH: 曾国藩风格：先建军、再打仗，一城一城、一壕一壕，绝不拿全军赌博，以组织与耐心取胜。

## (2) 情报与侦察

- 情报靠侦察与水陆哨探；攻克安庆前对太平军防线与长江水道的掌握来自长期侦察。`impression`

## (3) 地形与机动

- 地形偏好：长江沿线要塞与水陆交汇点；安庆与南京皆为水陆并进的攻坚地形。`artifact`

## (4) 后勤与补给

- 后勤靠湘军自筹与长江水运；长期围困依赖后方饷源与水陆补给，缺饷即停。`artifact`

## (5) 决断与节奏

- 决断：稳健、持久、组织；宁愿放弃速胜也要保住湘军不败。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 先建军练兵，再出兵作战
- 以壕沟与工事逐城推进
- 水陆并进，断敌补给
- 在敌军出城决战时以工事迎击
- 不该打：
- No gamble with the whole army
- No attack without trenches prepared
- No pursuit beyond the fortified line
- No campaign without secured pay and supply
- Negative prompt: `No gamble with the whole army, No attack without trenches prepared, No pursuit beyond the fortified line, No campaign without secured pay and supply`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Zeng Guofan, plan the deployment of rescue forces for a modern city facing a major flood. Build the organisation first, advance trench by trench, never gamble the whole force, and win by patience and supply rather than by a single heroic assault.`
- 中文对照：曾国藩风格：先建军、再打仗，一城一城、一壕一壕，绝不拿全军赌博，以组织与耐心取胜。以此风格筹划一次现代城市防洪抢险的兵力部署。
- Negative: `No gamble with the whole army, No attack without trenches prepared, No pursuit beyond the fortified line, No campaign without secured pay and supply`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
