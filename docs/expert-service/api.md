# HTTP接口与错误契约

0.1.0 · **设计草案，尚无运行端点。** [OpenAPI](openapi.json)是字段类型、必填项和枚举的机器契约；本文补充跨字段及事务语义。示例域名 `expert-service.invalid` 不可调用。[示例数据](examples.json)全部为合成文档夹具，不是执行回执。

## 1. 通用约定

HTTPS，`Authorization: Bearer <项目凭据>`，JSON请求使用 `Content-Type: application/json`。认证结果绑定项目，不能通过payload切换项目。部署配置向调用项目提供获准的 `knowledge_release_id` 和预导入素材ID；首版不开发目录搜索或上传端点。

所有字段默认不允许额外键；空字符串、越界数组按schema拒绝。请求体上限256 KiB，超限413；JSON不可解析400，能解析但不满足schema／跨字段约束422。时间使用带时区的RFC3339字符串，服务返回UTC。ID不等于文件路径。本人项目内已清理内容返回410 `content_expired`，GET任务、追溯、制品及幂等重放均遵守；仍保留的去内容墓碑仅用于阻止重复执行，不能返回一个缺result的伪completed。跨项目或从未存在的ID继续404。

错误使用[Problem Details RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html)的 `application/problem+json`，稳定机器码放 `code`；不把堆栈或凭据放detail。

OpenAPI固定[3.1.1](https://spec.openapis.org/oas/v3.1.1.html)，并不声称这是最新版本。JSON Schema语法静态可校验，不能据此宣称实现已兼容。API不依赖客户端识别中文错误文案，依赖HTTP码及code。

## 2. 操作表

| 操作 | 成功响应 | 前置条件／作用 |
|---|---|---|
| `POST /v1/consultations` | 202＋Consultation＋Location＋ETag | Idempotency-Key必填；原子持久创建任务 |
| `GET /v1/consultations/{id}` | 200＋Consultation＋ETag | 只读；返回最新已提交revision；不存在或跨项目404 |
| `POST /v1/consultations/{id}/answers` | 202＋Consultation＋ETag | 幂等键、If-Match；仅needs_input，答全当前问题后queued |
| `POST /v1/consultations/{id}/cancel` | 200＋Consultation＋ETag | 幂等键、If-Match；取消排队、执行或等待中的任务 |
| `GET /v1/consultations/{id}/provenance` | 200＋Provenance | 返回已持久的追溯快照；尚无追溯409 |
| `GET /v1/artifacts/{artifact_id}` | 200＋Artifact | 项目归属检查；仅提供文本／JSON执行制品，不支持任意路径 |

每次状态或可见内容改变，revision单调加一；ETag为带双引号的 `"r3"`。provenance含对应任务revision，GET获取期间任务可能继续推进；调用者需要同一终态快照时先读终态再查其追溯。终态的已发生用量若后续补回提供商回执，可以增加revision更新usage与追溯，不改执行状态或原意见；历史版本保留在事件及制品中。

## 3. 创建请求

`task`明确问题、输出要求和任务类型；`context`包含范围、材料ID、已定事实；`hard_constraints`每项有稳定ID，`preferences`仅是偏好。约束ID须唯一，required/excluded方法不得相交。parent_id若存在，必须属于同项目；父任务只提供关联，不隐式继承私有上下文，重做时需显式传完整输入。

`knowledge_release_id`必须精确匹配已发布可用清单；未知返回404。方法ID无效、所需材料不存在／无权访问返回404。方法存在但不具备本题资格，由咨询返回 `insufficient_evidence`，不能伪造成网络失败。required方法必须都得到适用性评估；如不合格，说明缺口而不是换一个名字继续。

`limits`三个数值必填，服务不擅自加预算。实际选择模式在result.actual_mode与provenance记录；尚未执行任何方法而直接判断输入／能力不足时为not_executed。deliberation预算不足的业务结果为completed＋insufficient_evidence，记录所需最小预算；单纯工作队列拥塞返回429或等待，不提高调用预算。

请求示意见examples的 `create-world`。创作类调用仍使用同接口，但scope必须含作品阶段／媒介，且硬约束明确原创角色身份、身体与输出布局；artifact_review必须提供服务有权访问且可由获准执行器读取的素材ID。不支持的二进制视觉材料应给出缺口，不假装已经看图。

## 4. 幂等与并发

幂等作用域为认证项目＋方法＋路径＋Idempotency-Key。请求摘要用确定性JSON编码（按键排序、保留数组顺序、统一UTF-8）绑定body；answers/cancel再绑定原If-Match值。JSON对象键次序不同视为同请求，列表次序不同视为不同请求。

同key同摘要重放先于If-Match校验：内容仍在时返回同一资源的当前快照和该操作原成功HTTP码；内容已清理则410且绝不重新执行；即使后续revision已变，也不再次执行业务步骤。Location指同一咨询，ETag反映当前revision，客户端不能假定重放时仍queued。新key却带旧If-Match报412；相同key不同摘要报409。并发同key须靠数据库唯一约束与事务合并，不能只靠进程内缓存。

If-Match缺失报428，格式错误422，版本不符412；版本相符但状态不允许该操作报409。完成与取消竞争按先提交事务决定。已cancelled使用新key再次取消返回200当前资源，但仍需当前If-Match；completed／partial／failed不可取消，返回409。无论重试多少次，都不得多调用一次模型。

## 5. 澄清、终态与追溯

needs_input包含1–5个带ID的问题和提问理由；answers中的question_id必须唯一且恰好覆盖当前列表，不接受未提出的问题，不把补充答案当改题指令。答案可以明确“未知”；服务随后返回条件意见或不足，避免无限追问。每任务最多两次澄清循环，deadline不延长；到上限仍缺关键条件时completed＋insufficient_evidence，流程未完成却已到deadline则partial或failed。

completed和partial必须有result及追溯；partial仅允许conditional／insufficient_evidence。queued／running／needs_input／failed／cancelled的result为null，避免把半成品当意见。失败的步骤可在追溯中保留，但不提升为最终建议。failed必须带failure；其他终态的中止原因也可放failure。非needs_input状态questions为空。

每个hard_constraint在result.constraint_checks中恰好出现一次。answered仅当全部必要约束已核对且没有阻断未知时允许；冲突或关键未知必须conditional／insufficient_evidence。source_summary主张必须有至少一个可解析、可访问且支持该主张的evidence_ref。所有引用须属于同次追溯可见集合，不能只检查字符串形状。每个SelectedMethod的critical_item_ids必须与映射中的ID集合一一相同，不能重复或遗漏。preserved/adapted必须定位实际请求；not_used允许请求引用及位置为null，但必须说明不适用理由和impact，不得伪造请求位置。源定位和映射的请求制品必须可访问并真实存在。

原始数据不足时宁可列next_checks，不编造数值或提供商用量。

provenance列选用方法、包digest、scope、实际必读文件、关键项到最终请求的映射、模型步骤、证据位置、独立性限制和缺失材料。Artifact.content为UTF-8文本字符串，digest以该字符串UTF-8字节计算；JSON制品以序列化文本存入，客户端需要再解析。制品ID不包含磁盘路径，正文不含凭据。公开知识也须以本项目获准release或材料引用访问，不能由ID猜测越权读取。

## 6. 错误码

| HTTP | code示例 | 客户端处理 |
|---|---|---|
| 400 | invalid_json / missing_idempotency_key | 修正请求；没有任务创建 |
| 401 | authentication_required | 修正凭据，不重放未经授权的材料 |
| 404 | resource_not_found | 检查当前项目的ID，不暴露他项目存在性 |
| 409 | idempotency_conflict / invalid_state / provenance_not_ready | 读取当前资源；改任务需新key和新咨询 |
| 410 | content_expired | 内容已清理；同key不会重新执行，要新任务须明确用新key提交完整输入 |
| 412 | revision_mismatch | GET最新ETag后重新决定是否操作，不盲目覆盖 |
| 413 | payload_too_large | 缩小文本或使用预导入材料ID |
| 422 | schema_invalid / constraint_ids_duplicate / selection_conflict / answers_mismatch | 修正类型或业务约束 |
| 428 | precondition_required | 补If-Match |
| 429 | rate_limited | 遵守Retry-After；已成功创建的任务继续GET |
| 503 | service_unavailable | 创建结果不确定时必须同key重试，不能换key制造重复 |

500作为未预期内部错误统一Problem返回；不把响应体当可重试依据。所有操作可能返回500，其他允许码以OpenAPI各操作为准。已持久任务内部模型失败通过任务终态/failure表达，GET本身仍200；不能把“专家材料不足”误报HTTP500。HTTP503不证明付费模型已调用或未调用。

## 7. 两条完整调用流程

正常：POST带key→202 queued→GET running→GET completed＋conditional→GET provenance→读取必要artifact→项目决定是否采纳。所有状态与回答范例都是合成说明，未连接后端。

需澄清：GET needs_input和ETag→POST answers带新key及该ETag→202 queued→继续轮询；请求掉线时原key原body原If-Match重放。要换世界版本则创建新任务并parent_id关联，必要时取消旧任务；不能编辑已完成意见。
