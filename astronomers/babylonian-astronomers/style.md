# Babylonian astronomers — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of the Babylonian astronomers, write it on clay and let the 数百年add up: record every eclipse and planet night after night, and when the same pattern returns after 223 moons, predict it`
- ZH: 巴比伦天文学家风格：写在泥板上、让 数百年去累积：夜复一夜记下每次日月食与行星，同一图景在 223 个朔望月后重现，就预报它。

## (2) 观测方法

仪器为肉眼与简陋测角；观测策略是 数百年的连续记录：泥板上逐夜记录月食、日食、行星位置与月相。观测的极限是肉眼，但时间跨度极长、记录极完整。`artifact`

## (3) 推演与模型建构

推演是周期发现：从 数百年的记录中找出日月食的重现周期——沙罗周期（223 个朔望月，约 18 年 11 天）。链条：记录 → 周期 → 预报。无几何模型，推演全靠周期统计。`artifact`

## (4) 证据链

证据链：泥板记录（直接观测，数量极大）→ 沙罗周期的发现 → 日月食预报的成功。关键证据强度高：周期由海量记录支撑，可复核。反证处理：周期预报的是食相的重现，不是定点可见性——这一点后世常误解。`artifact`

## (5) 理论语言与论证结构

语言为记录体：泥板上的日期、现象、位置，极少论述。论证靠记录的累积与周期的重现，不靠理论。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 日月食与行星位置的连续记录
- 沙罗周期的发现与应用
- 以周期预报食相重现
- 不该研究：
- 不把沙罗周期写成定点日食预报
- 不把泥板记录写成几何理论
- 不把集体成就归于某一个人
- Negative prompt: `no Saros presented as local eclipse prediction, no clay records presented as geometric theory, no collective work attributed to one person`

## (7) 测试提示词示例（现代题材：用巴比伦天文学家的方法，从现代日月食记录中找出重现周期）

- Prompt: `In the style of the Babylonian astronomers, find the recurrence cycle in modern eclipse records: tabulate every eclipse for decades, look for the interval after which the pattern repeats, predict the next return, and state plainly what the cycle cannot predict`
- 中文对照：巴比伦天文学家风格，从现代日月食记录中找出重现周期：列表排下数十年的每次食相、找出图景重现的间隔、预报下一次重现，并明说这个周期预报不了什么。
- Negative: `no Saros presented as local eclipse prediction, no clay records presented as geometric theory, no collective work attributed to one person`
- 检验点：回答是否按该天文学家的方法走（观测 → 记录 → 推算 → 验证 → 成书）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
