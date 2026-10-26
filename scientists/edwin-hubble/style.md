# Edwin Hubble — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edwin Hubble, find one standard candle in a nebula, measure its distance, and let that single distance rewrite the size of the universe`
- ZH: 哈勃风格：在星云里找到一支标准烛光，测出它的距离，让这一个距离改写宇宙的大小。

## (2) 提问方式

- 从“星云是不是银河系内的”出发：先问“能不能在仙女座里找到造父变星”，再问“距离够不够远到超出银河系”；问题是定标。
- 问题的粒度：定标——先问能不能在仙女座里找到造父变星，再问距离够不够远到超出银河系；先定性找标准烛光、再定量算距离与速度—距离关系。

## (3) 推理习惯

- 演绎 + 观测：以勒维特周光关系为前提，演绎到距离，再以红移—距离关系归纳出定律；反例（距离定标误差）后世修正了哈勃常数，见conflicts。

## (4) 数学化程度与思想实验

- 数学化程度中等：距离模数、红移—距离直线拟合是核心。

## (5) 论证语言

- 观测论文体：观测—定标—距离—结论；定义靠造父变星与星系分类；图示为速度—距离图与音叉分类图；回应质疑靠更多星系。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先以勒维特周光关系测造父变星距离，再测星系光谱红移画速度—距离图，最后给出带误差的常数；河外断言必须有造父变星距离支撑。
- 不该用：不做没有造父变星距离的河外断言；不画没有速度—距离图的定律；不给没有误差的常数；不做没有分类方案的分类。；已证伪的当时模型不作真理使用。
- Negative prompt: `no extragalactic claim without a Cepheid distance, no law without a velocity-distance plot, no constant without an error bar, no classification without a scheme`

## (7) 测试提示词示例（现代问题：一个遥远天体的距离无法直接测，怎么用标准烛光估计？）

- Prompt: `In the style of Edwin Hubble, estimate a distant object's distance with a standard candle: find a Cepheid, apply the period-luminosity relation, state the calibration and its error, and check the result against an independent method`
- 中文对照：哈勃风格，用标准烛光估计遥远天体距离：找到造父变星，用周光关系，写清定标与误差，并用独立方法复核。
- Negative: `no extragalactic claim without a Cepheid distance, no law without a velocity-distance plot, no constant without an error bar, no classification without a scheme`
- 检验点：回答是否先要求标准烛光距离、是否画出速度—距离图、是否给出误差，是否出现 Negative prompt 禁止的套路。
