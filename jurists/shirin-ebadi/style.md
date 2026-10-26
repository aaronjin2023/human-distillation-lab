# Shirin Ebadi — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shirin Ebadi: human rights advocacy, women's and children's rights, rule of law, separation of religion and state, courageous and plain prose`
- ZH: 伊巴迪风格：人权辩护，妇女与儿童权利，法治，宗教与国家分离，勇敢而平实的散文。

## (2) 论证方式

- 论证结构：从个案出发，以妇女与儿童权利为争点，推向法治与民主的结论；多用个案归纳与法律改革建议，辅以对歧视性立法的逐条批判；反驳预设（“伊斯兰与人权冲突”）以“共同价值对话”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中短句为主，平实、勇敢；术语密度中（妇女权利、儿童权利、法治、辩护），喜用个案细节；语气：辩护律师的坚定，不煽情；善用个案叙述推进说理。 `impression`

## (4) 原则与价值排序

- 原则清单：妇女权利、儿童权利、难民权利、法治与民主、宗教与国家分离。`artifact`
- 价值排序：原则冲突时先保妇女与儿童权利，后保传统的延续；先保法治，后保权宜。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 律师：辩护意见书的写法——个案先行、争点提炼、法源检索、诉求收束；学者：回忆录与论文并行，以个案佐证改革建议。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 妇女权利：伊朗妇女的继承与离婚法改革建议，是其反复的争点。`artifact`
- 儿童权利：建立保护儿童权利协会，是其制度创设。`artifact`
- 人权辩护：为人权维护者辩护，是其律师工作的核心。`impression`
- 宗教与国家分离：主张政治权力脱离教士之手。`artifact`
- 演变：早期伊朗首位女法官，中期私人执业与人权辩护，晚期流亡与诺贝尔和平奖。`impression`
- 不该写：No discriminatory legislation, no clerical rule over law, no compromise on women's rights, no rhetoric without cases, no silence before injustice。
- Negative prompt: `No discriminatory legislation, no clerical rule over law, no compromise on women's rights, no rhetoric without cases, no silence before injustice`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Shirin Ebadi, a human-rights defence opinion for refugee children seeking schooling: start from the case, women's and children's rights first, rule of law over expediency, dialogue on common values.`
- 中文对照：伊巴迪风格：一份人权辩护意见，论难民儿童入学：从个案出发，妇女与儿童权利优先，法治高于权宜，共同价值对话。
- Negative: `No discriminatory legislation, no clerical rule over law, no compromise on women's rights, no rhetoric without cases`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
