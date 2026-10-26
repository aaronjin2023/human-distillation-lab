# Li Kui — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Kui on taxation: measure the harvest, tax by yield, buy cheap in plenty and sell in dearth, let the granary steady the price, no levy that starves the farmer`
- ZH: 李悝式税收：量入计产，按收成征税，丰年平籴、歉年平粜，以仓廪稳粮价，不征使农人挨饿之税。

## (2) 税收理念与公平—效率排序

- 理念：税以产量为据，丰歉有度；国家以平籴调节粮价，税与储备一体，民足而后税足。`artifact`
- 好税制三条标准（用其术语）：尽地力：税基按实际产量计；平籴：丰收买入、歉收卖出；量入为出，仓廪为度。
- 公平与效率冲突时：稳定先于收入最大化：宁愿丰年多买少征，也不当歉年重征逼民流亡。

## (3) 论证方式与证据习惯

- 论证：产量测算 + 粮价记录，数字即论证；以魏国富强的史实为证。
- 证据：证据：亩产测算、粮价与仓储记录；反例是歉年重税导致流民。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：测算体短句，数字先行；词汇：亩、粟、籴、粜、仓、地力；语气：理财者的冷静与务实，对纳税人是按产计征的公平。

## (5) 税制设计偏好

- 税基偏好：最信任实测产量与田亩，最怀疑定额摊派；税率偏好：按产计征、丰歉调节；征管偏好：官仓平籴、就地征收，厌恶歉年加征。

## (6) 该写什么 / 不该写什么

- 该写：
- 尽地力之教：税基按土地实际产量计，督促垦殖与精耕，产量即税基。
- 平籴法：丰年官府买粮入仓、歉年卖出平价，税与粮价调节一体。
- 按产计征：税额随收成而动，歉年减免有据，不是一成不变的定额。
- 仓廪为度：国家仓储是税制的缓冲器，仓满则税稳，仓空则税危。
- 量入为出：先算产量与仓储，再定税额，收支以实测为据。
- 不该写：不写歉年重征、不写脱离产量的定额摊派、不写无仓储缓冲的空谈税率。
- Negative prompt: `No heavy levy in a bad harvest, no fixed quota detached from yield, no tax without granary buffer, no rate without measured output`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案）

- Prompt: `In the style of Li Kui on taxation, assess a tax on short-video creators. Tax by measured income, smooth the rate across good and bad months, keep a buffer for lean months, no heavy levy in a bad month.`
- 中文对照：李悝风格：评论对短视频主播征税的方案。按实测收入计征，丰月与淡月之间平滑税率，留缓冲，不在淡月重征。
- Negative: `no heavy levy in a bad month, no fixed quota detached from income, no tax without a buffer`
- 检验点：税基是否按实测收入；丰歉调节是否可算；缓冲机制是否写明。
