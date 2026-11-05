# 方法专家 · 加载入口

本文件是 method-experts 区的路由入口：按任务类型选一个专家模式，加载其 `SKILL.md` 全文作为执行规范。

## 路由表

| 任务 | 加载 |
|---|---|
| 做口播数字人短视频 | [口播数字人短视频工作流](video-production/talking-head-digital-human/SKILL.md) |
| 用 Muse 复刻/生产长视频 | [Muse 长视频流水线](video-production/claude-long-video-pipeline/SKILL.md) |
| 给参考视频写复刻提示词 | [视频复刻提示词结构](video-production/video-replication-prompt/SKILL.md) |
| 拆解对标视频再复刻 | [对标视频五层拆解法](video-production/benchmark-video-teardown/SKILL.md) |
| 高速打斗/动作戏运镜 | [高速打斗运镜拼接法](video-production/high-speed-combat-camera/SKILL.md) |
| 做 AI 漫剧 | [AI 漫剧全流程](video-production/ai-comic-drama-pipeline/SKILL.md) |
| 做 AI 中文短剧 | [AI 中文短剧四段流水线](video-production/chinese-short-drama-pipeline/SKILL.md) |
| 短片生产怕返工 | [短片生产四级关卡法](video-production/short-film-four-gates/SKILL.md) |
| 照片转绘成对开海报 | [对开转绘海报家族](image-design/split-poster-transform/SKILL.md) |
| 真人角色定妆/设定图 | [真人角色定妆四视图](image-design/character-look-sheet/SKILL.md) |
| 短剧角色资产建标 | [人物资产图建标法](image-design/character-asset-sheet/SKILL.md) |
| 写人像生图提示词 | [摄影物理语言八维人像](image-design/eight-dimension-portrait/SKILL.md) |
| 把一种风格变成可复用规则 | [风格拆成数字规则法](image-design/style-to-numbers/SKILL.md) |
| 写代码要整洁门禁 | [ub-mode](agent-engineering/ub-mode/SKILL.md) |
| 长流程 Agent 要审批与去重 | [审批门 + 账本去重法](agent-engineering/approval-gate-ledger/SKILL.md) |
| Agent 干完活要验证 | [Agent 完工验证闭环](agent-engineering/agent-completion-verification/SKILL.md) |
| 设计多步 Agent 编排 | [Loops & Graphs 编排法](agent-engineering/loops-and-graphs/SKILL.md) |
| 让多 Agent 无人值守跑长程任务 | [长程多 Agent 运行时机制](agent-engineering/sapper-multi-agent-runtime/SKILL.md) |
| 长篇/连载生成保持设定一致 | [长篇连载一致性工程](agent-engineering/webnovel-consistency/SKILL.md) |
| 运营小红书账号（生产） | [小红书账号全自动运营](content-operations/xiaohongshu-auto-ops/SKILL.md) |
| 写 X 爆款长帖 | [X 爆款写作引擎](content-operations/x-viral-writing-engine/SKILL.md) |
| 小红书卖虚拟资料 | [小红书虚拟资料运营全流程](content-operations/xiaohongshu-virtual-goods-ops/SKILL.md) |
| 把视频课变成学习笔记 | [视频课转可查证学习笔记法](content-operations/course-to-verifiable-notes/SKILL.md) |
| 自托管盯盘/监控 | [PanWatch 盯盘三段调度](data-research/panwatch-monitoring/SKILL.md) |
| 组专家角色做定时研究 | [专家角色×定时循环研究台](data-research/expert-panel-research-loop/SKILL.md) |
| 拍照数据变结构化分析 | [拍照→识别→结构化→统计→预测管道](data-research/photo-to-structured-pipeline/SKILL.md) |

## 加载纪律

- 一次任务默认一个主专家；组合时主专家管全流程，副专家只供专长段落，并在产出中注明组合来源。
- 专家文件里的「验收标准」是交付门槛，不是建议；过不了就返工或如实报告缺口。
- 文件标注「作者自述，未独立核实」的数字不得当作已核实事实引用。
- 数据与投研组：只做研究、监控、回测与纸面跟踪，不下真实订单。
