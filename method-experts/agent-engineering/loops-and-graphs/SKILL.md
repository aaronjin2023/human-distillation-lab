# Loops & Graphs 编排法（专家模式）

- 领域：Agent 工程
- 来源：Hoodie（@HoodieFade_）长文《Loops & Graphs: how to stop being the slowest node in your agent system and approve only one step》，收录于西瓜小本本第 307 条；vault 笔记《Loops & Graphs：只批最后一步的 Agent 编排法笔记》
- 核验状态：方法本体（长文约 8,200 字）完整取回；主帖承诺的现成提示词在评论区，未取回；文中 Karpathy autoresearch、「Opus 5.5」型号、Bun 移植数字、子 agent 上限等均为作者陈述，未独立核查；31→17 分钟为作者自注的示意计时（ILLUSTRATIVE）
- 适用：设计多步骤 Agent 工作流时，让每个工作单元自己循环到正确、人只审批最后不可逆的那一步——解决「只建 loop 不建 graph，人成了系统里最慢的节点」

## 定位

核心论点一句话：**loop 让单个工作单元无人盯着也能变正确，graph 决定有哪些单元、什么顺序、哪里由人签字**。多数人只建 loop 不建 graph，于是自己被迫逐步审批、成了瓶颈。这套方法由六件套组成：检查先行、循环五件套、图先于顺序、节点契约、失败处置表、按不可逆性设人工门。

## 何时用 / 何时不用

- 用：多步骤、可拆分、需要无人值守跑一段时间的 Agent 任务；有明确验证手段（测试、schema、数据源）的任务最合适
- 不用：一次性小任务（拆图和写检查的成本超过收益）；完全没有客观检查手段的开放创作（证据分级会退化到 NOISE 级，loop 只会空转烧预算）
- 注意：谁来画图由「运行频率 × 出错不可逆成本」决定；周频任务忌每次从零重新生成工作流——拆法每次都变，经验无法沉淀

## 方法步骤

### ① 检查先行（证据分级）

1. 先写**能真正失败的检查**，再写任务本身；检查过不了，单元就不算完成
2. 证据按四级取用，弱证据不许冒充强证据：

```
STRONG   tests exit 0 / output matches the schema / diff stays inside the plan
MEDIUM   the cited source actually supports the claim / an independent path reaches the same answer
WEAK     a reviewer agent approves
NOISE    "looks good to me" / the model says it's confident / no errors were thrown
```

3. **沉默 ≠ 成功**：空错误日志只代表没报错，不代表没出错；把沉默当成功，loop 会重复同一个错误直到烧完预算

### ② 循环五件套（每个 loop 单元必备）

4. 五件套：**完成测试 ＋ 轮次上限 ＋ 预算 ＋ 尝试记忆 ＋ 卡住叫人**
5. 尝试记忆（seen）必须包含**被否决的发现**，防止反复捡回已否决项
6. 开放任务的停止条件按「去重后的新发现数」计：**连续 2 轮无新发现即停**（参考实现：上限 6 轮，dry 计数连续 2 轮无 fresh 就 break），不用「做到好为止」

### ③ 图先于顺序（拓扑）

7. 先画图再排顺序：节点一职、一入、一出
8. **逐边变量测试**：每条边都要说得出沿边传递的变量；说不出，就删边、改并行
9. 四种拓扑打底，覆盖近乎一切：**链 / 扇出＋汇合 / 路由器 / 有界循环**
10. 并行 worker 必须用**独立上下文**，互不污染

### ④ 节点契约（四行）

11. 每个节点写四行契约，描述不出四行，这个节点就无法测试、无法替换：

```
NODE  source_researcher
JOB   find one primary source per claim
IN    { topic, source_type }
OUT   { claim, url, quote }
FAILS AS  no_primary_source
```

12. **节点选型**：先问「它是否在做判断 / 决策 / 评估 / 总结」——不在做这些的节点用代码、不用模型

### ⑤ 失败处置表（预先决定，不整批退回）

13. 失败按预设表处置，只退回失败的单个单元，附**失败测试 ＋ 证据 ＋ 范围限定**（如 "this file only"）：

```
tool or network blip      → RETRY
model or source down      → FALLBACK
optional branch failed    → SKIP
output failed its check   → REPAIR that unit only
3 repairs failed          → ESCALATE, the plan is wrong
budget or permission hit  → STOP, wake a human
```

14. 同一单元修复 3 次不过，升级为「计划错了」（ESCALATE），不再原地重试
15. 修复通过后，把失败成因**写成规则回灌**，供下次拆任务时使用

### ⑥ 人工门按不可逆性设

16. 人工门按**不可逆性**而非置信度开：可一键回滚的操作自动放行；**迁移 / 删除 / 生产写入 / 付款永远由人签最后一步**
17. 不用置信度阈值当门：分数能被调低，关闭的通道没有分数可调

## 提示词与模板

主帖承诺的现成提示词在原帖评论区，未取回，本文件不虚构其原文。可直接套用的结构件有三：证据分级表（STRONG/MEDIUM/WEAK/NOISE）、停止条件参考实现（seen/dry 计数、连续 2 轮无去重新发现即停、上限 6 轮）、节点契约四行模板（NODE/JOB/IN/OUT/FAILS AS）与失败处置表，均见方法步骤。

## 验收标准

- [ ] 每个工作单元开工前都已有「能真正失败的检查」，且检查的证据等级标明（STRONG/MEDIUM/WEAK，NOISE 不计）
- [ ] 每个 loop 都配齐五件套：完成测试、轮次上限、预算、尝试记忆（含被否决项）、卡住叫人
- [ ] 开放任务的停止条件是「连续 2 轮无去重新发现」，不是无限循环
- [ ] 图中每条边都说得出传递的变量；说不出的边已删除或改并行
- [ ] 每个节点都有四行契约；不做判断/决策/评估/总结的节点用的是代码而非模型
- [ ] 失败都按预设处置表处理，只退回单个单元且附失败测试＋证据＋范围
- [ ] 同一单元修复满 3 次已升级为计划问题，没有继续原地重试
- [ ] 所有不可逆操作（迁移/删除/生产写入/付款）都留了人工签字点；可回滚操作没有多余的人工门
- [ ] 已修复的失败成因已写成规则回灌

## 边界与风险

- 作者的现成提示词未取回（在评论区），本文件只有方法与结构件，没有提示词原文
- 文中 31 分钟 → 17 分钟的链式改扇出对比是作者自注的示意计时（原文自标 ILLUSTRATIVE TIMINGS），不是实测数据，不要当性能承诺引用
- Karpathy 发布 autoresearch、「Opus 5.5」型号名、Bun 移植数字（约 75 万行 Rust、11 天、测试通过率 99.8%，原文自带 Reportedly）、Claude Code 动态工作流子 agent 上限、LangGraph 1.0 等均为作者陈述，未独立核查
- 证据分级的前提是任务有客观检查手段；纯主观质量任务上这套方法的收益有限

## 出处

- 小本本第 307 条；vault 笔记《Loops & Graphs：只批最后一步的 Agent 编排法笔记》
- 原帖：https://x.com/HoodieFade_/status/2118010863038746652（英文长文约 8,200 字，含 76 个内容块与 MARKDOWN 实体，方法全文已取回）
