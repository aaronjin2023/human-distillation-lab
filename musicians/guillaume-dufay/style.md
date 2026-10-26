# Guillaume Dufay — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Early Renaissance polyphony, cantus firmus mass, fauxbourdon, clear triadic sonority, smooth voice leading, sacred and secular in one language`
- ZH: 文艺复兴早期复调，定旋律弥撒，假低音（fauxbourdon），清晰的三和弦音响，平滑声部进行，圣俗同源。

## (2) 音高与和声方向

- 主：定旋律（cantus firmus）为结构骨架；三和弦音响清晰，三度、六度协和；fauxbourdon 平行六度。禁：功能和声的大面积属—主、半音化泛滥。调性：调式中心稳定，收束靠 musica ficta 临时升降；不协和短暂、按规则解决。

## (3) 旋律与节奏

- 旋律：定旋律长音在次中音声部，上下声部以歌唱性线条环绕；级进为主，跳进温和。节奏：流畅、少切分，节拍感含蓄。织体：四声部复调，时有 fauxbourdon 三声部平行段落。

## (4) 配器与音色

- 人声：四声部无伴奏合唱为主；经文歌偶有乐器加倍（见 conflicts）。音色：温暖、透明、均衡。力度：靠声部密度与音区，不靠力度标记。

## (5) 曲式与结构

- 曲式：定旋律弥撒套曲（五乐章共享同一 cantus firmus）、经文歌（motet）、尚松。结构：定旋律在各乐章以不同节奏出现，统一全曲；高潮在 Gloria / Credo 的织体最密处。结尾：调式收束。

## (6) 该写什么 / 不该写什么

- 该写：定旋律弥撒、fauxbourdon、经文歌、尚松、清晰三和弦复调。
- 不该写：功能和声、奏鸣曲式、半音化泛滥、乐队化配器、通俗旋律。
- Negative prompt: `functional harmony, sonata form, rampant chromaticism, orchestral texture, catchy pop melody`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Guillaume Dufay, a cup of coffee on a windowsill, early Renaissance polyphony, cantus firmus, fauxbourdon, clear triadic sonority, smooth voice leading, four voices, warm and transparent`
- 中文对照：迪费风格，一杯放在窗台上的咖啡，文艺复兴早期复调，定旋律，假低音，清晰三和弦，平滑声部进行，四声部，温暖透明。
- Negative: `functional harmony, sonata form, rampant chromaticism, orchestral texture, catchy pop melody`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
