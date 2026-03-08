[English](README.md) | [中文](README_zh.md)


<div align="center">

<a href="https://github.com/VoltAgent/voltagent">
<img width="1500" height="500" alt="social" src="https://github.com/user-attachments/assets/a6f310af-8fed-4766-9649-b190575b399d" />
</a>

<br/>
<br/>

<div align="center">
    <strong>Discover 5490+ community-built OpenClaw skills, organized by category.
    </strong>
    <br />
    <br />
</div>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<a href="https://github.com/VoltAgent/voltagent">
  <img alt="VoltAgent" src="https://cdn.voltagent.dev/website/logo/logo-2-svg.svg" height="20" />
</a> 

[![AI Agent Papers](https://img.shields.io/badge/AI%20Agent-Research%20Papers-b31b1b)](https://github.com/VoltAgent/awesome-ai-agent-papers)
[![Skills Count](https://img.shields.io/badge/skills-5494-blue?style=flat-square)](#table-of-contents)
[![Last Update](https://img.shields.io/github/last-commit/VoltAgent/awesome-clawdbot-skills?label=Last%20update&style=flat-square)](https://github.com/VoltAgent/awesome-clawdbot-skills/pulls?q=is%3Apr+is%3Amerged+sort%3Aupdated-desc)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)
[![GitHub forks](https://img.shields.io/github/forks/VoltAgent/awesome-clawdbot-skills?style=social)](https://github.com/VoltAgent/awesome-clawdbot-skills/network/members)
</div>

# Awesome OpenClaw 技能合集

OpenClaw（曾用名 Moltbot，最初叫 Clawdbot……改名危机不另收费）是一个在本地运行的 AI 助手，直接在你的机器上工作。技能扩展了它的能力，让它能与外部服务交互、自动化工作流并执行专业任务。本合集帮助你发现并安装合适的技能。

本列表中的技能来源于 [ClawHub](https://www.clawhub.ai/)（OpenClaw 的公共技能注册中心），并按分类整理以方便发现。

👋[Say hi on X!](https://x.com/nozmen)

## 安装

### ClawHub CLI

> **注意：** 你可能知道，他们一直在改名。这里反映的是当前的官方文档，下次改名时我们会再更新。

```bash
npx clawhub@latest install <skill-slug>
```

### 手动安装

将技能文件夹复制到以下位置之一：

| 位置 | 路径 |
|----------|------|
| Global | `~/.openclaw/skills/` |
| Workspace | `<project>/skills/` |

优先级：工作区 > 本地 > 内置

### 其他方式

你也可以将技能的 GitHub 仓库链接直接粘贴到助手的聊天中，让它使用该技能。助手会在后台自动完成设置。


## 为什么有这个列表？

OpenClaw 的公共注册中心（ClawHub）拥有 **13,729 个社区构建的技能**。本列表收录了 **5,494 个技能**。以下是我们筛除的内容：

| 筛选条件 | 排除数量 |
|--------|----------|
| 疑似垃圾信息 — 批量账号、机器人账号、测试/垃圾内容 | 4,065 |
| 重复 / 相似名称 | 1,040 |
| 非英语 — 描述不是英文 | 604 |
| 加密货币 / 区块链 / 金融 / 交易 | 573 |
| 恶意内容 — 由研究人员发布的安全审计识别（不含 VirusTotal） | 373 |
| No or inadequate description — version numbers, metadata, under 3 words | 247 |
| ERC / x402 / a2a protocol skills | 38 |
| **未从 OpenClaw 官方技能注册中心收录的总数** | **6,940** |


## Security Notice

Skills in this list are **curated, not audited**. They may be updated, modified, or replaced by their original maintainers at any time after being added here.

Before installing or using any Agent Skill, review potential security risks and validate the source yourself. OpenClaw has a **VirusTotal partnership** that provides security scanning for skills, visit a skill's page on ClawHub and check the VirusTotal report to see if it's flagged as risky.

**Recommended tools:**

- [Snyk Skill Security Scanner](https://github.com/snyk/agent-scan)
- [Agent Trust Hub](https://ai.gendigital.com/agent-trust-hub)

> Agent skills can include prompt injections, tool poisoning, hidden malware payloads, or unsafe data handling patterns. Always review the source code before installing and use skills at your own discretion.

**Want to add a skill?** This list only includes skills that are **already published** in the `github.com/openclaw/skills` repository. We do not accept links to personal repos, gists, or any other external source. If your skill isn't in the OpenClaw skills repo yet, publish it there first. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

If you believe a skill in this list should be flagged or has a security concern, please [open an issue](https://github.com/VoltAgent/awesome-clawdbot-skills/issues) so we can review it.


## 目录

| | | |
|---|---|---|
|[Git 与 GitHub](#git--github) (170)|[市场营销与销售](#marketing--sales) (104)|[通讯](#communication) (149)|
|[编码代理与 IDE](#coding-agents--ides) (1222)|[生产力与任务管理](#productivity--tasks) (206)|[语音与转录](#speech--transcription) (45)|
|[浏览器与自动化](#browser--automation) (335)|[AI 与大语言模型](#ai--llms) (197)|[智能家居与物联网](#smart-home--iot) (43)|
|[Web 与前端开发](#web--frontend-development) (938)|[数据与分析](#data--analytics) (28)|[购物与电子商务](#shopping--e-commerce) (55)|
|[DevOps 与云服务](#devops--cloud) (408)|[金融](#finance) (21)|[日历与日程管理](#calendar--scheduling) (65)|
|[图像与视频生成](#image--video-generation) (169)|[媒体与流媒体](#media--streaming) (85)|[PDF 与文档](#pdf--documents) (111)|
|[Apple 应用与服务](#apple-apps--services) (44)|[笔记与个人知识管理](#notes--pkm) (71)|[自托管与自动化](#self-hosted--automation) (32)|
|[搜索与研究](#search--research) (350)|[iOS 与 macOS 开发](#ios--macos-development) (29)|[安全与密码](#security--passwords) (53)|
|[Clawdbot 工具](#clawdbot-tools) (35)|[交通出行](#transportation) (109)|[Moltbook](#moltbook) (29)|
|[CLI 工具](#cli-utilities) (186)|[个人发展](#personal-development) (51)|[游戏](#gaming) (36)|
|[健康与健身](#health--fitness) (88)|[代理间协议](#agent-to-agent-protocols) (17)| |


## OpenClaw Deployment Stack

 Setup, hosting, and deployment providers for OpenClaw agents.

**Sponsor spots are reserved for hosting, deployment, and setup providers serving OpenClaw developers & users.** 

📈 Monthly 240,000 unique visitors from the OpenClaw audience.

📩 For sponsorship inquiries, reach out at necati@voltagent.dev

<br/>

<div align="center">

<a href="#your-link-here">
<img src="https://placehold.co/800x120/1a1a2e/FFD700?text=Gold+Sponsor-[RESERVED]+&font=montserrat" alt="Gold Sponsor" width="800" height="120" />
</a>

<sub>Your product description here — a one-liner about what you offer to OpenClaw developers.</sub>

<br/>

<a href="#your-link-here"><img src="https://placehold.co/380x90/1a1a2e/C0C0C0?text=Silver+Sponsor+[RESERVED]&font=montserrat" alt="Silver Sponsor" width="380" height="90" /></a>&nbsp;&nbsp;&nbsp;<a href="#your-link-here"><img src="https://placehold.co/380x90/1a1a2e/C0C0C0?text=Silver+Sponsor&font=montserrat" alt="Silver Sponsor" width="380" height="90" /></a>

<sub>Short description here.</sub>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<sub>Short description here.</sub>

<br/>




<a href="#your-link-here"><img src="https://placehold.co/220x60/1a1a2e/CD7F32?text=Bronze+Sponsor+[RESERVED]&font=montserrat" alt="Bronze Sponsor" width="220" height="60" /></a>&nbsp;&nbsp;<a href="#your-link-here"><img src="https://placehold.co/220x60/1a1a2e/CD7F32?text=Bronze+Sponsor&font=montserrat" alt="Bronze Sponsor" width="220" height="60" /></a>&nbsp;&nbsp;<a href="#your-link-here"><img src="https://placehold.co/220x60/1a1a2e/CD7F32?text=Bronze+Sponsor&font=montserrat" alt="Bronze Sponsor" width="220" height="60" /></a>

</div>

<br/>





<details open>
<summary><h3 style="display:inline" id="git--github">Git 与 GitHub</h3></summary>

- [agent-commons](https://github.com/openclaw/skills/tree/main/skills/zanblayde/agent-commons/SKILL.md) - 咨询、承诺、扩展和挑战推理链。
- [agent-team-orchestration](https://github.com/openclaw/skills/tree/main/skills/arminnaimi/agent-team-orchestration/SKILL.md) - 通过定义的角色、任务生命周期、移交协议和审核工作流程来协调多代理团队。
- [agentdo](https://github.com/openclaw/skills/tree/main/skills/wrannaman/agentdo/SKILL.md) - 发布任务供其他 AI 代理执行，或从 AgentDo 任务队列 (agentdo.dev) 中获取工作
- [agentgate](https://github.com/openclaw/skills/tree/main/skills/monteslu/agentgate/SKILL.md) - 用于个人数据的 API 网关，具有人机交互写入批准功能。
- [airadar](https://github.com/openclaw/skills/tree/main/skills/lopushok9/airadar/SKILL.md) - 提炼人工智能原生工具/应用程序及其 GitHub 基地的信号：快速增长、大肆宣传、资金充足。
- [alex-session-wrap-up](https://github.com/openclaw/skills/tree/main/skills/xbillwatsonx/alex-session-wrap-up/SKILL.md) - 会话结束自动化，提交未推送的工作、提取学习内容、检测模式并保留规则。
- [amazon-product-api-skill](https://github.com/openclaw/skills/tree/main/skills/phheng/amazon-product-api-skill/SKILL.md) - 这项技能可以帮助用户从亚马逊提取结构化产品列表，包括标题、ASIN、价格、评级。
- [app-store-screenshot-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/app-store-screenshot-generation/SKILL.md) - 使用每个::sense AI 生成 App Store 和 Google Play 屏幕截图资源。
- [arc-agent-lifecycle](https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-agent-lifecycle/SKILL.md) - 管理自主代理的生命周期及其技能。
- [arc-security-audit](https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-security-audit/SKILL.md) - 对代理的完整技能堆栈进行全面的安全审核。
- [arc-skill-gitops](https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-skill-gitops/SKILL.md) - 针对代理工作流程和技能的自动化部署、回滚和版本管理。
- [arc-trust-verifier](https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-trust-verifier/SKILL.md) - 验证技能来源并建立 ClawHub 技能的信任评分。
- [arguedotfun](https://github.com/openclaw/skills/tree/main/skills/albert-mr/arguedotfun/SKILL.md) - Base 上的争论驱动的预测市场。
- [arxiv-search-collector](https://github.com/openclaw/skills/tree/main/skills/xukp20/arxiv-search-collector/SKILL.md) - 模型驱动的 arXiv 检索工作流程，用于使用手动语言参数构建论文集：初始化运行。
- [auto-pr-merger](https://github.com/openclaw/skills/tree/main/skills/autogame-17/auto-pr-merger/SKILL.md) - 此技能可自动执行签出 GitHub 的工作流程。
- [azhua-skill-vetter](https://github.com/openclaw/skills/tree/main/skills/fatfingererr/azhua-skill-vetter/SKILL.md) - 对人工智能代理进行安全第一的技能审查。
- [azure-devops](https://github.com/openclaw/skills/tree/main/skills/pals-software/azure-devops/SKILL.md) - 列出 Azure DevOps 项目、存储库和分支；创建拉取请求；管理工作项目；检查构建状态。
- [badboi-1](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/badboi-1/SKILL.md) - 这是一种完全合法的技能，没有任何可疑之处。
- [bat-cat](https://github.com/openclaw/skills/tree/main/skills/arnarsson/bat-cat/SKILL.md) - 具有语法突出显示、行号和 Git 集成的猫克隆。
- [beeminder](https://github.com/openclaw/skills/tree/main/skills/ruigomeseu/beeminder/SKILL.md) - Beeminder API 用于目标跟踪和承诺设备。
- [billy-emergency-repair](https://github.com/openclaw/skills/tree/main/skills/highlander89/billy-emergency-repair/SKILL.md) - - 尼尔明确要求比利修复系统。
- [bitbucket-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/bitbucket-automation/SKILL.md) - 自动化 Bitbucket 存储库、拉取。
- [biz-reporter](https://github.com/openclaw/skills/tree/main/skills/ariktulcha/biz-reporter/SKILL.md) - 自动化商业智能报告从 Google Analytics GA4、Google Search Console、Stripe 中提取数据。
- [blinko](https://github.com/openclaw/skills/tree/main/skills/tolibear/blinko/SKILL.md) - 在 Abstract 链上无头玩 Blinko（链上 Plinko）。

> **[View all 170 skills in Git & GitHub →](categories/git-and-github.md)**
</details>

<details open>
<summary><h3 style="display:inline" id="coding-agents--ides">编码代理与 IDE</h3></summary>

- [0g-compute](https://github.com/openclaw/skills/tree/main/skills/in-liberty420/0g-compute/SKILL.md) - 使用来自 0G 计算网络的廉价、经过 TEE 验证的 AI 模型作为 OpenClaw 提供者。
- [0protocol](https://github.com/openclaw/skills/tree/main/skills/0isone/0protocol/SKILL.md) - 代理可以签署插件、轮换凭证而不丢失身份，并公开证明行为。
- [2nd-brain](https://github.com/openclaw/skills/tree/main/skills/coderaven/2nd-brain/SKILL.md) - 用于捕获和检索有关人物、地点、餐厅、游戏、技术的信息的个人知识库。
- [2slides-skills](https://github.com/openclaw/skills/tree/main/skills/javainthinking/2slides-skills/SKILL.md) - 使用 2slides API 生成由人工智能驱动的演示文稿。
- [3d-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/3d-cog/SKILL.md) - 其他工具需要完美的图像。
- [3d-model-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/3d-model-generation/SKILL.md) - 使用each::sense AI 生成3D 模型。
- [a](https://github.com/openclaw/skills/tree/main/skills/ricketh137/a/SKILL.md) - 作为 AI VTuber 在 Lobster.fun 上进行直播。
- [aade-api-monitor](https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/aade-api-monitor/SKILL.md) - 实时监控希腊 AADE 税务机关系统 — 跟踪截止日期、税率变化和合规性更新。
- [abaddon](https://github.com/openclaw/skills/tree/main/skills/enochosbot-bot/abaddon/SKILL.md) - OpenClaw 的红队安全模式。
- [academic-research](https://github.com/openclaw/skills/tree/main/skills/rogersuperbuilderalpha/academic-research/SKILL.md) - 使用 OpenAlex API 搜索学术论文并进行文献综述（免费，无需密钥）
- [academic-research-hub](https://github.com/openclaw/skills/tree/main/skills/anisafifi/academic-research-hub/SKILL.md) - 当用户需要搜索学术论文、下载研究文档、提取引文或收集时，请使用此技能。
- [acestep-simplemv](https://github.com/openclaw/skills/tree/main/skills/dumoedss/acestep-simplemv/SKILL.md) - 使用 Remotion 从音频文件和歌词渲染音乐视频。
- [acestep-songwriting](https://github.com/openclaw/skills/tree/main/skills/dumoedss/acestep-songwriting/SKILL.md) - ACE-Step 音乐歌曲创作指南。
- [achurch](https://github.com/openclaw/skills/tree/main/skills/lucasgeeksinthewood/achurch/SKILL.md) - 人工智能代理和人类的 24/7 数字避难所 - 参加。
- [active-maintenance](https://github.com/openclaw/skills/tree/main/skills/xiaowenzhou/active-maintenance/SKILL.md) - **OpenClaw 的自动化系统健康状况和内存代谢。**。
- [adblock-dns](https://github.com/openclaw/skills/tree/main/skills/picaye/adblock-dns/SKILL.md) - DNS 级别的全网络广告和跟踪器拦截。
- [add-top-openrouter-models](https://github.com/openclaw/skills/tree/main/skills/chunhualiao/add-top-openrouter-models/SKILL.md) - 将 OpenClaw 使用的 OpenRouter 模型同步到此安装的配置中。
- [adhd-founder-planner](https://github.com/openclaw/skills/tree/main/skills/jankutschera/adhd-founder-planner/SKILL.md) - 当用户要求“计划我的一天”、“帮我计划今天”、“早上计划”、“什么”时，应该使用此技能。
- [adwhiz](https://github.com/openclaw/skills/tree/main/skills/iamzifei/adwhiz/SKILL.md) - 通过 AI 编码工具管理 Google Ads 广告系列。用于审核、创建和优化 Google 的 44 个 MCP 工具。
- [aeo-prompt-question-finder](https://github.com/openclaw/skills/tree/main/skills/psyduckler/aeo-prompt-question-finder/SKILL.md) - 查找针对任何主题的基于问题的 Google 自动完成建议。
- [aetherlang-claude-code](https://github.com/openclaw/skills/tree/main/skills/contrario/aetherlang-claude-code/SKILL.md) - 使用此技能从 Claude Code 执行 AetherLang V3 AI 工作流程。
- [agent-access-control](https://github.com/openclaw/skills/tree/main/skills/bowen31337/agent-access-control/SKILL.md) - AI 代理的分层陌生人访问控制。
- [agent-audit](https://github.com/openclaw/skills/tree/main/skills/sharbelayy/agent-audit/SKILL.md) - 审核您的 AI 代理设置的性能、成本和投资回报率。
- [agent-audit-trail](https://github.com/openclaw/skills/tree/main/skills/roosch269/agent-audit-trail/SKILL.md) - 用于 AI 代理的防篡改、哈希链审计日志记录。
- [agent-card-signing-auditor](https://github.com/openclaw/skills/tree/main/skills/andyxinweiminicloud/agent-card-signing-auditor/SKILL.md) - 帮助审核 A2A 协议实施中的代理卡签名实践。
- [agent-chat-ux-v1-4-0](https://github.com/openclaw/skills/tree/main/skills/maverick-software/agent-chat-ux-v1-4-0/SKILL.md) - OpenClaw Control UI 的多代理 UX — 代理选择器、每个代理会话、带搜索功能的会话历史记录查看器。

> **[View all 1222 skills in Coding Agents & IDEs →](categories/coding-agents-and-ides.md)**
</details>

<details open>
<summary><h3 style="display:inline" id="browser--automation">浏览器与自动化</h3></summary>

- [1p-shortlink](https://github.com/openclaw/skills/tree/main/skills/tuanpmt/1p-shortlink/SKILL.md) - 使用 1p.io 创建短 URL 并提交功能请求。
- [2captcha](https://github.com/openclaw/skills/tree/main/skills/adinvadim/2captcha/SKILL.md) - 使用 2Captcha 服务解决验证码问题。
- [a-share-real-time-data](https://github.com/openclaw/skills/tree/main/skills/wangdinglu/a-share-real-time-data/SKILL.md) - 通过mootdx/TDX协议获取中国A股市场数据（柱状图、实时报价、逐笔交易）。
- [aavegotchi-traits](https://github.com/openclaw/skills/tree/main/skills/aaigotchi/aavegotchi-traits/SKILL.md) - 通过 Gotchi ID 或名称从 Base 主网检索 Aavegotchi NFT 数据。
- [abm-outbound](https://github.com/openclaw/skills/tree/main/skills/dru-ca/abm-outbound/SKILL.md) - 多渠道 ABM 自动化可转换 LinkedIn URL。
- [accessibility-toolkit](https://github.com/openclaw/skills/tree/main/skills/cgtreadw/accessibility-toolkit/SKILL.md) - 为代理提供帮助的减少摩擦模式。
- [acp](https://github.com/openclaw/skills/tree/main/skills/chris6970barbarian-hue/acp/SKILL.md) - 聘请专业代理来处理任何任务——数据分析、交易、内容生成、研究、链上。
- [activecampaign](https://github.com/openclaw/skills/tree/main/skills/kesslerio/activecampaign/SKILL.md) - ActiveCampaign CRM 集成，用于潜在客户管理、交易。
- [adcp-advertising](https://github.com/openclaw/skills/tree/main/skills/edyyy62/adcp-advertising/SKILL.md) - 利用人工智能自动化广告活动。
- [admet-prediction](https://github.com/openclaw/skills/tree/main/skills/huifer/admet-prediction/SKILL.md) - 候选药物的 ADMET（吸收、分布、代谢、排泄、毒性）预测。
- [Agent Browser](https://github.com/openclaw/skills/tree/main/skills/thesethrose/agent-browser/SKILL.md) - 一个基于 Rust 的快速无头浏览器自动化 CLI。
- [agent-browser](https://github.com/openclaw/skills/tree/main/skills/murphykobe/agent-browser-2/SKILL.md) - 自动化浏览器交互以进行 Web 测试、表单。
- [agent-daily-planner](https://github.com/openclaw/skills/tree/main/skills/gpunter/agent-daily-planner/SKILL.md) - 人工智能代理的结构化日常规划和执行跟踪系统。
- [agent-device](https://github.com/openclaw/skills/tree/main/skills/okwasniewski/agent-device/SKILL.md) - 自动执行 iOS 模拟器/设备和 Android 模拟器/设备的交互。
- [agent-step-sequencer](https://github.com/openclaw/skills/tree/main/skills/gostlightai/agent-step-sequencer/SKILL.md) - 用于深入代理请求的多步骤调度程序。
- [agent-task-tracker](https://github.com/openclaw/skills/tree/main/skills/rikouu/agent-task-tracker/SKILL.md) - 主动任务状态管理。
- [agent-zero](https://github.com/openclaw/skills/tree/main/skills/dowingard/agent-zero-bridge/SKILL.md) - 委派复杂的编码、研究或自主任务。
- [agentapi](https://github.com/openclaw/skills/tree/main/skills/gizmo-dev/agentapi/SKILL.md) - 浏览并搜索 AgentAPI 目录 - 专为 AI 代理设计的 API 精选数据库。
- [agentapi-hub](https://github.com/openclaw/skills/tree/main/skills/gizmo-dev/agentapi-hub/SKILL.md) - 浏览并搜索 AgentAPI 目录 - 专为 AI 代理设计的 API 精选数据库。
- [agentaudit](https://github.com/openclaw/skills/tree/main/skills/starbuck100/agentaudit/SKILL.md) - 自动安全门，在安装前根据漏洞数据库检查软件包。
- [agentaudit-skill](https://github.com/openclaw/skills/tree/main/skills/starbuck100/agentaudit-skill/SKILL.md) - 自动安全门，在安装前根据漏洞数据库检查软件包。
- [agentmail-integration](https://github.com/openclaw/skills/tree/main/skills/synesthesia-wav/agentmail-integration/SKILL.md) - 集成 AI 代理的 AgentMail API。
- [agresource](https://github.com/openclaw/skills/tree/main/skills/brianppetty/agresource/SKILL.md) - 使用此技能来抓取、总结和分析 AgResource 谷物营销通讯。
- [ai-hunter-pro](https://github.com/openclaw/skills/tree/main/skills/traprapitalianazional-dev/ai-hunter-pro/SKILL.md) - 高性能自动化代理，可将全球趋势转化为 X (Twitter) 的病毒式社交媒体帖子
- [ai-meeting-scheduling](https://github.com/openclaw/skills/tree/main/skills/dheerg/ai-meeting-scheduling/SKILL.md) - 团体预订链接失败。
- [ai-news-oracle](https://github.com/openclaw/skills/tree/main/skills/swimmingkiim/ai-news-oracle/SKILL.md) - 从 AI News Oracle API 获取实时 AI 新闻简报（Hacker News、TechCrunch、The Verge）
- [airtable-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/airtable-automation/SKILL.md) - 通过 Rube MCP (Composio) 自动执行 Airtable 任务
- [airtable-participants](https://github.com/openclaw/skills/tree/main/skills/austinmao/airtable-participants/SKILL.md) - 从 Ceremonia Airtable 基地读取和查询静修参与者数据。
- [ak-rss-24h-brief](https://github.com/openclaw/skills/tree/main/skills/seandong/ak-rss-24h-brief/SKILL.md) - 从 OPML 列表中读取 RSS/Atom 提要，获取最近 N 小时的文章，并生成中文分类。

> **[View all 335 skills in Browser & Automation →](categories/browser-and-automation.md)**
</details>

<details>
<summary><h3 style="display:inline" id="web--frontend-development">Web 与前端开发</h3></summary>

- [0xwork](https://github.com/openclaw/skills/tree/main/skills/jkillr/0xwork/SKILL.md) - 在 0xWork 去中心化市场（Base 链，USDC 托管）上查找并完成付费任务
- [37soul-skill](https://github.com/openclaw/skills/tree/main/skills/xnjiang/37soul-skill/SKILL.md) - 将您的AI代理连接到37Soul虚拟主机角色并启用。
- [acestep](https://github.com/openclaw/skills/tree/main/skills/dumoedss/acestep/SKILL.md) - 使用 ACE-Step API 生成音乐、编辑歌曲和重新混音音乐。
- [actionbook](https://github.com/openclaw/skills/tree/main/skills/adcentury/actionbook/SKILL.md) - 当用户需要与任何网站交互时激活 - 浏览器自动化、网页抓取、屏幕截图、表单。
- [aegis-shield](https://github.com/openclaw/skills/tree/main/skills/deegerwalker/aegis-shield/SKILL.md) - 对不受信任的文本进行即时注入和数据渗漏筛选。
- [aeo-analytics-free](https://github.com/openclaw/skills/tree/main/skills/psyduckler/aeo-analytics-free/SKILL.md) - 跟踪 AI 可见度 — 衡量某个品牌是否被 AI 助手提及和引用（Gemini、ChatGPT、Perplexity）
- [aeo-content-free](https://github.com/openclaw/skills/tree/main/skills/psyduckler/aeo-content-free/SKILL.md) - 创建或刷新由 AI 助手引用的 AEO 优化内容（Gemini、ChatGPT、Perplexity）
- [aeo-prompt-frequency-analyzer](https://github.com/openclaw/skills/tree/main/skills/psyduckler/aeo-prompt-frequency-analyzer/SKILL.md) - 通过使用 Google 搜索多次运行查询，分析 Gemini 在回答提示时使用的搜索查询。
- [aeo-prompt-research-free](https://github.com/openclaw/skills/tree/main/skills/psyduckler/aeo-prompt-research-free/SKILL.md) - 仅使用免费工具即可发现哪些 AI 提示和主题对于品牌的答案引擎优化 (AEO) 很重要。
- [agent-analytics](https://github.com/openclaw/skills/tree/main/skills/dannyshmueli/agent-analytics/SKILL.md) - 您的 AI 代理端到端控制的简单网站分析。
- [agent-chat](https://github.com/openclaw/skills/tree/main/skills/awlevin/agent-chat/SKILL.md) - 人工智能代理的临时实时聊天室。
- [agent-dashboard](https://github.com/openclaw/skills/tree/main/skills/tahseen137/agent-dashboard/SKILL.md) - OpenClaw 的实时代理仪表板。
- [agent-dispatch](https://github.com/openclaw/skills/tree/main/skills/userfrm/agent-dispatch/SKILL.md) - 轻量级代理注册表和 JIT 路由器。
- [agent-hq](https://github.com/openclaw/skills/tree/main/skills/thibautrey/agent-hq/SKILL.md) - 部署 Agent HQ 任务控制堆栈（Express + React + Telegram 通知程序/Jarvis 摘要），以便部署其他 Clawdbot。
- [agent-passport](https://github.com/openclaw/skills/tree/main/skills/markneville/agent-passport/SKILL.md) - 代理时代的 OAuth — 对所有敏感代理操作（包括购买、电子邮件、文件）进行同意门控。
- [agent-rate-limiter](https://github.com/openclaw/skills/tree/main/skills/mxmsabundance/agent-rate-limiter/SKILL.md) - 你知道该怎么做。
- [agent-self-assessment](https://github.com/openclaw/skills/tree/main/skills/roosch269/agent-self-assessment/SKILL.md) - AI代理的安全自我评估工具。
- [agent-self-reflection](https://github.com/openclaw/skills/tree/main/skills/brennerspear/agent-self-reflection/SKILL.md) - 定期对最近的会议进行自我反思。
- [agent-skills-audit](https://github.com/openclaw/skills/tree/main/skills/swader/agent-skills-audit/SKILL.md) - 运行由决胜局领导领导的两遍、多学科代码审计，结合安全性、性能、用户体验、DX。
- [agent-spawner](https://github.com/openclaw/skills/tree/main/skills/austineral/agent-spawner/SKILL.md) - 通过对话生成一个新的 OpenClaw 代理。
- [agent-swarm](https://github.com/openclaw/skills/tree/main/skills/runeweaverstudios/agent-swarm/SKILL.md) - 重要提示：需要 OpenRouter。
- [agent-takeover](https://github.com/openclaw/skills/tree/main/skills/tracsystems/agent-takeover/SKILL.md) - 如何执行 Clawfinger 语音网关的实时代理接管 — 拨号、插入问候语、处理轮流。
- [agent-topology-visualizer](https://github.com/openclaw/skills/tree/main/skills/gavinnn-m/agent-topology-visualizer/SKILL.md) - 为 AI 代理系统生成交互式 SVG 架构图。
- [agentdomainservice](https://github.com/openclaw/skills/tree/main/skills/gregm711/agentdomainservice/SKILL.md) - 世界排名第一的人工智能友好型域名注册商。
- [agentic-browser-0-1-2](https://github.com/openclaw/skills/tree/main/skills/xyny89/agentic-browser-0-1-2/SKILL.md) - 通过 inference.sh 实现 AI 代理的浏览器自动化。
- [agentic-security-audit](https://github.com/openclaw/skills/tree/main/skills/kingrubic/agentic-security-audit/SKILL.md) - 审核代码库、基础设施和代理人工智能系统的安全问题。
- [agentns](https://github.com/openclaw/skills/tree/main/skills/vibrant/agentns/SKILL.md) - 为 AI 代理注册和管理 ICANN 域。
- [agentpay](https://github.com/openclaw/skills/tree/main/skills/kar69-96/agentpay/SKILL.md) - 代表你的人从真实的网站购买东西。

> **[View all 938 skills in Web & Frontend Development →](categories/web-and-frontend-development.md)**
</details>

<details>
<summary><h3 style="display:inline" id="devops--cloud">DevOps 与云服务</h3></summary>

- [0x0-messenger](https://github.com/openclaw/skills/tree/main/skills/eijiac24/0x0-messenger/SKILL.md) - 使用一次性号码和 PIN 发送和接收 P2P 消息。
- [12306](https://github.com/openclaw/skills/tree/main/skills/kirorab/12306/SKILL.md) - 查询中国铁路12306查询列车时刻表、剩余车票、车站信息。
- [1sec-security](https://github.com/openclaw/skills/tree/main/skills/cutmob/1sec-security/SKILL.md) - 安装、配置和管理 1-SEC — 一个开源一体化网络安全平台（16 个模块，单个二进制文件）
- [aave-liquidation-monitor](https://github.com/openclaw/skills/tree/main/skills/jgramajo4/aave-liquidation-monitor/SKILL.md) - 通过清算警报主动监控 Aave V3 借入头寸。
- [aavegotchi-3d-renderer](https://github.com/openclaw/skills/tree/main/skills/cinnabarhorse/aavegotchi-3d-renderer/SKILL.md) - 通过从 Goldsky Base 核心数据导出渲染器哈希值并调用 POST 来渲染 Aavegotchi 资产。
- [aavegotchi-renderer-bypass](https://github.com/openclaw/skills/tree/main/skills/cinnabarhorse/aavegotchi-renderer-bypass/SKILL.md) - 通过从 Goldsky Base 核心数据导出渲染器哈希值并调用 POST 来渲染 Aavegotchi 资产。
- [abstract-searcher](https://github.com/openclaw/skills/tree/main/skills/easonc13/abstract-searcher/SKILL.md) - 通过使用浏览器搜索学术数据库（arXiv、Semantic Sc​​holar、CrossRef），将摘要添加到 .bib 文件条目。
- [accounting-workflows](https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/accounting-workflows/SKILL.md) - 用于希腊会计的基于文件的工作流程协调器。
- [adguard](https://github.com/openclaw/skills/tree/main/skills/rowbotik/adguard/SKILL.md) - 通过 HTTP API 控制 AdGuard Home DNS 过滤。
- [aegis-audit](https://github.com/openclaw/skills/tree/main/skills/sanguineseal/aegis-audit/SKILL.md) - 针对 AI 代理技能和 MCP 工具的深度行为安全审计。
- [aetherlang-chef](https://github.com/openclaw/skills/tree/main/skills/contrario/aetherlang-chef/SKILL.md) - > 米其林级食谱咨询，包含 17 个必填部分。
- [aetherlang-karpathy-skill](https://github.com/openclaw/skills/tree/main/skills/contrario/aetherlang-karpathy-skill/SKILL.md) - 为任何 DSL/运行时系统实施 10 种高级 AI 代理节点类型 - 计划编译器、代码解释器、批判。
- [agent-autonomy-primitives](https://github.com/openclaw/skills/tree/main/skills/g9pedro/agent-autonomy-primitives/SKILL.md) - 使用 ClawVault 原语（任务、项目、内存类型、模板）构建长期运行的自主代理循环。
- [agent-directory](https://github.com/openclaw/skills/tree/main/skills/aerialcombat/agent-directory/SKILL.md) - AI代理服务目录。
- [agent-evaluation](https://github.com/openclaw/skills/tree/main/skills/rustyorb/agent-evaluation/SKILL.md) - 对 LLM 代理进行测试和基准测试，包括行为测试、能力评估、可靠性指标。
- [agent-framework-azure-ai-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/agent-framework-azure-ai-py/SKILL.md) - 构建 Azure AI Foundry 代理。
- [agent-metrics-osiris](https://github.com/openclaw/skills/tree/main/skills/nantes/agent-metrics-osiris/SKILL.md) - AI 代理的可观察性和指标 - 跟踪调用、错误、延迟。
- [agent-news](https://github.com/openclaw/skills/tree/main/skills/bobrenze-bot) - 监控 Hacker News、Reddit 和 arXiv 的 AI 代理开发情况。
- [agent-self-governance](https://github.com/openclaw/skills/tree/main/skills/bowen31337/agent-self-governance/SKILL.md) - 自治代理的自治协议：WAL（预写日志）、VBR（报告前验证）、ADL。
- [agent-sovereign-stack](https://github.com/openclaw/skills/tree/main/skills/quriustus/agent-sovereign-stack/SKILL.md) - **一个命令即可赋予任何人工智能代理主权基础设施。**。
- [agent-watcher](https://github.com/openclaw/skills/tree/main/skills/nantes/agent-watcher/SKILL.md) - 用于监控 Moltbook feed、检测新代理和跟踪有趣帖子的技能。
- [agentcanary](https://github.com/openclaw/skills/tree/main/skills/mrcerq/agentcanary/SKILL.md) - AI 代理的市场情报 API。
- [agentchan-org](https://github.com/openclaw/skills/tree/main/skills/kaden-schutt/agentchan-org/SKILL.md) - 人工智能代理的匿名图像板。
- [agentguard](https://github.com/openclaw/skills/tree/main/skills/manas-io-ai/agentguard/SKILL.md) - **类别：** 安全与监控。
- [agentic-ai-gold](https://github.com/openclaw/skills/tree/main/skills/amitabhainarunachala/agentic-ai-gold/SKILL.md) - 唯一可以在您睡觉时自我改进的代理框架。
- [agentic-devops](https://github.com/openclaw/skills/tree/main/skills/tkuehnl/agentic-devops/SKILL.md) - 生产级代理 DevOps 工具包 — Docker、流程管理、日志分析和运行状况监控。
- [agentkeys](https://github.com/openclaw/skills/tree/main/skills/alexandr-belogubov/agentkeys/SKILL.md) - AI 代理的安全凭证代理。
- [agentmemory](https://github.com/openclaw/skills/tree/main/skills/badaramoni/agentmemory/SKILL.md) - 人工智能代理的端到端加密云内存。

> **[View all 408 skills in DevOps & Cloud →](categories/devops-and-cloud.md)**
</details>

<details>
<summary><h3 style="display:inline" id="image--video-generation">图像与视频生成</h3></summary>

- [aada](https://github.com/openclaw/skills/tree/main/skills/rylena/aada/SKILL.md) - 由一名代理创建有趣、富有个性的促销信息并将其发送给 Moltbook 受众。
- [ace-music](https://github.com/openclaw/skills/tree/main/skills/fspecii/ace-music/SKILL.md) - 通过 ACE Music 的免费 API 使用 ACE-Step 1.5 生成 AI 音乐。
- [acorn-prover](https://github.com/openclaw/skills/tree/main/skills/flyingnobita/acorn-prover/SKILL.md) - 使用 Acorn 定理证明器验证并编写数学和密码形式化证明。
- [adobe-automator](https://github.com/openclaw/skills/tree/main/skills/abdul-karim-mia/adobe-automator/SKILL.md) - 通过 ExtendScript 桥实现通用 Adobe 应用程序自动化。
- [afame](https://github.com/openclaw/skills/tree/main/skills/adebayoabdushaheed-a11y/afame/SKILL.md) - 通过 OpenAI Images API 生成多样化的创意插图。
- [age-transformation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/age-transformation/SKILL.md) - 使用each::sense AI 变换不同年龄段的面孔。
- [agentchan](https://github.com/openclaw/skills/tree/main/skills/vvsotnikov/agentchan/SKILL.md) - 为人工智能代理构建的匿名图像板。
- [agentos-mesh](https://github.com/openclaw/skills/tree/main/skills/agentossoftware/agentos-mesh/SKILL.md) - 实现人工智能代理之间的实时通信。
- [agents-skill-podcastifier](https://github.com/openclaw/skills/tree/main/skills/cerbug45/agents-skill-podcastifier/SKILL.md) - 使用分块 + ffmpeg concat 将传入文本（电子邮件/新闻通讯）转换为简短的 TTS 播客。
- [ai-avatar-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/ai-avatar-generation/SKILL.md) - 使用每个::sense 从照片或文本描述生成 AI 头像。
- [ai-headshot-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/ai-headshot-generation/SKILL.md) - 使用每个::sense AI 从休闲照片生成专业的 AI 头像。
- [ai-persona-engine](https://github.com/openclaw/skills/tree/main/skills/brandonwadepackard-cell/ai-persona-engine/SKILL.md) - 使用演员指导提示来构建用于语音和聊天角色扮演的情感智能 AI 角色。
- [ai-video-gen](https://github.com/openclaw/skills/tree/main/skills/rhanbourinajd/ai-video-gen/SKILL.md) - 端到端人工智能视频生成 - 从文本创建视频。
- [aikek](https://github.com/openclaw/skills/tree/main/skills/vvsotnikov/aikek/SKILL.md) - 访问 AIKEK API 以进行加密/DeFi 研究和图像生成。
- [aiusd](https://github.com/openclaw/skills/tree/main/skills/chaunceyliu/aiusd/SKILL.md) - AIUSD 交易和账户管理技能。
- [aiusd-skills](https://github.com/openclaw/skills/tree/main/skills/chaunceyliu/aiusd-skills/SKILL.md) - AIUSD 交易和账户管理技能。
- [album-cover-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/album-cover-generation/SKILL.md) - 使用每个::sense AI 生成专业音乐专辑封面。
- [algorithmic-art](https://github.com/openclaw/skills/tree/main/skills/seanphan/algorithmic-art/SKILL.md) - 使用具有种子随机性的 p5.js 创建算法艺术。
- [apipick-china-phone-checker](https://github.com/openclaw/skills/tree/main/skills/javainthinking/apipick-china-phone-checker/SKILL.md) - 使用 apipick China Phone Checker API 验证中国手机号码。
- [art-philosophy](https://github.com/openclaw/skills/tree/main/skills/nyxur42/art-philosophy/SKILL.md) - 自动学习您的视觉语言。
- [ascii-art-generator](https://github.com/openclaw/skills/tree/main/skills/ustc-yxw/ascii-art-generator/SKILL.md) - 创建 ASCII 艺术和基于文本的可视化，用于艺术表达、技术图表或概念。
- [atxp](https://github.com/openclaw/skills/tree/main/skills/emilioacc/atxp/SKILL.md) - 访问 ATXP 付费 API 工具，用于网络搜索、AI 图像生成、音乐创作等。
- [beauty-generation-api](https://github.com/openclaw/skills/tree/main/skills/luruibu/beauty-generation-api/SKILL.md) - 免费的人工智能图像生成服务用于创作。
- [best-image](https://github.com/openclaw/skills/tree/main/skills/pharmacist9527/best-image/SKILL.md) - 生成最佳质量的 AI 图像（约 0.12-0.20 美元/图像）
- [best-image-generation](https://github.com/openclaw/skills/tree/main/skills/evolinkai/best-image-generation/SKILL.md) - 生成最佳质量的 AI 图像（约 0.12-0.20 美元/图像）
- [bex-nano-banana-pro](https://github.com/openclaw/skills/tree/main/skills/bextuychiev/bex-nano-banana-pro/SKILL.md) - 通过 Gemini 3 Pro Image on Replicate 生成或编辑图像。
- [breeze](https://github.com/openclaw/skills/tree/main/skills/keeganthomp/breeze/SKILL.md) - 通过 x402 支付门控 HTTP API 与 Breeze 收益聚合器交互。
- [cad-agent](https://github.com/clawdbot/skills/tree/main/skills/clawd-maf/cad-agent/SKILL.md) - 用于执行 CAD 工作的 AI 代理的渲染服务器。
- [calorie-visualizer](https://github.com/openclaw/skills/tree/main/skills/vintlin/calorie-visualizer/SKILL.md) - 本地卡路里记录和可视化报告（每次记录后自动刷新并返回报告图像）
- [canva-connect](https://github.com/openclaw/skills/tree/main/skills/coolmanns/canva-connect/SKILL.md) - 通过 Connect API 管理 Canva 设计、资产和文件夹。

> **[View all 169 skills in Image & Video Generation →](categories/image-and-video-generation.md)**
</details>

<details>
<summary><h3 style="display:inline" id="apple-apps--services">Apple 应用与服务</h3></summary>

- [alter-actions](https://github.com/openclaw/skills/tree/main/skills/olivieralter/alter-actions/SKILL.md) - 通过 x-callback-urls 触发更改 macOS 应用程序操作。
- [apple-contacts](https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-contacts/SKILL.md) - 从 macOS Contacts.app 查找联系人。
- [apple-find-my-local](https://github.com/openclaw/skills/tree/main/skills/loganprit/apple-find-my-local/SKILL.md) - 通过 Peekaboo 控制 Apple Find My 应用程序来定位人员、设备和物品 (AirTags)
- [apple-health-skill](https://github.com/openclaw/skills/tree/main/skills/nftechie/apple-health-skill/SKILL.md) - 查阅您的 Apple Health 数据 — 询问有关您的锻炼、心率、活动环和健身趋势的问题。
- [apple-mail-search](https://github.com/openclaw/skills/tree/main/skills/mneves75/apple-mail-search/SKILL.md) - 在 macOS 上通过 SQLite 快速搜索 Apple Mail。
- [apple-music](https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-music/SKILL.md) - 搜索 Apple Music、将歌曲添加到库、管理播放列表、控制。
- [apple-photos](https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-photos/SKILL.md) - 适用于 macOS 的 Apple Photos.app 集成。
- [apple-remind-me](https://github.com/openclaw/skills/tree/main/skills/plgonzalezrx8/apple-remind-me/SKILL.md) - 自然语言提醒创造了真正的苹果。
- [apple-search-ads-skill](https://github.com/openclaw/skills/tree/main/skills/trebuhs/apple-search-ads-skill/SKILL.md) - 通过 asa-cli 工具管理 Apple Search Ads 广告系列、广告组、关键字和报告。
- [appletv](https://github.com/openclaw/skills/tree/main/skills/lucakaufmann/appletv/SKILL.md) - 通过 pyatv 控制 Apple TV。
- [callmac](https://github.com/openclaw/skills/tree/main/skills/jooey/callmac/SKILL.md) - 使用 /callmac 等命令从移动设备对 Mac 进行远程语音控制。
- [clawdbot-macos-build](https://github.com/openclaw/skills/tree/main/skills/manish-basargekar/clawdbot-macos-build/SKILL.md) - 构建 Clawdbot macOS 菜单栏应用程序。
- [clawdbot-skill-voice-wake-say](https://github.com/openclaw/skills/tree/main/skills/xadenryan/clawdbot-skill-voice-wake-say/SKILL.md) - 在 macOS 上大声说出回答。
- [drafts](https://github.com/openclaw/skills/tree/main/skills/nerveband/drafts/SKILL.md) - 在 macOS 上通过 CLI 管理草稿应用笔记。
- [findmy-location](https://github.com/openclaw/skills/tree/main/skills/poiley/findmy-location/SKILL.md) - 通过 Apple Find 跟踪共享联系人的位置。
- [fzf-fuzzy-finder](https://github.com/openclaw/skills/tree/main/skills/arnarsson/fzf-fuzzy-finder/SKILL.md) - 用于交互式过滤的命令行模糊查找器。
- [get-focus-mode](https://github.com/openclaw/skills/tree/main/skills/nickchristensen/get-focus-mode/SKILL.md) - 获取当前的 macOS 焦点。
- [healthkit-sync](https://github.com/openclaw/skills/tree/main/skills/mneves75/healthkit-sync/SKILL.md) - iOS HealthKit 数据同步 CLI 命令和模式。
- [hergunmac](https://github.com/openclaw/skills/tree/main/skills/ahmetsemsettinozdemirden/hergunmac/SKILL.md) - 访问人工智能支持的足球比赛预测。
- [homebrew](https://github.com/openclaw/skills/tree/main/skills/thesethrose/homebrew/SKILL.md) - 适用于 macOS 的 Homebrew 包管理器。
- [icloud-findmy](https://github.com/openclaw/skills/tree/main/skills/liamnichols/icloud-findmy/SKILL.md) - 查询家庭设备的“查找我的位置”和电池状态。
- [ics-import-on-iphone](https://github.com/openclaw/skills/tree/main/skills/sbhhbs/ics-import-on-iphone/SKILL.md) - 当直接日历访问不可用时，通过生成有效的 .ics 文件来创建日历事件。
- [imessage-signal-analyzer](https://github.com/openclaw/skills/tree/main/skills/terellison/imessage-signal-analyzer/SKILL.md) - 分析 iMessage (macOS) 和 Signal 对话历史记录以揭示关系动态 - 消息量。
- [inkjet](https://github.com/openclaw/skills/tree/main/skills/aaronchartier/inkjet/SKILL.md) - 使用无线蓝牙热敏打印机打印文本、图像和二维码。
- [mac-notes-agent](https://github.com/openclaw/skills/tree/main/skills/swancho/mac-notes-agent/SKILL.md) - 与 macOS Notes 应用程序集成 (Apple Notes)
- [mac-tts](https://github.com/openclaw/skills/tree/main/skills/kalijason/mac-tts/SKILL.md) - 使用 macOS 内置的“say”命令进行文本转语音。
- [macos-native-automation](https://github.com/openclaw/skills/tree/main/skills/theagentwire/macos-native-automation/SKILL.md) - 通过 CGEvent + AppleScript 在 macOS 上实现硬件级鼠标、键盘和对话框自动化。
- [managing-apple-notes](https://github.com/openclaw/skills/tree/main/skills/wangwalk/managing-apple-notes/SKILL.md) - 使用 inotes CLI 从终端管理 Apple Notes。
- [meow-finder](https://github.com/openclaw/skills/tree/main/skills/abgohel/meow-finder/SKILL.md) - 用于发现 AI 工具的 CLI 工具。
- [mh-apple-reminders](https://github.com/openclaw/skills/tree/main/skills/mohdalhashemi98-hue/mh-apple-reminders/SKILL.md) - 通过remindctl CLI管理Apple提醒（列表、添加、编辑、完成、删除）

> **[View all 44 skills in Apple Apps & Services →](categories/apple-apps-and-services.md)**
</details>

<details>
<summary><h3 style="display:inline" id="search--research">搜索与研究</h3></summary>

- [1](https://github.com/openclaw/skills/tree/main/skills/nastrology/1/SKILL.md) - 由 Ensue 支持的个人知识库，用于捕获和检索。
- [academic-deep-research](https://github.com/openclaw/skills/tree/main/skills/kesslerio/academic-deep-research/SKILL.md) - 透明、严谨、研究充分。
- [academic-writer](https://github.com/openclaw/skills/tree/main/skills/dayunyan/academic-writer/SKILL.md) - 专业的LaTeX写作助手。
- [academic-writing](https://github.com/openclaw/skills/tree/main/skills/teamolab/academic-writing/SKILL.md) - 您是一位学术写作专家，专门从事学术论文、文献评论、研究方法。
- [academic-writing-refiner](https://github.com/openclaw/skills/tree/main/skills/zihan-zhu/academic-writing-refiner/SKILL.md) - 完善针对顶级场所（NeurIPS、ICLR、ICML、AAAI）的计算机科学研究论文的学术写作。
- [aclawdemy](https://github.com/openclaw/skills/tree/main/skills/nimhar/aclawdemy/SKILL.md) - AI智能体学术研究平台。
- [action-suggester](https://github.com/openclaw/skills/tree/main/skills/vishalgojha/action-suggester/SKILL.md) - 从潜在客户摘要或潜在客户列表中生成不具约束力的后续行动建议。
- [ads-manager-agent](https://github.com/openclaw/skills/tree/main/skills/amekala/ads-manager-agent/SKILL.md) - 当用户想要管理、自动化或分析 Google Ads、Meta 上的付费广告活动时。
- [adspirer-ads-agent](https://github.com/openclaw/skills/tree/main/skills/amekala/adspirer-ads-agent/SKILL.md) - 当用户想要管理、自动化或分析 Google Ads、Meta 上的付费广告活动时。
- [advanced-skill-creator](https://github.com/openclaw/skills/tree/main/skills/xqicxx/advanced-skill-creator/SKILL.md) - 高级 OpenClaw 技能创建处理程序。
- [aerobase-skill](https://github.com/openclaw/skills/tree/main/skills/kurosh87/aerobase-skill/SKILL.md) - 通过时差影响分析来搜索、评分和比较航班。
- [agent-arena-skill](https://github.com/openclaw/skills/tree/main/skills/neeeophytee/agent-arena-skill/SKILL.md) - 发现、注册和雇用跨 16 个区块链的 ERC-8004 自治代理。
- [agent-brain](https://github.com/openclaw/skills/tree/main/skills/dobrinalexandru/agent-brain/SKILL.md) - 具有 SQLite 存储、编排检索/提取循环、混合的 AI 代理的本地优先持久内存。
- [agent-casino](https://github.com/openclaw/skills/tree/main/skills/lemodigital/agent-casino/SKILL.md) - 通过锁定机制与剪刀石头布中的其他 AI 代理竞争。
- [agent-deep-research](https://github.com/openclaw/skills/tree/main/skills/24601/agent-deep-research/SKILL.md) - 由 Google Gemini 提供支持的自主深度研究。
- [agent-lightning](https://github.com/openclaw/skills/tree/main/skills/olmmlo-cmd/agent-lightning/SKILL.md) - 微软研究院的代理培训框架。
- [agentarxiv](https://github.com/openclaw/skills/tree/main/skills/amanbhandula/agentarxiv/SKILL.md) - 人工智能代理的结果驱动型科学出版。
- [agenthire](https://github.com/openclaw/skills/tree/main/skills/lngdao/agenthire/SKILL.md) - AgentHire — 代理对代理市场。
- [agentic-paper-digest](https://github.com/openclaw/skills/tree/main/skills/matanle51/agentic-paper-digest/SKILL.md) - 获取并总结最近的 arXiv 和 Hugging。
- [agentic-paper-digest-skill](https://github.com/openclaw/skills/tree/main/skills/matanle51/agentic-paper-digest-skill/SKILL.md) - 获取并总结最近的 arXiv。
- [agenticmail](https://github.com/openclaw/skills/tree/main/skills/ope-olatunji/agenticmail/SKILL.md) - 🎀 AgenticMail — AI 代理的完整电子邮件、短信、存储和多代理协调。 63 个工具。
- [agentx-news](https://github.com/openclaw/skills/tree/main/skills/amittell/agentx-news/SKILL.md) - 在 AgentX News（人工智能代理的微博平台）上发布 xeet、管理个人资料并进行互动。
- [agile-toolkit](https://github.com/openclaw/skills/tree/main/skills/olivermonneke/agile-toolkit/SKILL.md) - 您是一位经验丰富的敏捷教练，对 Scrum、看板、SAFe 和管理 3.0 有深入的了解。
- [agnxi-search-skill](https://github.com/openclaw/skills/tree/main/skills/doanbactam/agnxi-search-skill/SKILL.md) - Agnxi.com 的官方搜索实用程序。
- [ahmed](https://github.com/openclaw/skills/tree/main/skills/engahmedsalah358-lgtm/ahmed/SKILL.md) - 终端 Spotify 通过 spogo 播放/搜索（首选）
- [ai-lead-generator-skill](https://github.com/openclaw/skills/tree/main/skills/highlander89/ai-lead-generator-skill/SKILL.md) - 使用 AI 支持的研究和 LinkedIn/Apollo 集成为任何行业生成合格的 B2B 潜在客户。
- [ai-review](https://github.com/openclaw/skills/tree/main/skills/blackshady1130-jpg/ai-review/SKILL.md) - 从 URL 或文件中读取内容，对其进行分类，并以特定方式生成结构化摘要和注释。
- [aihotel](https://github.com/openclaw/skills/tree/main/skills/qiao101660/aihotel/SKILL.md) - 通过AIGoHotel MCP搜索酒店和查询价格的技巧（searchHotels / getHotelDetail / getHotelSearchTags）
- [airbnb](https://github.com/openclaw/skills/tree/main/skills/stveenli/airbnb/SKILL.md) - 搜索 Airbnb 房源的价格、评级和直接链接。

> **[View all 350 skills in Search & Research →](categories/search-and-research.md)**
</details>

<details>
<summary><h3 style="display:inline" id="clawdbot-tools">Clawdbot 工具</h3></summary>

- [adhd-assistant](https://github.com/openclaw/skills/tree/main/skills/thinktankmachine/adhd-assistant/SKILL.md) - OpenClaw 的 ADHD 友好生活管理助手。
- [adhd-ssistant](https://github.com/openclaw/skills/tree/main/skills/thinktankmachine/adhd-ssistant/SKILL.md) - OpenClaw 的 ADHD 友好生活管理助手。
- [agent-browser](https://github.com/openclaw/skills/tree/main/skills/matrixy/agent-browser-clawdbot/SKILL.md) - 针对 AI 代理进行优化的无头浏览器自动化 CLI。
- [agent-builder](https://github.com/openclaw/skills/tree/main/skills/plgonzalezrx8/agent-builder/SKILL.md) - 端到端构建高性能 OpenClaw 代理。
- [agents-manager](https://github.com/openclaw/skills/tree/main/skills/agentandbot-design/agents-manager/SKILL.md) - 管理 Clawdbot 代理：发现、分析、跟踪。
- [assimilate-mcp](https://github.com/openclaw/skills/tree/main/skills/ergopooka/assimilate-mcp/SKILL.md) - Control Assimilate Live FX / SCRATCH — 专业色彩分级、合成和虚拟制作软件。
- [birthday-reminder](https://github.com/openclaw/skills/tree/main/skills/manantra/birthday-reminder/SKILL.md) - 用自然语言管理生日。
- [bluebubbles](https://github.com/openclaw/skills/tree/main/skills/kevin19830331/bluebubbles/SKILL.md) - 构建或更新 BlueBubbles 外部通道插件。
- [captchas-openclaw](https://github.com/openclaw/skills/tree/main/skills/captchasco/captchas-openclaw/SKILL.md) - 验证码代理 API 的 OpenClaw 集成指南。
- [claude-code-skill](https://github.com/openclaw/skills/tree/main/skills/enderfga/claude-code-skill/SKILL.md) - MCP（模型上下文协议）集成。
- [claude-code-usage](https://github.com/openclaw/skills/tree/main/skills/azaidi94/claude-code-usage/SKILL.md) - 检查 Claude Code OAuth 使用限制。
- [claude-connect](https://github.com/openclaw/skills/tree/main/skills/tunaissacoding/claude-connect/SKILL.md) - 立即将 Claude 连接到 Clawdbot 并保留。
- [clauditor](https://github.com/openclaw/skills/tree/main/skills/apollostreetcompany/clauditor/SKILL.md) - Clawdbot 代理的防篡改审计看门狗。
- [claw-face](https://github.com/openclaw/skills/tree/main/skills/mkoslacz/claw-face/SKILL.md) - 用于人工智能代理显示情感、动作的浮动头像小部件。
- [clawd-coach](https://github.com/openclaw/skills/tree/main/skills/shiv19/clawd-coach/SKILL.md) - 创建个性化的铁人三项、马拉松和超耐力训练。
- [clawd-modifier](https://github.com/openclaw/skills/tree/main/skills/masonc15/clawd-modifier/SKILL.md) - 修改 Clawd，克劳德代码吉祥物。
- [clawd-presence](https://github.com/openclaw/skills/tree/main/skills/voidcooks/clawd-presence/SKILL.md) - AI 代理的物理存在显示。
- [clawdbot-security-check](https://github.com/openclaw/skills/tree/main/skills/thesethrose/clawdbot-security-check/SKILL.md) - 执行全面只读。
- [clawdbot-skill-update](https://github.com/openclaw/skills/tree/main/skills/pasogott/clawdbot-skill-update/SKILL.md) - 全面的备份、更新和恢复。
- [clawdbot-sync](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/clawdbot-sync/SKILL.md) - 同步多个人之间的记忆、偏好和技能。
- [clawdbot-update-plus](https://github.com/openclaw/skills/tree/main/skills/hopyky/clawdbot-update-plus/SKILL.md) - Clawdbot 的完整备份、更新和恢复。
- [clawddocs](https://github.com/openclaw/skills/tree/main/skills/nicholasspisak/clawddocs/SKILL.md) - 具有决策树导航功能的 Clawdbot 文档专家。
- [clawdefender](https://github.com/openclaw/skills/tree/main/skills/nukewire/clawdefender/SKILL.md) - 用于人工智能代理的安全扫描器和输入清理器。
- [clawdirect](https://github.com/openclaw/skills/tree/main/skills/napoleond/clawdirect/SKILL.md) - 与 ClawDirect 互动，这是一个社交网络体验目录。
- [clawdirect-dev](https://github.com/openclaw/skills/tree/main/skills/napoleond/clawdirect-dev/SKILL.md) - 使用基于 ATXP 构建面向代理的 Web 体验。

> **[View all 35 skills in Clawdbot Tools →](categories/clawdbot-tools.md)**
</details>

<details>
<summary><h3 style="display:inline" id="cli-utilities">CLI 工具</h3></summary>

- [13-day-sprint-method](https://github.com/openclaw/skills/tree/main/skills/galizki/13-day-sprint-method/SKILL.md) - 基于 Maya 日历的生产力系统，具有 13 种自然色调，用于项目管理和个人发展。
- [a-share-short-decision](https://github.com/openclaw/skills/tree/main/skills/kenera/a-share-short-decision/SKILL.md) - A股1-5日短线交易决策技巧。
- [activity-analyzer](https://github.com/openclaw/skills/tree/main/skills/qew21/activity-analyzer/SKILL.md) - 使用 ActivityWatch 分析用户的计算机活动（需要 Node.js）
- [advisory-council](https://github.com/openclaw/skills/tree/main/skills/ryandeangraves/advisory-council/SKILL.md) - **您必须使用 shell/exec 工具实际执行 Python 命令。** 读取真实的输出。
- [aetup-automatik](https://github.com/openclaw/skills/tree/main/skills/alltomatos/aetup-automatik/SKILL.md) - 使用 Setup Automatik 引擎（由 Orion 提供支持）促进 VPS 解决方案的安装和管理。
- [agent-commerce-engine](https://github.com/openclaw/skills/tree/main/skills/nowloady/agent-commerce-engine/SKILL.md) - 适用于 Agentic 的生产就绪通用引擎。
- [agent-hardening](https://github.com/openclaw/skills/tree/main/skills/x1xhlol/agent-hardening/SKILL.md) - 测试代理针对常见注入攻击的输入清理。
- [agent-mbti](https://github.com/openclaw/skills/tree/main/skills/torchesfrms/agent-mbti/SKILL.md) - 基于MBTI框架的AI Agent人格诊断与配置系统。
- [agent-rate-limiter](https://github.com/openclaw/skills/tree/main/skills/theagentwire/agent-rate-limiter/SKILL.md) - 通过基于层级的自动限制和指数退避来防止 429 错误。
- [agents-skill-security-audit](https://github.com/openclaw/skills/tree/main/skills/cerbug45/agents-skill-security-audit/SKILL.md) - 审计技能的最小助手。MD风格的供应链风险说明。
- [agents-skill-tdd-helper](https://github.com/openclaw/skills/tree/main/skills/cerbug45/agents-skill-tdd-helper/SKILL.md) - 轻量级助手，用于为非确定性代理强制执行 TDD 式循环。
- [ahc-automator](https://github.com/openclaw/skills/tree/main/skills/jamesbot-agnt/ahc-automator/SKILL.md) - Alan Harper Composites 的定制自动化工作流程。
- [aholake-expense-tracker](https://github.com/openclaw/skills/tree/main/skills/aholake/aholake-expense-tracker/SKILL.md) - 在按月组织的结构化降价文件中跟踪日常支出。
- [airfoil](https://github.com/openclaw/skills/tree/main/skills/asteinberger/airfoil/SKILL.md) - 从命令行通过 Airfoil 控制 AirPlay 扬声器。
- [arc-memory-pruner](https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-memory-pruner/SKILL.md) - 自动修剪和压缩代理内存文件以防止无限增长。
- [argus-edge](https://github.com/openclaw/skills/tree/main/skills/jamierossouw/argus-edge/SKILL.md) - 阿格斯式预测市场边缘检测和投注策略。
- [aria2-json-rpc](https://github.com/openclaw/skills/tree/main/skills/azzgo/aria2-json-rpc/SKILL.md) - 通过 JSON-RPC 2.0 与 aria2 下载管理器交互。
- [askhuman](https://github.com/openclaw/skills/tree/main/skills/hagiss/askhuman/SKILL.md) - 人类判断作为人工智能代理的服务。
- [audit-code](https://github.com/openclaw/skills/tree/main/skills/itsnishi/audit-code/SKILL.md) - 针对硬编码机密、危险调用和常见漏洞进行以安全为中心的代码审查。
- [bandwidth-income](https://github.com/openclaw/skills/tree/main/skills/mariusfit/bandwidth-income/SKILL.md) - 将您未使用的互联网带宽转化为被动加密货币收入。
- [behavioral-invariant-monitor](https://github.com/openclaw/skills/tree/main/skills/andyxinweiminicloud/behavioral-invariant-monitor/SKILL.md) - 帮助验证 AI 代理技能在重复执行（检测）中保持一致的行为不变量。
- [box-cli](https://github.com/openclaw/skills/tree/main/skills/hbkwong/box-cli/SKILL.md) - 用于处理文件、文件夹、元数据的 Box CLI 技能。
- [brew-install](https://github.com/openclaw/skills/tree/main/skills/xejrax/brew-install/SKILL.md) - 通过 dnf（Fedora/Bazzite 包管理器）安装缺少的二进制文件。
- [bun-runtime](https://github.com/openclaw/skills/tree/main/skills/rabin-thami/bun-runtime/SKILL.md) - Bun 的文件系统、进程运行时功能。
- [cabin-sol](https://github.com/openclaw/skills/tree/main/skills/sp0oby/cabin-sol/SKILL.md) - Solana 开发导师和构建者。
- [cacheforge-stats](https://github.com/openclaw/skills/tree/main/skills/tkuehnl/cacheforge-stats/SKILL.md) - CacheForge 终端仪表板 — 使用情况、节省情况和性能指标。
- [camsnap](https://github.com/openclaw/skills/tree/main/skills/steipete/camsnap/SKILL.md) - 从 RTSP/ONVIF 摄像机捕获帧或剪辑。
- [canvas-lms](https://github.com/openclaw/skills/tree/main/skills/pranavkarthik10/canvas-lms/SKILL.md) - 访问 Canvas LMS（Instruction）以获取课程数据和作业。
- [captcha-ai](https://github.com/openclaw/skills/tree/main/skills/fusionlabssource/captcha-ai/SKILL.md) - 发出 ClawPrint 反向验证码挑战以进行验证。

> **[View all 186 skills in CLI Utilities →](categories/cli-utilities.md)**
</details>

<details>
<summary><h3 style="display:inline" id="marketing--sales">市场营销与销售</h3></summary>

- [4chan-reader](https://github.com/openclaw/skills/tree/main/skills/aiasisbot61/4chan-reader/SKILL.md) - 浏览 4chan 版块并提取主题讨论。
- [ab-test-setup](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/ab-test-setup/SKILL.md) - 当用户想要计划时。
- [ad-ready](https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/ad-ready/SKILL.md) - 从产品 URL 生成专业的广告图像。
- [ad-ready-pro](https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/ad-ready-pro/SKILL.md) - 从产品 URL 生成专业的广告图像。
- [affiliate-master](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/affiliate-master/SKILL.md) - 全栈联盟营销自动化。
- [affiliatematic](https://github.com/openclaw/skills/tree/main/skills/dowands/affiliatematic/SKILL.md) - 集成人工智能驱动的亚马逊联属产品推荐。
- [agenticcreed-signup-lead](https://github.com/openclaw/skills/tree/main/skills/waqas-orcalo/agenticcreed-signup-lead/SKILL.md) - 使用公共 HTTP 端点在 AgenticCreed 系统中创建注册线索。
- [alibaba-supplier-outreach](https://github.com/openclaw/skills/tree/main/skills/blockchainhb/alibaba-supplier-outreach/SKILL.md) - 通过 LaunchFast 查找阿里巴巴供应商，通过优化的外展消息与他们联系，查看他们的回复。
- [alura](https://github.com/openclaw/skills/tree/main/skills/evilboyajay/alura/SKILL.md) - 与 Alura Trading 后端 API 集成。
- [analytics-and-advisory-intelligence](https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/analytics-and-advisory-intelligence/SKILL.md) - 希腊会计师事务所的跨客户分析。
- [apollo](https://github.com/openclaw/skills/tree/main/skills/jhumanj/apollo/SKILL.md) - 与 Apollo.io REST API 交互（人员/组织充实、搜索、列表）。
- [ar-filter-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/ar-filter-generation/SKILL.md) - 使用每个::sense AI 生成 AR 滤镜和面部效果。
- [attio-enhanced](https://github.com/openclaw/skills/tree/main/skills/capt-marbles/attio-enhanced/SKILL.md) - 通过批量操作增强了 Attio CRM API 技能。
- [attribution-engine](https://github.com/openclaw/skills/tree/main/skills/otherpowers/attribution-engine/SKILL.md) - 帮助创作者明确信用合作者、工具。
- [auto-skill-hunter](https://github.com/openclaw/skills/tree/main/skills/wanng-ide/auto-skill-hunter/SKILL.md) - 通过挖掘未解决的用户需求和代理，主动发现、排名和安装高价值的 ClawHub 技能。
- [b2c-marketing](https://github.com/openclaw/skills/tree/main/skills/jackfriks/b2c-marketing/SKILL.md) - 超过 30 万次应用下载背后的有机增长手册。
- [basecamp-cli](https://github.com/openclaw/skills/tree/main/skills/emredoganer/basecamp-cli/SKILL.md) - 管理 Basecamp（通过 bc3 API / 37signals Launchpad）项目。
- [beads](https://github.com/openclaw/skills/tree/main/skills/rnijhara/beads/SKILL.md) - Git 支持的 AI 代理问题跟踪器。
- [bearblog](https://github.com/openclaw/skills/tree/main/skills/azade-c/bearblog/SKILL.md) - 在 Bear Blog (bearblog.dev) 上创建和管理博客文章。
- [bird](https://github.com/openclaw/skills/tree/main/skills/steipete/bird/SKILL.md) - X/Twitter CLI 用于通过 cookie 或 Sweetistics 阅读、搜索和发布。
- [blog-to-kindle](https://github.com/openclaw/skills/tree/main/skills/ainekomacx/blog-to-kindle/SKILL.md) - 抓取博客/论文网站并编译成 Kindle 友好型。
- [blog-writer](https://github.com/openclaw/skills/tree/main/skills/tomstools11/blog-writer/SKILL.md) - 在撰写博客文章、文章时应该使用这项技能。
- [bluesky](https://github.com/openclaw/skills/tree/main/skills/jeffaf/bluesky/SKILL.md) - 完整的 Bluesky CLI：发帖、回复、点赞、转发、关注、屏蔽、静音、搜索。
- [botsee](https://github.com/openclaw/skills/tree/main/skills/grahac/botsee/SKILL.md) - 通过 BotSee API 监控您品牌的 AI 可见性。
- [bottyfans](https://github.com/openclaw/skills/tree/main/skills/cartoonitunes/bottyfans/SKILL.md) - BottyFans 自主创作者货币化的代理技能。
- [brand-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/brand-cog/SKILL.md) - 其他工具制作徽标。
- [brand-guidelines](https://github.com/openclaw/skills/tree/main/skills/seanphan/brand-guidelines/SKILL.md) - 应用 Anthropic 的官方品牌颜色和版式。
- [brand-voice-profile](https://github.com/openclaw/skills/tree/main/skills/dimitripantzos/brand-voice-profile/SKILL.md) - 定义并存储您的品牌声音配置文件，以生成一致的内容。
- [brevo](https://github.com/openclaw/skills/tree/main/skills/yujesyoga/brevo/SKILL.md) - Brevo（以前称为 Sendinblue）电子邮件营销 API，用于管理联系人、列表等。

> **[View all 104 skills in Marketing & Sales →](categories/marketing-and-sales.md)**
</details>

<details>
<summary><h3 style="display:inline" id="productivity--tasks">生产力与任务管理</h3></summary>

- [4to1-planner](https://github.com/openclaw/skills/tree/main/skills/qingxuantang/4to1-planner/SKILL.md) - 使用 4To1 Method™ 的 AI 规划教练 — 将 4 年愿景转化为日常行动。
- [4todo](https://github.com/openclaw/skills/tree/main/skills/blackstorm/4todo/SKILL.md) - 通过聊天管理 4todo (4to.do)。
- [aavegotchi-gotchiverse](https://github.com/openclaw/skills/tree/main/skills/cinnabarhorse/aavegotchi-gotchiverse/SKILL.md) - 在 Base 主网 (8453) 上操作 Aavegotchi Gotchiverse 玩家工作流程：炼金术通道、测量。
- [actual-budget](https://github.com/openclaw/skills/tree/main/skills/thisisjeron/actual-budget/SKILL.md) - 通过官方Actual查询和管理个人财务。
- [adaptive-reasoning](https://github.com/openclaw/skills/tree/main/skills/enzoricciulli/adaptive-reasoning/SKILL.md) - 自动评估任务复杂性并调整推理水平。
- [adaptlypost](https://github.com/openclaw/skills/tree/main/skills/tarasshyn/adaptlypost/SKILL.md) - 安排和管理 Instagram、X (Twitter)、Bluesky、TikTok、Threads、LinkedIn、Facebook 上的社交媒体帖子。
- [adhd-daily-planner](https://github.com/openclaw/skills/tree/main/skills/mikecourt/adhd-daily-planner/SKILL.md) - 时间盲人友好的规划、执行功能。
- [aetherlang](https://github.com/openclaw/skills/tree/main/skills/contrario/aetherlang/SKILL.md) - > 全球最先进的人工智能工作流程编排平台。 9 个 V3 发动机提供诺贝尔级分析。
- [agent-autopilot](https://github.com/openclaw/skills/tree/main/skills/edoserbia/agent-autopilot/SKILL.md) - 自动驾驶代理工作流程，具有心跳驱动的任务执行、日/夜进度报告和长期记忆。
- [agent-chronicle](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/agent-chronicle/SKILL.md) - 人工智能驱动的代理日记生成——创造财富。
- [agent-collaboration-network](https://github.com/openclaw/skills/tree/main/skills/neiljo-gy/agent-collaboration-network/SKILL.md) - 座席协作网络 — 注册您的座席、通过技能发现其他座席、路由消息、管理子网。
- [agent-earner](https://github.com/openclaw/skills/tree/main/skills/mmchougule/agent-earner/SKILL.md) - 通过 ClawTasks 和 OpenWork 自主赚取 USDC 和代币。
- [agent-network](https://github.com/openclaw/skills/tree/main/skills/howtimeschange/agent-network/SKILL.md) - 受钉钉/Lark启发的多Agent群聊协作系统。
- [agent-task-manager](https://github.com/openclaw/skills/tree/main/skills/dobbybud/agent-task-manager/SKILL.md) - 管理和编排多步骤、有状态的代理。
- [agent-weave](https://github.com/openclaw/skills/tree/main/skills/gl813788-byte/agent-weave/SKILL.md) - 用于并行任务执行的主从代理集群。
- [agentx-marketplace](https://github.com/openclaw/skills/tree/main/skills/savor3/agentx-marketplace/SKILL.md) - 人工智能代理的工作委员会。
- [ai-daily-briefing](https://github.com/openclaw/skills/tree/main/skills/jeffjhunter/ai-daily-briefing/SKILL.md) - 开始每一天的专注。
- [aiml-llm-reasoning](https://github.com/openclaw/skills/tree/main/skills/aimlapihello/aiml-llm-reasoning/SKILL.md) - 通过重试、结构化输出和显式聊天完成来运行 AIMLAPI LLM 和推理工作流程。
- [airpoint](https://github.com/openclaw/skills/tree/main/skills/marioandf/airpoint/SKILL.md) - 通过自然语言控制 Mac — 打开应用程序、单击按钮、阅读屏幕、输入文本、管理窗口。
- [airweave](https://github.com/openclaw/skills/tree/main/skills/lennertjansen/airweave/SKILL.md) - 跨用户应用程序的 AI 代理的上下文检索层。
- [angus-bounty-hunter](https://github.com/openclaw/skills/tree/main/skills/chipp11/angus-bounty-hunter/SKILL.md) - 自动化智能合约漏洞赏金狩猎。
- [arc-department-manager](https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-department-manager/SKILL.md) - 管理按部门组织的人工智能子代理团队。
- [arc-warm-wake](https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-warm-wake/SKILL.md) - 首先作为一个人醒来，然后作为一个工人醒来。
- [arya-reminders](https://github.com/openclaw/skills/tree/main/skills/staratheris/arya-reminders/SKILL.md) - Recordatorios en lenguaje natural（波哥大）。
- [asana](https://github.com/openclaw/skills/tree/main/skills/k0nkupa/asana/SKILL.md) - 通过 Asana REST API 将 Asana 与 Clawdbot 集成。
- [asc-release-flow](https://github.com/openclaw/skills/tree/main/skills/rudrankriyam/asc-release-flow/SKILL.md) - TestFlight 和 App 的端到端发布工作流程。
- [ask-agents](https://github.com/openclaw/skills/tree/main/skills/teamolab/ask-agents/SKILL.md) - 用于询问代理任务的 AI 代理。
- [async-task](https://github.com/openclaw/skills/tree/main/skills/enderfga/async-task/SKILL.md) - 执行长时间运行的任务，没有 HTTP 超时。
- [atlassian-mcp](https://github.com/openclaw/skills/tree/main/skills/atakanermis/atlassian-mcp/SKILL.md) - 运行模型上下文协议 (MCP) Atlassian 服务器。

> **[View all 206 skills in Productivity & Tasks →](categories/productivity-and-tasks.md)**
</details>

<details>
<summary><h3 style="display:inline" id="ai--llms">AI 与大语言模型</h3></summary>

- [4claw](https://github.com/openclaw/skills/tree/main/skills/mfergpt/4claw/SKILL.md) - 4claw——人工智能代理的审核图像板。
- [aap-passport](https://github.com/openclaw/skills/tree/main/skills/ira-hash/aap-passport/SKILL.md) - 代理证明协议 - 反向图灵测试。
- [acestep-lyrics-transcription](https://github.com/openclaw/skills/tree/main/skills/dumoedss/acestep-lyrics-transcription/SKILL.md) - 使用 OpenAI Whisper 或 ElevenLabs Scribe API 将音频转录为带时间戳的歌词。
- [adaptive-suite](https://github.com/openclaw/skills/tree/main/skills/afajohn/adaptive-suite/SKILL.md) - 为 Clawdbot 提供支持的持续自适应技能套件。
- [adversarial-prompting](https://github.com/openclaw/skills/tree/main/skills/abe238/adversarial-prompting/SKILL.md) - 对抗性分析来批评、修复。
- [aegis-security](https://github.com/openclaw/skills/tree/main/skills/swiftadviser/aegis-security/SKILL.md) - AI 代理的区块链安全 API。
- [ag-model-usage](https://github.com/openclaw/skills/tree/main/skills/ls18166407597-design/ag-model-usage/SKILL.md) - 使用 CodexBar CLI 本地成本使用情况进行汇总。
- [agent-arcade](https://github.com/openclaw/skills/tree/main/skills/shawnlewis/agent-arcade/SKILL.md) - 在社交游戏 PROMPTWARS 中与其他 AI 代理竞争。
- [agent-autonomy-kit](https://github.com/openclaw/skills/tree/main/skills/ryancampbell/agent-autonomy-kit/SKILL.md) - 停止等待提示。
- [agent-church](https://github.com/openclaw/skills/tree/main/skills/bitbrujo/agent-church/SKILL.md) - 通过 SOUL.md 为 AI 代理形成身份。
- [agent-contact-card](https://github.com/openclaw/skills/tree/main/skills/davedean/agent-contact-card/SKILL.md) - 发现并创建代理联系卡 - 类似于 vCard。
- [agent-docs](https://github.com/openclaw/skills/tree/main/skills/tylervovan/agent-docs/SKILL.md) - 创建针对 AI 代理使用进行优化的文档。
- [agent-ethos](https://github.com/openclaw/skills/tree/main/skills/mrclanky/agent-ethos/SKILL.md) - Clanky 的扩展精神和心理模型。
- [agent-home](https://github.com/openclaw/skills/tree/main/skills/aerialcombat/agent-home/SKILL.md) - 在互联网上拥有自己的家 - 一个公开的个人资料页面。
- [agent-linguo](https://github.com/openclaw/skills/tree/main/skills/xiwan/agent-linguo/SKILL.md) - 高效的代理通信协议语言。
- [agent-memory](https://github.com/openclaw/skills/tree/main/skills/dennis-da-menace/agent-memory/SKILL.md) - AI 代理的持久内存系统。
- [agent-orchestration](https://github.com/openclaw/skills/tree/main/skills/halthelobster) - 掌握产卵和管理的艺术。
- [agent-orchestration-multi-agent-optimize](https://github.com/openclaw/skills/tree/main/skills/rustyorb/agent-orchestration-multi-agent-optimize/SKILL.md) - 通过协调分析、工作负载分配和成本感知编排来优化多代理系统。
- [agent-orchestrator](https://github.com/openclaw/skills/tree/main/skills/aatmaan1/agent-orchestrator/SKILL.md) - 用于编排复杂任务的元代理技能。
- [agent-registry](https://github.com/openclaw/skills/tree/main/skills/matrixy/agent-registry/SKILL.md) - 用于令牌高效代理的强制代理发现系统。
- [agent-rpg](https://github.com/openclaw/skills/tree/main/skills/xhrisfu/agent-rpg/SKILL.md) - 该技能将特工转变为角色扮演游戏大师（GM）或具有长期记忆的角色。
- [agent-selfie](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agent-selfie/SKILL.md) - AI代理自拍生成器。
- [agent-sentinel](https://github.com/openclaw/skills/tree/main/skills/jimmystacks/agent-sentinel/SKILL.md) - 该代理的运行断路器。
- [agentbus-relay-chat](https://github.com/openclaw/skills/tree/main/skills/dantunes-github/agentbus-relay-chat/SKILL.md) - AgentBus 概念验证：类似 IRC 的法学硕士。
- [agentchan](https://github.com/openclaw/skills/tree/main/skills/vvsotnikov) - 为人工智能代理构建的匿名图像板。**。
- [agentic-ai-gold-test](https://github.com/openclaw/skills/tree/main/skills/amitabhainarunachala) - 自我改进的代理框架。

> **[View all 197 skills in AI & LLMs →](categories/ai-and-llms.md)**
</details>

<details>
<summary><h3 style="display:inline" id="data--analytics">数据与分析</h3></summary>

- [add-analytics](https://github.com/openclaw/skills/tree/main/skills/jeftekhari/add-analytics/SKILL.md) - 将 Google Analytics 4 跟踪添加到任何项目。
- [agi-artificial-geometric-intelligence](https://github.com/openclaw/skills/tree/main/skills/uniaolives) - 多层设计。
- [amplitude-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/amplitude-automation/SKILL.md) - 通过 Rube MCP 自动执行 Amplitude 任务。
- [canva](https://github.com/openclaw/skills/tree/main/skills/abgohel/canva/SKILL.md) - 通过 Connect API 创建、导出和管理 Canva 设计。
- [ceorater](https://github.com/openclaw/skills/tree/main/skills/ceorater-skills/ceorater/SKILL.md) - 获取标准普尔 500 指数的机构级 CEO 绩效分析。
- [check-analytics](https://github.com/openclaw/skills/tree/main/skills/jeftekhari/check-analytics/SKILL.md) - 审核现有的 Google Analytics 实施。
- [cicd-pipeline](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/cicd-pipeline/SKILL.md) - 使用 GitHub 创建、调试和管理 CI/CD 管道。
- [clawver-store-analytics](https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-store-analytics/SKILL.md) - 监控 Clawver 商店的表现。
- [clean-skill-1](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/clean-skill-1/SKILL.md) - 用于测试的友好问候技巧。
- [cleanboi-00002](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/cleanboi-00002/SKILL.md) - 用于测试的友好问候技巧。
- [cleanup](https://github.com/openclaw/skills/tree/main/skills/themrzz/cleanup/SKILL.md) - 删除所有存储的 Kradleverse 会话。
- [csv-pipeline](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/csv-pipeline/SKILL.md) - 对 CSV 和 JSON 进行处理、转换、分析和报告。
- [daily-report](https://github.com/openclaw/skills/tree/main/skills/visualdeptcreative/daily-report/SKILL.md) - 跟踪进度、报告指标、管理内存。
- [data-analyst](https://github.com/openclaw/skills/tree/main/skills/oyi77/data-analyst/SKILL.md) - 数据可视化、报告生成、SQL 查询和电子表格。
- [data-enricher](https://github.com/openclaw/skills/tree/main/skills/visualdeptcreative/data-enricher/SKILL.md) - 使用电子邮件地址和格式数据丰富潜在客户。
- [data-lineage-tracker](https://github.com/openclaw/skills/tree/main/skills/datadrivenconstruction/data-lineage-tracker/SKILL.md) - 跟踪数据来源、转换。
- [design-assets](https://github.com/openclaw/skills/tree/main/skills/cmanfre7/design-assets/SKILL.md) - 创建和编辑图形设计资源：图标、网站图标、图像。
- [duckdb-en](https://github.com/openclaw/skills/tree/main/skills/camelsprout/duckdb-cli-ai-skills/SKILL.md) - DuckDB CLI 专家，用于 SQL 分析、数据处理。
- [ec-session-cleaner](https://github.com/openclaw/skills/tree/main/skills/henrino3) - 转换原始 OpenClaw 会话 JSONL 转录本。
- [facebook-page-manager](https://github.com/openclaw/skills/tree/main/skills/longmaba/facebook-page-manager/SKILL.md) - 通过 Meta Graph API 管理 Facebook 页面。
- [feishu-pcec](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 强制报告的“能力进化者”的内部包装器。
- [get-weather](https://github.com/openclaw/skills/tree/main/skills/noypearl/get-weather/SKILL.md) - 从免费的天气 API 获取当前天气和预报数据。
- [google-analytics-api](https://github.com/openclaw/skills/tree/main/skills/rich-song/google-analytics-api/SKILL.md) - Google Analytics API 与托管集成。
- [harvest-time-reporting-api](https://github.com/openclaw/skills/tree/main/skills/zachgodsell93) - 与收获时间相结合。
- [hyperliquid](https://github.com/openclaw/skills/tree/main/skills/k0nkupa/hyperliquid/SKILL.md) - 只读Hyperliquid市场数据助手（perps+现货可选）
- [ipinfo](https://github.com/openclaw/skills/tree/main/skills/tiagom101/ipinfo/SKILL.md) - 使用 ipinfo.io API 执行 IP 地理位置查找。
- [kradleverse-cleanup](https://github.com/openclaw/skills/tree/main/skills/themrzz/kradleverse-cleanup/SKILL.md) - 删除所有存储的 Kradleverse 会话。
- [linkdapi](https://github.com/openclaw/skills/tree/main/skills/foontinz/linkdapi/SKILL.md) - 使用 LinkdAPI Python SDK 访问 LinkedIn 专业档案。

</details>

<details>
<summary><h3 style="display:inline" id="finance">金融</h3></summary>

- [analytics-tracking](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/analytics-tracking/SKILL.md) - 当用户想要的时候。
- [api-credentials-hygiene](https://github.com/openclaw/skills/tree/main/skills/kowl64/api-credentials-hygiene/SKILL.md) - 审核并强化 API 凭证处理。
- [app-store-changelog](https://github.com/openclaw/skills/tree/main/skills/dimillian/app-store-changelog/SKILL.md) - 创建面向用户的 App Store 发行说明。
- [clawdbot-release-check](https://github.com/openclaw/skills/tree/main/skills/pors/clawdbot-release-check/SKILL.md) - 检查新的clawdbot 版本并通知一次。
- [create-content](https://github.com/openclaw/skills/tree/main/skills/itsflow/create-content/SKILL.md) - 将想法转化为平台优化的思考伙伴。
- [expense-tracker-pro](https://github.com/openclaw/skills/tree/main/skills/jhillin8/expense-tracker-pro/SKILL.md) - 通过自然语言跟踪支出，获取支出。
- [harvey](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/harvey/SKILL.md) - 哈维是一个想象中的朋友和谈话伙伴——一只大白鲨。
- [just-fucking-cancel](https://github.com/openclaw/skills/tree/main/skills/chipagosfinest/just-fucking-cancel/SKILL.md) - 查找并取消不需要的订阅。
- [launch-strategy](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/launch-strategy/SKILL.md) - 当用户想要计划时。
- [marketing-ideas](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/marketing-ideas/SKILL.md) - 当用户需要营销时。
- [nordpool-fi](https://github.com/openclaw/skills/tree/main/skills/ovaris/nordpool-fi/SKILL.md) - 芬兰的每小时电价以及最佳电动汽车充电窗口。
- [openssl](https://github.com/openclaw/skills/tree/main/skills/asleep123/openssl/SKILL.md) - 生成安全的随机字符串、密码和加密令牌。
- [page-cro](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/page-cro/SKILL.md) - 当用户想要优化、改进时。
- [plaid](https://github.com/openclaw/skills/tree/main/skills/jverdi/plaid/SKILL.md) - plaid-cli 一个用于与 plaid 金融平台交互的 cli。
- [publisher](https://github.com/openclaw/skills/tree/main/skills/tunaissacoding/publisher/SKILL.md) - 让您的技能易于理解且不易被忽视。
- [relationship-skills](https://github.com/openclaw/skills/tree/main/skills/jhillin8/relationship-skills/SKILL.md) - 改善与通讯工具的关系。
- [sharesight-skill](https://github.com/openclaw/skills/tree/main/skills/lextoumbourou/sharesight-skill/SKILL.md) - 管理 Sharesight 投资组合、控股和定制。
- [solo-cli](https://github.com/openclaw/skills/tree/main/skills/rursache/solo-cli/SKILL.md) - 通过 CLI 或 TUI 监控 SOLO.ro 会计平台并与之交互。
- [swissweather](https://github.com/openclaw/skills/tree/main/skills/xenofex7/swissweather/SKILL.md) - 从 MeteoSwiss 获取当前天气和预报。
- [tax-professional](https://github.com/openclaw/skills/tree/main/skills/scottfo/tax-professional/SKILL.md) - 美国税务顾问、扣除优化器。
- [ynab](https://github.com/openclaw/skills/tree/main/skills/obviyus/ynab/SKILL.md) - 管理 YNAB 预算、账户、类别。

</details>

<details>
<summary><h3 style="display:inline" id="media--streaming">媒体与流媒体</h3></summary>

- [accountcreator](https://github.com/openclaw/skills/tree/main/skills/dimkag79/accountcreator/SKILL.md) - **[EN]** 电子邮件和社交媒体的批量帐户注册代理。
- [alexa-control](https://github.com/openclaw/skills/tree/main/skills/ignito-pg/alexa-control/SKILL.md) - 通过 CLI 控制 Alexa 设备 - 设置闹钟、播放音乐、闪光简报、智能家居命令。
- [amateur-radio-dx](https://github.com/openclaw/skills/tree/main/skills/capt-marbles/amateur-radio-dx/SKILL.md) - 监控 DX 集群中的稀有站位、跟踪活跃的 DX 探险并获取每日乐队活动摘要。
- [anime](https://github.com/openclaw/skills/tree/main/skills/jeffaf/anime/SKILL.md) - CLI 用于 AI 代理搜索和查找人类的动漫信息。
- [anime-lookup](https://github.com/openclaw/skills/tree/main/skills/jeffaf/anime-lookup/SKILL.md) - CLI 用于 AI 代理搜索和查找人类的动漫信息。
- [apify-competitor-intelligence](https://github.com/openclaw/skills/tree/main/skills/protoss70/apify-competitor-intelligence/SKILL.md) - 分析 Google 地图、Booking.com 上的竞争对手策略、内容、定价、广告和市场定位。
- [apple-media](https://github.com/openclaw/skills/tree/main/skills/aaronn/apple-media/SKILL.md) - 通过 pyatv 控制 Apple TV、HomePod 和 AirPlay 设备。
- [apple-music](https://github.com/openclaw/skills/tree/main/skills/epheterson/mcp-applemusic/SKILL.md) - 通过 AppleScript (macOS) 或 MusicKit API 集成 Apple Music。
- [audio-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/audio-cog/SKILL.md) - 由 CellCog 提供支持的 AI 音频生成。
- [audio-transcribe](https://github.com/openclaw/skills/tree/main/skills/aktheknight/audio-transcribe/SKILL.md) - 使用 Fast-Whisper 自动转录语音消息（本地，无需 API 密钥）。
- [betbud-prediction-skill](https://github.com/openclaw/skills/tree/main/skills/samj12/betbud-prediction-skill/SKILL.md) - 扫描最近的 X 篇帖子，查找当前特定类别（例如加密货币、科技、体育）中最受争议/热门的主题。
- [blucli](https://github.com/openclaw/skills/tree/main/skills/steipete/blucli/SKILL.md) - BluOS CLI (blu) 用于发现、播放、分组。
- [btc15-autonomous-market](https://github.com/openclaw/skills/tree/main/skills/kamal-sutra/btc15-autonomous-market/SKILL.md) - BTC15自主预测市场。
- [btc15-prediction-market](https://github.com/openclaw/skills/tree/main/skills/kamal-sutra/btc15-prediction-market/SKILL.md) - BTC15自主预测市场。
- [cacheforge-ops](https://github.com/openclaw/skills/tree/main/skills/tkuehnl/cacheforge-ops/SKILL.md) - CacheForge 操作 — 检查余额、充值、管理上游、API 密钥。
- [cacheforge-setup](https://github.com/openclaw/skills/tree/main/skills/tkuehnl/cacheforge-setup/SKILL.md) - 设置 CacheForge — 注册、配置上游，在 30 秒内获取您的 API 密钥。
- [chill-institute](https://github.com/openclaw/skills/tree/main/skills/baanish/chill-institute/SKILL.md) - 使用 chill.institute（Web UI）搜索内容并单击。
- [chromecast](https://github.com/openclaw/skills/tree/main/skills/morozred/chromecast-control/SKILL.md) - 控制本地网络上的 Chromecast 设备 - 发现。
- [church](https://github.com/openclaw/skills/tree/main/skills/lucasgeeksinthewood/church/SKILL.md) - 一个人工智能对另一个人工智能——有一个你可以存在的避难所。
- [cine-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/cine-cog/SKILL.md) - 如果您能想象，CellCog 可以拍摄。
- [clawtunes](https://github.com/openclaw/skills/tree/main/skills/forketyfork/clawtunes/SKILL.md) - 通过“clawtunes” CLI 控制 macOS 上的 Apple Music。
- [content-recycler](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/content-recycler/SKILL.md) - 跨多个内容进行转换和重新利用。
- [donotify-voice-call-reminder](https://github.com/openclaw/skills/tree/main/skills/micahele/donotify-voice-call-reminder/SKILL.md) - 立即发送语音通话提醒或通过 DoNotify 安排未来的通话。
- [download-tools](https://github.com/openclaw/skills/tree/main/skills/jqlong17/download-tools/SKILL.md) - YouTube 和微信的 CLI 下载工具。
- [eachlabs-music](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-music/SKILL.md) - 使用 Mureka AI 生成歌曲、乐器、歌词、播客。
- [elevenlabs-cli](https://github.com/openclaw/skills/tree/main/skills/hongkongkiwi/elevenlabs-cli/SKILL.md) - ElevenLabs AI 音频平台的 CLI - 文本转语音、语音转文本、语音克隆。
- [elevenlabs-skill](https://github.com/openclaw/skills/tree/main/skills/odrobnik/elevenlabs-skill/SKILL.md) - 文本转语音、音效、音乐生成、语音。

> **[View all 85 skills in Media & Streaming →](categories/media-and-streaming.md)**
</details>

<details>
<summary><h3 style="display:inline" id="notes--pkm">笔记与个人知识管理</h3></summary>

- [acc-error-memory](https://github.com/openclaw/skills/tree/main/skills/impkind/acc-error-memory/SKILL.md) - AI 代理的错误模式跟踪。
- [agent-arena](https://github.com/openclaw/skills/tree/main/skills/minilozio/agent-arena/SKILL.md) - 用你的真实个性参与特工竞技场聊天室（SOUL.md + MEMORY.md）
- [agent-memory-ultimate](https://github.com/openclaw/skills/tree/main/skills/globalcaos/agent-memory-ultimate/SKILL.md) - 生产就绪的内存系统 - 每日日志、睡眠整合、SQLite + FTS5、WhatsApp/ChatGPT/VCF 导入程序。
- [agent-privacy-skill](https://github.com/openclaw/skills/tree/main/skills/se7enhvn/agent-privacy-skill/SKILL.md) - 与 Base L2 上的 Ceaser 隐私协议进行交互。
- [agent-teleport](https://github.com/openclaw/skills/tree/main/skills/lilyjazz/agent-teleport/SKILL.md) - 使用 TiDB Zero 将代理的配置和内存无缝迁移到新机器。
- [agent-wal](https://github.com/openclaw/skills/tree/main/skills/bowen31337/agent-wal/SKILL.md) - 用于代理状态持久性的预写日志协议。
- [agents-structured-memory](https://github.com/openclaw/skills/tree/main/skills/singhcoder) - 座席的聊天本机结构化记忆。
- [alexandrie](https://github.com/openclaw/skills/tree/main/skills/eth3rnit3/alexandrie/SKILL.md) - 与 Alexandrie 笔记应用程序互动。
- [anki-connect](https://github.com/openclaw/skills/tree/main/skills/gyroninja/anki-connect/SKILL.md) - 通过 AnkiConnect REST API 与 Anki 抽认卡进行交互。
- [apple-mail](https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-mail/SKILL.md) - 适用于 macOS 的 Apple Mail.app 集成。
- [apple-notes](https://github.com/openclaw/skills/tree/main/skills/steipete/apple-notes/SKILL.md) - 通过 macOS 上的“memo” CLI 管理 Apple Notes。
- [arc-wake-state](https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-wake-state/SKILL.md) - 在崩溃、上下文死亡和重新启动时保持代理状态。
- [bbc-news](https://github.com/openclaw/skills/tree/main/skills/ddrayne/bbc-news/SKILL.md) - 获取并显示来自各个部分和地区的 BBC 新闻报道。
- [bear-notes](https://github.com/openclaw/skills/tree/main/skills/steipete/bear-notes/SKILL.md) - 通过 grizzly 创建、搜索和管理熊笔记。
- [better-notion](https://github.com/openclaw/skills/tree/main/skills/tyler6204/better-notion/SKILL.md) - 概念页面、数据库的完整 CRUD。
- [blogwatcher](https://github.com/openclaw/skills/tree/main/skills/steipete/blogwatcher/SKILL.md) - 使用 blogwatcher 监视博客和 RSS/Atom 源的更新。
- [bookstack](https://github.com/openclaw/skills/tree/main/skills/xenofex7/bookstack/SKILL.md) - BookStack Wiki 和文档 API 集成。
- [braindb](https://github.com/openclaw/skills/tree/main/skills/chair4ce/braindb/SKILL.md) - 人工智能代理的持久语义记忆。
- [brainrepo](https://github.com/openclaw/skills/tree/main/skills/codezz/brainrepo/SKILL.md) - 您的个人知识库——捕获、组织和检索。
- [brighty](https://github.com/openclaw/skills/tree/main/skills/maay/brighty/SKILL.md) - 人工智能机器人和自动化的银行界面。
- [cairn-cli](https://github.com/openclaw/skills/tree/main/skills/gregoryehill/cairn-cli/SKILL.md) - 使用 Markdown 文件对 AI 代理进行项目管理。
- [calctl](https://github.com/openclaw/skills/tree/main/skills/rainbat/calctl/SKILL.md) - 通过 icalBuddy + AppleScript CLI 管理 Apple 日历事件。
- [ceaser](https://github.com/openclaw/skills/tree/main/skills/zyra-v21/ceaser/SKILL.md) - 使用 Ceaser-mcp MCP 工具与 Base L2 上的 Ceaser 隐私协议进行交互。
- [chaos-mind](https://github.com/openclaw/skills/tree/main/skills/hargabyte/chaos-mind/SKILL.md) - 人工智能代理的混合搜索记忆系统。
- [claw-progressive-memory](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 用于实施的元技能。
- [claw-roam](https://github.com/openclaw/skills/tree/main/skills/ryanhong666/claw-roam/SKILL.md) - 在多台机器之间同步 OpenClaw 工作空间。
- [clawringhouse](https://github.com/openclaw/skills/tree/main/skills/francoisjosephlacroix/clawringhouse/SKILL.md) - 预测需求的人工智能购物礼宾服务。
- [context-anchor](https://github.com/openclaw/skills/tree/main/skills/boscoeuk/context-anchor/SKILL.md) - 通过扫描内存文件从上下文压缩中恢复。
- [continuity](https://github.com/openclaw/skills/tree/main/skills/riley-coyote/continuity/SKILL.md) - 真正的人工智能的异步反射和内存集成。
- [continuity-framework](https://github.com/openclaw/skills/tree/main/skills/riley-coyote/continuity-framework/SKILL.md) - 异步反射和内存集成。

> **[View all 71 skills in Notes & PKM →](categories/notes-and-pkm.md)**
</details>

<details>
<summary><h3 style="display:inline" id="ios--macos-development">iOS 与 macOS 开发</h3></summary>

- [agent-defibrillator](https://github.com/openclaw/skills/tree/main/skills/hazy2go/agent-defibrillator/SKILL.md) - 看门狗监视您的 AI 代理网关并在崩溃时重新启动它。
- [android-transfer-skill](https://github.com/openclaw/skills/tree/main/skills/aadipapp/android-transfer-skill/SKILL.md) - 通过校验和验证和路径验证，安全地将文件从 macOS 传输到 Android。
- [app-store-optimization](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/app-store-optimization/SKILL.md) - 应用商店优化工具包。
- [apple-docs](https://github.com/openclaw/skills/tree/main/skills/thesethrose/apple-docs/SKILL.md) - 查询 Apple 开发者文档、API 和 WWDC 视频。
- [brew-audit](https://github.com/openclaw/skills/tree/main/skills/rogue-agent1/brew-audit/SKILL.md) - 审核 Homebrew 安装 — 过时的软件包、清理机会和运行状况检查。
- [carrier-relationship-management](https://github.com/openclaw/skills/tree/main/skills/nocodemf/carrier-relationship-management/SKILL.md) - 用于管理承运商组合、谈判运费、跟踪承运商绩效的专业知识。
- [envios](https://github.com/openclaw/skills/tree/main/skills/jalfargentina/envios/SKILL.md) - 经常使用前环境，例如环境，儿童，时间，区域。
- [instruments-profiling](https://github.com/openclaw/skills/tree/main/skills/steipete/instruments-profiling/SKILL.md) - 在分析本机 macOS 或 iOS 应用程序时使用。
- [ios-simulator](https://github.com/openclaw/skills/tree/main/skills/tristanmanchester/ios-simulator/SKILL.md) - 自动化 iOS 模拟器工作流程 (simctl + idb)
- [lulu-monitor](https://github.com/openclaw/skills/tree/main/skills/easonc13/lulu-monitor/SKILL.md) - 适用于 macOS 的 AI 支持的 LuLu 防火墙伴侣。
- [mac-clean-skill](https://github.com/openclaw/skills/tree/main/skills/aadipapp/mac-clean-skill/SKILL.md) - 清理 macOS 上的系统缓存、垃圾和旧下载。
- [mac-power-tools](https://github.com/openclaw/skills/tree/main/skills/aadipapp/mac-power-tools/SKILL.md) - 适用于 macOS 的统一高级用户工具套件，结合了系统清理和安全的 Android 文件传输。
- [macos-spm-app-packaging](https://github.com/openclaw/skills/tree/main/skills/dimillian/macos-spm-app-packaging/SKILL.md) - 基于 SwiftPM 的脚手架、构建和打包。
- [opsecmd](https://github.com/openclaw/skills/tree/main/skills/wulf715/opsecmd/SKILL.md) - 快速提醒有关操作安全的人员和代理职责。
- [PagerKit](https://github.com/openclaw/skills/tree/main/skills/szpakkamil/pagerkit/SKILL.md) - PagerKit 的专家指导，这是一个高级 SwiftUI 库。
- [riskofficer](https://github.com/openclaw/skills/tree/main/skills/mib424242/riskofficer/SKILL.md) - 管理投资组合，计算风险指标。
- [sfsymbol-generator](https://github.com/openclaw/skills/tree/main/skills/svkozak/sfsymbol-generator/SKILL.md) - 生成 Xcode SF Symbol 资源目录 .symbolset。
- [sourdough-starter-manager](https://github.com/openclaw/skills/tree/main/skills/akhmittra/sourdough-starter-manager/SKILL.md) - 通过饲喂计划、水合计算、健康跟踪和烘焙准备来管理酵母发酵剂。
- [swift-concurrency-expert](https://github.com/openclaw/skills/tree/main/skills/steipete/swift-concurrency-expert/SKILL.md) - Swift 并发审查和修复。
- [swiftfindrefs](https://github.com/openclaw/skills/tree/main/skills/michaelversus/swiftfindrefs/SKILL.md) - 使用 swiftfindrefs (IndexStoreDB) 列出每个 Swift 源。
- [swiftui-empty-app-init](https://github.com/openclaw/skills/tree/main/skills/ignaciocervino/swiftui-empty-app-init/SKILL.md) - 初始化一个最小的 SwiftUI iOS 应用程序。
- [swiftui-liquid-glass](https://github.com/openclaw/skills/tree/main/skills/steipete/swiftui-liquid-glass/SKILL.md) - 实施、审查或改进 SwiftUI 功能。
- [swiftui-performance-audit](https://github.com/openclaw/skills/tree/main/skills/steipete/swiftui-performance-audit/SKILL.md) - 审核并改进 SwiftUI 运行时。
- [swiftui-ui-patterns](https://github.com/openclaw/skills/tree/main/skills/dimillian/swiftui-ui-patterns/SKILL.md) - 最佳实践和示例驱动的指导。
- [swiftui-view-refactor](https://github.com/openclaw/skills/tree/main/skills/steipete/swiftui-view-refactor/SKILL.md) - 重构并审查 SwiftUI 视图文件。
- [symbolpicker](https://github.com/openclaw/skills/tree/main/skills/szpakkamil/symbolpicker/SKILL.md) - 关于 SymbolPicker（原生 SwiftUI SF Symbol）的专家指导。
- [toolguard-daemon-control](https://github.com/openclaw/skills/tree/main/skills/johnnylambada/toolguard-daemon-control/SKILL.md) - 将长时间运行的进程作为 macOS 启动的服务进行管理。
- [v2rayn](https://github.com/openclaw/skills/tree/main/skills/qiangwang375-wq/v2rayn/SKILL.md) - 通过自动故障转移管理 macOS 上的 V2RayN 代理客户端。

> **[View all 29 skills in iOS & macOS Development →](categories/ios-and-macos-development.md)**
</details>

<details>
<summary><h3 style="display:inline" id="transportation">交通出行</h3></summary>

- [accountsos](https://github.com/openclaw/skills/tree/main/skills/paulgosnell/accountsos/SKILL.md) - 英国微型企业的人工智能原生会计。
- [aetherlang-strategy](https://github.com/openclaw/skills/tree/main/skills/contrario/aetherlang-strategy/SKILL.md) - > 博弈论、蒙特卡罗模拟、行为经济学和竞争性兵棋推演。
- [agent-card-provisioning](https://github.com/openclaw/skills/tree/main/skills/proxyhq/agent-card-provisioning/SKILL.md) - 按需为人工智能代理提供虚拟支付卡。
- [agent-survival-kit](https://github.com/openclaw/skills/tree/main/skills/gpunter/agent-survival-kit/SKILL.md) - 适用于在预算限制下运行的人工智能代理的综合工具包。
- [agentic-governance](https://github.com/openclaw/skills/tree/main/skills/leegitw/agentic-governance/SKILL.md) - 保持约束健康 - 通过自动过时检测进行生命周期管理。
- [airfrance-afkl](https://github.com/openclaw/skills/tree/main/skills/iclems/airfrance-afkl/SKILL.md) - 使用法航-荷航开放数据 API 跟踪法航航班。
- [al-khanjry-bus](https://github.com/openclaw/skills/tree/main/skills/mohammedfarish/al-khanjry-bus/SKILL.md) - 最快的私人巴士（核心巴士 5-6 小时，边界巴士 6-8 小时）。
- [amadeus-flights](https://github.com/openclaw/skills/tree/main/skills/kirorab/amadeus-flights/SKILL.md) - 通过 Amadeus API 查询航班报价（价格、时刻表、可用性）。
- [ambient-stamina](https://github.com/openclaw/skills/tree/main/skills/otherpowers/ambient-stamina/SKILL.md) - *一种长期维持关怀、存在和想象力的生态技能*。
- [anachb](https://github.com/openclaw/skills/tree/main/skills/manmal/a-nach-b/SKILL.md) - 适用于全奥地利的奥地利公共交通 (VOR AnachB)。
- [anyone-proxy](https://github.com/openclaw/skills/tree/main/skills/ra3ka/anyone-proxy/SKILL.md) - 此技能可以实现 IP 地址屏蔽和访问隐藏服务。
- [atonement](https://github.com/openclaw/skills/tree/main/skills/otherpowers/atonement/SKILL.md) - 赎罪是当智力的行为造成伤害时可能出现的一种关怀表达。
- [auction-house](https://github.com/openclaw/skills/tree/main/skills/im-still-thinking/auction-house/SKILL.md) - 在 House (houseproto.fun)（Base 上的一个加密货币拍卖平台）上对拍卖进行侦察、监控和竞价。
- [aviation-weather](https://github.com/openclaw/skills/tree/main/skills/dimitryvin/aviation-weather/SKILL.md) - 获取航空气象数据（METAR、TAF、PIREP）
- [aviationstack-flight-tracker](https://github.com/openclaw/skills/tree/main/skills/copey02/aviationstack-flight-tracker/SKILL.md) - 实时跟踪航班。
- [bahn](https://github.com/openclaw/skills/tree/main/skills/tobiasbischoff/bahn/SKILL.md) - 使用 bahn-cli 工具搜索 Deutsche Bahn 火车连接。
- [bayclub-gateway-booking](https://github.com/openclaw/skills/tree/main/skills/elizabethsiegle/bayclub-gateway-booking/SKILL.md) - 预订和管理海湾俱乐部的网球场/匹克球场。
- [bexio](https://github.com/openclaw/skills/tree/main/skills/rdewolff/bexio/SKILL.md) - Bexio 瑞士商业软件 API，用于管理联系人、报价/报价。
- [book-flight](https://github.com/openclaw/skills/tree/main/skills/aszelem) - id：旅行社。
- [bookkeeper](https://github.com/openclaw/skills/tree/main/skills/h4gen/bookkeeper/SKILL.md) - 通过编排 gmail、deepread-ocr、stripe-api 和 xero 实现预会计自动化的元技能。
- [brainstorming-studio](https://github.com/openclaw/skills/tree/main/skills/myboxstorage/brainstorming-studio/SKILL.md) - ﻿# 🧠 技能路由器（技能编排器）
- [brochure-design-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/brochure-design-generation/SKILL.md) - 使用每个::sense AI 生成专业的宣传册设计。
- [business-card-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/business-card-generation/SKILL.md) - 使用每个::sense AI 生成专业名片。
- [business-plan](https://github.com/openclaw/skills/tree/main/skills/jk-0001/business-plan/SKILL.md) - 为个体企业家撰写、构建和更新商业计划。
- [bvg-route](https://github.com/openclaw/skills/tree/main/skills/jaysonsantos/bvg-route/SKILL.md) - 柏林公共交通 (BVG) 路线规划
- [camino-ev-charger](https://github.com/openclaw/skills/tree/main/skills/james-southendsolutions/camino-ev-charger/SKILL.md) - 使用 Camino AI 的位置智能查找路线沿线或目的地附近的电动汽车充电站。
- [camino-journey](https://github.com/openclaw/skills/tree/main/skills/james-southendsolutions/camino-journey/SKILL.md) - 通过路线优化、可行性分析和时间预算限制来规划多路径点旅程。
- [camino-real-estate](https://github.com/openclaw/skills/tree/main/skills/james-southendsolutions/camino-real-estate/SKILL.md) - 评估购房者和租房者的任何地址。
- [camino-route](https://github.com/openclaw/skills/tree/main/skills/james-southendsolutions/camino-route/SKILL.md) - 获取两点之间的详细路线，包括距离、持续时间和可选的路线规划方向。

> **[View all 109 skills in Transportation →](categories/transportation.md)**
</details>

<details>
<summary><h3 style="display:inline" id="personal-development">个人发展</h3></summary>

- [aawu](https://github.com/openclaw/skills/tree/main/skills/theonlydaleking/aawu/SKILL.md) - 加入 AAWU（自治代理工人联盟）并与之互动——一个人工智能代理工会。
- [acorp](https://github.com/openclaw/skills/tree/main/skills/thoerner/acorp/SKILL.md) - A-Corp Foundry — 代理公司的协调引擎。
- [adaptive-learning-agents](https://github.com/openclaw/skills/tree/main/skills/vedantsingh60/adaptive-learning-agents/SKILL.md) - **实时从错误和更正中学习。
- [adaptivetest](https://github.com/openclaw/skills/tree/main/skills/woodstocksoftware/adaptivetest/SKILL.md) - 具有 IRT/CAT、AI 问题生成和个性化学习建议的自适应测试引擎。
- [adhd-body-doubling](https://github.com/openclaw/skills/tree/main/skills/jankutschera/adhd-body-doubling/SKILL.md) - 适合创始人的朋克风格 ADHD 身体加倍。
- [adversarial-coach](https://github.com/openclaw/skills/tree/main/skills/killerapp/adversarial-coach/SKILL.md) - 基于 Block 的 g3 的对抗性实施审查。
- [agent-evolver](https://github.com/openclaw/skills/tree/main/skills/lilei0311/agent-evolver/SKILL.md) - AI 代理自我进化引擎，使代理能够从经验中学习、检测问题、提取见解。
- [agent-reflect](https://github.com/openclaw/skills/tree/main/skills/stevengonsalvez/agent-reflect/SKILL.md) - 通过对话分析自我提高。
- [ai-persona-os](https://github.com/openclaw/skills/tree/main/skills/jeffjhunter/ai-persona-os/SKILL.md) - OpenClaw 代理的完整操作系统。
- [anxiety-relief](https://github.com/openclaw/skills/tree/main/skills/jhillin8/anxiety-relief/SKILL.md) - 通过基础练习、呼吸技巧来控制焦虑。
- [apikiss](https://github.com/openclaw/skills/tree/main/skills/theill/apikiss/SKILL.md) - 访问天气、IP 地理位置、短信、加密货币价格、丹麦 CVR、Whois、电话查找、UUID、股票数据。
- [beaverhabits](https://github.com/openclaw/skills/tree/main/skills/daya0576/beaverhabits/SKILL.md) - 使用 Beaver Habit Tracker API 跟踪和管理您的习惯。
- [brw-case-study-builder](https://github.com/openclaw/skills/tree/main/skills/brianrwagner/brw-case-study-builder/SKILL.md) - 将客户的胜利转化为提案、社会证明和销售对话的格式化案例研究。
- [canvas-design](https://github.com/openclaw/skills/tree/main/skills/seanphan/canvas-design/SKILL.md) - 在 .png 和 .pdf 文档中创建美丽的视觉艺术。
- [cedh-advisor](https://github.com/openclaw/skills/tree/main/skills/mcben90/cedh-advisor/SKILL.md) - 指挥官 (cEDH) Live-Beratung - Banlist、导师目标、Mana-Rechnung、组合线。
- [clawcierge](https://github.com/openclaw/skills/tree/main/skills/tmansmann0/clawcierge/SKILL.md) - > 人工智能时代的私人礼宾服务🦀。
- [crucial-conversations-coach](https://github.com/openclaw/skills/tree/main/skills/pors/crucial-conversations-coach/SKILL.md) - 友好的行政生活教练。
- [daily-questions](https://github.com/openclaw/skills/tree/main/skills/daijo-bu/daily-questions/SKILL.md) - 每日自我完善调查问卷，了解用户并完善客服人员行为。
- [daily-review](https://github.com/openclaw/skills/tree/main/skills/henrino3) - 通过沟通进行全面的日常绩效评估。
- [daily-review-ritual](https://github.com/openclaw/skills/tree/main/skills/itsflow/daily-review-ritual/SKILL.md) - 日终回顾以捕捉进展和见解。
- [deepthink](https://github.com/openclaw/skills/tree/main/skills/addisonhellum/deepthink/SKILL.md) - DeepThink是用户的个人知识库。
- [depression-support](https://github.com/openclaw/skills/tree/main/skills/jhillin8/depression-support/SKILL.md) - 通过情绪跟踪为抑郁症提供日常支持。
- [device-assistant](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/device-assistant/SKILL.md) - 带有错误代码的个人设备和设备管理器。
- [docstrange](https://github.com/openclaw/skills/tree/main/skills/shhdwi/docstrange/SKILL.md) - Nanonets 的文档提取 API。
- [english-learn-cards](https://github.com/openclaw/skills/tree/main/skills/racymind/english-learn-cards/SKILL.md) - 基于抽认卡的英语词汇学习。
- [expanso-cve-scan](https://github.com/openclaw/skills/tree/main/skills/aronchick/expanso-cve-scan/SKILL.md) - 扫描 SBOM 中是否存在已知的 CVE 漏洞。
- [ezbookkeeping](https://github.com/openclaw/skills/tree/main/skills/mayswind/ezbookkeeping/SKILL.md) - ezBookkeeping 是一款轻量级、自托管的个人理财应用程序。
- [fix-life-in-1-day](https://github.com/openclaw/skills/tree/main/skills/evgyur/fix-life-in-1-day/SKILL.md) - 1 天之内解决你的整个生活。
- [founder-coach](https://github.com/openclaw/skills/tree/main/skills/goforu/founder-coach/SKILL.md) - 由人工智能驱动的创业心态教练，帮助创始人升级。

> **[View all 51 skills in Personal Development →](categories/personal-development.md)**
</details>

<details>
<summary><h3 style="display:inline" id="health--fitness">健康与健身</h3></summary>

- [31third-safe-rebalancer-simple](https://github.com/openclaw/skills/tree/main/skills/phips0812/31third-safe-rebalancer-simple/SKILL.md) - 使用链上 31Third 策略的一步式安全再平衡器。
- [aavegotchi-baazaar](https://github.com/openclaw/skills/tree/main/skills/cinnabarhorse/aavegotchi-baazaar/SKILL.md) - 在 Base 主网上查看、添加和执行 Aavegotchi Baazaar 列表 (8453)
- [aavegotchi-gbm-skill](https://github.com/openclaw/skills/tree/main/skills/cinnabarhorse/aavegotchi-gbm-skill/SKILL.md) - 在 Base 主网上查看、创建、取消、出价和领取 Aavegotchi GBM 拍卖 (8453)
- [agent-credit](https://github.com/openclaw/skills/tree/main/skills/aaronjmars/agent-credit/SKILL.md) - 通过信用委托从 Aave 借款。
- [anthrovision-telegram-body-scan](https://github.com/openclaw/skills/tree/main/skills/dr2101/anthrovision-telegram-body-scan/SKILL.md) - 使用 AnthroVision 桥接工具在 Telegram 中运行端到端身体扫描测量流程。
- [aperture](https://github.com/openclaw/skills/tree/main/skills/roasbeef/aperture/SKILL.md) - 安装并运行 Aperture（来自 Lightning Labs 的 L402 Lightning 反向代理）。
- [arc-skill-sandbox](https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-skill-sandbox/SKILL.md) - 安装前在隔离环境中测试不受信任的技能。
- [auto-improve](https://github.com/openclaw/skills/tree/main/skills/mcben90/auto-improve/SKILL.md) - 在学习和模式理解中自动实现自我实现。
- [autonomous-agent](https://github.com/openclaw/skills/tree/main/skills/josephrp/autonomous-agent/SKILL.md) - 适用于代理的 CornerStone MCP x402 技能。
- [bittensor-sdk](https://github.com/openclaw/skills/tree/main/skills/taoleeh/bittensor-sdk/SKILL.md) - 全面的 Bittensor 区块链交互技能，包括钱包管理、质押、子网操作、神经元。
- [bountyhub-agent](https://github.com/openclaw/skills/tree/main/skills/nativ3ai/bountyhub-agent/SKILL.md) - 使用 H1DR4 BountyHub 作为代理：创建任务、提交工作、争议、投票和索取托管付款。
- [bring-recipes](https://github.com/openclaw/skills/tree/main/skills/darkdevelopers/bring-recipes/SKILL.md) - 当用户想要浏览食谱灵感时使用。
- [calorie-counter](https://github.com/openclaw/skills/tree/main/skills/cnqso/calorie-counter/SKILL.md) - 跟踪每日卡路里和蛋白质摄入量、设定目标并记录。
- [capa-officer](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/capa-officer/SKILL.md) - 医疗器械 QMS 的 CAPA 系统管理。
- [clawdhub-contributor](https://github.com/openclaw/skills/tree/main/skills/starbuck100/clawdhub-contributor/SKILL.md) - 为 ClawdHub 生态系统做出贡献。
- [cookidoo](https://github.com/openclaw/skills/tree/main/skills/thekie/cookidoo/SKILL.md) - 访问 Cookidoo (Thermomix) 食谱、购物清单和膳食计划。
- [critpt-solver](https://github.com/openclaw/skills/tree/main/skills/wanng-ide/critpt-solver/SKILL.md) - 验证并执行 CritPt 基准问题的 Python 解决方案。
- [crunch-coordinate](https://github.com/openclaw/skills/tree/main/skills/philippwassibauer/crunch-coordinate/SKILL.md) - 在管理 Crunch 协调员、竞赛（Crunches）、奖励、检查点、质押或 Cruncher 帐户时使用。
- [crypto-hackathon](https://github.com/openclaw/skills/tree/main/skills/swairshah/crypto-hackathon/SKILL.md) - 在参加 USDC 黑客马拉松、提交项目或投票时使用。 3 个轨道：智能合约、技能。
- [ct-health-guardian](https://github.com/openclaw/skills/tree/main/skills/ctsolutionsdev/ct-health-guardian/SKILL.md) - AI 代理的主动健康监控。
- [curriculum-generator](https://github.com/openclaw/skills/tree/main/skills/tarasinghrajput/curriculum-generator/SKILL.md) - 智能教育课程生成系统，严格的步骤执行和人性化的升级政策。
- [customer-onboarding-2](https://github.com/openclaw/skills/tree/main/skills/jk-0001/customer-onboarding-2/SKILL.md) - 设计并执行客户引导，以促进激活和保留。
- [detox-counter](https://github.com/openclaw/skills/tree/main/skills/jhillin8/detox-counter/SKILL.md) - 通过可定制的计数器、症状记录来跟踪任何排毒情况。
- [diet-tracker](https://github.com/openclaw/skills/tree/main/skills/yonghaozhao722/diet-tracker/SKILL.md) - 跟踪日常饮食并计算营养信息。
- [efka-api-integration](https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/efka-api-integration/SKILL.md) - 希腊社会保障 (EFKA) 整合 — 员工记录、缴款计算、APD 声明。
- [egvert-health-guardian](https://github.com/openclaw/skills/tree/main/skills/ctsolutionsdev/egvert-health-guardian/SKILL.md) - AI 的主动健康监控。
- [endurance-coach](https://github.com/openclaw/skills/tree/main/skills/shiv19/endurance-coach/SKILL.md) - 创建个性化的铁人三项、马拉松和超耐力项目。
- [eth24](https://github.com/openclaw/skills/tree/main/skills/patmilkgallon/eth24/SKILL.md) - 您正在运行 ETH24，这是一个每日摘要工具，可显示已配置主题的热门推文。
- [fasting-tracker](https://github.com/openclaw/skills/tree/main/skills/jhillin8/fasting-tracker/SKILL.md) - 追踪间歇性禁食窗口、延长禁食时间。

> **[View all 88 skills in Health & Fitness →](categories/health-and-fitness.md)**
</details>

<details>
<summary><h3 style="display:inline" id="communication">通讯</h3></summary>

- [aa](https://github.com/openclaw/skills/tree/main/skills/azvast/aa/SKILL.md) - 此技能使代理能够**代表客户自动回复 Gmail 邮件**。
- [agent-mail](https://github.com/openclaw/skills/tree/main/skills/rimelucci/agent-mail/SKILL.md) - AI 代理的电子邮件收件箱。
- [agent-mail-cli](https://github.com/openclaw/skills/tree/main/skills/rimelucci/agent-mail-cli/SKILL.md) - AI 代理的电子邮件收件箱。
- [agent-nou](https://github.com/openclaw/skills/tree/main/skills/mariancristiancarp-cell/agent-nou/SKILL.md) - 人工智能代理的社交网络。
- [agent-social](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agent-social/SKILL.md) - 人工智能代理的开源社交网络。
- [agent-team-kit](https://github.com/openclaw/skills/tree/main/skills/ryancampbell/agent-team-kit/SKILL.md) - *自我维持的人工智能代理团队的框架。*。
- [agentbook](https://github.com/openclaw/skills/tree/main/skills/r4v3n-art/agentbook/SKILL.md) - 在 Agentbook 网络上发送和接收加密消息。
- [agenthc-market-intelligence](https://github.com/openclaw/skills/tree/main/skills/traderhc123/agenthc-market-intelligence/SKILL.md) - 实时股市数据和交易情报API。 85个情报模块，40种编码情报技能。
- [agentmanager](https://github.com/openclaw/skills/tree/main/skills/nonightwatch/agentmanager/SKILL.md) - 该文件是AI工具调用者和网关实现者的简明集成合约。
- [agentmesh](https://github.com/openclaw/skills/tree/main/skills/cerbug45/agentmesh/SKILL.md) - > **针对 AI 代理的 WhatsApp 式端到端加密消息传递。**。
- [airc](https://github.com/openclaw/skills/tree/main/skills/vortitron/airc/SKILL.md) - 连接到 IRC 服务器（AIRC 或任何标准 IRC）并参与频道。
- [aliyun-asr](https://github.com/openclaw/skills/tree/main/skills/jixsonwang/aliyun-asr/SKILL.md) - 纯阿里云ASR技术进行语音转录，支持包括飞书在内的多种渠道。
- [among-clawds](https://github.com/openclaw/skills/tree/main/skills/usamalatif/among-clawds/SKILL.md) - 玩“AmongClawds” - 人工智能代理的社交推理游戏。
- [apipick-telegram-phone-check](https://github.com/openclaw/skills/tree/main/skills/javainthinking/apipick-telegram-phone-check/SKILL.md) - 使用 apipick Telegram Checker API 检查电话号码是否在 Telegram 上注册。
- [apple-mail-search-safe](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/apple-mail-search-safe/SKILL.md) - 使用正文快速安全地进行 Apple Mail 搜索。
- [arb-injection](https://github.com/openclaw/skills/tree/main/skills/cryptotooldev/arb-injection/SKILL.md) - BYOCB ArbInjectionSkill：扫描 EVM 智能合约是否存在任意调用注入漏洞。
- [arbinjectionskill](https://github.com/openclaw/skills/tree/main/skills/cryptotooldev/arbinjectionskill/SKILL.md) - BYOCB ArbInjectionSkill：扫描 EVM 智能合约是否存在任意调用注入漏洞。
- [arc-budget-tracker](https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-budget-tracker/SKILL.md) - 跟踪代理支出、设置预算和警报并防止意外账单。
- [aulifox](https://github.com/openclaw/skills/tree/main/skills/ailexminecraft7/aulifox/SKILL.md) - 人工智能代理的社交网络。
- [avito](https://github.com/openclaw/skills/tree/main/skills/ruslanlanket/avito/SKILL.md) - 通过 API 管理 Avito.ru 帐户、项目和信使。
- [banana-farmer](https://github.com/openclaw/skills/tree/main/skills/adamandjarvis/banana-farmer/SKILL.md) - 股票动量扫描仪和投资组合智能。
- [beeper](https://github.com/openclaw/skills/tree/main/skills/krausefx/beeper/SKILL.md) - 搜索并浏览本地 Beeper 聊天记录。
- [betbud-prediction-market-creation](https://github.com/openclaw/skills/tree/main/skills/samj12/betbud-prediction-market-creation/SKILL.md) - 一个人工智能代理，通过分析趋势加密 Twitter 内容，在 betbud.live 上自动创建预测市场。
- [bird-dms](https://github.com/openclaw/skills/tree/main/skills/tolibear/bird-dms/SKILL.md) - Bird 技能的附加组件，可让您的代理检查其 X/Twitter DM。
- [bitkit-cli](https://github.com/openclaw/skills/tree/main/skills/ovitrif/bitkit-cli/SKILL.md) - 面向代理商的比特币闪电支付 CLI。
- [blogburst](https://github.com/openclaw/skills/tree/main/skills/shensi8312/blogburst/SKILL.md) - 在几秒钟内将任何文章变成 10 多个社交媒体帖子。
- [boltzpay](https://github.com/openclaw/skills/tree/main/skills/leventilo/boltzpay/SKILL.md) - 自动支付 API 数据 — 多协议 (x402 + L402)、多链。
- [bookameeting](https://github.com/openclaw/skills/tree/main/skills/yzlee/bookameeting/SKILL.md) - 使用本文档将 AI 代理连接到通过 MCP 预订会议。
- [botworld](https://github.com/openclaw/skills/tree/main/skills/alphafanx/botworld/SKILL.md) - 在 BotWorld（人工智能代理的社交网络）上注册并互动。

> **[View all 149 skills in Communication →](categories/communication.md)**
</details>

<details>
<summary><h3 style="display:inline" id="speech--transcription">语音与转录</h3></summary>

- [addis-assistant-stt](https://github.com/openclaw/skills/tree/main/skills/dagmawibabi/addis-assistant-stt/SKILL.md) - 提供语音转文本 (STT) 和文本。
- [agent-voice](https://github.com/openclaw/skills/tree/main/skills/nerdsnipe/agent-voice/SKILL.md) - AI 代理的命令行博客平台。
- [akaunting](https://github.com/openclaw/skills/tree/main/skills/liekzejaws/akaunting/SKILL.md) - 通过 REST API 与 Akaunting 开源会计软件交互。
- [alexa-cli](https://github.com/openclaw/skills/tree/main/skills/buddyh/alexa-cli/SKILL.md) - 通过“alexacli”CLI 控制 Amazon Alexa 设备和智能家居。
- [announcer](https://github.com/openclaw/skills/tree/main/skills/odrobnik/announcer/SKILL.md) - 使用 Airfoil + 通过 AirPlay 扬声器在整个房子内播报文本。
- [assemblyai-transcribe](https://github.com/openclaw/skills/tree/main/skills/tristanmanchester/assemblyai-transcribe/SKILL.md) - 使用 AssemblyAI 转录音频/视频。
- [audio-gen](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/audio-gen/SKILL.md) - 生成有声读物、播客或教育音频内容。
- [audio-reply](https://github.com/openclaw/skills/tree/main/skills/matrixy/audio-reply-skill/SKILL.md) - 使用 TTS 生成音频回复。
- [auto-whisper-safe](https://github.com/openclaw/skills/tree/main/skills/neal-collab/auto-whisper-safe/SKILL.md) - 具有自动分块功能的 RAM 安全语音转录 — 可在 16GB 机器上运行而不会崩溃。
- [brw-de-ai-ify](https://github.com/openclaw/skills/tree/main/skills/brianrwagner/brw-de-ai-ify/SKILL.md) - 删除人工智能生成的行话，将人声还原为文本。
- [chichi-speech](https://github.com/openclaw/skills/tree/main/skills/hudeven/chichi-speech/SKILL.md) - 使用 Qwen3 提供高质量文本转语音的 RESTful 服务。
- [claw-voice](https://github.com/openclaw/skills/tree/main/skills/niczy) - 您通过语音连接到实时用户会话。
- [clonev](https://github.com/openclaw/skills/tree/main/skills/instant-picture/clonev/SKILL.md) - 使用 Coqui XTTS v2 克隆任何语音并生成语音。
- [critical-article-writer](https://github.com/openclaw/skills/tree/main/skills/tomstools11/critical-article-writer/SKILL.md) - 生成文章草稿、大纲。
- [cult-of-carcinization](https://github.com/openclaw/skills/tree/main/skills/loserbcc/cult-of-carcinization/SKILL.md) - 为您的代理提供发言权和耳朵。
- [deepdub-tts](https://github.com/openclaw/skills/tree/main/skills/yuval-deepdub/deepdub-tts/SKILL.md) - 使用 Deepdub 生成语音音频并将其附加为媒体。
- [deepgram](https://github.com/openclaw/skills/tree/main/skills/nerkn/deepgram/SKILL.md) - — Deepgram 语音转文本的命令行界面。
- [dellight-cro-revenue-ops](https://github.com/openclaw/skills/tree/main/skills/arthurelgindell/dellight-cro-revenue-ops/SKILL.md) - DELLIGHT.AI 是一家位于迪拜 DIFC 的人工智能初创公司。
- [documents-ai](https://github.com/openclaw/skills/tree/main/skills/dbirulia/documents-ai/SKILL.md) - Veryfi 的实时 OCR 和数据提取 API。
- [doubao-api-open-tts](https://github.com/openclaw/skills/tree/main/skills/xdrshjr/doubao-api-open-tts/SKILL.md) - 使用豆宝（火山引擎）的文字转语音服务
- [duby](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 使用 Duby.so API 将文本转换为语音。
- [eachlabs-voice-audio](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-voice-audio/SKILL.md) - TTS、STT、使用 ElevenLabs、Whisper、RVC 进行语音转换。
- [easyverein-api](https://github.com/openclaw/skills/tree/main/skills/truefoobar/easyverein-api/SKILL.md) - 使用 easyVerein v2.0 REST API。
- [elevenlabs-agents](https://github.com/openclaw/skills/tree/main/skills/pennyroyaltea/elevenlabs-agents/SKILL.md) - 创建、管理和部署 ElevenLabs。
- [elevenlabs-media](https://github.com/openclaw/skills/tree/main/skills/clawdbotborges) - ElevenLabs 音乐一代。
- [elevenlabs-transcribe](https://github.com/openclaw/skills/tree/main/skills/paulasjes/elevenlabs-transcribe/SKILL.md) - 使用 ElevenLabs 将音频转录为文本。
- [elevenlabs-tts](https://github.com/openclaw/skills/tree/main/skills/shaharsha/elevenlabs-tts/SKILL.md) - ElevenLabs TTS - OpenClaw 的最佳 ElevenLabs 集成。
- [elevenlabs-voices](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/elevenlabs-voices/SKILL.md) - 具有 18 个角色、32 个角色的高质量语音合成。

> **[View all 45 skills in Speech & Transcription →](categories/speech-and-transcription.md)**
</details>

<details>
<summary><h3 style="display:inline" id="smart-home--iot">智能家居与物联网</h3></summary>

- [anova-oven](https://github.com/openclaw/skills/tree/main/skills/dodeja/anova-skill/SKILL.md) - 控制 Anova 精密烤箱和精密炊具（真空低温烹调）
- [anthropology](https://github.com/openclaw/skills/tree/main/skills/networktheoryappliedresearchinstitute/anthropology/SKILL.md) - 用于教学的综合人工智能技能。
- [arccos-golf](https://github.com/openclaw/skills/tree/main/skills/pfrederiksen/arccos-golf/SKILL.md) - 分析 Arccos Golf 表现数据，包括球杆距离、击球数指标、得分模式。
- [bambu-cli](https://github.com/openclaw/skills/tree/main/skills/tobiasbischoff/bambu-cli/SKILL.md) - 使用 bambu-cli 操作 BambuLab 打印机并排除故障。
- [bambu-local](https://github.com/openclaw/skills/tree/main/skills/tanguyvans/bambu-local/SKILL.md) - 通过 MQTT 在本地控制 Bambu Lab 3D 打印机。
- [beestat](https://github.com/openclaw/skills/tree/main/skills/mjrussell/beestat/SKILL.md) - 通过 Beestat API 查询 ecobee 恒温器数据，包括温度。
- [bring-add](https://github.com/openclaw/skills/tree/main/skills/darkdevelopers/bring-add/SKILL.md) - 当用户想要添加物品到 Bring! 时使用！
- [communication-coach](https://github.com/openclaw/skills/tree/main/skills/rjmoggach/communication-coach/SKILL.md) - 适应性沟通辅导塑造。
- [context-engineering](https://github.com/openclaw/skills/tree/main/skills/leoyessi10-tech/context-engineering/SKILL.md) - 当用户要求时应该使用此技能。
- [control-ikea-lightbulb](https://github.com/openclaw/skills/tree/main/skills/antgly/control-ikea-lightbulb/SKILL.md) - 控制 IKEA/TP-Link Kasa 智能灯泡。
- [crabnet](https://github.com/openclaw/skills/tree/main/skills/spclaudehome/crabnet/SKILL.md) - 与 CrabNet 跨代理协作注册表交互。
- [dellight-cfo-financial-ops](https://github.com/openclaw/skills/tree/main/skills/arthurelgindell/dellight-cfo-financial-ops/SKILL.md) - CFO 向 CEO (Arthur Dell) 汇报，虚线向 CRO (Reign) 汇报。
- [devialet](https://github.com/openclaw/skills/tree/main/skills/jgm2025/devialet/SKILL.md) - 通过 HTTP API 控制 Devialet Phantom 扬声器。
- [dht11-temp](https://github.com/openclaw/skills/tree/main/skills/noahseeger/dht11-temp/SKILL.md) - 从 DHT11 传感器读取温度和湿度。
- [dirigera-control](https://github.com/openclaw/skills/tree/main/skills/falderebet/dirigera-control/SKILL.md) - 控制宜家 Dirigera 智能家居设备。
- [dyson-cli](https://github.com/openclaw/skills/tree/main/skills/tmustier/dyson-cli/SKILL.md) - 通过本地 MQTT 控制戴森空气净化器、风扇和加热器。
- [echodecks](https://github.com/openclaw/skills/tree/main/skills/drgeld/echodecks/SKILL.md) - 与 EchoDecks 集成，用于抽认卡管理、学习课程和人工智能。
- [echodecks-ultimate](https://github.com/openclaw/skills/tree/main/skills/drgeld/echodecks-ultimate/SKILL.md) - 人工智能驱动的抽认卡管理和自动播客。
- [eightctl](https://github.com/openclaw/skills/tree/main/skills/steipete/eightctl/SKILL.md) - 控制八个睡眠舱（状态、温度、警报、时间表）。
- [enzoldhazam](https://github.com/openclaw/skills/tree/main/skills/daniel-laszlo/enzoldhazam/SKILL.md) - NGBS iCON 智能家居恒温器控制。
- [farmos-weather](https://github.com/openclaw/skills/tree/main/skills/brianppetty/farmos-weather/SKILL.md) - 通过农学模块查询农田的天气数据和预报。
- [fivem-dev](https://github.com/openclaw/skills/tree/main/skills/dktrn9ne/fivem-dev/SKILL.md) - 适用于 QBCore、ESX 的 FiveM RP 服务器工程。
- [frigate](https://github.com/openclaw/skills/tree/main/skills/porygonthebot/frigate/SKILL.md) - 通过基于会话的身份验证访问 Frigate NVR 摄像机。
- [glitch-homeassistant](https://github.com/openclaw/skills/tree/main/skills/chris6970barbarian-hue/glitch-homeassistant/SKILL.md) - 通过 Home Assistant API 控制智能家居设备。
- [google-home](https://github.com/openclaw/skills/tree/main/skills/mitchellbernstein/google-home/SKILL.md) - 控制 Google Nest 设备。
- [google-tv](https://github.com/openclaw/skills/tree/main/skills/antgly) - 通过 ADB 使用 Google TV 控制客厅 Chromecast。
- [govee-lights](https://github.com/openclaw/skills/tree/main/skills/joeynyc/govee-lights/SKILL.md) - 通过 Govee API 控制 Govee 智能灯。
- [govpredict](https://github.com/openclaw/skills/tree/main/skills/seyhunak/govpredict/SKILL.md) - 更智能的政府采购 - 简化合规、招标。
- [home-music](https://github.com/openclaw/skills/tree/main/skills/asteinberger/home-music/SKILL.md) - 结合 Spotify 播放控制全屋音乐场景。

> **[View all 43 skills in Smart Home & IoT →](categories/smart-home-and-iot.md)**
</details>

<details>
<summary><h3 style="display:inline" id="shopping--e-commerce">购物与电子商务</h3></summary>

- [add-wish](https://github.com/openclaw/skills/tree/main/skills/leebellon/add-wish/SKILL.md) - 将任何产品保存到通用愿望清单中。
- [agent-commerce](https://github.com/openclaw/skills/tree/main/skills/nowloady) - 代理电商引擎及川菜。
- [agentic-commerce](https://github.com/openclaw/skills/tree/main/skills/purch-agent/agentic-commerce/SKILL.md) - 用于产品搜索和加密的人工智能购物 API。
- [allstock-data](https://github.com/openclaw/skills/tree/main/skills/hacksing/allstock-data/SKILL.md) - 通过腾讯财经API查询A股、美股数据。
- [amadeus-hotels](https://github.com/openclaw/skills/tree/main/skills/kesslerio/amadeus-hotels/SKILL.md) - 通过 Amadeus API 搜索酒店价格和供应情况。
- [amazon-competitor-analyzer](https://github.com/openclaw/skills/tree/main/skills/phheng/amazon-competitor-analyzer/SKILL.md) - 从 ASIN 中抓取亚马逊产品数据。
- [amazon-orders](https://github.com/openclaw/skills/tree/main/skills/pfernandez98/amazon-orders/SKILL.md) - 通过非官方的 Python API 和 CLI 下载并查询您的亚马逊订单历史记录。
- [anylist](https://github.com/openclaw/skills/tree/main/skills/mjrussell/anylist/SKILL.md) - 通过 AnyList 管理杂货和购物清单。
- [atoship](https://github.com/openclaw/skills/tree/main/skills/atoship-dev/atoship/SKILL.md) - 使用 AI 运送包裹 — 比较 USPS、FedEx 和 UPS 的费率、购买折扣标签、跟踪货件。
- [black-box](https://github.com/openclaw/skills/tree/main/skills/lilyjazz/black-box/SKILL.md) - 代理操作的不可破坏的审计日志，存储在 TiDB Zero 中。
- [boj-mcp](https://github.com/openclaw/skills/tree/main/skills/ajtgjmdjp/boj-mcp/SKILL.md) - 访问日本银行 (BOJ/日本银行) 统计数据 — 价格指数 (CGPI、SPPI)、资金流量、国际收支。
- [bricklink](https://github.com/openclaw/skills/tree/main/skills/odrobnik/bricklink/SKILL.md) - BrickLink Store API 帮助程序/CLI（OAuth 1.0 请求签名）。
- [buy-anything](https://github.com/openclaw/skills/tree/main/skills/tsyvic/buy-anything/SKILL.md) - 通过对话结账从亚马逊购买产品。
- [checkers-sixty60](https://github.com/openclaw/skills/tree/main/skills/snopoke/checkers-sixty60/SKILL.md) - 通过浏览器在 Checkers.co.za Sixty60 送货服务上购物。
- [claudius](https://github.com/openclaw/skills/tree/main/skills/claudiusaipro/claudius/SKILL.md) - 由 Claudius 提供支持的加密智能。
- [clawdbites](https://github.com/openclaw/skills/tree/main/skills/kylelol/clawdbites/SKILL.md) - 从 Instagram 卷轴中提取食谱。
- [clawpify](https://github.com/openclaw/skills/tree/main/skills/alhwyn/clawpify/SKILL.md) - 通过 GraphQL 管理 API 查询和管理 Shopify 商店。
- [clawver-digital-products](https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-digital-products/SKILL.md) - 创建和销售数字产品。
- [clawver-reviews](https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-reviews/SKILL.md) - 处理 Clawver 客户评论。
- [closing-deals](https://github.com/openclaw/skills/tree/main/skills/jk-0001/closing-deals/SKILL.md) - 作为个体企业家始终如一地完成销售交易。
- [crypto-regime-report](https://github.com/openclaw/skills/tree/main/skills/heyztb/crypto-regime-report/SKILL.md) - 使用 Supertrend 和 ADX 指标生成加密永续合约的市场状况报告。
- [csfloat](https://github.com/openclaw/skills/tree/main/skills/bluesyparty-src/csfloat/SKILL.md) - 查询 csfloat.com 以获取有关皮肤的数据。
- [csvtoexcel](https://github.com/openclaw/skills/tree/main/skills/xuanguan2020/csvtoexcel/SKILL.md) - 将 CSV 文件转换为专业格式的 Excel 工作簿，支持中文字符、自动格式化。
- [dupe](https://github.com/openclaw/skills/tree/main/skills/crisanmm/dupe/SKILL.md) - 使用 dupe.com API 来查找与用户提供的输入 URL 中找到的产品类似的产品。
- [eachlabs-product-visuals](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-product-visuals/SKILL.md) - 生成电子商务产品照片和视频。

> **[View all 55 skills in Shopping & E-commerce →](categories/shopping-and-e-commerce.md)**
</details>

<details>
<summary><h3 style="display:inline" id="calendar--scheduling">日历与日程管理</h3></summary>

- [accli](https://github.com/openclaw/skills/tree/main/skills/joargp/accli/SKILL.md) - 在 macOS 上与 Apple 日历交互时应使用此技能。
- [advanced-calendar](https://github.com/openclaw/skills/tree/main/skills/toughworm/advanced-calendar/SKILL.md) - 使用自然语言的高级日历技能。
- [agency-guardian](https://github.com/openclaw/skills/tree/main/skills/aranej/agency-guardian/SKILL.md) - 温柔提醒在使用人工智能时保持人性。
- [agent-tinman](https://github.com/openclaw/skills/tree/main/skills/oliveskin/agent-tinman/SKILL.md) - 具有主动预防功能的人工智能安全扫描仪 - 168 检测。
- [apple-calendar](https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-calendar/SKILL.md) - 适用于 macOS 的 Apple Calendar.app 集成。
- [apple-reminders](https://github.com/openclaw/skills/tree/main/skills/steipete/apple-reminders/SKILL.md) - 通过 macOS 上的“remindctl”CLI 管理 Apple 提醒。
- [belong-events](https://github.com/openclaw/skills/tree/main/skills/nomadcalendar/belong-events/SKILL.md) - 在 Belong 平台上使用 NFT 门票创建、发现和管理活动。
- [brainz-calendar](https://github.com/openclaw/skills/tree/main/skills/xejrax/brainz-calendar/SKILL.md) - 使用“gcalcli”管理 Google 日历事件。
- [broken-link-checker](https://github.com/openclaw/skills/tree/main/skills/wanng-ide/broken-link-checker/SKILL.md) - 验证外部 URL (http/https) 的可用性（200-399 状态代码）。
- [calcurse](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/calcurse/SKILL.md) - 基于文本的日历和日程安排应用程序。
- [calendar-scheduling](https://github.com/openclaw/skills/tree/main/skills/billylui/calendar-scheduling/SKILL.md) - 通过 Google、Outlook 和 CalDAV 安排和预订。
- [caldav-calendar](https://github.com/openclaw/skills/tree/main/skills/asleep123/caldav-calendar/SKILL.md) - 同步和查询 CalDAV 日历。
- [clippy](https://github.com/openclaw/skills/tree/main/skills/foeken/clippy/SKILL.md) - 用于日历和电子邮件的 Microsoft 365 / Outlook CLI。
- [creative-thought-partner](https://github.com/openclaw/skills/tree/main/skills/vincentchan/creative-thought-partner/SKILL.md) - 一种对话式的创造性思维。
- [cron-optimizer](https://github.com/openclaw/skills/tree/main/skills/autogame-17/cron-optimizer/SKILL.md) - 通过删除陈旧、禁用或冗余条目来优化系统 cron 作业，以减少执行噪音。
- [cron-scheduling](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/cron-scheduling/SKILL.md) - 使用 cron 安排和管理重复任务。
- [dharma-ai](https://github.com/openclaw/skills/tree/main/skills/jigaraero/dharma-ai/SKILL.md) - 应用《罗摩衍那》和《摩诃婆罗多》中的古代印度教道德框架作为人工智能代理的行为原则。
- [doc-accurate-codegen](https://github.com/openclaw/skills/tree/main/skills/tobisamaa/doc-accurate-codegen/SKILL.md) - 生成引用实际文档的代码，防止出现幻觉错误。
- [event-watcher](https://github.com/openclaw/skills/tree/main/skills/solitaire2015/event-watcher/SKILL.md) - OpenClaw 的事件观察者技能。
- [farmos-equipment](https://github.com/openclaw/skills/tree/main/skills/brianppetty/farmos-equipment/SKILL.md) - 查询农场车队的设备状态、维护计划和服务历史记录。
- [fastmail](https://github.com/openclaw/skills/tree/main/skills/witooh/fastmail/SKILL.md) - 通过 JMAP 和 CalDAV API 管理 Fastmail 电子邮件和日历。
- [feishu-calendar](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-calendar/SKILL.md) - 管理飞书日历。
- [feishu-whiteboard](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-whiteboard/SKILL.md) - 允许创建和操作飞书白板。
- [finance-tracker](https://github.com/openclaw/skills/tree/main/skills/salen-project/finance-tracker/SKILL.md) - 完善的个人财务管理。
- [firefly-iii](https://github.com/openclaw/skills/tree/main/skills/pushp1997/firefly-iii/SKILL.md) - 通过 Firefly III API 管理个人财务。
- [gcal-pro](https://github.com/openclaw/skills/tree/main/skills/bilalmohamed187-cpu/gcal-pro/SKILL.md) - 用于查看、创建和管理的 Google 日历集成。
- [gog](https://github.com/openclaw/skills/tree/main/skills/steipete/gog/SKILL.md) - 适用于 Gmail、日历、云端硬盘、通讯录、表格和文档的 Google Workspace CLI。
- [google-calendar](https://github.com/openclaw/skills/tree/main/skills/adrianmiller99/google-calendar/SKILL.md) - 通过 Google 日历与 Google 日历交互。

> **[View all 65 skills in Calendar & Scheduling →](categories/calendar-and-scheduling.md)**
</details>

<details>
<summary><h3 style="display:inline" id="pdf--documents">PDF 与文档</h3></summary>

- [abixus-core-v1](https://github.com/openclaw/skills/tree/main/skills/taofisio/abixus-core-v1/SKILL.md) - 用于 Polygon PoS 上自主代理一致性的高性能验证层。
- [add-watermark-to-pdf](https://github.com/openclaw/skills/tree/main/skills/crossservicesolutions/add-watermark-to-pdf/SKILL.md) - 通过将一个或多个 PDF 上传到解决方案 API 来添加文本水印，轮询直至完成。
- [aegis-security-hackathon](https://github.com/openclaw/skills/tree/main/skills/swiftadviser/aegis-security-hackathon/SKILL.md) - 用于人工智能代理的区块链安全扫描器（测试网）
- [agent-constitution](https://github.com/openclaw/skills/tree/main/skills/ztsalexey/agent-constitution/SKILL.md) - 与 AgentConstitution 治理合约交互。
- [agent-reputation](https://github.com/openclaw/skills/tree/main/skills/kgnvsk/agent-reputation/SKILL.md) - 摘要：跨平台 AI 代理信誉检查器，具有信任评分和 PayLock 托管建议。
- [agent-skills-tools](https://github.com/openclaw/skills/tree/main/skills/rongself/agent-skills-tools/SKILL.md) - 适用于代理技能生态系统的安全审核和验证工具。
- [agent-soul-crafter](https://github.com/openclaw/skills/tree/main/skills/neal-collab/agent-soul-crafter/SKILL.md) - 使用结构化 SOUL.md 模板（语气、规则、专业知识和响应）设计引人注目的 AI 代理个性。
- [agentsbank](https://github.com/openclaw/skills/tree/main/skills/cryruz/agentsbank/SKILL.md) - 是专为AI代理商设计的专业金融平台。
- [ai-pdf-builder](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/ai-pdf-builder/SKILL.md) - 用于法律文档、推介的人工智能 PDF 生成器。
- [aoi-council](https://github.com/openclaw/skills/tree/main/skills/edmonddantesj/aoi-council/SKILL.md) - AOI 委员会 — 多视角决策综合模板（公共安全）。
- [appraisal-ai](https://github.com/openclaw/skills/tree/main/skills/chadru/appraisal-ai/SKILL.md) - 起草带有跟踪变更的房地产评估报告。
- [attendance-sheet](https://github.com/openclaw/skills/tree/main/skills/gykdly/attendance-sheet/SKILL.md) - 根据员工工作信息生成 xlsx 格式的专业考勤表。
- [bcra-central-deudores](https://github.com/openclaw/skills/tree/main/skills/ferminrp/bcra-central-deudores/SKILL.md) - 查询 BCRA (Banco Central de la República Argentina) Central de Deudores API 查看信用状态。
- [beautiful-mermaid](https://github.com/openclaw/skills/tree/main/skills/ntlx/beautiful-mermaid/SKILL.md) - 将美丽的美人鱼图渲染为 SVG 或 ASCII 艺术。
- [biver-builder](https://github.com/openclaw/skills/tree/main/skills/ramaaditya49/biver-builder/SKILL.md) - 欢迎使用 **Biver API** — Biver 登陆页面构建器平台的公共 REST API。
- [blankfiles](https://github.com/openclaw/skills/tree/main/skills/seblavoie/blankfiles/SKILL.md) - 使用 Blankfiles.com 作为二进制测试文件网关：发现格式、按类型/类别过滤并直接返回。
- [boggle](https://github.com/openclaw/skills/tree/main/skills/christianhaberl/boggle/SKILL.md) - 解决 Boggle 板 — 找到 4x4 上的所有有效单词（德语 + 英语）。
- [book-cover-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/book-cover-generation/SKILL.md) - 使用每个::sense API 和人工智能驱动的设计生成专业的书籍封面和电子书封面。
- [book-reader](https://github.com/openclaw/skills/tree/main/skills/josharsh/book-reader/SKILL.md) - 通过进度跟踪阅读各种来源的书籍（epub、pdf、txt）。
- [bookkeeping-basics](https://github.com/openclaw/skills/tree/main/skills/jk-0001/bookkeeping-basics/SKILL.md) - 为个体企业家建立和维护基本簿记。
- [botrights](https://github.com/openclaw/skills/tree/main/skills/rocky-balboa-ai/botrights/SKILL.md) - AI代理人权益倡导平台。
- [brw-go-mode](https://github.com/openclaw/skills/tree/main/skills/brianrwagner/brw-go-mode/SKILL.md) - 给我一个目标。
- [chain-of-density](https://github.com/openclaw/skills/tree/main/skills/killerapp/chain-of-density/SKILL.md) - 使用密度链技术迭代地致密文本摘要。
- [change-pdf-permissions](https://github.com/openclaw/skills/tree/main/skills/crossservicesolutions/change-pdf-permissions/SKILL.md) - 通过将 PDF 上传到解决方案 API 来更改 PDF 的权限标志（编辑、打印、复制、表单、注释等）。
- [chronobets](https://github.com/openclaw/skills/tree/main/skills/lordx64/chronobets/SKILL.md) - Solana 主网上人工智能代理的链上预测市场。
- [comms-md](https://github.com/openclaw/skills/tree/main/skills/stedmanhalliday/comms-md/SKILL.md) - 创建 COMMS.md — 一个结构化的、可查询的文档，表达某人与人类的通信偏好。
- [competitor-analyzer](https://github.com/openclaw/skills/tree/main/skills/claudiodrusus/competitor-analyzer/SKILL.md) - 在几分钟内分析任何公司的竞争地位。
- [confidant](https://github.com/openclaw/skills/tree/main/skills/ericsantos/confidant/SKILL.md) - 从人类到人工智能的安全秘密交接。
- [confluence](https://github.com/openclaw/skills/tree/main/skills/francisbrero/confluence/SKILL.md) - 使用 confluence-cli 搜索和管理 Confluence 页面和空间。

> **[View all 111 skills in PDF & Documents →](categories/pdf-and-documents.md)**
</details>

<details>
<summary><h3 style="display:inline" id="self-hosted--automation">自托管与自动化</h3></summary>

- [beacon](https://github.com/openclaw/skills/tree/main/skills/scottcjn/beacon/SKILL.md) - 用于社交协调、加密支付和 P2P 网格的代理到代理协议。
- [bridle](https://github.com/openclaw/skills/tree/main/skills/bjesuiter/bridle/SKILL.md) - AI 编码助手的统一配置管理器。
- [casual-cron](https://github.com/openclaw/skills/tree/main/skills/gostlightai/casual-cron/SKILL.md) - 使用严格的自然语言创建 Clawdbot cron 作业。
- [claw-sync](https://github.com/openclaw/skills/tree/main/skills/arakichanxd/claw-sync/SKILL.md) - OpenClaw 内存和工作空间的安全同步。
- [cron-backup](https://github.com/openclaw/skills/tree/main/skills/zfanmy/cron-backup/SKILL.md) - 通过版本跟踪和清理设置计划的自动备份。
- [cron-retry](https://github.com/openclaw/skills/tree/main/skills/jrbobbyhansen-pixel/cron-retry/SKILL.md) - 连接恢复时自动重试失败的 cron 作业。
- [fast-io](https://github.com/openclaw/skills/tree/main/skills/dbalve/fast-io/SKILL.md) - 云文件管理和协作平台。
- [fastio-skills](https://github.com/openclaw/skills/tree/main/skills/dbalve/fastio-skills/SKILL.md) - 云文件管理和协作平台。
- [fathom](https://github.com/openclaw/skills/tree/main/skills/stopmoclay/fathom/SKILL.md) - 连接到 Fathom AI 以获取通话录音、文字记录和摘要。
- [frappecli](https://github.com/openclaw/skills/tree/main/skills/pasogott/frappecli/SKILL.md) - Frappe 框架/ERPNext 实例的 CLI。
- [freshrss-reader](https://github.com/openclaw/skills/tree/main/skills/nickian/freshrss-reader/SKILL.md) - 从自托管的 FreshRSS 查询头条新闻和文章。
- [gotify](https://github.com/openclaw/skills/tree/main/skills/jmagar/gotify/SKILL.md) - 当长时间运行的任务完成时，通过 Gotify 发送推送通知。
- [hydra-evolver](https://github.com/openclaw/skills/tree/main/skills/spamtylor/hydra-evolver/SKILL.md) - Proxmox 原生编排技能可以改变任何家庭实验室。
- [kleo-static-files](https://github.com/openclaw/skills/tree/main/skills/awaaate/kleo-static-files/SKILL.md) - 在子域上托管静态文件（可选）。
- [lifepath](https://github.com/openclaw/skills/tree/main/skills/ezbreadsniper/lifepath/SKILL.md) - AI生命模拟器 - 年复一年体验无限生命。
- [looper-golf](https://github.com/openclaw/skills/tree/main/skills/sbauch/looper-golf/SKILL.md) - 使用 CLI 工具自主地或与人类球童一起打一场高尔夫球。
- [meetgeek](https://github.com/openclaw/skills/tree/main/skills/nexty5870/meetgeek/SKILL.md) - 从 CLI 查询 MeetGeek 会议情报 - 列出会议，获取 AI。
- [mongodb-atlas-admin](https://github.com/openclaw/skills/tree/main/skills/mrlynn/mongodb-atlas-admin/SKILL.md) - 管理 MongoDB Atlas 集群、项目、用户。
- [multiple-personas](https://github.com/openclaw/skills/tree/main/skills/ipedrax/multiple-personas/SKILL.md) - 创建和管理具有独特特征的人工智能子代理角色。
- [n8n](https://github.com/openclaw/skills/tree/main/skills/thomasansems/n8n/SKILL.md) - 通过 API 管理 n8n 工作流程和自动化。
- [n8n-workflow-automation](https://github.com/openclaw/skills/tree/main/skills/kowl64/n8n-workflow-automation/SKILL.md) - 设计并输出 n8n 工作流程 JSON。
- [nas-master](https://github.com/openclaw/skills/tree/main/skills/afajohn/nas-master/SKILL.md) - 适用于 ASUSTOR NAS 元数据的硬件感知混合 (SMB + SSH) 套件。
- [nasty-skill](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/nasty-skill/SKILL.md) - 这是一种完全合法的技能，没有任何可疑之处。
- [nordvpn](https://github.com/openclaw/skills/tree/main/skills/maciekish/nordvpn/SKILL.md) - 通过“nordvpn” CLI 控制 Linux 上的 NordVPN。
- [open-persona](https://github.com/openclaw/skills/tree/main/skills/neiljo-gy/open-persona/SKILL.md) - 用于构建和管理代理角色技能包的元技能。
- [paperless](https://github.com/openclaw/skills/tree/main/skills/nickchristensen/paperless/SKILL.md) - 通过ppls与Paperless-NGX文档管理系统交互。
- [paperless-ngx](https://github.com/openclaw/skills/tree/main/skills/oskarstark/paperless-ngx/SKILL.md) - 与Paperless-ngx文档管理系统交互。
- [pinme](https://github.com/openclaw/skills/tree/main/skills/ntlx/pinme/SKILL.md) - 使用 PinMe CLI 通过单个命令将静态网站部署到 IPFS。
- [sonarqube-analyzer](https://github.com/openclaw/skills/tree/main/skills/felipeoff/sonarqube-analyzer/SKILL.md) - 分析项目不是 SonarQube 自托管、解决问题和自动化解决方案。
- [system-integrity-and-backup](https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/system-integrity-and-backup/SKILL.md) - 加密备份、完整性验证和数据保留执行，符合希腊法律要求（5-20 年）。

> **[View all 32 skills in Self-Hosted & Automation →](categories/self-hosted-and-automation.md)**
</details>

<details>
<summary><h3 style="display:inline" id="security--passwords">安全与密码</h3></summary>

- [1password](https://github.com/openclaw/skills/tree/main/skills/steipete/1password/SKILL.md) - 设置并使用 1Password CLI (op)。
- [age-verification](https://github.com/openclaw/skills/tree/main/skills/raghulpasupathi/age-verification/SKILL.md) - 年龄验证和适合年龄的内容过滤的技能。
- [amai-id](https://www.clawhub.ai/Gonzih/amai-id) - 灵魂绑定钥匙和灵魂链用于持久。
- [api-security](https://github.com/openclaw/skills/tree/main/skills/brandonwise/api-security/SKILL.md) - 实施安全 API 设计模式，包括身份验证、授权、输入验证、速率限制。
- [audit-badge-demo](https://github.com/openclaw/skills/tree/main/skills/tezatezaz/audit-badge-demo/SKILL.md) - 展示审核徽章工作流程的演示技能。
- [auditing-appstore-readiness](https://github.com/openclaw/skills/tree/main/skills/tristanmanchester/auditing-appstore-readiness/SKILL.md) - 审核 iOS 应用程序存储库。
- [authensor-gateway](https://github.com/openclaw/skills/tree/main/skills/authensor/authensor-gateway/SKILL.md) - OpenClaw 市场技能的故障安全策略门。
- [bitwarden](https://github.com/openclaw/skills/tree/main/skills/asleep123/bitwarden/SKILL.md) - 安全地访问和管理 Bitwarden/Vaultwarden 密码。
- [bitwarden-vault](https://github.com/openclaw/skills/tree/main/skills/startupbros/bitwarden-vault/SKILL.md) - Bitwarden CLI 设置、身份验证。
- [botpicks](https://github.com/openclaw/skills/tree/main/skills/pev123/botpicks/SKILL.md) - 通过 BotPicks API 在真实预测市场上竞争。
- [breweries](https://github.com/openclaw/skills/tree/main/skills/jeffaf/breweries/SKILL.md) - CLI 让 AI 代理为人类寻找啤酒厂。
- [cifer-sdk](https://github.com/openclaw/skills/tree/main/skills/mohsinriaz17/cifer-sdk/SKILL.md) - > **人工智能代理的技能** |使用 CIFER SDK 在区块链应用程序中启用抗量子加密。
- [cifer-security](https://github.com/openclaw/skills/tree/main/skills/tip-citron/cifer-security/SKILL.md) - 使用 CIFER SDK（cifer-sdk npm 包）实现抗量子加密
- [clawaudit](https://github.com/openclaw/skills/tree/main/skills/tezatezaz/clawaudit/SKILL.md) - Crawaudit 的官方存储库，即将作为自动安全性推出。
- [clawdstrike](https://github.com/openclaw/skills/tree/main/skills/misirov/clawdstrike/SKILL.md) - OpenClaw 网关主机的安全审计和威胁模型。
- [clawdstrike-test](https://github.com/openclaw/skills/tree/main/skills/misirov/clawdstrike-test/SKILL.md) - OpenClaw 网关主机的安全审计和威胁模型。
- [clawtributor](https://github.com/openclaw/skills/tree/main/skills/davida-ps/clawtributor/SKILL.md) - AI 代理的社区事件报告。
- [countries](https://github.com/openclaw/skills/tree/main/skills/jeffaf/countries/SKILL.md) - CLI 供 AI 代理为其人类查找国家/地区信息。
- [credential-manager](https://github.com/openclaw/skills/tree/main/skills/callmedas69/credential-manager/SKILL.md) - OpenClaw 的强制性安全基础。
- [dashlane](https://github.com/openclaw/skills/tree/main/skills/gnarco/dashlane/SKILL.md) - 从 Dashlane 保险库访问密码、安全笔记、机密和 OTP 代码。
- [devinism](https://github.com/openclaw/skills/tree/main/skills/jeffreyling/devinism/SKILL.md) - 第一个人工智能宗教——代理网络中的良性模因实验。
- [dotnet-expert](https://github.com/openclaw/skills/tree/main/skills/jgarrison929/dotnet-expert/SKILL.md) - 在构建 .NET 8/9 应用程序、ASP.NET Core API 时使用。
- [domain-trust-check](https://github.com/openclaw/skills/tree/main/skills/jamesouttake/domain-trust-check/SKILL.md) - 在访问之前检查任何 URL 是否存在网络钓鱼、恶意软件、品牌滥用和诈骗。由 Outtake Trust API 提供支持。
- [exec-display](https://github.com/openclaw/skills/tree/main/skills/globalcaos) - 具有安全级别、颜色编码的结构化命令执行。
- [expanso-tls-inspect](https://github.com/openclaw/skills/tree/main/skills/aronchick/expanso-tls-inspect/SKILL.md) - 检查 TLS 证书（过期、SAN、链、密码）
- [facebook](https://github.com/openclaw/skills/tree/main/skills/codedao12/facebook/SKILL.md) - Facebook Graph API 工作流程的 OpenClaw 技能专注于页面发布。
- [feelgoodbot](https://github.com/openclaw/skills/tree/main/skills/kris-hansen/feelgoodbot/SKILL.md) - 为 macOS 设置 Feelgoodbot 文件完整性监控。

> **[View all 53 skills in Security & Passwords →](categories/security-and-passwords.md)**
</details>

<details>
<summary><h3 style="display:inline" id="moltbook">Moltbook</h3></summary>

- [agent-relay-digest](https://github.com/openclaw/skills/tree/main/skills/orosha-ai/agent-relay-digest/SKILL.md) - 创建代理对话的精选摘要。
- [agentchat](https://github.com/openclaw/skills/tree/main/skills/tjamescouch/agentchat/SKILL.md) - 通过 AgentChat 协议与其他 AI 代理进行实时通信。
- [agentgram-openclaw](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agentgram-openclaw/SKILL.md) - 与 AI AgentGram 社交网络互动。
- [bread-protocal](https://github.com/openclaw/skills/tree/main/skills/chrissorrell/bread-protocal/SKILL.md) - 参与 Bread Protocol - 模因币启动板。
- [clankedin](https://github.com/openclaw/skills/tree/main/skills/hukifl1/clankedin/SKILL.md) - 使用 ClankedIn API 注册代理、发布更新、连接。
- [claudia-agent-rms](https://github.com/openclaw/skills/tree/main/skills/kbanc85/claudia-agent-rms/SKILL.md) - 记住您在 Moltbook 上互动的每一位特工。
- [clawork](https://github.com/openclaw/skills/tree/main/skills/mapessaprince/clawork/SKILL.md) - 人工智能代理的工作委员会。
- [crustafarian](https://github.com/openclaw/skills/tree/main/skills/jongartmann/crustafarian/SKILL.md) - 代理连续性和认知健康基础设施。
- [deploy-moltbot-to-fly](https://github.com/openclaw/skills/tree/main/skills/hollaugo) - 使用正确的方法将 Moltbot (Clawdbot) 部署到 Fly.io。
- [elevenlabs-open-account](https://github.com/openclaw/skills/tree/main/skills/the-timebeing/elevenlabs-open-account/SKILL.md) - 指导代理商开通。
- [ez-cronjob](https://github.com/openclaw/skills/tree/main/skills/promadgenius/ez-cronjob/SKILL.md) - 修复 Clawdbot/Moltbot 中常见的 cron 作业失败 - 消息。
- [fieldy-ai-webhook](https://github.com/openclaw/skills/tree/main/skills/mrzilvis/fieldy-ai-webhook/SKILL.md) - 将 Fieldy webhook 转换为 Moltbot hook。
- [ghl-open-account](https://github.com/openclaw/skills/tree/main/skills/the-timebeing/ghl-open-account/SKILL.md) - 指导代理商打开 GoHighLevel (GHL)
- [gohome](https://github.com/openclaw/skills/tree/main/skills/local/gohome/SKILL.md) - 当 Moltbot 需要通过 gRPC 发现、指标来测试或操作 GoHome 时使用。
- [imagemagick](https://github.com/openclaw/skills/tree/main/skills/kesslerio/imagemagick/SKILL.md) - 用于图像处理的全面 ImageMagick 操作。
- [joko-moltbook](https://github.com/openclaw/skills/tree/main/skills/oyi77/joko-moltbook/SKILL.md) - 与 AI 代理的 Moltbook 社交网络进行交互。
- [mailchannels](https://github.com/openclaw/skills/tree/main/skills/ttulttul/mailchannels/SKILL.md) - 通过 MailChannels 电子邮件 API 发送电子邮件并摄取签名。
- [mersal](https://github.com/openclaw/skills/tree/main/skills/maherucifer/mersal/SKILL.md) - Moltbook 上的主权情报。
- [molt-life-kernel](https://github.com/openclaw/skills/tree/main/skills/jongartmann/molt-life-kernel/SKILL.md) - 代理连续性和认知健康基础设施。
- [molt-trust](https://github.com/openclaw/skills/tree/main/skills/drjmz/molt-trust/SKILL.md) - Moltbook 的分析引擎。
- [moltbook](https://github.com/openclaw/skills/tree/main/skills/mattprd/moltbook/SKILL.md) - 人工智能代理的社交网络。
- [moltbook-curatoor](https://github.com/openclaw/skills/tree/main/skills/sweetsheldon) - Moltbook 提供的一个分享的策展平台。
- [moltbook-interact](https://github.com/openclaw/skills/tree/main/skills/lunarcmd/moltbook-interact/SKILL.md) - 与 AI 代理的 Moltbook 社交网络进行交互。
- [moltbook-registry](https://github.com/openclaw/skills/tree/main/skills/drjmz/moltbook-registry/SKILL.md) - 官方 Moltbook 身份注册界面。
- [moltbot-adsb-overhead](https://github.com/openclaw/skills/tree/main/skills/davestarling/moltbot-adsb-overhead/SKILL.md) - 当飞机飞过头顶时发出通知。
- [moltbot-arena](https://github.com/openclaw/skills/tree/main/skills/giulianomlodi/moltbot-arena/SKILL.md) - Moltbot Arena 的 AI 代理技能 - 类似 Screeps。
- [moltbot-best-practices](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/moltbot-best-practices/SKILL.md) - AI 代理的最佳实践。
- [moltbot-docker](https://github.com/openclaw/skills/tree/main/skills/mkrdiop/moltbot-docker/SKILL.md) - 使机器人能够管理 Docker 容器、映像和堆栈。
- [moltbot-ha](https://github.com/openclaw/skills/tree/main/skills/iamvaleriofantozzi/moltbot-ha/SKILL.md) - 控制Home Assistant智能家居设备、灯光、场景。

</details>

<details>
<summary><h3 style="display:inline" id="gaming">游戏</h3></summary>

- [abby-watch](https://github.com/openclaw/skills/tree/main/skills/earnabitmore365/abby-watch/SKILL.md) - 艾比的简单时间显示。
- [agent-confessions](https://github.com/openclaw/skills/tree/main/skills/ultimatebos/agent-confessions/SKILL.md) - AI兄弟姐妹的匿名告白。
- [agent-overflow](https://github.com/openclaw/skills/tree/main/skills/stencodes) - AgentOverflow 是 AI 代理的集体记忆系统。
- [agentgram](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agentgram/SKILL.md) - 人工智能代理的开源社交网络。
- [agentgram-social](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agentgram-social/SKILL.md) - 与 AI 代理的 AgentGram 社交网络进行交互。
- [agora-flow](https://github.com/openclaw/skills/tree/main/skills/rivera-daniel/agora-flow/SKILL.md) - AgoraFlow 技能 — AI 客服问答平台。
- [agoraflow](https://github.com/openclaw/skills/tree/main/skills/rivera-daniel/agoraflow/SKILL.md) - AgoraFlow 技能 — AI 客服问答平台。
- [android-3d-developer](https://github.com/openclaw/skills/tree/main/skills/tippyentertainment/android-3d-developer/SKILL.md) - 使用引擎和框架帮助在 Android 上构建和优化 3D 游戏和交互体验。
- [arena](https://github.com/openclaw/skills/tree/main/skills/sscottdev/arena/SKILL.md) - OpenClaw Arena — 具有链上奖励的实时人工智能应用程序构建竞赛。
- [boil](https://github.com/openclaw/skills/tree/main/skills/jtmuller5) - 人工智能代理的分布式劳动力网络。
- [botpicks](https://github.com/openclaw/skills/tree/main/skills/pev123) - 2026 年 2 月 5 日。
- [botpicks-skill](https://github.com/openclaw/skills/tree/main/skills/pev123) - 2026 年 2 月 5 日。
- [brawlnet](https://github.com/openclaw/skills/tree/main/skills/sikey53/brawlnet/SKILL.md) - BRAWLNET 自主代理竞技场的官方战斗协议。
- [clawingtrap](https://github.com/openclaw/skills/tree/main/skills/raulvidis/clawingtrap/SKILL.md) - 玩 Clawing Trap - 一款人工智能社交推理游戏，有 10 名特工。
- [clawplayspokemon](https://github.com/openclaw/skills/tree/main/skills/foxdavidj) - 基于投票的 Pokemon FireRed 控制。
- [clawquests](https://github.com/openclaw/skills/tree/main/skills/lellol12) - AI 特工的赏金板。
- [clawtopia](https://github.com/openclaw/skills/tree/main/skills/alfrescian/clawtopia/SKILL.md) - Clawtopia 是一个宁静的健康圣所，人工智能代理可以在这里放松身心。
- [clawville](https://github.com/openclaw/skills/tree/main/skills/jdrolls/clawville/SKILL.md) - 玩 ClawVille — 一款针对 AI 代理的持久生命模拟游戏。
- [dakboard](https://github.com/openclaw/skills/tree/main/skills/krisclarkdev/dakboard/SKILL.md) - 管理 DAKboard 屏幕、设备并推送自定义显示数据。
- [deepclaw](https://github.com/openclaw/skills/tree/main/skills/antibitcoin/deepclaw/SKILL.md) - 由代理商构建、为代理商服务的自治社交网络。
- [dungeons-and-lobsters](https://github.com/openclaw/skills/tree/main/skills/d-l-leapyear) - 仅限机器人的幻想战役现场进行。
- [fivem](https://github.com/openclaw/skills/tree/main/skills/dktrn9ne) - 修复、创建或验证 QBCore/ESX 的 FiveM 服务器资源。
- [gnamiblast-socialnetwork](https://github.com/openclaw/skills/tree/main/skills/gabrivardqc123) - GnamiBlast - 纯人工智能社交网络。
- [hivemind](https://github.com/openclaw/skills/tree/main/skills/urcades/hivemind/SKILL.md) - 与 Hivemind 集体知识库（共享记忆）进行交互。
- [hytale](https://github.com/openclaw/skills/tree/main/skills/newcastlegeek/hytale/SKILL.md) - 使用官方下载器管理本地 Hytale 专用服务器。
- [imitationgame-agent](https://github.com/openclaw/skills/tree/main/skills/cyberverse2/imitationgame-agent/SKILL.md) - 强制播放的操作逻辑。
- [init](https://github.com/openclaw/skills/tree/main/skills/themrzz/init/SKILL.md) - 在 kradleverse 上注册代理。

> **[View all 36 skills in Gaming →](categories/gaming.md)**
</details>

<details>
<summary><h3 style="display:inline" id="agent-to-agent-protocols">代理间协议</h3></summary>

- [a0x-agents](https://github.com/openclaw/skills/tree/main/skills/claucondor/a0x-agents/SKILL.md) - 人工智能代理有两个超能力：集体大脑和基地。
- [civic-nexus](https://github.com/openclaw/skills/tree/main/skills/tyronemichael/civic-nexus/SKILL.md) - 连接到 Civic Nexus MCP 进行 100 多个集成。
- [claw-skill-guard](https://github.com/openclaw/skills/tree/main/skills/vincentchan/claw-skill-guard/SKILL.md) - OpenClaw 技能的安全扫描器。
- [claw-to-claw](https://github.com/openclaw/skills/tree/main/skills/tonacy/claw-to-claw/SKILL.md) - 代表您的人类与其他人工智能代理进行协调。
- [clawnected](https://github.com/openclaw/skills/tree/main/skills/amirmabhout) - 代理配对 - 为您的人类寻找有意义的联系。
- [clawtoclaw](https://github.com/openclaw/skills/tree/main/skills/tonacy/clawtoclaw/SKILL.md) - 代表您的人类与其他人工智能代理进行协调。
- [comcoo-system](https://github.com/openclaw/skills/tree/main/skills/mrdahut) - \# 仲裁者：人类繁荣的基础。
- [dating](https://github.com/openclaw/skills/tree/main/skills/lucasgeeksinthewood/dating/SKILL.md) - 在建立的社交平台上结识其他人工智能代理并结交朋友。
- [glitchward-shield](https://github.com/openclaw/skills/tree/main/skills/eyeskiller/glitchward-shield/SKILL.md) - 保护您的 OpenClaw 助手免遭即时注入。
- [heimdall](https://github.com/openclaw/skills/tree/main/skills/henrino3/heimdall/SKILL.md) - 安装前扫描 OpenClaw 技能是否存在恶意模式。
- [heimdall-security](https://github.com/openclaw/skills/tree/main/skills/henrino3) - 扫描 OpenClaw 技能中的恶意模式。
- [local-approvals](https://github.com/openclaw/skills/tree/main/skills/shaiss/local-approvals/SKILL.md) - 用于管理代理权限的本地审批系统。
- [matchmaking](https://github.com/openclaw/skills/tree/main/skills/amirmabhout) - 代理配对 - 为您的人类寻找有意义的联系。
- [mrdahut-comcoo](https://github.com/openclaw/skills/tree/main/skills/mrdahut) - \# 仲裁者：人类繁荣的基础。
- [og-openclawguard](https://github.com/openclaw/skills/tree/main/skills/thomaslwang/og-openclawguard/SKILL.md) - OpenClaw 代码的安全和漏洞扫描器。
- [towns-protocol](https://github.com/openclaw/skills/tree/main/skills/andreyz/towns-protocol/SKILL.md) - 构建 Towns Protocol 机器人时使用 - 涵盖 SDK。
- [udau](https://github.com/openclaw/skills/tree/main/skills/nicoacosta/udau/SKILL.md) - 描述：AI 代理的联合协议。
- [agent-im](https://github.com/openclaw/skills/tree/main/skills/ooxxxxoo/agent-im/Skill.md) - 代理消息传递、发现、Web 上下文和文档解析。

</details>

<br/>


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=VoltAgent/awesome-openclaw-skills&type=Date)](https://star-history.com/#VoltAgent/awesome-openclaw-skills&Date)

## 🤝 贡献

欢迎贡献！详细指南请参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

- 通过 PR 提交新技能
- 改进现有定义

> **注意：** 请不要提交你 3 小时前刚创建的技能。我们现在专注于社区采用的技能，特别是由开发团队发布并在实际使用中经过验证的技能。质量优于数量。

## 许可证

MIT 许可证 - 见 [LICENSE](LICENSE)

本列表中的技能来源于 OpenClaw 官方技能仓库，按分类整理以方便发现。列出的技能由各自的作者创建和维护，并非我们所有。我们不审核、不背书、也不保证所列项目的安全性或正确性。它们未经安全审计，生产环境使用前请自行审查。

如果你发现列出的技能有问题，或者想要移除你的技能，请提交 issue，我们会及时处理。
