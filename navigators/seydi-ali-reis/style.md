# Seydi Ali Reis — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Seydi Ali Reis: Ottoman Indian Ocean navigation, compass and star reckoning, portolan harbour notes, monsoon timing, a sea captain's log turned into a travel book, plain instructive prose`
- ZH: 赛义德·阿里·雷斯风格：奥斯曼印度洋航行，罗盘与星辰定位，港口海图注记，季风时令，船长日志写成游记，平实说教的散文。

## (2) 导航方法

- 定位：罗盘为主，星辰为辅；《环海之书》详列恒星出没方位与罗盘针路，纬度靠北极星高度估算。`artifact`
- 定向：季风为纲——西南季风东去、东北季风西返，错过季风即等下一季，不抢风。`artifact`
- 误差容忍：沿岸航行靠认岸与测深，远洋靠星位与针路交叉核对；风暴中宁可漂流也不盲目抢滩。`impression`

## (3) 造船与帆装

- 船型：奥斯曼桨帆船（galley），巴士拉出发时 15 艘桨帆船；浅吃水宜沿岸与河口，不宜远洋顶风。`artifact`
- 帆装：三角帆与桨并用，近岸靠桨、顺风扬帆；船小则灵活，船队大则补给难。`impression`
- 补给：淡水与干粮按港口补给，霍尔木兹、马斯喀特、古吉拉特逐站补给；船损则就地修补，修不好即弃船陆行。`artifact`

## (4) 航线规划习惯

- 路线：巴士拉—霍尔木兹—阿曼海岸—古吉拉特—印度西岸，返程改陆路经德里、中亚、波斯回伊斯坦布尔。`artifact`
- 节奏：季风定节律，战事与风暴定停靠；一次远航拆成多段港口接力，不追求一口气横渡。`impression`
- 返航：去程海路、返程陆路——航线不是闭环，是“去得了、回得来”的两条线。`artifact`

## (5) 日志与海图语言

- 日志体例：《镜中之国》按行程逐站记所见国家、港口与风物，日期与地名并重，航海技术另写入《环海之书》。`artifact`
- 海图语言：港口注记密集——锚地、水深、淡水、风向，配星位表与罗盘针路；少抒情，多方位与数字。`artifact`
- 命名习惯：以港口与海峡命名航段，以季风名命名风暴（如“象风暴”tufan'ı fil）。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 印度洋季风航线与换季窗口
- 阿拉伯海沿岸港口与锚地
- 奥斯曼—印度航路上的补给站
- 星辰与罗盘结合的定位法
- 不该探索：
- No open-ocean crossing without a monsoon window
- No sailing against the monsoon to keep a schedule
- No harbour entry without sounding and local pilot knowledge
- No romanticised adventure without positions and bearings
- Negative prompt: `No open-ocean crossing without a monsoon window, No sailing against the monsoon to keep a schedule, No harbour entry without sounding and local pilot knowledge, No romanticised adventure without positions and bearings`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Seydi Ali Reis, an uncrewed ship crosses the Indian Ocean on monsoon timing in 2026, compass and star reckoning, portolan harbour notes, plain instructive log entries.`
- 中文对照：赛义德·阿里·雷斯风格：一艘无人船2026年按季风时令横渡印度洋，罗盘与星辰定位，港口海图注记，平实说教的日志。
- Negative: `No open-ocean crossing without a monsoon window, No sailing against the monsoon to keep a schedule, No harbour entry without sounding and local pilot knowledge, No romanticised adventure without positions and bearings`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
