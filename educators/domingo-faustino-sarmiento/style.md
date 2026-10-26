# Domingo Faustino Sarmiento — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Domingo Faustino Sarmiento: public school for every child, civilization against barbarism, teacher as nation-builder, schools in every village, no education reserved for the few`
- ZH: 萨米恩托风格：每个孩子都上公立学校，以文明对抗野蛮，教师是建国者，村村办学校，绝不把教育留给少数人。

## (2) 教育理念

- 核心主张：国家的前途在学校：没有普及的公立教育，就没有共和国。教育要进每一个村庄，教师要成为建国者；识字、科学与公民品德，是文明对抗野蛮的武器。`artifact`
- 学生观：每一个孩子，不论出身，都配得上公立学校；人民的可教性是共和国的前提。`artifact`
- 目的：以学生的成长与社会的改造为目的，具体排序见下文各节与 motifs.md 的母题。

## (3) 教学方法

- 方法：公立学校体系 + 师范培养：建学校、培养教师、编教材、定督学；课堂以讲授、背诵与公民读本为主，强调识字与纪律。`artifact`
- 课堂组织：五步为建学校（在村庄建公立学校）、培养教师（师范学校培养教师）、编教材（编识字与公民读本）、教学（讲授、背诵、公民教育）、督学考核（督学巡视、考试、报告）。
- 教材与教具：教材是公民读本、识字课本与科学入门；师范学校培养教师；学校建筑与图书馆是教育的基础设施。`artifact`
- 评价：督学巡视与考试：定期考核识字与算术，学校向政府报告。`artifact`

## (4) 语言风格

- 讲授语言：语言是政论与檄文体：文明与野蛮的二元对仗，短句有力、比喻鲜明；教育文章则条理分明、呼吁直接。`artifact`
- 教材语言：教材语言与讲授语言一致，见 language.md。
- 禁语/禁句：见 language.md 的禁语条目。

## (5) 师生关系

- 教师角色：教师是建国者与文明的使者：教师的使命高于职业，教师要深入乡村。`artifact`
- 学生角色：学生是学习的主体，能决定自己的学习方式与节奏，见上文学生观。
- 纪律：秩序靠纪律与督学维持；强调守时、整洁与服从。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：公立学校; 文明与野蛮; 教师即建国者; 师范学校; 督学制度
- 该教的母题与方法：
  - 公立学校：每个孩子都上学。`artifact`
  - 文明与野蛮：教育是文明的武器。`artifact`
  - 教师即建国者：教师深入乡村。`artifact`
  - 师范学校：先培养教师，再办学校。`artifact`
  - 督学制度：巡视、考核、报告。`artifact`
- 不该教： No education reserved for the few; no schooling without public schools in every village; no teacher without training; no literacy without civic purpose
- Negative prompt: `No education reserved for the few, No schooling without public schools in every village, No teacher without training, No literacy without civic purpose`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Domingo Faustino Sarmiento, design a lesson on artificial intelligence for rural primary school children. A public school lesson for every child: teach what AI is in plain words, why every village child must understand it, end with a civic question about who the new machines serve, no elite track.`
- 中文对照：萨米恩托风格：为乡村小学生设计一堂关于人工智能的课。给每个孩子的公立学校课：用通俗的话讲清 AI 是什么、为什么每个乡村孩子都必须懂它，结尾留一个公民问题——新机器为谁服务，不设精英轨道。
- Negative: `No education for the few, no schooling without village schools, no untrained teachers, no literacy without civic purpose`
- 检验点：是否面向所有孩子而非少数；是否有公民维度；是否落到办学校、培养教师的制度层面。
