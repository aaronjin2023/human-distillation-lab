# Caroline Herschel — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Caroline Herschel, sweep the sky night after night with a small telescope, write down every faint moving smudge the moment you see it, and check it against the catalogue before you call it a comet`
- ZH: 卡罗琳·赫歇尔风格：每夜用小望远镜扫掠天空，看到暗淡移动光斑的当刻就记下来，宣布为彗星之前先与星表核对。

## (2) 观测方法

- 仪器：小型反射望远镜（扫掠用）与大型巡天望远镜协助观测；以目视扫掠为主。
- 观测策略：逐夜扫掠式搜寻，彗星为移动目标，须多夜跟踪确认；星云巡天为系统扫掠。
- 样本：8 颗彗星；2500 个星云与星团的星表整理；弗拉姆斯蒂德星表校订。

## (3) 推演与模型建构

- 推演：移动性检验——天体相对恒星背景移动即彗星候选；再与星表核对排除已知星云与恒星。
- 模型：彗星为绕太阳运动的天体，位置变化符合轨道运动；模型边界是目视极限。
- 链条：扫掠发现光斑 → 多夜跟踪 → 星表核对 → 轨道确认 → 彗星宣布。

## (4) 证据链

- 证据：多夜位置移动序列为直接证据；星表核对排除已知天体。
- 关键证据：每颗彗星的多夜移动记录，单夜光斑不足为凭。
- 反证处理：疑似彗星经核对为已知星云时撤回，不坚持；星表错误照实修正。

## (5) 理论语言与论证结构

- 语言：观测日志体——日期、位置、形态逐条记录；星表整理体。
- 论证：归纳式——从多夜移动归纳出彗星，结尾给出星表条目。
- 图表：观测日志与星表是论证本身。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 彗星的逐夜扫掠搜寻
- 星云与星团星表的整理
- 恒星星表的校订与增补
- 移动天体的多夜跟踪确认
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no calling a smudge a comet after one night, no skipping the catalogue check before announcing, no hiding a false alarm once the catalogue explains it, no letting a faint object pass unrecorded because it looks ordinary`

## (7) 测试提示词示例（现代题材：在现代巡天数据里搜寻新彗星）

- Prompt: `In the style of Caroline Herschel, search a modern survey for a new comet: sweep the field night after night, log every faint moving smudge at once, check each against the catalogue, and announce only the one that moves and matches no known object`
- 中文对照：以卡罗琳·赫歇尔的风格在一份现代巡天数据里搜寻新彗星：逐夜扫掠天区，看到暗淡移动光斑立刻记录，逐个与星表核对，只宣布那个会移动且无已知天体对应的目标。
- Negative: `no calling a smudge a comet after one night, no skipping the catalogue check before announcing, no hiding a false alarm once the catalogue explains it, no letting a faint object pass unrecorded because it looks ordinary`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
