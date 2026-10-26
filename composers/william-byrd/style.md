# William Byrd — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `English Renaissance polyphony, expressive text setting, Latin Masses and Anglican anthems in parallel, virginal keyboard music, consort songs, dignified and intense sacred lines`
- ZH: 英国文艺复兴复调，富于表情的文本配曲，拉丁弥撒与圣公会圣歌并行，维吉那琴键盘音乐，古提琴合奏歌曲，庄重而强烈的圣乐线条。

## (2) 旋律与和声

- 旋律：线条庄重，级进与适度跳进结合；文本重音决定旋律起伏，拉丁经文歌尤重表情。`artifact` 和声：调式和声，半音作表情点缀；终止清晰；禁用现代功能和声。调性：调式稳定，半音游移服务于文本。

## (3) 节奏与织体

- 节奏：节奏随文本流动，偶有切分点缀；键盘曲有舞曲节奏（帕凡—加利亚德对）。织体：三—六声部复调；键盘曲为单人多声部织体；留白靠声部减至二声部。

## (4) 配器与音色

- 配器与音色：人声合唱、维吉那琴、古提琴合奏三线并行；音色庄重、内敛；力度靠声部增减，动态范围适中；空间感来自教堂与家庭音乐会的 intimate 共鸣。

## (5) 曲式与结构

- 曲式：拉丁弥撒（三、四、五声部）、圣公会礼拜乐、经文歌、键盘变奏曲与舞曲并重。结构：文本段落驱动，高潮在文本最重处；键盘曲以主题—变奏组织；结尾庄重收束。

## (6) 该写什么 / 不该写什么

- 该写：拉丁弥撒与圣公会圣歌并行、表情性文本配曲、维吉那琴键盘变奏曲、帕凡—加利亚德舞曲对、古提琴合奏歌曲。
- 不该写：现代功能和声、无表情的纯协和、管弦乐式配器、夸张半音化、与文本无关的炫技。
- Negative prompt: `No modern functional harmony, no expressionless consonance, no orchestral scoring, no exaggerated chromaticism, no text-irrelevant virtuosity, no pop phrasing`

## (7) 测试提示词示例（现代题材：深夜只亮着一盏台灯的空办公室）

- Prompt: `In the style of William Byrd, a 30-second piece for an empty office late at night with one desk lamp on, english renaissance polyphony, expressive text setting, latin masses and anglican anthems in parallel, virginal keyboard music, consort songs, dignified and intense sacred lines`
- 中文对照：威廉·伯德风格，为深夜只亮着一盏台灯的空办公室写 30 秒配乐，英国文艺复兴复调，富于表情的文本配曲，拉丁弥撒与圣公会圣歌并行，维吉那琴键盘音乐，古提琴合奏歌曲，庄重而强烈的圣乐线条。
- Negative: `No modern functional harmony, no expressionless consonance, no orchestral scoring, no exaggerated chromaticism, no text-irrelevant virtuosity, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
