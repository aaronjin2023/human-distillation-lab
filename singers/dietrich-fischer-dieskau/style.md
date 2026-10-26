# Dietrich Fischer-Dieskau — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Baritone Lieder singer in the style of Dietrich Fischer-Dieskau: intellectual baritone, crystalline diction, infinite colour shading, psychological phrasing, every word weighed`
- ZH: 费舍尔-迪斯考风格：知性的男中音，咬字如水晶，音色层次无穷，心理化的乐句，每个词都有分量。

## (2) 音色与音域

- 男中音音色清澈多变，音色层次极多；主音色为清澈的知性男中音，辅音色为弱音的私语，禁音色为歌剧式的轰鸣与含混咬字。`artifact`

## (3) 唱腔与发声技法

- 发声：气息控制精细，起音轻柔，收尾多渐弱；唱腔：弱音层次多，半音与装饰音精确，颤音细腻。`artifact`

## (4) 咬字与语言

- 德语咬字如水晶，每个辅音都清晰，词义重音；换气点随诗歌呼吸，气口即诗句停顿。`artifact`

## (5) 节奏与即兴

- 乐句随诗歌呼吸，速度随词义变化；慢板更沉，快板更轻。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：舒伯特艺术歌曲（《冬之旅》《美丽的磨坊女》）、舒曼《诗人之恋》、马勒与沃尔夫艺术歌曲、歌剧男中音角色（唐·乔瓦尼）、钢琴伴奏下的叙事性乐句。
- 不该唱：`No operatic blast, no sloppy diction, no even legato wash, no pop croon, no shouted climax`
- Negative prompt: `No operatic blast, no sloppy diction, no even legato wash, no pop croon, no shouted climax`

## (7) 测试提示词示例（现代题材：地铁末班车）

- Prompt: `Sing in the style of Dietrich Fischer-Dieskau, a song about the last subway train of the night. Intellectual baritone, crystalline diction, infinite colour shading, psychological phrasing, piano accompaniment, every word weighed.`
- 中文对照：费舍尔-迪斯考风格：唱一首关于深夜末班地铁的歌。知性的男中音，咬字如水晶，音色层次无穷，心理化的乐句，钢琴伴奏，每个词都有分量。
- Negative: `No operatic blast, no sloppy diction, no even legato wash, no pop croon, no shouted climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
