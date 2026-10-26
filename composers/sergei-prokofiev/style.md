# Sergei Prokofiev — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Neoclassical clarity with biting dissonance, motoric rhythm, sharp wit, lyrical second themes, brilliant orchestration, fairytale and grotesque side by side`
- ZH: 新古典主义清晰，带刺的不协和，动感节奏，机智锋利，抒情第二主题，辉煌配器，童话与怪诞并置。

## (2) 旋律与和声

- 旋律：轮廓清晰、级进中带突兀大跳；抒情主题歌唱性强，常以简单音型起手再转折。`artifact`
- 和声：调性为底，半音与错位和弦制造锋利色彩；不协和短暂出现即解决，极少长期悬置。`artifact`

## (3) 节奏与织体

- 节奏：动感十足，固定音型驱动；切分与重音错位制造机智感；织体：主调为主，复调为辅，声部清晰可辨。

## (4) 配器与音色

- 配器：色彩鲜明，铜管与打击乐突出；《彼得与狼》每件乐器代表一个角色；钢琴协奏曲独奏与乐队对答锋利。

## (5) 曲式与结构

- 曲式：奏鸣曲式、组曲、芭蕾多乐章；高潮在乐章中后段，结尾常以明亮有力的全奏收束。

## (6) 该写什么 / 不该写什么

- 该写：动感固定音型、锋利短小动机、抒情第二主题、童话体裁、乐器拟人化配器、钢琴与乐队对答。
- 不该写：vague impressionist wash、no endless chromatic wandering、no sentimental swell without rhythmic drive、no dense counterpoint obscuring the theme、no soft-focus orchestration。
- Negative prompt: `No vague impressionist wash, no endless chromatic wandering, no sentimental swell without rhythmic drive, no dense counterpoint obscuring the theme, no soft-focus orchestration`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Sergei Prokofiev, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, motoric rhythm, sharp witty motif, lyrical second theme, bright brass and strings`
- 中文对照：普罗科菲耶夫风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，动感节奏，机智锋利动机，抒情第二主题，明亮铜管与弦乐。
- Negative: `No vague impressionist wash, no endless chromatic wandering, no sentimental swell without rhythmic drive, no dense counterpoint obscuring the theme, no soft-focus orchestration`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
