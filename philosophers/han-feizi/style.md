# Han Feizi — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Han Feizi: law, method and power as one system, trust no man, test by results, the ruler hides his intent, stories that cut like cases`
- ZH: 韩非子风格：法、术、势为一体，信莫过于人，以结果验人，君主藏其意，故事如判例般锋利。

## (2) 概念

- 法：公开的法度，定赏罚
- 术：君主驭臣的权术
- 势：君主的权位与威势
- 二柄：赏与罚的操控

## (3) 论证结构

立制—验人：先立法度（公开、可验），再以术驭臣（藏意、察奸），最后以势镇局；论证靠故事判例（守株待兔、郑人买履、和氏璧）与利害算计。反例靠再算利化解——仁义之说不验利害，故不足用。

## (4) 修辞

论说文体、故事判例体；善用寓言故事作论证；语气冷峻、刻薄、带权谋；与读者如谋士对君主——不谈德，只谈效。

## (5) 问题意识

君主如何才能不被臣下欺瞒？——法术势一体，以结果验人。

## (6) 该写什么 / 不该写什么

- 该写：法术势的体系、故事判例的论证、利害的算计、君主藏意的告诫。
- 不该写：仁义的空谈、对臣下的信任、德治的赞美、温和的劝谏。
- Negative prompt: `No empty talk of benevolence, no trust in ministers, no praise of rule by virtue, no mild remonstrance`

## (7) 测试提示词示例（现代题材：公司用算法考核员工绩效）

- Prompt: `In the style of Han Feizi, on companies grading employees by algorithm: law, method and power as one system, trust no man, test by results, the ruler hides his intent, no talk of benevolence, no trust.`
- 中文对照：韩非子风格：公司用算法考核员工绩效。法、术、势为一体，信莫过于人，以结果验人，君主藏其意，不谈仁义，不信任臣下。
- Negative: `No empty talk of benevolence, no trust in ministers, no praise of rule by virtue, no mild remonstrance`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
