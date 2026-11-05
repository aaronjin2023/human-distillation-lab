# 摄影物理语言八维人像专家（专家模式）

- 领域：图像设计
- 来源：AYi（@AYi_AInotes）原帖，经 Soran（@Soranlan）转发实测，收录于西瓜小本本第 257 条；vault 笔记《八维人像提示词：AYi 摄影物理语言框架笔记》
- 核验状态：框架本体与逐维英文词例在原帖正文、自带可直接拼用；Soran 的三组样例经逐张看过，皮肤质感、光影与抓拍感与框架主张互证；完整英文 Prompt 在原帖一楼回复、未取回；作者资历为自述，未独立核实
- 适用：写 AI 人像提示词时治「油腻塑料感、假人味」——把空泛形容词系统性换成真实摄影与物理语言

## 定位

这个专家的诊断只有一条：人像出油、出塑料感，病根在用评价性形容词（漂亮、高级、自然）约束模型。对策是八个维度逐维改写成可落地的摄影/物理描述——人设用阶层气质锚、质感用面料名与垂坠、表情用瞬间情绪、相机感用焦段光圈颗粒、皮肤用方向光加毛孔保留、环境用散焦层次、审美下限用克制词组、最后负面词成串封口。每个维度都不许出现评价性形容词。

## 何时用 / 何时不用

- 用：真人感人像生图（单人肖像、时尚编辑风、生活抓拍风），出图有塑料感、磨皮感、CG 感时按八维逐维排查改写。
- 不用：单点极端特化（如唇部微距）用面部极限微距公式（小本本第 209 条）更专，本条是全维框架、与之互补；动漫/插画风人像的物理语言体系不同，不要硬套真人摄影词。

## 方法步骤

1. **定人设（维度①）**：用年龄＋族裔＋阶层气质锚＋题材定位写人物，如 `25-year-old East Asian woman, old-money relaxed elegance, editorial fashion portrait`——不写「美女」「高级感」。
2. **写质感（维度②）**：用面料名与垂坠的物理状态替代直白形容，如 `raw silk, fitted merino knit, subtle collarbone shadow, tailored silhouette`。
3. **定表情（维度③）**：指定瞬间情绪与「未察觉镜头」状态消死鱼眼，如 `candid moment, soft knowing glance, caught mid-reaction, unaware of the camera`。
4. **给相机感（维度④）**：用焦段、光圈、景深、颗粒与光学压缩写镜头，如 `85mm portrait lens, f/1.8 shallow depth of field, subtle film grain, natural optical compression`。
5. **雕皮肤（维度⑤）**：方向性柔光＋轮廓光＋明确保留毛孔与真实纹理，如 `soft diffuse directional light, gentle rim light, authentic skin texture with visible pores and natural highlights`。
6. **托环境（维度⑥）**：用散焦层次与氛围把主体托出，如 `soft morning cafe ambiance, muted warm background bokeh, natural depth`。
7. **卡审美下限（维度⑦）**：用克制词组封住下限，如 `classy, effortless beauty, understated luxury, natural proportions`。
8. **负面封口（维度⑧）**：工业级负面词成串写满，如 `no plastic skin, no doll face, no extra limbs, no 3D render look, no over-smoothed texture`。
9. **自检**：逐维回读，全文不得残留评价性形容词（漂亮/高级/自然/精致等）；缺哪维补哪维，不要靠加长某一维代替补维。

## 提示词与模板

八维拼装顺序（一句一段，词例可直接抄用，替换为自己的题材变量）：

```text
[人设] <年龄 + 族裔 + 阶层气质锚>, editorial fashion portrait
[质感] <面料名>, <垂坠/剪裁物理描述>, subtle collarbone shadow, tailored silhouette
[表情] candid moment, <瞬间情绪>, caught mid-reaction, unaware of the camera
[相机] 85mm portrait lens, f/1.8 shallow depth of field, subtle film grain, natural optical compression
[皮肤] soft diffuse directional light, gentle rim light, authentic skin texture with visible pores and natural highlights
[环境] <场景氛围>, muted warm background bokeh, natural depth
[下限] classy, effortless beauty, understated luxury, natural proportions
[负面] no plastic skin, no doll face, no extra limbs, no 3D render look, no over-smoothed texture
```

注：作者拼好的完整英文 Prompt 放在原帖一楼回复，未取回；上表为按原帖正文八维与词例的拼装结构，词例本身均为原帖原文。

## 验收标准

- [ ] 八维齐全，无缺维（尤其⑤毛孔保留与⑧负面封口最常漏）
- [ ] 全文无评价性形容词残留（漂亮/高级/自然/精致/美女等），每个维度都是摄影或物理描述
- [ ] 表情是「瞬间状态」而非静态摆拍词（有 caught mid-reaction / unaware of the camera 一类）
- [ ] 相机参数成套（焦段＋光圈＋颗粒＋压缩），不是孤零零一个 85mm
- [ ] 皮肤维度同时有光的方向与「visible pores」保留项
- [ ] 出图检查：无塑料皮、无娃娃脸、无过度磨皮、无 3D 渲染感；有问题先定位是哪一维缺失再改词

## 边界与风险

- 完整英文 Prompt 未取回（在原帖一楼回复），本专家给的是框架＋原帖词例的拼装法，不是作者原稿全文；作者后续若公开全文，应以原文替换拼装结构。
- 原帖后半段嵌有 Flatkey API 中转站植入推广（厂商话术，与方法无关），引用原帖时不要把推广内容当方法证据。
- 作者自述「资深/10 年人像摄影经验」不可核；帖中「开源」是修辞，无实际仓库；效果旁证来自 Soran 转发样例（含其水印的 2×2 拼图及 2026-11-04 补记的绿皮车题材四联），属转发实测口径，非第三方独立评测。

## 出处

- 小本本第 257 条；vault 笔记《八维人像提示词：AYi 摄影物理语言框架笔记》；原帖（Soran 转发帖）https://x.com/soranlan/status/2117518164900930026
- 关系条目：面部极限微距生图公式（小本本第 209 条，单点特化，与本条全维框架互补）
