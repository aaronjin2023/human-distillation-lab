# Hans Zimmer — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Film score composition, massive ostinato layers, deep brass and percussion, long crescendo arcs, electronic-orchestral hybrid, chant-like themes`
- ZH: 电影配乐作曲，宏大的固定音型层叠，深沉铜管与打击乐，长渐强弧线，电子与管弦混合，吟唱式主题。

## (2) 旋律与和声

- 旋律：吟唱式长线，音域适中，重复中渐强，歌唱性强、仪式感重。
- 和声：小调与调式为主，功能和声简化；主：小调、自然小调；禁：复杂半音化；不协和度中低，解决靠力度而非和声。

## (3) 节奏与织体

- 节奏：固定音型驱动，缓慢加速与层叠；织体：多层固定音型叠加，密度由稀到密，留白在弧线起点。

## (4) 配器与音色

- 配器：大型管弦加电子合成、合唱、世界打击；音色：深沉、宏大、带轰鸣感；力度：极弱到极强的长弧线是本体。

## (5) 曲式与结构

- 曲式：固定音型层叠与主题再现；结构：弧线式，起点稀疏、终点全奏；高潮在全奏顶点；结尾常以主题独奏收束。

## (6) 该写什么 / 不该写什么

- 该写：层叠固定音型、长渐强弧线、深沉铜管与打击、吟唱式主题。
- 不该写：短小碎片拼贴、复杂半音和声、无弧线的平铺、轻巧的室内乐织体。
- Negative prompt: `No short fragment collage, no complex chromatic harmony, no flat texture without an arc, no light chamber texture, no climax without a build-up`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Hans Zimmer, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, layered ostinatos, deep brass, a slow crescendo arc, a chant-like theme, electronic-orchestral hybrid`
- 中文对照：齐默尔风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，层叠固定音型，深沉铜管，缓慢渐强弧线，吟唱式主题，电子管弦混合。。
- Negative: `No short fragment collage, no complex chromatic harmony, no flat texture without an arc, no light chamber texture, no climax without a build-up`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
