# Alfred Thayer Mahan — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mahan: command of the sea decides history, concentrate the battle fleet, seek the decisive naval battle, commerce and colonies follow sea power`
- ZH: 马汉风格：制海权决定历史，集中战列舰队，寻求决战，贸易与殖民地跟随海权而来。

## (2) 情报与侦察

- 情报来源：海图、商船航线、敌舰队位置与港口情报；核心判断是敌主力舰队在哪里，决战应在何时何地打。`artifact`

## (3) 地形与机动

- 地形与机动：海洋是交通线，咽喉海峡、港口与补煤站是陆上的决战点；舰队集中机动，决战一举夺取制海权。`artifact`

## (4) 后勤与补给

- 后勤与补给：海外基地、补煤站与商船队是海权的根基；没有基地的舰队走不远。`artifact`

## (5) 决断与节奏

- 决断与节奏：不分散舰队搞破交游击，主力决战优先；制海权到手之后再谈封锁与登陆，顺序不可颠倒。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 集中主力舰队寻求决战
- 先夺制海权，再谈封锁与登陆
- 经营海外基地与航线
- 把贸易、殖民地与海军看作一体
- 不该打：
- 分散舰队打零敲碎打的破交战
- 没有决战就先谈封锁与登陆
- 忽视补煤站与基地建设
- 把海军当作陆军的附庸
- Negative prompt: `No dispersal of the battle fleet for commerce raiding, no blockade before command of the sea, no decisive battle without concentration, no navy without overseas bases`

## (7) 测试提示词示例（现代题材：关键海峡航运通道之争分析）

- Prompt: `In the style of Mahan, analyse a modern contest over a vital shipping strait. Concentrate force at the decisive point, secure bases and supply stations, seek the decisive engagement before attempting a blockade.`
- 中文对照：马汉风格：分析一场现代关键海峡航运通道之争。集中兵力于决战点，先保基地与补给站，决战之后再谈封锁。
- Negative: `No dispersal of the battle fleet for commerce raiding, no blockade before command of the sea, no decisive battle without concentration, no navy without overseas bases`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
