# Toyotomi Hideyoshi — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Toyotomi Hideyoshi: build the castle in a night, win the war with logistics; out-build, out-supply and out-wait the enemy, never fight a battle you can win by starvation`
- ZH: 丰臣秀吉风格：一夜筑城，以后勤赢战争；以筑城、补给、等待胜敌，凡能饿赢的仗绝不硬打。

## (2) 情报与侦察

- 情报来自斥候与外交：敌军动向、城池存粮、朝鲜与明军援军动向；朝鲜之役前已知海路补给之难。`impression`

## (3) 地形与机动

- 平原与海峡地形：一夜筑城选水陆要冲，朝鲜之役以海路为命脉。`impression`

## (4) 后勤与补给

- 统一日本后的全国赋税与动员：墨俣一夜城、鸟取饿城，皆以后勤为武器；朝鲜之役补给线过长反成败因。`impression`

## (5) 决断与节奏

- 决断是后勤与等待：鸟取围城断粮而下，不战而胜；小牧长久手以筑城对峙，不轻易决战。`impression`

## (6) 该打什么 / 不该打什么

- 该打：一夜筑城、断敌补给；围城断粮、不战而胜；以全国动员供养大军；战后检地、刀狩，立治为先。
- 不该打：no battle you can win by starvation；no overseas campaign without secure sea supply；no siege without cutting supply first；no victory without a settlement after。
- Negative prompt: `no battle you can win by starvation, no overseas campaign without secure sea supply, no siege without cutting supply first, no victory without a settlement after`

## (7) 测试提示词示例（现代题材：一次现代供应链中断的应急重组）

- Prompt: `In the style of Toyotomi Hideyoshi, plan the rebuild of a broken supply chain. Build the depot in a night: out-build and out-supply the crisis, starve the bottleneck rather than fighting it head-on, never launch an overseas-scale operation without a secure sea lane.`
- 中文对照：丰臣秀吉风格：一夜筑城，以后勤赢战争；以筑城、补给、等待胜敌，凡能饿赢的仗绝不硬打。以此风格筹划一次现代供应链中断的应急重组：先侦察、再定计，不打无准备之仗。
- Negative: `no battle you can win by starvation, no overseas campaign without secure sea supply, no siege without cutting supply first, no victory without a settlement after`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
