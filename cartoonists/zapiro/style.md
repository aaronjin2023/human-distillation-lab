# Zapiro — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zapiro, South African editorial cartoon, bold caricature, Mandela and politicians, one panel one punchline`
- ZH: 扎皮罗风格：南非社论漫画，大胆漫画化，曼德拉与政客，一幅一点题。

## (2) 线条、网点/色彩

- 线条：大胆的漫画化线条，轮廓夸张有力；政客面容漫画化，一笔可认。`impression`
- 色彩：黑白与彩色并行；彩色版平涂明快。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：单幅社论漫画为主，一幅一点题；标题文字点题。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：曼德拉——微笑、慈祥；政客漫画化，体型与面容对照；人物表情夸张。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：少用对话框；多在画下配一句点题文字；拟声词小。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：曼德拉的微笑：曼德拉形象、南非政客：漫画化的政客、种族隔离与后种族隔离南非、社论漫画：紧贴时局、南非日常：街头与议会、一幅一点题。`verbatim`
- 不该画：No gentle poetic blank space、No photorealistic detail、No ornate decoration、No wordless ambiguity。`impression`
- Negative prompt: `No gentle poetic blank space, No photorealistic detail, No ornate decoration, No wordless ambiguity`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Zapiro, a small Yorkshire terrier sitting on a subway seat, South African editorial cartoon, bold caricature, one panel one punchline`
- 中文对照：扎皮罗风格：一只小约克夏犬坐在地铁座位上，南非社论漫画，大胆漫画化，一幅一点题。
- Negative: `No gentle poetic blank space, no photorealistic detail, no ornate decoration, no wordless ambiguity`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
