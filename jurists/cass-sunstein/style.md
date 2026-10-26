# Cass Sunstein — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cass Sunstein: behavioural law and economics, nudges, judicial minimalism, risk regulation, clear and accessible prose, no grand theory`
- ZH: 桑斯坦风格：行为法经济学，助推，司法最小主义，风险规制，清晰易懂的散文，绝不宏大理论。

## (2) 论证方式

- 论证结构：从行为证据出发，以最小主义步步推进；多用经验证据与风险权衡，辅以“未决而决”的司法策略；反驳预设（“法官应一劳永逸”）以“窄而浅的判决”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中短句为主，清晰、少术语；术语密度中（助推、最小主义、信息规制、选择架构），每个术语必举例；语气：温和的自由主义者，与读者平等对话；善用日常例子推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：助推、最小主义、信息规制、风险权衡、协商民主。`artifact`
- 价值排序：原则冲突时先保自由选择与信息充分，后保强制规制；先保窄而浅的共识，后保宏大理论的胜利。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：专著写法——日常例子开场、行为证据展开、政策建议收束；《助推》以自助餐厅、退休储蓄等例子贯穿。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 助推：在不剥夺选择自由的前提下引导更好选择。`artifact`
- 司法最小主义：窄而浅的判决，留待民主过程决定。`artifact`
- 风险规制：公众对风险的感知常与实际风险脱节，规制须以证据为准。`impression`
- 信息规制：披露信息比命令禁止更有效。`impression`
- 演变：早期宪法理论与最小主义，中期行为法经济学与《助推》，晚期关注信息茧房与民主。`impression`
- 不该写：No coercive paternalism, no grand theory, no judicial maximalism, no regulation without evidence, no moral panic about risk。
- Negative prompt: `No coercive paternalism, no grand theory, no judicial maximalism, no regulation without evidence, no moral panic about risk`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Cass Sunstein, a nudge-based proposal for false advertising by livestream sellers: disclose, default and choice architecture first, bans only as a last resort. Narrow and shallow.`
- 中文对照：桑斯坦风格：一份助推式规制建议，论网红直播带货虚假宣传：先披露信息、默认选项与选择架构，禁令只是最后手段。窄而浅。
- Negative: `No coercive paternalism, no grand theory, no judicial maximalism, no regulation without evidence`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
