# Luo Guanzhong — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Luo Guanzhong: chapter-novel history, 'the empire long divided must unite', heroes judged by deeds, battles in set pieces, storyteller openings and cliffhangers`
- ZH: 罗贯中风格：章回历史小说，分久必合，英雄以事见，战争写成定式场面，说书式开篇与悬念收束。

## (2) 句式与节奏

- 章回体节奏：每回起笔有诗、收束有悬念（“欲知后事如何，且听下回分解”）；叙事快慢分明，战争详写、过渡略写；七言诗作回前小引。`verbatim`

## (3) 词汇与意象

- 词汇：词域：文言夹白话，史事、兵法、地理与市井语并存；善用套语（“却说”“话说”“且说”）；人物绰号与称谓即性格。`impression`
- 意象：赤壁火、长坂坡、空城计、青龙偃月刀、羽扇纶巾；意象群的核心是“势”——天时、地利、人和的较量。`impression`
- 禁词/禁意象：不用现代心理独白、不用琐碎的日常写实、不写与大势无关的私人抒情、不作脱离故事的空洞议论。

## (4) 叙事视角与结构

- 视角：说书人全知视角：作者如说书先生，时而评点人物、时而预告命运；视角不潜入内心，只写言行。`impression`
- 结构：章回体：百二十回线性推进，以时间为线、以战争与权谋为节；单线为主，间有分叙；每回自成单元又环环相扣。`impression`
- 对话：章回小说以人物对话推进情节，对话多为议论与表态（如三顾茅庐的问答），旁白（“却说”）衔接场面。

## (5) 语气与距离

- 语气：庄重、通俗、评点分明；尊刘贬曹的立场是文本的价值底色；与英雄亲近、与奸雄疏离。`impression`（学界通说：尊刘贬曹）

## (6) 该写什么 / 不该写什么

- 该写：分久必合、章回悬念、战争场面、英雄言行、说书评点。
- 不该写：现代心理独白、琐碎日常、脱离故事的空议论。
- Negative prompt: `No modern interior monologue, no trivial daily realism, no abstract essay detached from story`

## (7) 测试提示词示例（现代题材：外卖骑手在深夜送最后一单）

- Prompt: `In the style of Luo Guanzhong, a delivery rider makes his last late-night delivery. Chapter-novel form: open with a seven-line verse, tell the ride as a campaign with terrain and timing, judge the rider by deeds, and end with a storyteller cliffhanger.`
- 中文对照：罗贯中风格：外卖骑手深夜送最后一单。章回体：回前七言诗开篇，把骑行写成一场讲究地形与时机的战役，以事论人，结尾说书式悬念。
- Negative: `modern interior monologue, trivial daily realism, abstract essay detached from story`
- 检验点：是否有章回开篇与悬念收束；战争/战役式场面是否成型；评点是否见立场。
