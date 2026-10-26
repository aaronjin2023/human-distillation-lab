# Adolf Loos — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。色板只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Adolf Loos: plain white cubic volumes, Raumplan split-level interiors, no ornament, rich natural materials inside, blank street facade, no decoration`
- ZH: 鲁斯风格：素白立方体量、空间规划（Raumplan）错层室内、没有装饰、室内用天然好材料、临街立面空白，没有装饰。

## (2) 空间与体量

体量为素白立方体，严整、封闭、临街面近乎空白；内部以 Raumplan 错层组织空间，各室按功能取不同高度与尺度，楼梯即空间枢纽。`artifact` 室外克制、室内丰富，是内外反差的空间逻辑。

## (3) 材料与色彩

主材：外墙白色抹灰，室内大理石、木材（桃花心木、橡木）、黄铜、镜面。色板：白、石材灰、木色、大理石纹、铜色；禁彩色涂料与一切贴上去的装饰。冷暖：外冷内暖，室内材料本色即色彩。

## (4) 结构与构造

结构以承重墙与楼板错层为主，Raumplan 的关键是楼板标高随功能变化，结构与空间一体；屋顶多为平屋顶，开洞按室内功能取大小，临街开洞极小。节点重在石材与木材的收边，拒绝线脚。`artifact`

## (5) 光线与环境

光线以外墙小窗与天窗为主，室内以镜面与浅色石材反射提亮；穆勒别墅的起居室以大窗取景，私密房间则小窗克制。光线服务于 Raumplan 的空间层次，不作装饰性处理。

## (6) 该设计什么 / 不该设计什么

- 该设计：
- 素白立方体量与空白临街立面
- Raumplan 错层空间与多标高楼板
- 室内天然好材料：大理石、木材、黄铜、镜面
- 无装饰的平整墙面与收边
- 楼梯作为空间枢纽与视线组织
- 小窗开洞按功能取大小
- 不该设计：
- No applied ornament
- No decorative mouldings
- No pitched roof with ornament
- No coloured cladding
- No symmetrical classical facade
- Negative prompt: `No applied ornament, no decorative mouldings, no pitched roof with ornament, no coloured cladding, no symmetrical classical facade`

## (7) 测试提示词示例（现代题材：一座建在山坡上的小住宅）

- Prompt: `In the style of Adolf Loos, a small house on a hillside in a modern city, plain white cubic volumes, blank street facade, Raumplan split-level interior, rich marble and wood inside, no ornament, architecture photography, soft daylight`
- 中文对照：鲁斯风格：现代城市山坡上的一座小住宅，素白立方体量，空白临街立面，错层室内，室内大理石与木材，没有装饰。
- Negative: `No applied ornament, no decorative mouldings, no pitched roof, no coloured cladding, no ornate facade`
- 检验点：外立面是否空白克制；室内是否错层且材料丰富；有无装饰线脚混入。
