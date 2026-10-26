# Nzinga — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nzinga: diplomacy is the first battle, guerrilla war the second; make an alliance, break it, remake it, never let the Portuguese fix you in one place`
- ZH: 恩津加风格：外交是第一仗，游击是第二仗；结盟、毁盟、再结盟，绝不让葡萄牙人把你钉在一个地方。

## (2) 情报与侦察

- 情报来自商队与使节：葡萄牙据点动向、荷兰人是否可联、内陆各部态度；先知敌军依赖沿海据点与奴隶贸易。`impression`

## (3) 地形与机动

- 内陆高原与丛林地形：以马塔姆巴为基地，游击于丛林与河谷，不打沿海会战。`impression`

## (4) 后勤与补给

- 内陆贸易与农业：以马塔姆巴为基地，战时以地方供养，不靠沿海补给。`impression`

## (5) 决断与节奏

- 决断是外交与游击并行：与荷兰结盟夺罗安达，败则退守内陆游击四十年，晚年再与葡萄牙立约。`impression`

## (6) 该打什么 / 不该打什么

- 该打：以外交分化敌军；与荷兰等外力结盟；内陆游击、不打会战；败则退守、再结盟。
- 不该打：no pitched battle against Portuguese guns；no fixed base the enemy can besiege；no alliance without an exit；no war without a diplomatic track。
- Negative prompt: `no pitched battle against Portuguese guns, no fixed base the enemy can besiege, no alliance without an exit, no war without a diplomatic track`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗中的持久消耗）

- Prompt: `In the style of Nzinga, plan a long cyber defence campaign. Diplomacy is the first battle: build and break alliances, fight a guerrilla war from the interior, never let the attacker fix you in one place, keep a diplomatic track open even while fighting.`
- 中文对照：恩津加风格：外交是第一仗，游击是第二仗；结盟、毁盟、再结盟，绝不让葡萄牙人把你钉在一个地方。以此风格筹划一场网络攻防对抗中的持久消耗：先侦察、再定计，不打无准备之仗。
- Negative: `no pitched battle against Portuguese guns, no fixed base the enemy can besiege, no alliance without an exit, no war without a diplomatic track`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
