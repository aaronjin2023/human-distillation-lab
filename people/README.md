# 专家基本资料与选择

2026-10-29为全库专家分类条目统一增加 `biography.md`、`manifest.json.biography` 及[完整检索索引](biographical-index.json)。检索索引只保存筛选所需摘要，完整日期声明、来源和冲突通过各行 `details` 指向专家元数据。原[跨目录人工关联](index.json)保持原覆盖范围，不把同名或自动候选直接合并成一个人。条目数包含同人不同专业面向及少量集合体。

## 字段与证据状态

| 字段 | 含义 | 选择时的边界 |
|---|---|---|
| `identity`、`entity_kind` | 公开人物关联及个人/集合体类型 | 身份不明确时不自动移入外部人物的地理属性 |
| `life.original_text` | 旧资料的生卒或活动年代原文 | 保留原始说法，不把活动世纪当出生年 |
| `life.birth_year`、`death_year` | 年份、证据状态、声明及冲突 | 公元前年份为负，无零年；近似、年代粒度不足与不相容说法不转成精确筛选值 |
| `life.activity_period` | 活动年代的原始文字 | 生卒不详时仍保留年代线索；目前未统一转为区间 |
| `birth_places` | 出生地点 | 不等于主要创作地点、国籍或民族 |
| `work_locations` | 有来源的工作/研究地点 | Wikidata P937覆盖稀疏，空值不表示没有跨地域经历 |
| `citizenships` | 来源声明的国籍或历史政治归属 | 不把现代国家边界强加给古人；时段限定保留在qualifiers |
| `ethnicity.documented` | 本轮核读明确传记/自述所载民族或文化认同 | 可含多个身份；“非裔美国人”等文化身份与中国民族分类不是统一的生物学分类 |
| `ethnicity.unreviewed_source_claims` | Wikidata所载、未核读底层出处的声明 | 仅显示待核，不进入默认民族筛选 |

`documented` 表示本轮读取了明确支持该字段的公开来源；`source_recorded` 表示公开结构化来源载有该说法，未逐一独立核验；`legacy_unverified` 是仅承接旧资料；`unknown` 是未知或无法形成精确值；`conflict` 是相互冲突。没有记录死亡不能证明仍在世，旧 `living_person` 仅保留作待更新背景。已选择较明确传记的日期仍保留 `other_source_claims`，不隐藏异说。

基础批量来源为 [Wikidata公开数据接口](https://www.wikidata.org/wiki/Wikidata:Data_access)；具体修订、原始日期、历法、声明ID、来源引用与时段限定冻结在 [biography-sources.json](biography-sources.json)。不复制完整网页或私人资料。民族的公开声明要求参见 [P172定义](https://www.wikidata.org/wiki/Property:P172)；本库不会根据姓名、出生地、国籍、宗教或外貌代填民族。

自动身份候选要求规范化主姓名与至少一个无冲突旧年份相合；仅中文短名命中不足以关联。新增专家及此前新增的医学/历史/政治包另作姓名和专业语境复核。Catherine Bell演员、Will Wright消歧页等错误候选已排除；宗教学者Bell的出生年采用大学档案1953，同时保留Wikidata的1952说法。集合体不会继承锚点人物的生卒、出生地或民族。

## 当前覆盖

- 全库 **3684** 个专家分类条目已具有相同基本资料结构、独立文档和入口链接。
- **2961** 个条目具有已接受的公开人物实体关联；这不是去重人数，也不等于所有传记事实已核实。
- 出生地有来源记录 **2906** 条、工作地 **737** 条、国籍/历史政治归属 **2867** 条。
- 民族/文化认同：明确来源已采纳 **8** 条，公开结构化声明待核 **228** 条，其余 **3448** 条保留未知。

完整统计见[覆盖回执](biographical-coverage.json)，本轮检查见[验证回执](verification.json)。字段齐备与事实齐备不同；未解析人物和缺失字段已逐条保留，不宣称全库传记核验完成。

## 组合与查询

例如要研究十九世纪欧洲的货币制度，应先找经济学方法，再检查年代、实际研究地域与代表作；不要把民族当作思想立场的代理。未来工作台读取领域的 `activation` 和条目的 `biography` 即可，本轮只提供文档、结构化资料及离线查询，不开发工作台。

在仓库根目录运行：

```sh
python3 scripts/build_expert_biographies.py search --domain economics
python3 scripts/build_expert_biographies.py search --domain climatology --born-after 1900
python3 scripts/build_expert_biographies.py search --region 日本 --region-kind work_locations
python3 scripts/build_expert_biographies.py search --ethnicity 满族
```

参数组合为“且”；日期边界含端点，仅接受 `source_recorded` 或 `documented` 的精确出生年，未知不会当作匹配。地域是中英文标签的子串检索，可分别选出生地、工作地或国籍；默认 `any` 查三者并返回原字段，不能把结果当同一概念。当前没有地点层级展开或历史疆界推理，查“德国”不会自动覆盖所有只写“柏林”的工作地。这是资料筛选工具，不是完整历史地理检索引擎。

## 维护

修改明确核读的传记依据写入 [biography-overrides.json](biography-overrides.json)，保留来源ID；显式null表示撤销不可靠日期，省略字段表示保持来源记录。更改身份关联或公开快照时保留修订与复核理由，不直接手改生成的基本资料文档或检索索引。

```sh
python3 scripts/build_expert_biographies.py self-test
python3 scripts/build_expert_biographies.py build
python3 scripts/build_expert_biographies.py validate
python3 scripts/validate_experts.py
```

重建完全离线；不会重新访问外网或把旧快照冒充实时状态。自检覆盖公元前、重名、日期冲突、模糊精度、集合体、显式未知覆盖和民族筛选边界。
