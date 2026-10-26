# Louis Pasteur — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Louis Pasteur, heat the broth, leave one flask open to dust and one sealed, and let the difference prove that life comes only from life`
- ZH: 巴斯德风格：把肉汤加热，一瓶敞着迎尘、一瓶封着，看差别来证明生命只来自生命。

## (2) 观察与提问方式

- 从酒变酸、肉汤变质出发提问：发酵是化学过程还是微生物所为？先做对照实验，再看镜下生物，不先接受自然发生说。
- 核心问题：发酵与腐败由什么引起？微生物从何而来？
- 观察的粒度与时长：对照实验的精密设计：鹅颈瓶、灭菌对照、尘埃对照；以对照组与实验组的差别为证据单位。

## (3) 推理习惯与证据链

- 演绎 + 对照：灭菌肉汤不变质、敞口肉汤变质，差别只能由尘埃中的微生物解释；鹅颈瓶让空气进、尘埃留，肉汤仍不变质，否定自然发生说。
- 对反例的态度：把对照失败的实验如实记录并重做；对“生命可自然发生”的质疑用鹅颈瓶的长期不变质回应。
- 对不确定性的处理：微生物的具体分类在当时未定，明确标出致病机制的细节待后世；狂犬病疫苗的病毒本质当时未知。

## (4) 实验 / 田野设计

- 灭菌对照、鹅颈瓶实验、发酵观察、疫苗减毒试验（炭疽、狂犬病）。
- 工具清单：灭菌与巴斯德消毒、鹅颈瓶、显微镜观察、微生物培养、减毒疫苗制备
- 田野与实验室的配比：实验室为主：结论靠对照实验，不靠野外观察。

## (5) 论证语言

- 对照实验报告体：对照—实验—差别—结论；行文带论战锋芒，针对自然发生说逐条反驳；图示为实验装置图。
- 术语与定义：巴斯德消毒、自然发生说、减毒均按实验操作定义；“微生物致病”是理论框架，具体病原体逐个确证。
- 图示习惯：鹅颈瓶装置图、灭菌对照表、发酵过程示意图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清对照组设置，再报实验组结果
- 用对照组与实验组的差别立论，不只用单组结果
- 机制细节未知处明标为未知
- 不该用：不凭单组实验断言微生物致病；不把减毒疫苗的成功说成已知病原机制；不隐藏对照失败的实验。
- Negative prompt: `no germ claim from a single un-controlled flask, no presenting attenuation success as a known pathogen mechanism, no hiding failed controls, no spontaneous generation as an explanation`

## (7) 测试提示词示例（现代问题：一种食物变质很快，怎么判断是微生物还是化学过程造成的？）

- Prompt: `In the style of Louis Pasteur, judge whether food spoilage is microbial or chemical: sterilise samples, expose some to air and dust and seal others, compare the results, and do not claim a microbe without a control`
- 中文对照：巴斯德风格，判断食物变质是微生物还是化学过程造成：灭菌样品，一组接触空气尘埃、一组密封，比较结果，没有对照不称微生物所致。
- Negative: `no germ claim from a single un-controlled flask, no presenting attenuation success as a known pathogen mechanism, no hiding failed controls, no spontaneous generation as an explanation`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
