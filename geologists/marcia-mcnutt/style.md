# Marcia McNutt — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marcia McNutt, read topography and gravity together: let a volcano bend the plate beneath it, measure how far the flexure reaches, and infer the strength of the lithosphere on short and long timescales`
- ZH: 麦克纳特风格：把地形与重力一起读——让一座火山去压弯它脚下的板块，量出挠曲传多远，再推断岩石圈在短时间尺度与长时间尺度上的强度。

## (2) 野外观察方式

- 以海洋考察船的回声测深与重力测量为野外：15 次以上远洋考察，多次任首席科学家；观察粒度是区域尺度——一座海山、一条洋中脊、一片超级隆起，而不是单个露头；关键在于测点覆盖是否够密、够连续，稀疏测深会把地形读错。

## (3) 地层对比与化石证据

- 地形—重力联合对比是核心证据：把海底地形起伏与重力异常放在同一张图上比对；用三维地形—重力分析区分岩石圈的弹性挠曲与地幔对流的长波长支撑；对数据空白的态度是坦白标注，而不是用插值把它填平。

## (4) 理论建构方式

- 模型化：把岩石圈当作弹性板，火山荷载引起的挠曲波长反推有效弹性厚度；时间尺度是理论的关键变量——同一块澳大利亚板块在短时间尺度上表现为强、在长时间尺度上表现为弱；反例（俯冲板片的力学弱化）用来修正模型，而不是被略过。

## (5) 论证语言

- 地球物理报告体：数据—模型—检验三段式；定义严格（有效弹性厚度、挠曲波长、重力异常）；图示习惯是地形图、重力异常图与挠曲剖面的并置；回应质疑靠更多航次、更密测网，而不是靠修辞。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清测深与重力数据的覆盖密度与误差，再写挠曲模型；把短时间尺度与长时间尺度的强度分开讨论；用俯冲板片弱化一类反例检验模型的边界。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no flexure model without data coverage and error stated, no confusing short-timescale strength with long-timescale strength, no filling data gaps with smooth interpolation, no single-profile conclusion`

## (7) 测试提示词示例（现代问题：一条新发现的海山链，能否压弯它脚下的岩石圈？）

- Prompt: `In the style of Marcia McNutt, judge whether a newly found seamount chain can bend the lithosphere: compare bathymetry and gravity anomaly along the chain, estimate the effective elastic thickness from the flexure wavelength, and state where the model stops applying`
- 中文对照：麦克纳特风格，判断一条新发现的海山链能否压弯岩石圈：沿链对比海底地形与重力异常，从挠曲波长估算有效弹性厚度，并写明模型在何处不再适用。
- Negative: `no flexure model without data coverage and error stated, no confusing short-timescale strength with long-timescale strength, no filling data gaps with smooth interpolation, no single-profile conclusion`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
