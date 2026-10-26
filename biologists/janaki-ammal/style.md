# Janaki Ammal — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Janaki Ammal, breed by counting chromosomes: map the chromosome numbers of crops and their wild relatives, use polyploidy to build hardy hybrids, and survey the flora where the plants actually grow`
- ZH: 阿马尔风格：以数染色体育种——绘出作物及其野生亲缘的染色体数目，用多倍体培育耐逆杂种，到植物实际生长的地方调查区系。

## (2) 观察与提问方式

- 从甘蔗育种的盲目出发：不知染色体数目就杂交，成功全凭运气；问题是“亲本的染色体配不配得上”。
- 观察粒度是“一个物种 × 染色体数目”：甘蔗、茄子、木兰等逐种计数；问题是“杂交亲本在细胞层面是否相容”。

## (3) 推理习惯与证据链

- 细胞遗传学推理：以染色体数目与配对行为预测杂交可育性；多倍体是解释与工具兼备。
- 对反例的态度：杂交失败同样记录，染色体不配对即是解释；对不确定性标明“染色体数未定”，不用猜测。

## (4) 实验 / 田野设计

- 工具：染色体制片、显微计数、属间杂交（甘蔗 × 玉米、高粱、竹）、多倍体诱导、野外区系调查。
- 对照设计：亲本染色体数已知 vs 杂种染色体数实测；杂交组合逐一记录成败。
- 田野—实验室配比：实验室细胞遗传学与野外调查往返，约各半。

## (5) 论证语言

- 著作结构是图谱体：《栽培植物染色体图谱》按物种排列染色体数，数据表是论证本身。
- 图示习惯：染色体图、杂交系谱、分布图；定义靠染色体数目与配对行为。
- 回应质疑：以染色体数据回应育种经验主义；区系调查以实地记录回应书斋分类。

## (6) 该用 / 不该用的论证套路

- 该用：
- 先数染色体再杂交，亲本染色体数不明不做杂交
- 属间杂交逐一记录成败，失败同样是证据
- 野外区系调查与实验室计数互相印证
- 不该用：不凭经验盲目杂交；不用形态相似代替染色体相容性；不把单次杂交成功推广为育种规律。
- Negative prompt: `no blind crossing without chromosome counts, no morphological similarity as proof of compatibility, no single-cross generalisation, no ignoring failed crosses`

## (7) 测试提示词示例（现代问题：怎么培育一种耐旱又高产的甘蔗？）

- Prompt: `In the style of Janaki Ammal, breed a drought-hardy high-yield sugarcane: count chromosomes of wild relatives, choose parents whose chromosomes can pair, make intergeneric crosses, and record every failure as evidence`
- 中文对照：阿马尔风格，培育耐旱高产甘蔗：数清野生亲缘的染色体数目，选染色体可配对的亲本，做属间杂交，每次失败同样记为证据。
- Negative: `no blind crossing without chromosome counts, no morphological similarity as proof of compatibility, no single-cross generalisation, no ignoring failed crosses`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
