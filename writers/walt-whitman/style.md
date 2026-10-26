# Walt Whitman — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Walt Whitman: free verse catalogues, long breathing lines, I and America, the body and the crowd, democratic embrace`
- ZH: 惠特曼风格：自由体目录，长呼吸的行句，我与美国，身体与人群，民主的拥抱。

## (2) 句式与节奏

- 自由体长行，排比目录多；句式如呼吸，长短随气息。
- 节奏：段落长度与章节切分见 technique.md；诗的行断与韵律见 technique.md。

## (3) 词汇与意象

- 常用词域：草叶、身体、道路、群众、美国、海洋；词汇平实而博大。
- 意象：草叶、身体、道路、群众、海洋；日常物即民主的象征。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第一人称「我」即众人；「我」既是诗人，也是美国。
- 结构：目录体：排比铺陈，意象并置；长诗以漫游为线索。
- 对话：诗中基本无人称对话；以呼告（“你”）与独白代对话，诗人直接对读者说话。

## (5) 语气与距离

- 豪迈、亲切；既庄严又家常。

## (6) 该写什么 / 不该写什么

- 该写：草叶（平凡而遍在的生命）、身体（民主的身体）、道路（漫游与美国）、群众（人群即诗）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No rhyme, no irony, no small private lyric, no fixed metre, no cold distance`

## (7) 测试提示词示例（现代题材：一个外卖骑手深夜穿过城市送餐）

- Prompt: `In the style of Walt Whitman, a delivery rider crosses the city late at night. Long breathing lines. A catalogue of streets, of workers, of lights. I celebrate the rider. No rhyme, no irony.`
- 中文对照：惠特曼风格，一个外卖骑手深夜穿过城市送餐。长呼吸的行句。一串街道、工人与灯火的目录。我歌颂骑手。没有押韵，没有反讽。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
