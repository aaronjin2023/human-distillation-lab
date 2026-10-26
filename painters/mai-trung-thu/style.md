# Mai Trung Thu — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Vietnamese silk painting, ink and gouache on silk, soft luminous washes, slender women in ao dai, dreamy eyes, lyrical and serene, East-West synthesis`
- ZH: 越南丝绸画，丝上水墨淡彩，柔和透亮的晕染，奥黛长衫的纤细女子，梦幻的眼神，抒情宁静，东西合璧。

## (2) 色板方向

- 主色（7 色，颜料名）：墨色、藤黄、朱红、石绿、群青、淡粉、赭石。`verbatim` / `artifact`
- 以淡彩为主：藤黄与淡粉画奥黛，石绿与群青画背景，墨色只勾线；丝面的透亮是画的光。`verbatim`
- 辅色：淡赭画木器、淡紫画衣纹。
- 禁色：油画式厚涂与明暗；高饱和大面积平涂；粗黑硬线。
- 冷暖：整体偏暖偏淡，暖在藤黄与淡粉，冷只一点石绿群青。
- 明暗 / 饱和：无写实明暗；体积靠淡彩的薄染与线的疏密；亮在丝面本身的透亮处。

## (3) 笔触与线条

- 笔触：丝面晕染——淡彩在丝上自然晕化，笔触不可见；墨色只勾线。`verbatim`
- 线条：细墨线勾边定一切，线均匀、纤细、有韧性；奥黛的衣纹线流畅、疏密有致。`verbatim`
- 质感：丝面的光滑透亮 + 水墨的晕染 + 淡彩的薄染；无油彩堆积，无木刻刀味。

## (4) 构图习惯

- 画幅：竖幅为主，人物半身或全身，背景极简。`artifact`
- 视点：平视；无透视，平面构成。
- 布局：人物居中偏一侧，背景留空给丝面本身；视线落在女子的眼神上。`verbatim`
- 裁切：人物不顶边，留白即是丝面；不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在丝面本身的透亮与淡彩处。
- 阴影：无写实阴影；面部的体积靠淡彩的薄染。
- 透视：无透视；空间靠前后人物的叠压，不靠焦点透视。

## (6) 该画什么 / 不该画什么

- 该画：奥黛女子、弹月琴的少女、母与子、顺化风景、闺中情景。`verbatim`
- 不该画：油画式厚涂；高饱和大面积平涂；粗黑硬线；无眼神的程式化美人脸。
- Negative prompt: `heavy oil paint, high-saturation flat colour, thick bold outlines, photorealistic shading, identical stereotyped faces`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Mai Trung Thu, a small Yorkshire terrier sitting on a subway seat, Vietnamese silk painting, ink and gouache on silk, soft luminous washes, the dog with dreamy eyes, lyrical and serene, East-West synthesis`
- 中文对照：梅忠恕风格，一只小约克夏犬坐在地铁座位上，越南丝绸画，丝上水墨淡彩，柔和透亮的晕染，狗有着梦幻的眼神，抒情宁静，东西合璧。
- Negative: 见第 (6) 节。
- 检验点：丝面是否透亮、晕染是否柔和；眼神是否梦幻；奥黛式的淡彩是否克制。
