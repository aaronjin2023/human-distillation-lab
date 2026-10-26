# 歌手蒸馏 · 歌手类：人类历史上最杰出的 100 名歌手（草稿 v1）

> 状态：草稿 v1，待用户确认。不要直接把这份名单当成定论。
> 项目：aaronjin2023/human-distillation-lab
> 日期：2026-10-26
> 参照：`writers-top100-draft.md`（格式范本）、`painters-top100-draft.md` 第 3 节（四维 + 证据分级 + style/process 规格）、`musicians-top100-draft.md` 第 7 节（音乐家模板适配的写法）、`second-batch-22cat-selfcheck.md`（前两批的教训）。

## 0. 范围与选人原则（与画家 v2 第 1 节、作家第 0 节对应）

- **只蒸行业头部**：只收各时期、各流派、各地区公认的顶级歌手，不按销量榜照抄——销量只是其中一部分，演唱成就、风格开创性与历史影响同样入选标准；也不只收在世或当代歌手。
- **只用成果物**：蒸馏材料只限演唱作品本身及其演唱成就——录音、现场演出、音色、唱腔、咬字、气息、即兴、舞台表现。不碰私生活、聊天记录、八卦、轶事、心理传记。
- **与音乐家类的区分**：音乐家类（musicians）蒸的是作曲风格；本类蒸的是演唱风格。同一人可以在两类都出现（例如创作型歌手、歌剧作曲家兼演唱家），不要去重——两类蒸的东西不同。
- **类别全覆盖**：歌剧与古典声乐、爵士、摇滚、流行、灵魂 / R&B / 福音、民歌与世界音乐、拉美、华语与东亚八类都收；同一人跨流派时以其最具代表性的演唱传统归组，代表作可跨流派列出。
- **样本多样性**：非西方与女性要有合理占比（见第 3 节统计），不全是西方男性；同一流派内风格高度重叠的“同类项”只留最具区分度的一两位。
- **最终用途**：
  1. **音频模型**：用这些 skill，按歌手的演唱风格演唱其他歌曲（音色、唱腔、咬字、气息、即兴）。
  2. **视频模型**：根据这些 skill，复刻录音与演出过程（选曲—编曲—录音—混音—演出）。
- **差异本身有价值**：同一工具、同一歌手，换选材、换时期、换蒸馏者，蒸出来的结果会不一样。差异要保留、要对照，不要强行统一。
- **在世歌手 38 人**：见第 3 节统计。在世者只蒸已发表演唱成果物，不碰未发表录音与私人生活；如用户要调整在世人物规则，另行定夺。

## 1. 范围说明：生卒与代表作的写法

- 格式：编号 | 英文名（中文名）| 生卒 | 流派 / 传统 | 代表作（2–3 部，只写歌曲名或专辑名，不编造年份）。
- 生卒只写年份，不写月日；约数加 `c.`；在世者只写生年 + `–`。
- 代表作只写歌曲名或专辑名，不写发行年份；歌剧歌手的代表作可以是歌剧名或咏叹调名，爵士歌手的代表作可以是标准曲名或专辑名。
- 译名以通行中文译名为准；同一歌曲有多个通行译名时取最常见的一种，异译记入正式蒸馏时的 `conflicts.md`。
- 本草稿已用 web 搜索核对了存疑项（莱昂泰·普赖斯在世状态、乌姆·库尔苏姆生年、美空云雀与坂本九生卒），其余生卒与代表作按音乐史通说写；未逐一核对到原文出处者列入第 5 节“缺口与不确定项”，正式蒸馏时逐人核对。

## 2. 名单（100 人）

### A. 歌剧与古典声乐（16 人）

| # | 歌手 | 生卒 | 流派 / 传统 | 代表作 |
|---|---|---|---|---|
| 1 | Enrico Caruso（恩里科·卡鲁索） | 1873–1921 | 意大利歌剧·男高音 | 《穿上戏装》《我的太阳》《今夜星光灿烂》 |
| 2 | Maria Callas（玛丽亚·卡拉斯） | 1923–1977 | 歌剧·女高音 | 《诺尔玛》《托斯卡》《茶花女》 |
| 3 | Luciano Pavarotti（卢恰诺·帕瓦罗蒂） | 1935–2007 | 意大利歌剧·男高音 | 《今夜无人入睡》《我的太阳》《女人善变》 |
| 4 | Plácido Domingo（普拉西多·多明戈） | 1941– | 歌剧·男高音 | 《奥赛罗》《卡门》《弄臣》 |
| 5 | Joan Sutherland（琼·萨瑟兰） | 1926–2010 | 歌剧·花腔女高音 | 《拉美莫尔的露琪亚》《梦游女》《茶花女》 |
| 6 | Birgit Nilsson（比吉特·尼尔森） | 1918–2005 | 歌剧·戏剧女高音 | 《尼伯龙根的指环》《特里斯坦与伊索尔德》《图兰朵》 |
| 7 | Leontyne Price（莱昂泰·普赖斯） | 1927– | 歌剧·女高音 | 《阿依达》《蝴蝶夫人》《托斯卡》 |
| 8 | Jessye Norman（杰西·诺曼） | 1945–2019 | 歌剧·女高音 | 《特里斯坦与伊索尔德》《蓝胡子城堡》《四首最后的歌曲》 |
| 9 | Dietrich Fischer-Dieskau（迪特里希·费舍尔-迪斯考） | 1925–2012 | 艺术歌曲·男中音 | 《冬之旅》《诗人之恋》《马勒艺术歌曲》 |
| 10 | Elisabeth Schwarzkopf（伊丽莎白·施瓦茨科普夫） | 1915–2006 | 歌剧·艺术歌曲·女高音 | 《玫瑰骑士》《魔笛》《四首最后的歌曲》 |
| 11 | Renata Tebaldi（蕾娜塔·泰巴尔迪） | 1922–2004 | 意大利歌剧·女高音 | 《托斯卡》《阿依达》《茶花女》 |
| 12 | Jussi Björling（约西·比约林） | 1911–1960 | 歌剧·男高音 | 《今夜无人入睡》《波希米亚人》《乡村骑士》 |
| 13 | Fritz Wunderlich（弗里茨·文德里希） | 1930–1966 | 歌剧·艺术歌曲·抒情男高音 | 《魔笛》《唐·乔瓦尼》《美丽的磨坊女》 |
| 14 | Cecilia Bartoli（塞西莉亚·芭托莉） | 1966– | 歌剧·花腔女中音 | 《塞维利亚的理发师》《灰姑娘》《诺尔玛》 |
| 15 | José Carreras（何塞·卡雷拉斯） | 1946– | 歌剧·男高音 | 《波希米亚人》《茶花女》《弄臣》 |
| 16 | Montserrat Caballé（蒙特塞拉特·卡巴耶） | 1933–2018 | 歌剧·女高音 | 《拉美莫尔的露琪亚》《诺尔玛》《巴塞罗那》 |

### B. 爵士（12 人）

| # | 歌手 | 生卒 | 流派 / 传统 | 代表作 |
|---|---|---|---|---|
| 17 | Louis Armstrong（路易斯·阿姆斯特朗） | 1901–1971 | 爵士·小号手兼歌手 | 《What a Wonderful World》《Hello, Dolly!》《West End Blues》 |
| 18 | Billie Holiday（比莉·霍利戴） | 1915–1959 | 爵士·布鲁斯 | 《Strange Fruit》《God Bless the Child》《Lady Sings the Blues》 |
| 19 | Ella Fitzgerald（艾拉·菲茨杰拉德） | 1917–1996 | 爵士·拟声唱法 | 《Summertime》《Cheek to Cheek》《Mack the Knife》 |
| 20 | Frank Sinatra（弗兰克·辛纳屈） | 1915–1998 | 爵士·流行标准曲 | 《My Way》《New York, New York》《Fly Me to the Moon》 |
| 21 | Sarah Vaughan（莎拉·沃恩） | 1924–1990 | 爵士·比波普 | 《Lullaby of Birdland》《Misty》《Tenderly》 |
| 22 | Nat King Cole（纳·金·科尔） | 1919–1965 | 爵士·流行标准曲 | 《Unforgettable》《Mona Lisa》《The Christmas Song》 |
| 23 | Nina Simone（妮娜·西蒙） | 1933–2003 | 爵士·灵魂·民谣 | 《Feeling Good》《I Put a Spell on You》《Mississippi Goddam》 |
| 24 | Tony Bennett（托尼·贝内特） | 1926–2023 | 爵士·流行标准曲 | 《I Left My Heart in San Francisco》《The Way You Look Tonight》《Body and Soul》 |
| 25 | Diana Krall（黛安娜·克劳尔） | 1964– | 爵士·流行标准曲 | 《The Look of Love》《Cry Me a River》《Let's Fall in Love》 |
| 26 | Mel Tormé（梅尔·托梅） | 1925–1999 | 爵士·流行标准曲 | 《Blue Moon》《Comin' Home Baby》《The Christmas Song》 |
| 27 | Anita O'Day（安妮塔·奥黛） | 1919–2006 | 爵士·比波普 | 《Sweet Georgia Brown》《Tea for Two》《Honeysuckle Rose》 |
| 28 | Chet Baker（切特·贝克） | 1929–1988 | 爵士·冷爵士 | 《My Funny Valentine》《Time After Time》《Let's Get Lost》 |

### C. 摇滚（13 人）

| # | 歌手 | 生卒 | 流派 / 传统 | 代表作 |
|---|---|---|---|---|
| 29 | Elvis Presley（埃尔维斯·普雷斯利） | 1935–1977 | 摇滚·摇滚乐先驱 | 《Can't Help Falling in Love》《Jailhouse Rock》《Suspicious Minds》 |
| 30 | Freddie Mercury（弗雷迪·默丘里） | 1946–1991 | 摇滚·华丽摇滚 | 《Bohemian Rhapsody》《We Are the Champions》《Somebody to Love》 |
| 31 | Mick Jagger（米克·贾格尔） | 1943– | 摇滚·布鲁斯摇滚 | 《(I Can't Get No) Satisfaction》《Paint It Black》《Sympathy for the Devil》 |
| 32 | Robert Plant（罗伯特·普兰特） | 1948– | 摇滚·硬摇滚 | 《Stairway to Heaven》《Whole Lotta Love》《Kashmir》 |
| 33 | Janis Joplin（贾尼斯·乔普林） | 1943–1970 | 摇滚·布鲁斯摇滚 | 《Piece of My Heart》《Me and Bobby McGee》《Cry Baby》 |
| 34 | John Lennon（约翰·列侬） | 1940–1980 | 摇滚·创作歌手 | 《Imagine》《Come Together》《Instant Karma!》 |
| 35 | Paul McCartney（保罗·麦卡特尼） | 1942– | 摇滚·流行摇滚 | 《Hey Jude》《Let It Be》《Yesterday》 |
| 36 | David Bowie（大卫·鲍伊） | 1947–2016 | 摇滚·华丽摇滚 | 《Space Oddity》《Heroes》《Life on Mars?》 |
| 37 | Bruce Springsteen（布鲁斯·斯普林斯汀） | 1949– | 摇滚·心地摇滚 | 《Born in the U.S.A.》《Born to Run》《Dancing in the Dark》 |
| 38 | Stevie Nicks（史蒂薇·尼克斯） | 1948– | 摇滚·流行摇滚 | 《Rhiannon》《Landslide》《Edge of Seventeen》 |
| 39 | Axl Rose（阿克塞尔·罗斯） | 1962– | 摇滚·硬摇滚 | 《Sweet Child o' Mine》《November Rain》《Welcome to the Jungle》 |
| 40 | Kurt Cobain（科特·柯本） | 1967–1994 | 摇滚·垃圾摇滚 | 《Smells Like Teen Spirit》《Come as You Are》《Lithium》 |
| 41 | Bono（保罗·休森，Bono） | 1960– | 摇滚·另类摇滚 | 《With or Without You》《One》《Beautiful Day》 |

### D. 流行（16 人）

| # | 歌手 | 生卒 | 流派 / 传统 | 代表作 |
|---|---|---|---|---|
| 42 | Michael Jackson（迈克尔·杰克逊） | 1958–2009 | 流行·舞曲 | 《Billie Jean》《Thriller》《Man in the Mirror》 |
| 43 | Madonna（麦当娜） | 1958– | 流行·舞曲 | 《Like a Virgin》《Vogue》《Material Girl》 |
| 44 | Whitney Houston（惠特尼·休斯顿） | 1963–2012 | 流行·R&B | 《I Will Always Love You》《Greatest Love of All》《I Wanna Dance with Somebody》 |
| 45 | Mariah Carey（玛丽亚·凯莉） | 1969– | 流行·R&B | 《Hero》《We Belong Together》《All I Want for Christmas Is You》 |
| 46 | Céline Dion（席琳·迪翁） | 1968– | 流行·成人抒情 | 《My Heart Will Go On》《The Power of Love》《Because You Loved Me》 |
| 47 | Barbra Streisand（芭芭拉·史翠珊） | 1942– | 流行·百老汇 | 《The Way We Were》《People》《Evergreen》 |
| 48 | Elton John（埃尔顿·约翰） | 1947– | 流行·创作歌手 | 《Your Song》《Rocket Man》《Candle in the Wind》 |
| 49 | Adele（阿黛尔） | 1988– | 流行·灵魂流行 | 《Someone Like You》《Rolling in the Deep》《Hello》 |
| 50 | Beyoncé（碧昂丝） | 1981– | 流行·R&B | 《Crazy in Love》《Halo》《Single Ladies》 |
| 51 | Taylor Swift（泰勒·斯威夫特） | 1989– | 流行·创作歌手 | 《Love Story》《Shake It Off》《Blank Space》 |
| 52 | Ed Sheeran（艾德·希兰） | 1991– | 流行·创作歌手 | 《Thinking Out Loud》《Shape of You》《Perfect》 |
| 53 | Bruno Mars（布鲁诺·马尔斯） | 1985– | 流行·放克 | 《Just the Way You Are》《Uptown Funk》《Grenade》 |
| 54 | Lady Gaga（Lady Gaga） | 1986– | 流行·舞曲 | 《Bad Romance》《Poker Face》《Shallow》 |
| 55 | Judy Garland（朱迪·加兰） | 1922–1969 | 流行·百老汇 | 《Over the Rainbow》《The Trolley Song》《Get Happy》 |
| 56 | Bing Crosby（宾·克罗斯比） | 1903–1977 | 流行·标准曲 | 《White Christmas》《Swinging on a Star》《Pennies from Heaven》 |
| 57 | ABBA（组合） | 组合，1972– | 流行·迪斯科 | 《Dancing Queen》《Mamma Mia》《Waterloo》 |

### E. 灵魂 / R&B / 福音（10 人）

| # | 歌手 | 生卒 | 流派 / 传统 | 代表作 |
|---|---|---|---|---|
| 58 | Aretha Franklin（阿蕾莎·富兰克林） | 1942–2018 | 灵魂·福音 | 《Respect》《(You Make Me Feel Like) A Natural Woman》《Think》 |
| 59 | Marvin Gaye（马文·盖伊） | 1939–1984 | 灵魂·R&B | 《What's Going On》《Sexual Healing》《Let's Get It On》 |
| 60 | Stevie Wonder（史蒂维·旺德） | 1950– | 灵魂·R&B | 《Superstition》《Isn't She Lovely》《I Just Called to Say I Love You》 |
| 61 | Ray Charles（雷·查尔斯） | 1930–2004 | 灵魂·R&B·福音 | 《Georgia on My Mind》《Hit the Road Jack》《I Can't Stop Loving You》 |
| 62 | James Brown（詹姆斯·布朗） | 1933–2006 | 灵魂·放克 | 《I Got You (I Feel Good)》《Papa's Got a Brand New Bag》《It's a Man's Man's Man's World》 |
| 63 | Otis Redding（奥蒂斯·雷丁） | 1941–1967 | 灵魂 | 《(Sittin' On) The Dock of the Bay》《Try a Little Tenderness》《Respect》 |
| 64 | Sam Cooke（山姆·库克） | 1931–1964 | 灵魂·福音 | 《A Change Is Gonna Come》《You Send Me》《Wonderful World》 |
| 65 | Etta James（艾塔·詹姆斯） | 1938–2012 | 灵魂·布鲁斯 | 《At Last》《I'd Rather Go Blind》《Tell Mama》 |
| 66 | Diana Ross（黛安娜·罗斯） | 1944– | 灵魂·流行 | 《Ain't No Mountain High Enough》《Endless Love》《Upside Down》 |
| 67 | Luther Vandross（卢瑟·范德罗斯） | 1951–2005 | R&B·灵魂 | 《Never Too Much》《Dance with My Father》《Here and Now》 |

### F. 民歌与世界音乐（12 人）

| # | 歌手 | 生卒 | 流派 / 传统 | 代表作 |
|---|---|---|---|---|
| 68 | Joan Baez（琼·贝兹） | 1941– | 民谣 | 《Diamonds & Rust》《The Night They Drove Old Dixie Down》《Farewell, Angelina》 |
| 69 | Woody Guthrie（伍迪·格思里） | 1912–1967 | 民谣 | 《This Land Is Your Land》《Deportee》《So Long, It's Been Good to Know Yuh》 |
| 70 | Leonard Cohen（莱昂纳德·科恩） | 1934–2016 | 民谣·创作歌手 | 《Hallelujah》《Suzanne》《Bird on the Wire》 |
| 71 | Joni Mitchell（琼尼·米切尔） | 1943– | 民谣·创作歌手 | 《Both Sides Now》《Big Yellow Taxi》《A Case of You》 |
| 72 | Miriam Makeba（米丽亚姆·玛凯巴） | 1932–2008 | 南非·世界音乐 | 《Pata Pata》《The Click Song》《Malaika》 |
| 73 | Youssou N'Dour（尤素·恩杜尔） | 1959– | 塞内加尔·姆巴拉克斯 | 《7 Seconds》《Birima》《Shakin' the Tree》 |
| 74 | Nusrat Fateh Ali Khan（努斯拉特·法塔赫·阿里·汗） | 1948–1997 | 巴基斯坦·卡瓦里 | 《Mustt Mustt》《Allah Hoo》《Dam Mast Qalandar》 |
| 75 | Umm Kulthum（乌姆·库尔苏姆） | c.1904–1975 | 阿拉伯·埃及古典歌唱 | 《Enta Omri》《Alf Leila wa Leila》《Al Atlal》 |
| 76 | Amália Rodrigues（阿玛莉亚·罗德里格斯） | 1920–1999 | 葡萄牙·法朵 | 《Gaivota》《Uma Casa Portuguesa》《Povo Que Lavas no Rio》 |
| 77 | Édith Piaf（艾迪特·皮亚芙） | 1915–1963 | 法国·香颂 | 《La Vie en rose》《Non, je ne regrette rien》《Hymne à l'amour》 |
| 78 | Jacques Brel（雅克·布雷尔） | 1929–1978 | 法国·香颂 | 《Ne me quitte pas》《Amsterdam》《Le Port d'Amsterdam》 |
| 79 | Mercedes Sosa（梅赛德斯·索萨） | 1935–2009 | 阿根廷·新民歌 | 《Gracias a la vida》《Alfonsina y el mar》《Todo cambia》 |

### G. 拉丁美洲（8 人）

| # | 歌手 | 生卒 | 流派 / 传统 | 代表作 |
|---|---|---|---|---|
| 80 | Celia Cruz（西莉亚·克鲁斯） | 1925–2003 | 古巴·萨尔萨 | 《La vida es un carnaval》《Quimbara》《La negra tiene tumbao》 |
| 81 | Héctor Lavoe（埃克托·拉沃） | 1946–1993 | 波多黎各·萨尔萨 | 《El Cantante》《Periódico de ayer》《Aguanile》 |
| 82 | Julio Iglesias（胡里奥·伊格莱西亚斯） | 1943– | 西班牙·拉丁流行 | 《Hey!》《Begin the Beguine》《To All the Girls I've Loved Before》 |
| 83 | Shakira（夏奇拉） | 1977– | 哥伦比亚·拉丁流行 | 《Hips Don't Lie》《Whenever, Wherever》《Waka Waka》 |
| 84 | Caetano Veloso（卡埃塔诺·维罗索） | 1942– | 巴西·热带主义 | 《Alegria, Alegria》《Você É Linda》《Sampa》 |
| 85 | Elis Regina（伊利斯·雷吉娜） | 1945–1982 | 巴西·波萨诺瓦 | 《Águas de Março》《Como Nossos Pais》《Madalena》 |
| 86 | João Gilberto（若昂·吉尔贝托） | 1931–2019 | 巴西·波萨诺瓦 | 《Chega de Saudade》《Desafinado》《Garota de Ipanema》 |
| 87 | Vicente Fernández（比森特·费尔南德斯） | 1940–2021 | 墨西哥·兰切拉 | 《Volver, Volver》《El Rey》《Por Tu Maldito Amor》 |

### H. 华语与东亚（13 人）

| # | 歌手 | 生卒 | 流派 / 传统 | 代表作 |
|---|---|---|---|---|
| 88 | Teresa Teng（邓丽君） | 1953–1995 | 华语流行 | 《月亮代表我的心》《甜蜜蜜》《我只在乎你》 |
| 89 | Anita Mui（梅艳芳） | 1963–2003 | 粤语流行 | 《女人花》《夕阳之歌》《似是故人来》 |
| 90 | Leslie Cheung（张国荣） | 1956–2003 | 粤语流行 | 《风继续吹》《Monica》《当爱已成往事》 |
| 91 | Lo Ta-yu（罗大佑） | 1954– | 华语·创作歌手 | 《童年》《鹿港小镇》《恋曲 1990》 |
| 92 | Cui Jian（崔健） | 1961– | 华语摇滚 | 《一无所有》《新长征路上的摇滚》《花房姑娘》 |
| 93 | Faye Wong（王菲） | 1969– | 华语流行 | 《红豆》《传奇》《容易受伤的女人》 |
| 94 | Eason Chan（陈奕迅） | 1974– | 粤语流行 | 《十年》《浮夸》《爱情转移》 |
| 95 | Jay Chou（周杰伦） | 1979– | 华语流行 | 《青花瓷》《稻香》《双截棍》 |
| 96 | Feng Fei-fei（凤飞飞） | 1953–2012 | 华语流行 | 《掌声响起》《追梦人》《我是一片云》 |
| 97 | Tsai Chin（蔡琴） | 1957– | 华语流行 | 《恰似你的温柔》《被遗忘的时光》《你的眼神》 |
| 98 | G.E.M.（邓紫棋） | 1991– | 华语流行 | 《泡沫》《光年之外》《句号》 |
| 99 | Hibari Misora（美空云雀） | 1937–1989 | 日本·演歌 | 《川流不息》《柔》《悲伤酒》 |
| 100 | Kyu Sakamoto（坂本九） | 1941–1985 | 日本·歌谣曲 | 《昂首向前走》《见上げてごらん夜の星を》《明日があるさ》 |

---

## 3. 分组统计

| 组 | 流派 / 地区 | 人数 |
|---|---|---|
| A | 歌剧与古典声乐 | 16 |
| B | 爵士 | 12 |
| C | 摇滚 | 13 |
| D | 流行 | 16 |
| E | 灵魂 / R&B / 福音 | 10 |
| F | 民歌与世界音乐 | 12 |
| G | 拉丁美洲 | 8 |
| H | 华语与东亚 | 13 |
| **合计** |  | **100** |

### 地区 / 性别占比（按本草稿口径）

- **非西方传统 25 人**：F 组 5（玛凯巴、恩杜尔、努斯拉特、乌姆·库尔苏姆、索萨）+ G 组 7（克鲁斯、拉沃、夏奇拉、维罗索、雷吉娜、吉尔贝托、费尔南德斯）+ H 组 13（华语 11 + 日本 2）。胡里奥·伊格莱西亚斯（西班牙）与阿玛莉亚·罗德里格斯（葡萄牙）按西欧传统计，未计入此数。
- **非裔美国传统 16 人**：B 组 6（阿姆斯特朗、霍利戴、菲茨杰拉德、沃恩、科尔、西蒙）+ E 组 10（富兰克林、盖伊、旺德、查尔斯、布朗、雷丁、库克、詹姆斯、罗斯、范德罗斯）；歌剧组的普赖斯、诺曼另计。
- **非西方 + 非裔美国传统合计 41 人**；其余 59 人为西欧 / 北美白人主流传统（含拉美西语系的伊格莱西亚斯与法朵的罗德里格斯）。
- **女性 47 人**（47%）：A 组 9（卡拉斯、萨瑟兰、尼尔森、普赖斯、诺曼、施瓦茨科普夫、泰巴尔迪、芭托莉、卡巴耶）、B 组 6（霍利戴、菲茨杰拉德、沃恩、西蒙、克劳尔、奥黛）、C 组 2（乔普林、尼克斯）、D 组 10（麦当娜、休斯顿、凯莉、迪翁、史翠珊、阿黛尔、碧昂丝、斯威夫特、Lady Gaga、加兰）、E 组 3（富兰克林、詹姆斯、罗斯）、F 组 7（贝兹、米切尔、玛凯巴、乌姆·库尔苏姆、罗德里格斯、皮亚芙、索萨）、G 组 3（克鲁斯、夏奇拉、雷吉娜）、H 组 7（邓丽君、梅艳芳、王菲、凤飞飞、蔡琴、邓紫棋、美空云雀）。歌手类女性头部本就多于作曲家类，本批按“尽量保留”口径收齐了各流派最具区分度的女性歌手。
- **在世 38 人**：A 组 4（普赖斯、多明戈、芭托莉、卡雷拉斯）、B 组 1（克劳尔）、C 组 7（贾格尔、普兰特、麦卡特尼、斯普林斯汀、尼克斯、罗斯、Bono）、D 组 11（麦当娜、凯莉、迪翁、史翠珊、埃尔顿·约翰、阿黛尔、碧昂丝、斯威夫特、希兰、马尔斯、Lady Gaga）、E 组 2（旺德、罗斯）、F 组 3（贝兹、米切尔、恩杜尔）、G 组 3（伊格莱西亚斯、夏奇拉、维罗索）、H 组 7（罗大佑、崔健、王菲、陈奕迅、周杰伦、蔡琴、邓紫棋）。另 #57 ABBA 四位成员均在世，计入组合条目，不重复计入 38 人。
- **与音乐家类重叠 3 人**：列侬（#34，音乐家类 #78 列侬—麦卡特尼组合成员）、麦卡特尼（#35，同）、迪伦未入本批（音乐家类 #77 以作曲成就入选；如需以演唱成就补入，可从第 4 节换回）。重叠是口径允许的：两类蒸的东西不同（作曲 vs 演唱）。

## 4. 可换回池（近榜人选，用户一句话即可换回）

- **歌剧与古典声乐**：玛丽安·安德森（Marian Anderson）、基里·特·卡娜娃（Kiri Te Kanawa）、安娜·奈瑞贝科（Anna Netrebko）、乔纳斯·考夫曼（Jonas Kaufmann）、安德烈·波切利（Andrea Bocelli）、莎拉·布莱曼（Sarah Brightman）、费奥多尔·夏里亚宾（Feodor Chaliapin）。
- **爵士**：迪娜·华盛顿（Dinah Washington）、卡门·麦克雷（Carmen McRae）、贝蒂·卡特（Betty Carter）、乔·威廉姆斯（Joe Williams）、哈里·贝拉方特（Harry Belafonte）、诺拉·琼斯（Norah Jones）。
- **摇滚**：罗杰·达尔特里（Roger Daltrey）、史蒂文·泰勒（Steven Tyler）、克里斯·康奈尔（Chris Cornell）、蒂娜·特纳（Tina Turner）、帕蒂·史密斯（Patti Smith）、黛比·哈利（Debbie Harry）、艾米·怀恩豪斯（Amy Winehouse）。
- **流行**：凯莉·米洛（Kylie Minogue）、席琳·迪翁已在表内——另有惠特尼·休斯顿已在表内——另有布兰妮·斯皮尔斯（Britney Spears）、贾斯汀·汀布莱克（Justin Timberlake）、杜阿·利帕（Dua Lipa）、菲尔·柯林斯（Phil Collins）、乔治·迈克尔（George Michael）、凯特·布什（Kate Bush）。
- **灵魂 / R&B**：艾尔·格林（Al Green）、柯蒂斯·梅菲尔德（Curtis Mayfield）、格莱蒂丝·奈特（Gladys Knight）、查卡·汗（Chaka Khan）、约翰·传奇（John Legend）、艾丽西亚·凯斯（Alicia Keys）。
- **民歌与世界音乐**：鲍勃·迪伦（Bob Dylan，演唱成就）、皮特·西格（Pete Seeger）、拉维·香卡已在音乐家类——另有拉维之女诺拉·琼斯见爵士池、拉塔·曼格什卡（Lata Mangeshkar，印度）、费鲁兹（Fairuz，黎巴嫩）、马哈茂德·达尔维什已在作家类——另有塞萨莉亚·埃沃拉（Cesária Évora，佛得角）。
- **拉美**：马克·安东尼（Marc Anthony）、路易斯·米格尔（Luis Miguel）、胡安·加布里埃尔（Juan Gabriel）、塞尔吉奥·门德斯（Sérgio Mendes）、阿斯特鲁·吉尔贝托（Astrud Gilberto）。
- **华语与东亚**：张学友、刘德华、林忆莲、莫文蔚、孙燕姿、林俊杰、五月天（组合）、中岛美雪、宇多田光、滨崎步。
- **说明**：本节为候选池，不占名额；换回时从同组或同传统内腾名额，优先补女性与非西方。

## 5. 缺口与不确定项（必须向用户明示）

1. **莱昂泰·普赖斯在世状态**：本次 web 搜索未找到其讣告；Wikipedia 旧版条目（2020 年快照）仍将其列为在世人物，answers.com 亦称“still alive”。本表按在世（1927–）处理；正式蒸馏时再核对一次最新状态，记 `conflicts.md`。
2. **乌姆·库尔苏姆生年有两说**：英文维基主条目作 c.1904 年 5 月 4 日，另有埃及来源作 1898 年 12 月 31 日。本表用 c.1904（维基通说），1898 一说记 `conflicts.md`。
3. **ABBA 为组合条目**：计 1 个名额，蒸馏对象是组合的和声与演唱风格（两位女主唱的声部配合、男女声交织），不蒸四位成员各自的单飞作品与私人关系。成员均在世，只蒸已发表录音。
4. **列侬与麦卡特尼的跨类重叠**：两人在音乐家类以“列侬—麦卡特尼创作组合”入选（作曲成就），在本类以个人演唱成就入选；蒸馏时两类材料分开，不混用。
5. **歌剧代表作的口径**：歌剧歌手的代表作列的是歌剧名（如《托斯卡》），蒸馏时以其在该剧中的具体唱段录音为准，不以整部歌剧的作曲成就代替演唱成就；正式蒸馏时在 manifest.json 中逐人写明所用录音版本。
6. **爵士与流行条目的“作品”口径**：爵士标准曲、流行歌曲以“曲”为单位，专辑（如《Lady Sings the Blues》《Thriller》）以“专辑”为单位，两者在 manifest.json 中分开标注，不混为一谈。
7. **翻唱与原唱的归属**：部分代表作是翻唱成名（如霍利戴《Strange Fruit》原作者为阿贝尔·梅罗波尔、休斯顿《I Will Always Love You》原作者为多莉·帕顿、雷丁《Respect》后被富兰克林翻唱成名），本表只蒸演唱者的演绎，不蒸词曲作者的作曲成就；归属记 `conflicts.md`。
8. **代表作年份未逐一核对**：与画家 v2、作家、音乐家相同，只写歌曲名，不写发行年份；正式蒸馏每位歌手时需逐首核对歌曲名、专辑与版本。歌词只作为演唱材料的一部分蒸（旋律与文字的咬合方式），不蒸歌词作者的生平立场。
9. **主骨架仍是主观榜单**：与画家 v1/v2 相同，本名单是修订拼盘，不是定论，任何一位都可替换；尤其 20 世纪英美流行与摇滚名额仍偏多，非洲（除玛凯巴、恩杜尔外）、东南亚、印度（除努斯拉特外）仍可再扩。

## 6. 模板适配：画家模板怎么改成歌手

> 画家模板见 `painters-top100-draft.md` 第 3 节：immortal-skill 四维（procedure / interaction / memory / personality）+ 证据分级（verbatim / artifact / impression）+ conflicts.md + 3.3 图像风格规格（style.md）+ 3.4 作画过程规格（process.md）。音乐家模板见 `musicians-top100-draft.md` 第 7 节。本节只写“怎么改”，不改画家与音乐家模板本身。
> 教训（见 `second-batch-22cat-selfcheck.md`）：style.md §6“该唱”必须列出实际曲目/母题，不许只写“见 motifs.md”指针；Negative prompt 必须以 `No` 开头逐项写，不许裸词；测试提示词必须每人填实，不许留 `{p['test_en']}` 之类空模板；不许把画家模板的词（该画、画布、笔触）泄露进歌手文件。

### 6.0 文件夹结构（与画家相同，只改内容）

```
<歌手英文名>/
├── SKILL.md            # 一句话：这是谁，什么时候用他 + 演唱风格一句话 + 过程一句话
├── style.md            # 6.2 演唱风格规格（给音频模型）
├── process.md          # 6.3 演唱过程规格（给音频/视频模型）
├── technique.md        # 6.1 技法（四维之 procedure）
├── language.md         # 6.1 声音语言（四维之 interaction）
├── motifs.md           # 6.1 母题与演变（四维之 memory）
├── decisions.md        # 6.1 决策逻辑（四维之 personality）
├── conflicts.md        # 说法不一致 / 归属存疑 / 版本矛盾，保留，不统一
└── manifest.json       # 来源录音清单、选材说明、版本、快照
```

### 6.1 四维对应（只限演唱作品）

| 画家维 | 歌手维 | 问什么 | 只从录音与演出里找什么 | 不写什么 |
|---|---|---|---|---|
| Procedure / 技法与工序 | **发声与演唱技法** | 他/她怎么唱出来的？ | 发声方式（胸声/头声/混声、气息支撑、共鸣位置）、唱腔（颤音、滑音、转音、装饰音）、咬字与语言处理、音域运用、即兴手法（拟声、变奏、延长）、录音室与现场的不同处理 | 不写“他性格如何导致他这样唱” |
| Interaction / 画面语言 | **声音语言** | 声音怎么跟听者说话？ | 音色（亮/暗、干/润、颗粒感）、音量与力度变化、节奏处理（拖拍/抢拍、摇摆感）、乐句呼吸、与乐队/伴奏的咬合、情感的递进与收放、听者的注意力引导 | 不写私生活八卦，不写歌词剧情 |
| Memory / 母题与演变 | **反复母题与曲目类型** | 他/她反复唱什么？怎么变的？ | 重复曲目类型（情歌/叙事歌/咏叹调/标准曲）、反复母题（某类旋律型、某类情感、某类收尾方式）、早期—中期—晚期演变、同一首歌在不同时期的演绎变化 | 不写编年传记，只写作品序列 |
| Personality / 决策逻辑 | **演唱决策** | 他/她在演唱里反复做的选择是什么？ | 他坚持什么、拒绝什么、宁愿牺牲什么也要保住什么（例如：宁愿牺牲音准的绝对干净也要保住即兴的自由；宁愿牺牲音量也要保住气声的亲密感；宁愿牺牲华丽装饰也要保住咬字的清晰） | 不写心理诊断，只写演唱上的取舍 |

### 6.2 style.md 改为演唱风格规格（给音频模型直接用）

每位歌手必填以下 7 项。只描述声音，不描述人生；引用歌词时只引短句并注明出处。

**（1）一句话风格（prompt-ready，英文 + 中文）**
- 英文一句，可直接放进音频生成提示词开头，例如比莉·霍利戴：`Jazz vocal in the style of Billie Holiday: behind-the-beat phrasing, intimate breathy timbre, limited range used with expressive bending, sparse vibrato, conversational delivery, emotional restraint rather than power`。
- 中文一句，对照翻译。

**（2）音色与音域**
- 音色：用通用声乐术语写（例如：明亮/暗沉、清亮/沙哑、圆润/颗粒感、气声/实声、胸声/头声比例），不要编造从录音上实测的精确频率值；如需给频率，必须标注“近似参考，非实测”。
- 音域：声部（女高音/男高音/女中音/男中音/低音）、常用音区、最高音与最低音的处理方式（例如：帕瓦罗蒂的高音 C 明亮开放；霍利戴的中低音区叙事感强，高音区收敛）。
- 写明：主音色 / 辅音色 / 禁音色（他几乎不用的音色，例如卡拉斯不用甜美的轻声、普雷斯利不用学院式美声）。

**（3）唱腔与发声技法**
- 发声：气息支撑方式、共鸣位置、起音方式（气息起音/硬起音/滑入）、收尾方式（渐弱/戛然而止/拖长）。
- 唱腔：颤音（快/慢/宽/窄）、滑音、转音、装饰音、拟声唱法（爵士）、哭腔/喊腔（摇滚与民歌）、花腔（歌剧）。
- 例：菲茨杰拉德拟声即兴如乐器独奏；默丘里真假声切换与歌剧式高音；邓丽君气声与咬字的轻柔贴合。

**（4）咬字与语言**
- 咬字：清晰/含混、元音处理、辅音轻重、方言与口音（例如：辛纳屈的美式标准发音、皮亚芙的巴黎腔、邓丽君的国语咬字与日语发音）。
- 语言：演唱语言（意/法/英/葡/西/中/日/阿拉伯语等）、多语演唱的处理、歌词与旋律的咬合方式（重音落在词义还是旋律上）。
- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念。

**（5）节奏与即兴**
- 节奏：拖拍/抢拍、摇摆感、自由节奏（rubato）、切分、与伴奏的错位与咬合。
- 即兴：即兴的范围（旋律变奏/拟声/延长/加花）、即兴与原旋律的关系、现场与录音室即兴的差异。
- 例：霍利戴永远拖在拍子后面；阿姆斯特朗把旋律唱成小号独奏；乌姆·库尔苏姆一首歌唱一小时靠现场即兴延展。

**（6）该唱什么 / 不该唱什么（Negative prompt）**
- 该唱：他反复唱的曲目类型、母题、情感、句式（只列演唱层面，必须列出实际曲目或母题，不许只写“见 motifs.md”）。
- 不该唱：风格上的禁区——例如霍利戴：不唱力量型高音、不唱规整节拍、不唱甜美圆润；帕瓦罗蒂：不唱气声耳语、不唱拖拍爵士、不唱沙哑摇滚；邓丽君：不唱撕裂高音、不唱含混咬字。
- 写成 `Negative prompt` 一行，每项以 `No` 开头，可直接给音频模型，例如：`No powerful belting, no straight on-beat phrasing, no sweet rounded tone, no operatic vibrato`。

**（7）测试提示词示例（每位歌手 1 条，唱一个现代题材）**
- 格式：英文主提示词 + 中文对照 + Negative prompt，每人必须填实，不许留空模板。
- 题目统一用现代题材，检验风格迁移能力，例如“唱一首关于深夜便利店的歌”“唱一首关于地铁里的约克夏犬的歌”“唱一首关于窗台上咖啡的歌”。
- 例（霍利戴，测试题：深夜便利店）：
  - Prompt: `Sing in the style of Billie Holiday, a song about a woman buying coffee at a convenience store late at night. Behind-the-beat phrasing, intimate breathy timbre, sparse vibrato, conversational delivery, small jazz combo, emotional restraint.`
  - Negative: `powerful belting, straight on-beat phrasing, sweet rounded tone, operatic vibrato, loud climax`
- 例（帕瓦罗蒂，测试题：地铁里的约克夏犬）：
  - Prompt: `Sing in the style of Luciano Pavarotti, a song about a small Yorkshire terrier sitting on a subway seat. Bright open tenor, ringing high notes, legato phrasing, full breath support, warm orchestral accompaniment, joyful and generous.`
  - Negative: `breathy whisper, jazz swing, rough rock shouting, mumbled diction, thin head voice`

### 6.3 process.md 改为演唱过程规格（给音频/视频模型复刻录音与演出过程）

每位歌手必填以下 4 项。只按演唱作品的制作逻辑写，不编造歌手本人的生活场景；有排练/录音记录可考者以公开记录为准，无记录者按录音反推，不声称复刻原过程。

**（1）演唱步骤顺序表（5 步，每步写清 4 件事）**

| 步骤 | 做什么 | 用什么技法 / 工具 | 唱什么、录哪里 | 作品状态 |
|---|---|---|---|---|
| 1 选曲 | 定曲目、定调、定编曲方向 | 试唱 / 钢琴伴奏试调 / 曲目单 | 只定骨架：曲目、调性、速度、情感基调 | 约 10–20% 完成，方向可见、正文未定 |
| 2 编曲 | 定伴奏、定乐队编制、定结构 | 编曲稿 / 乐队试排 / 和声进行 | 主伴奏一次定稿，定乐器组合与段落划分 | 约 30–40%，结构已定、演唱细节全无 |
| 3 录音 | 进棚录唱 | 麦克风选型 / 分轨录音 / 多遍录制 | 主唱分轨录制，保留多遍备选，定咬字与换气 | 约 60–70%，人声已立、混音未做 |
| 4 混音 | 混人声与伴奏、定空间感 | 混响 / 均衡 / 压缩 / 声像 | 只调声音关系，不改演唱本身 | 约 85–90%，声音已立，个别段落仍可替换 |
| 5 演出 | 现场演绎、与观众互动 | 现场乐队 / 灯光 / 舞台走位 | 全曲现场一次成形，保留即兴与临场变化 | 100%，完成态 |

- 每位歌手要把上表填成自己的版本：例如歌剧不是录音室分轨，而是“选剧 → 排练 → 乐队合排 → 彩排 → 首演”；爵士是“选标准曲 → 定和声进行 → 现场即兴 → 录音 → 混音”；卡瓦里是“选诗 → 定拉格 → 现场延展即兴 → 录音”。
- 每步注明：这一步**最容易唱错**的地方（例如霍利戴第 3 步一抢拍就散；帕瓦罗蒂第 3 步气息一断就破；邓丽君第 4 步混响一厚就糊）。

**（2）每一阶段的作品状态变化（过程音频/视频的节奏）**
- 写 5 个检查点（每步结束时的音频文字描述），说明听者能听到什么变化：例如第 1 步只有试唱、第 3 步有人声无混音、第 4 步空间感骤现。
- 节奏建议：选曲慢（让听者听清曲目方向）、编曲中速（听伴奏生长）、录音放慢（听逐句录制与换气）、演出停顿（听完成态）。
- 总时长建议：演示版 60–90 秒；过程版 3–5 分钟。不要把 5 步平均分配时间，按歌手特点分配（例如乌姆·库尔苏姆即兴步占 50%，帕瓦罗蒂录音步占 40%）。

**（3）过程呈现的镜头与字幕建议**
- 呈现：录音室分轨波形逐轨出现，关键演唱处用波形与歌词并排显示；每步左上角出小字步骤名（选曲 / 编曲 / 录音 / 混音 / 演出），不配画外音讲人生，只配步骤字幕。
- 机位（视频版）：录音室全景 / 麦克风特写 / 调音台特写三机位轮换；选曲用全景，录音用特写。
- 成片结尾：定格完成态 3 秒 + 并排出 2–3 首原作小段对照（只放录音，不放肖像）。
- 禁忌：不要用 AI 生成的“假手”长时间遮挡调音台；不要把过程剪成跳切，保留演唱的连续性；不要虚构歌手本人的生活场景。

**（4）过程示例（以霍利戴录《Strange Fruit》逻辑为例，不声称复刻原过程）**
- 选曲：定一首叙事歌，调定在中低音区，速度放慢，情感基调定为克制而非爆发。
- 编曲：小爵士乐队，钢琴轻铺，萨克斯只在间奏进入，不抢人声。
- 录音：人声一遍过，拖在拍子后面，换气点留在句尾，不补录高音。
- 混音：人声居中靠前，混响极少，伴奏压暗，只留钢琴与贝斯的底。
- 演出：现场灯光调暗，一首歌唱完即停，不返场、不解释。
- 节奏：选曲 10%、编曲 15%、录音 50%、混音 20%、演出 5%。

### 6.4 其余文件的改法（一句话对照）

| 画家文件 | 歌手文件 | 改法 |
|---|---|---|
| `technique.md`（技法与工序） | 同名 | 媒材→发声方式；笔法→唱腔与装饰音；分层→分轨录音；修改痕迹→多遍录制与版本证据 |
| `language.md`（画面语言） | 同名 | 笔触/线条/色彩→音色/咬字/节奏；构图→乐句结构；光影→力度与情感距离 |
| `motifs.md`（母题与演变） | 同名 | 画题→曲目类型与母题；系列画→系列录音；早期—晚期→早期—中期—晚期演绎序列 |
| `decisions.md`（决策逻辑） | 同名 | 画面取舍→演唱取舍（坚持什么、拒绝什么、牺牲什么） |
| `conflicts.md` | 同名 | 归属存疑→翻唱归属、版本、译名、生卒争议；不统一，只记录 |
| `manifest.json` | 同名 | 来源画作清单→来源录音清单（录音版本、现场/录音室分开标注、选材说明、快照）；色板字段删除，改为“声音样本”字段（短句演唱描述 + 出处） |
| `style.md` | 同名 | 见 6.2：色板→音色/音域；笔触→唱腔；构图→乐句结构；测试提示词改唱现代题材歌曲 |
| `process.md` | 同名 | 见 6.3：起稿/底色/分层/细化/罩染→选曲/编曲/录音/混音/演出 |

### 6.5 证据分级（沿用画家模板，只换证据类型）

- `verbatim` —— 录音本身：录音中直接可听，可指认到具体歌曲与段落/小节。
- `artifact` —— 成果物 / 文献：歌手本人关于演唱的公开文字、录音室记录、权威乐评、唱片说明。
- `impression` —— 他人印象：后人评论、影响史、学界共识。必须标明“谁的印象”。
- 矛盾保留：同一歌手不同时期说法不一、歌曲归属存疑（如翻唱原唱、歌剧唱段版本），记入 `conflicts.md`，不强行统一。
- 翻唱口径：蒸馏以演唱者的演绎为准；词曲作者只作参照，不作为 `verbatim` 证据。

---

## 7. 来源

**参照文件**：`writers-top100-draft.md`（名单格式与分组统计）、`painters-top100-draft.md` 第 3 节（四维 + 证据分级 + style/process 规格）、`musicians-top100-draft.md` 第 7 节（音乐家模板适配）、`second-batch-22cat-selfcheck.md`（前两批教训：§6 指针、Negative 前缀、空测试提示词、模板泄露）。

**本次核对（web 搜索，2026-10-26）**：
- 莱昂泰·普赖斯在世状态（未找到讣告；Wikipedia 2020 年快照列为在世；answers.com 称仍在世）— https://en.wikipedia.org/wiki/Leontyne%20Price ；https://www.answers.com/Q/Is_Leontyne_Price_dead
- 乌姆·库尔苏姆生年（维基 c.1904-05-04；另有埃及来源作 1898-12-31）— https://en.wikipedia.org/wiki/Om_Kalthoum ；https://egyptfwd.org/Article/6/4397/The-47th-anniversary-of-her-death-Um-Kulthum-Museum-opened
- 美空云雀（1937-05-29–1989-06-24）与坂本九（1941-12-10–1985-08-12）— https://www.cc.kyoto-su.ac.jp/~trobb/famous2/misorah.html ；https://en.wikipedia.org/wiki/Kyu_Sakamoto

**其余生卒与代表作**：按音乐史通说（Wikipedia / Britannica 共识）写，未逐条贴链接；正式蒸馏时逐人核对出处并记入各歌手文件夹的 manifest.json 与 conflicts.md。

---

*下一步（等用户确认整份名单）：1）确认分组与可换回池；2）选第一位试蒸（建议：比莉·霍利戴或邓丽君，演唱风格差异大，最能检验音频 + 过程两条线；或选一位歌剧歌手，例如卡拉斯或帕瓦罗蒂，检验古典声乐线）。*
