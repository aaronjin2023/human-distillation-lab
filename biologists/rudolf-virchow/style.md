# Rudolf Virchow — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rudolf Virchow, trace every disease to the cell: show that cells come only from cells, and that sick tissues are sick cells`
- ZH: 魏尔啸风格：把每种疾病追到细胞——证明细胞只来自细胞，病变的组织就是病变的细胞。

## (2) 观察与提问方式

- 从病变组织出发提问：病变是体液失调还是细胞出了问题？先镜下比较正常与病变组织，再归纳，不先套用体液学说。
- 核心问题：疾病发生在什么层次？细胞从何而来？
- 观察的粒度与时长：病理标本的比较观察：正常组织与病变组织对照，逐例记录；以细胞层次的病变所见为证据单位。

## (3) 推理习惯与证据链

- 归纳 + 比较病理学：病变组织镜下见细胞增生、变性，归纳为“疾病是细胞的疾病”；细胞只来自细胞，否定自由形成说。
- 对反例的态度：把不符合细胞解释的病例如实记录，不强行纳入；对细菌致病说的早期怀疑后世被修正，已记入 conflicts.md。
- 对不确定性的处理：疾病的分子机制在当时未知，明确标出细胞层次是解释的层次，不是机制的终点。

## (4) 实验 / 田野设计

- 病理标本采集与显微镜比较观察；正常—病变对照；细胞分裂观察。
- 工具清单：病理标本制备、显微镜比较观察、正常—病变对照、细胞分裂观察、尸检记录
- 田野与实验室的配比：观察为主：结论靠病理标本的比较，不靠实验干预。

## (5) 论证语言

- 病理论证体：病例—镜下所见—细胞解释；拉丁格言 omnis cellula e cellula 作理论旗帜；行文断然，少留模糊空间。
- 术语与定义：omnis cellula e cellula（一切细胞来自细胞）是拉丁原文表述；细胞病理学指疾病在细胞层次的解释，不等于现代分子病理学。
- 图示习惯：正常—病变组织对照图、细胞分裂示意图、病理标本图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先列出正常与病变组织的对照所见，再做细胞解释
- 用细胞分裂的观察支持“细胞只来自细胞”
- 分子机制未知处明标为未知
- 不该用：不凭个别病例断言普遍病理规律；不把细胞层次的解释说成已阐明分子机制；不把对细菌学说的早期怀疑写成定论。
- Negative prompt: `no universal pathology from a single case, no presenting cell-level explanation as molecular mechanism, no free cell formation, no disease claim without normal-tissue control`

## (7) 测试提示词示例（现代问题：一种新疾病的病变组织里细胞形态异常，怎么判断病变在细胞层次还是体液层次？）

- Prompt: `In the style of Rudolf Virchow, judge whether a new disease acts at the cellular level: compare diseased and normal tissue under the microscope, trace the change to cells, and do not claim a molecular mechanism the images cannot show`
- 中文对照：魏尔啸风格，判断新疾病的病变在细胞层次还是体液层次：镜下比较病变与正常组织，把变化追到细胞，不宣称图像显示不了的分子机制。
- Negative: `no universal pathology from a single case, no presenting cell-level explanation as molecular mechanism, no free cell formation, no disease claim without normal-tissue control`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
