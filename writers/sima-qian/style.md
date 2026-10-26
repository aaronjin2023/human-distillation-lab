# Sima Qian — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sima Qian: plain vigorous classical prose, biography as drama, dialogue in character voice, terse judgement after the narrative, history written as human fate`
- ZH: 司马迁风格：朴拙雄健的古文，以传记写戏剧，对话见人物性格，叙事之后一笔论断，史笔即人命。

## (2) 句式与节奏

- 散句为主，长短交错；叙事快、议论慢；本纪、世家、列传详略悬殊，详处如特写、略处如速写；“太史公曰”短段收束，如鼓点。`verbatim`

## (3) 词汇与意象

- 词汇：词域：史事、职官、地理、兵刑与日常口语并存；善用口语入传（市井语、方言语），使人物开口即有身份；虚词简省，动词有力。`impression`
- 意象：意象不在景物而在人事：白虹、烈士、游侠、刺客、帝王与布衣的对照；反复意象是“势”与“命”——时势造人，亦压人。`impression`（学界通说）
- 禁词/禁意象：不用骈俪堆砌、不作空泛道德说教、不以华丽辞藻掩盖史实、不写超然的神话抒情。

## (4) 叙事视角与结构

- 视角：全知史家视角，但常潜入人物内心与对话；叙述者时而隐身、时而以“太史公曰”现身作论。`verbatim`
- 结构：纪传体：本纪、表、书、世家、列传互见；一人一传、互见法（甲传详、乙传略）；开头多为家世籍贯，结尾以论赞收束；事件按人物命运组织而非编年平铺。`impression`
- 对话：人物言论以引语与对话场景写入纪传（如《项羽本纪》鸿门宴的对答），对话即史料与性格的证据。

## (5) 语气与距离

- 语气：沉郁、悲悯而克制；对失败者与边缘人物尤多同情；与人物距离近，与权力保持审视的距离。`impression`（《报任安书》自述发愤著书）

## (6) 该写什么 / 不该写什么

- 该写：纪传互见、人物对话、详略悬殊、太史公曰式的短论、命运感。
- 不该写：骈俪空文、道德说教、华丽铺陈、神话抒情。
- Negative prompt: `No parallel-prose ornament, no empty moralising, no florid description, no mythic lyricism`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Sima Qian, a small Yorkshire terrier sits on a subway seat. Write it as a liezhuan biography: origin, one vivid scene in its own voice, the indifference of the crowd, and end with a brief Taishigong-style judgement on fate.`
- 中文对照：司马迁风格：一只约克夏犬坐在地铁座位上。写成列传体：籍贯出身、一场有对话的生动场景、众人的冷漠，结尾以“太史公曰”式短论收束命运。
- Negative: `parallel-prose ornament, empty moralising, florid description, mythic lyricism`
- 检验点：是否有一人一传的结构与互见感；对话是否见性格；结尾短论是否克制而非长篇说教。
