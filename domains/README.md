# 医学、历史、教育与政治方法

2026-10-28检查本地仓库后建立这四个领域入口。既有人物保留原路径与专业范围，新增条目继续采用九文件接口；同名人物跨领域时关联，不覆盖原面向。

| 领域 | 本轮复用入口 | 新增方法条目 | 入口 |
|---|---:|---:|---|
| 医学 | 20 | 4 | [医学目录](medicine.md) |
| 历史 | 6 | 6 | [历史目录](history.md) |
| 教育 | 100 | 0 | [教育目录](education.md) |
| 政治 | 20 | 12 | [政治目录](politics.md) |

复用数量是本轮核对并选取的入口，不代表全库只有这些相关人物，也不是全库去重人数。教育区100份草稿均有九类非空文件；部分旧名单仍写“待确认”，这里按实际文件存在状态记录，不把草稿升级成已验收。

## 新增范围

医学补充Sackett的循证决策、Cochrane的有效性与资源问题、Bradford Hill的因果推理、Apgar的标准化观察。提取公开成果和方法，不建立诊疗、用药或个人健康评分服务。历史医学观点与现行临床建议分开。

历史补充修昔底德、司马光、班固、布洛赫、布罗代尔和陈寅恪的史学方法。司马光原有园林条目保持原样，新增条目仅讨论历史研究与编纂。原作、作者归属、后世研究与本库应用推演分别记录。

政治补充12份方法包，覆盖改革、执行、议事、外交、危机解释、宪政与社会政策。20个旧入口只是相关专业面向，思想家也不自动等于实际执政者。王安石、张居正、孙中山、安贝德卡尔、埃莉诺·罗斯福的新包通过`legacy_refs`关联同人旧条目，不复制旧来源作为新的独立证据。演说证明公开主张，政策成效仍需结果资料；争议、失败与权利代价保留在各自`conflicts.md`。

| 需要分析的问题 | 新包 |
|---|---|
| 制度改革、执行责任与试点纠错 | [王安石](../politicians/wang-anshi/SKILL.md)、[张居正](../politicians/zhang-juzheng/SKILL.md)、[邓小平](../politicians/deng-xiaoping/SKILL.md) |
| 议事能力、权力交接与宪政平等 | [孙中山](../politicians/sun-yat-sen/SKILL.md)、[安贝德卡尔](../politicians/b-r-ambedkar/SKILL.md) |
| 多边合作、共同文本与冲突转型 | [周恩来](../politicians/zhou-enlai/SKILL.md)、[埃莉诺·罗斯福](../politicians/eleanor-roosevelt/SKILL.md)、[曼德拉](../politicians/nelson-mandela/SKILL.md) |
| 危机决策的权限、范围与公共解释 | [林肯](../politicians/abraham-lincoln/SKILL.md)、[富兰克林·罗斯福](../politicians/franklin-d-roosevelt/SKILL.md) |
| 多元社会治理与保障政策的覆盖成本 | [李光耀](../politicians/lee-kuan-yew/SKILL.md)、[俾斯麦](../politicians/otto-von-bismarck/SKILL.md) |

每个新增目录包含`SKILL.md`、`style.md`、`process.md`、`technique.md`、`language.md`、`motifs.md`、`decisions.md`、`conflicts.md`、`manifest.json`。正文给出方法、具体步骤与反例；元数据记录可追溯来源、实际访问范围、材料条件和缺口。

## 使用与维护

从目录选一个与问题相符的专家条目，再按需结合[人格与行为组合指南](../docs/composition-guide.md)。专家声望不替代证据，既有文学/地理侧面的条目也不自动提供全部史学或医学能力。

机器索引为[index.json](index.json)。`python3 scripts/validate_experts.py`检查全部168个入口的九文件完整性及22个新增包的元数据、引用和链接。使用`--write-catalog`重建四个目录；`--self-test`检查错误来源、范围和人物在世状态能否被拒绝。旧条目史实、引文与效果未在本轮全面复核。数量均为条目数，跨领域同人不等于多位独立专家。
