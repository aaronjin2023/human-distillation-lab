# Ellen Biddle Shipman — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ellen Biddle Shipman, American country-place garden, a sequence of intimate outdoor rooms, boxwood parterre, reflecting pool, double camellia allee, lush impressionistic planting, design, greenery and privacy`
- ZH: 希普曼风格：美国庄园花园，一连串亲切的室外房间，黄杨花坛，镜面水池，双排山茶林荫道，印象派式的繁茂种植，设计、绿意与私密。

## (2) 空间布局

布局是“花园房间”的序列：以住宅为起点，一间一间向外展开——门廊花园、围墙花园、潘神花园、野花园，每间有自己的轴线与围合，房间之间以林荫道、拱门或水池过渡。`artifact` 尺度亲切，围合感强，游线曲折而有停顿，视线落点常是一座小亭、一泓金鱼池或一株老橡树。

## (3) 水石植物

水是小尺度的镜面与金鱼池：长方形映池、圆形金鱼池，水面平静、占比克制，驳岸为砖石规整收边。`artifact` 石材多用砖与石灰岩，铺地与矮墙皆砖砌。植物是本体：黄杨绿篱定骨架，山茶、杜鹃、鸢尾与多年生花境按印象派色块混植，花色浓郁但分层清晰；野花园一角保留本土鸢尾与乡土植物，与规整花坛对照。

## (4) 借景与框景

借景以内向为主：以高篱、砖墙与密植围合出私密，墙外只借老橡树与远处树冠线；园内对景靠轴线尽端的小亭、鸽舍或雕塑收束。`artifact` 框景靠门洞与林荫道尽端的开口，框内只取一池一树，不贪多。

## (5) 材料与季节变化

材料：砖、石灰岩、黄杨、山茶、鸢尾、多年生花境；砖墙与石径做旧，不用光亮新材。季节：春以杜鹃与鸢尾为高光，夏以绿荫与水面为高光，秋以山茶与橡树叶色收束；冬季靠黄杨骨架与砖墙结构撑住全园。光影靠树荫与水面倒影，不用强光。

## (6) 该造什么 / 不该造什么

- 该造：
- 花园房间序列：门廊花园、围墙花园、野花园依次展开
- 黄杨花坛与砖砌矮墙定骨架
- 长方形镜面映池与金鱼池
- 双排山茶林荫道与老橡树林荫道
- 印象派色块的多年生花境：鸢尾、杜鹃、福禄考
- 不该造：
- 不造开阔无围合的大草坪
- 不造规整对称的中轴大园
- 不造大面积几何花坛与浓艳重彩平涂
- 不造野趣草甸式无管理种植
- Negative prompt: `No open undivided lawn, no grand symmetrical axis, no large geometric flower beds, no wild unmanaged meadow, no bright heavy colours`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ellen Biddle Shipman, a small rooftop garden in a modern city, a sequence of intimate outdoor rooms, boxwood parterre, a small reflecting pool, lush impressionistic planting of iris and camellia, brick walls, design, greenery and privacy`
- 中文对照：希普曼风格：现代城市的一座小型屋顶花园，一连串亲切的室外房间，黄杨花坛，一泓小镜面水池，鸢尾与山茶的印象派式繁茂种植，砖墙围合，设计、绿意与私密。
- Negative: `No open undivided lawn, no grand symmetrical axis, no large geometric flower beds, no wild unmanaged meadow, no bright heavy colours`
- 检验点：花园房间是否一间一间展开而不是一大片；黄杨骨架是否清晰；花境是否繁茂而分层。
