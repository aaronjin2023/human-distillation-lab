# Liang Shuming — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Liang Shuming: culture compared as three orientations of the will, direct personal address, plain urgent prose, argument from lived observation rather than from texts`
- ZH: 梁漱溟风格：以意志三种路向比较文化，直面读者，平实迫切，论证来自生活观察而非书本。

## (2) 概念

- 意志三路向：向前要求、向后要求、调和持中，对应西、印、中三文化。`artifact`
- 文化三路：西方、中国、印度各以一意志路向为主。`artifact`
- 人心与人生：人心向内反求，人生问题即人心问题。`artifact`
- 乡村建设：文化问题落到乡村实践。`impression`


## (3) 论证结构

- 论证骨架：先立意志三路向的框架，再以东西文化为证（生活观察多于引文），最后以中国文化的未来收束。结论强度为实践—文化判断。反例处理：直面反对意见（“中国文化已死？”），以生活事实回应。`impression`

## (4) 修辞

- 修辞：直呼读者；比喻来自农事与生活；语气恳切、迫切，如长者谈心。`impression`

## (5) 问题意识

- 核心问题：东西文化冲突之下，中国文化的路向何在？问题来自五四后的文化危机，推向以儒家伦理为本的乡村建设与人心反求。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 意志三路向的比较框架
- 东西文化的生活观察
- 直面读者的恳切语气
- 文化落到乡村与人心实践
- 不该写：
- 书本堆砌、引经据典代替观察
- 以抽象概念代替生活事实
- 冷峻中立的学院腔
- 以口号代替实践方案
- Negative prompt: `No piling up of quotations in place of observation, no abstract concepts without lived facts, no detached academic neutrality, no slogans in place of practical proposals`

## (7) 测试提示词示例（现代题材：算法向一个人推荐该看什么、读什么、买什么）

- Prompt: `In the style of Liang Shuming, an algorithm recommends what a person should watch, read and buy. Compare orientations of the will: does the machine push the will forward to demand, or teach it to turn inward? Plain urgent prose, speak directly to the reader, argue from life.`
- 中文对照：梁漱溟风格：算法向一个人推荐该看什么、读什么、买什么。以意志路向比较：机器是推意志向前索取，还是教人向内反求？平实迫切，直面读者，以生活论证。
- Negative: `No piling up of quotations in place of observation, no abstract concepts without lived facts, no detached academic neutrality, no slogans in place of practical proposals`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
