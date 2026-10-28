# 人格、个性与个体差异资料

本区蒸馏公开测评框架的概念、使用方法、解释边界和组合方式。当前对象是框架，不是某个真人；这里没有真人测评结果。

行为、思考、文化和身体情境等扩展见[人类行为与差异区](../human-patterns/README.md)，共同选用方法见[跨层组合指南](../docs/composition-guide.md)。

## 结构与使用

- `frameworks/<id>/SKILL.md`：按任务选择并加载的技能入口。
- `frameworks/<id>/framework.md`：维度解释、操作方法、限制与来源。
- `frameworks/<id>/manifest.json`：类别、来源、材料使用条件、版本和已知缺口。
- `catalog.json`：全量框架目录；由 `../scripts/validate_library.py --write-catalog` 从 manifest 生成。
- `../people/index.json`：已人工核对的人物关联，未收录的人物继续使用原专家条目路径。
- `../profiles/`：把专家方法与框架组合的具体使用配方。

当前是同库增量扩展：原 36 类专家目录保持路径和内容，原条目的“只蒸作品”范围继续有效。人格框架及后续行为资料采用本区单独声明的来源与范围。

先按问题选择框架，再读该框架入口；不要一次装载全部框架，也不要把多个量表分数直接相加、互换或统一成“人格总分”。模型、测量工具、类型理论、职业兴趣、动机、价值观和关系维度分别登记。

## 蒸馏与证据

本区采用 immortal-skill / steamer-skill 的来源追踪、分维度提取和冲突保留方法，按本任务调整为“框架蒸馏”，不生成虚构的人物经历或私人记忆。

- 每条框架事实引用官方/作者/原始研究来源 ID。开发者的效度主张标为开发者材料，不冒充独立验证。
- `verbatim` 是可定位的短引文；`artifact` 是对已查阅文档的改写；`impression` 是未验证解释。证据形式不等于研究质量，直接引文也不自动更可靠。
- 本库编写的角色行为规则统一标为“设计推演”；它不是正式量表的评分规则，也不是对真人的测量结论。
- 不同版本、情境、时期的结论分别保留；不以“更新日期较晚”自动推翻更相关的研究。
- 官方量表、开放条目库与仅供介绍的框架分别记录材料使用条件。当前只保存原创摘要及来源链接，不复制商业题库、评分密钥或整套受限问卷。
- 框架名称与译名仅用于识别。这里的中文解释不是经验证的中文版量表，不使用模型生成的数字冒充常模分数或测评结果。

## 新条目格式

每个框架仅需 `SKILL.md`、`framework.md`、`manifest.json` 三个文件。SKILL 使用 YAML frontmatter（name 与目录 id 一致、description 清楚），正文保持简短并链接其余两文件。

manifest 共同字段：

```json
{
  "id": "example",
  "name": "框架名称",
  "kind": "trait-model",
  "version": "0.1.0",
  "updated_at": "2026-10-28",
  "status": "source-grounded-draft",
  "scope": "框架摘要，不是测评服务或真人画像",
  "dimensions": [{"id": "dimension-id", "name": "维度", "description": "含义"}],
  "sources": [{"id": "S1", "title": "来源标题", "url": "https://example.org/", "publisher": "作者或机构", "source_type": "author", "accessed_at": "2026-10-28", "supports": ["维度定义"]}],
  "rights": {"summary": "来源材料使用条件及尚未确认事项", "item_reproduction": "not-included", "source_ids": ["S1"]},
  "known_gaps": ["尚未完成的核验"],
  "distillation_method": "公开来源改写；参考 immortal-skill 与 steamer-skill；设计推演另标"
}
```

`kind` 可取 `trait-model`、`trait-instrument`、`item-bank`、`type-framework`、`behavior-framework`、`strengths-framework`、`values-framework`、`interest-framework`、`relationship-framework`、`motivation-framework`。来源类型可取 `author`、`official`、`primary-study`、`publisher`、`government`。

`framework.md` 应包含维度及含义、实际使用步骤、如何与专家能力结合、至少一个自检情景、研究/版本限制、材料使用条件和带 ID 的直接来源链接。自检须验证行为边界，例如材料不足时拒绝断定类型，不是验证标题存在。

## 扩展到真人时

需要另行定义对象、材料范围和具体用途；每项行为判断记录来源、情境、时期、反例以及观察/推断。未知结果保持未知，不能由作品风格、职业或姓名推测真人的 MBTI、心理健康等属性。真人档案与合成角色分别标记。
