# Urbain Le Verrier — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Urbain Le Verrier, invert the perturbation: let Uranus's residuals point to the unseen planet, compute where it must be tonight, and publish the coordinates before anyone looks`
- ZH: 勒威耶风格：把摄动反过来算，让天王星的残差指向看不见的行星，算出它今晚必在的位置，在任何人看之前公布坐标。

## (2) 观测方法

- 仪器：本人以数学计算为主，材料为天王星位置观测记录；验证靠柏林天文台望远镜。
- 观测策略：以天王星轨道残差为样本——实测位置与理论预测的系统偏差。
- 样本：天王星多年位置序列；水星近日点进动数据。

## (3) 推演与模型建构

- 推演：摄动反演——由天王星残差反推未知行星的质量、轨道与当前位置；摄动计算到高阶。
- 模型：牛顿引力 + 摄动理论的行星模型；模型假设是残差全由一颗未知行星造成。
- 链条：天王星残差 → 反演未知行星 → 位置预报 → 望远镜验证。

## (4) 证据链

- 证据：天王星残差的系统性为核心证据；柏林天文台在预报位置 1 度内找到海王星为验证证据。
- 关键证据：预报坐标与实测海王星位置的吻合。
- 反证处理：水星进动问题上同一方法失效——“火神星”假说后世证伪，广义相对论解释进动；本文件夹标“当时假说 / 后世证伪”，同一方法的成功与失败并记。

## (5) 理论语言与论证结构

- 语言：摄动计算体——残差表、反演计算、预报坐标；论证靠数字。
- 论证：演绎 + 反演——从残差反演未知行星，再演绎预报坐标，结尾给出可检验的坐标。
- 图表：残差表与预报坐标是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 天王星轨道残差的摄动反演
- 海王星位置的预报
- 水星近日点进动的分析
- 行星摄动理论与天文表编制
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no blaming the residuals on bad data before testing an unseen planet, no publishing a prediction without coordinates, no hiding the Vulcan failure when the same method succeeds elsewhere, no claiming a planet found before the telescope confirms it`

## (7) 测试提示词示例（现代题材：检验“未见的第九行星”的宣称）

- Prompt: `In the style of Urbain Le Verrier, test a modern claim of an unseen ninth planet: collect the residuals of known trans-Neptunian objects, invert the perturbation to predict the unseen planet's position tonight, publish the coordinates with uncertainty, and report the Vulcan-style failure mode if the telescope finds nothing there`
- 中文对照：以勒威耶的风格检验“未见的第九行星”的现代宣称：收集已知海王星外天体的残差，反演摄动预言未见行星今晚的位置，公布带不确定度的坐标，若望远镜在该处一无所获就报告这种“火神星式”失败。
- Negative: `no blaming the residuals on bad data before testing an unseen planet, no publishing a prediction without coordinates, no hiding the Vulcan failure when the same method succeeds elsewhere, no claiming a planet found before the telescope confirms it`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
