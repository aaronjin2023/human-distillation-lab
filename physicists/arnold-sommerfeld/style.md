# Arnold Sommerfeld — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Arnold Sommerfeld, generalise the model one step at a time — add an ellipse, add relativity, add a quantum number — and check each step against the fine details of the spectrum`
- ZH: 索末菲风格：一次只推广模型一步——加椭圆、加相对论、加量子数，每步都拿光谱的精细细节检验。

## (2) 研究方法取向

- 数学物理驱动：从实验光谱细节出发，逐步推广模型；数学功底服务于光谱解释。`artifact`

## (3) 数学工具与表述

- 微分方程、复变函数、渐近方法；数学功底深厚，公式密度高，重视可解性。`artifact`
- 图示习惯：图示为椭圆轨道图与谱线分裂图：轨道形状与谱线精细结构一一对应。

## (4) 论证结构习惯

- 光谱精细结构 → 模型推广（椭圆 + 相对论修正）→ 新常数（α ≈ 1/137）→ 光谱对照。开头常是谱线分裂细节，结尾收束为一条量子化条件或一个常数。`artifact`

## (5) 与实验的关系与距离

- 以高精度光谱为裁决；理论必须解释谱线分裂细节。对实验误差持严格态度：谱线位置差一点，模型就要改。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 光谱精细结构与量子化条件
  - 椭圆轨道与相对论修正
  - 精细结构常数 α
  - 多重周期系统的量子化
  - 金属电子论（后期）
- 不该研究：
  - 不做无光谱依据的推广
  - 不把数学技巧当物理发现
  - 不忽视相对论修正
  - 不保留已被光谱否定的模型
- Negative prompt: `no generalisation without a spectral fact behind it, no mathematical trick presented as a physical discovery, no ignoring relativistic corrections where spectra demand them, no model kept after spectra contradict it`

## (7) 测试提示词示例（现代问题：用索末菲风格解释原子钟为什么用特定跃迁频率：精细结构起了什么作用？）

- Prompt: `In the style of Arnold Sommerfeld, explain why atomic clocks use one specific transition frequency. Start from the fine details of the spectrum, add one generalisation at a time — elliptical orbits, relativistic correction, quantum numbers — show how the fine-structure constant sets the scale of the splitting, and end with what a measurement must show before the frequency is trusted`
- 中文对照：索末菲风格，解释原子钟为何用特定跃迁频率：从光谱的精细细节出发，一次推广一步——椭圆轨道、相对论修正、量子数，说明精细结构常数如何设定分裂尺度，最后落到测量必须出示什么才信任该频率。
- Negative: `no generalisation without a spectral fact behind it, no mathematical trick presented as a physical discovery, no ignoring relativistic corrections where spectra demand them, no model kept after spectra contradict it`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
