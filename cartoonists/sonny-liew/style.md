# Sonny Liew — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sonny Liew, multiple pastiche cartooning styles in one book, watercolour and ink, a fictional cartoonist's archive spanning 1950s to present Singapore, meta graphic novel page`
- ZH: 孙尼·廖风格，一书多仿古画风，水彩与墨水，虚构漫画家自 1950 年代至今的新加坡档案，元图像小说页。

## (2) 线条、网点/色彩

- 线条：线随仿古对象而变：1950 年代粗线、1970 年代网点、现代细线；同一本书里换七八种线。`verbatim`
- 网点/色彩：水彩柔和，旧报纸黄、褪色红、档案灰；色彩即年代。
- 质感：水彩 + 墨水 + 拼贴旧纸；做旧感，无数码平涂。

## (3) 分镜

- 格数与格形：格数随仿古对象而变：早期四格、后期自由格；档案页、草图、油画并置。
- 节奏：节奏如档案：年代跳接，一页可跨二十年。
- 视线引导：英式左→右阅读；视线被档案标题牵引，先看年代再看画。

## (4) 角色造型

- 造型：陈浩慈（Charlie Chan Hock Chye）：虚构的新加坡漫画家，七十余岁回望一生；马林基机器人：科幻小品主角。
- 角色类型：虚构漫画家、机器人、档案中的新加坡市民；主角是画家，配角是历史。
- 动作：动作随仿古对象而变：早期夸张、后期克制；动态靠风格切换。

## (5) 对话框与拟声词

- 对话框：对话框随年代而变；档案旁白多，作者本人偶尔出镜注解。
- 拟声词：拟声词随仿古对象而变，早期大字、后期极少。
- 文字量：每页文字密度中等，档案旁白与对话并重。

## (6) 该画什么 / 不该画什么

- 该画：虚构漫画家陈浩慈、一书多画风（仿古拼贴）、新加坡 1950 年代至今、马林基机器人、档案与旧报纸、政治与审查（补助金风波）、作者页边注解、漫画史即新加坡史。`verbatim`
- 不该画：不画单一固定画风、不画写实渲染、不画扁平数码色、不画拥挤动作格、不画去历史化的可爱笑话。
- Negative prompt: `No single fixed period style, no photorealistic rendering, no flat vector illustration, no crowded action panels, no apolitical cute gags, no empty minimal backgrounds`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Sonny Liew, a small Yorkshire terrier on a subway seat drawn as a fictional cartoonist's archive page, multiple pastiche styles, watercolour and ink, dated captions from 1950s to present`
- 中文对照：孙尼·廖风格：一只小约克夏犬坐在地铁座位上，画成虚构漫画家的档案页，多仿古画风，水彩与墨水，1950 年代至今的带日期旁白。
- Negative: `No single fixed period style, no photorealistic rendering, no flat vector illustration`
- 检验点：是否一页多画风；水彩是否做旧；档案感是否成立。
