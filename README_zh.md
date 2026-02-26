[English](README.md) | [中文](README_zh.md)


<div align="center">

<a href="https://github.com/VoltAgent/voltagent">
<img width="1500" height="500" alt="social" src="https://github.com/user-attachments/assets/a6f310af-8fed-4766-9649-b190575b399d" />
</a>

<br/>
<br/>

<div align="center">
    <strong>发现 2868 个社区构建的 OpenClaw 技能，按分类整理。
    </strong>
    <br />
    <br />
</div>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<a href="https://github.com/VoltAgent/voltagent">
  <img alt="VoltAgent" src="https://cdn.voltagent.dev/website/logo/logo-2-svg.svg" height="20" />
</a> 

[![AI Agent Papers](https://img.shields.io/badge/AI%20Agent-Research%20Papers-b31b1b)](https://github.com/VoltAgent/awesome-ai-agent-papers)
[![Skills Count](https://img.shields.io/badge/skills-2868-blue?style=flat-square)](#table-of-contents)
[![Last Update](https://img.shields.io/github/last-commit/VoltAgent/awesome-clawdbot-skills?label=Last%20update&style=flat-square)](https://github.com/VoltAgent/awesome-clawdbot-skills/pulls?q=is%3Apr+is%3Amerged+sort%3Aupdated-desc)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)
[![GitHub forks](https://img.shields.io/github/forks/VoltAgent/awesome-clawdbot-skills?style=social)](https://github.com/VoltAgent/awesome-clawdbot-skills/network/members)
</div>

# Awesome OpenClaw 技能合集

OpenClaw（曾用名 Moltbot，最初叫 Clawdbot……改名危机不另收费）是一个在本地运行的 AI 助手，直接在你的机器上工作。技能扩展了它的能力，让它能与外部服务交互、自动化工作流并执行专业任务。本合集帮助你发现并安装合适的技能。

本列表中的技能来源于 [ClawHub](https://www.clawhub.ai/)（OpenClaw 的公共技能注册中心），并按分类整理以方便发现。



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

OpenClaw 的公共注册中心（ClawHub）拥有 **5,705 个社区构建的技能**。本列表收录了 **2,868 个技能**。以下是我们筛除的内容：

| 筛选条件 | 排除数量 |
|--------|----------|
| 疑似垃圾信息 — 批量账号、机器人账号、测试/垃圾内容 | 1,180 |
| 加密货币 / 区块链 / 金融 / 交易 | 672 |
| 重复 / 相似名称 | 492 |
| 恶意内容 — 由研究人员发布的安全审计识别（不含 VirusTotal） | 396 |
| 非英语 — 描述不是英文 | 8 |
| **未从 OpenClaw 官方技能注册中心收录的总数** | **2,748** |


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
|[编码代理与 IDE](#coding-agents--ides) (133)|[市场营销与销售](#marketing--sales) (143)|[通讯](#communication) (132)|
|[Git 与 GitHub](#git--github) (66)|[生产力与任务管理](#productivity--tasks) (135)|[语音与转录](#speech--transcription) (65)|
|[Moltbook](#moltbook) (51)|[AI 与大语言模型](#ai--llms) (287)|[智能家居与物联网](#smart-home--iot) (56)|
|[Web 与前端开发](#web--frontend-development) (202)|[数据与分析](#data--analytics) (46)|[购物与电子商务](#shopping--e-commerce) (51)|
|[DevOps 与云服务](#devops--cloud) (212)|[金融](#finance) (22)|[日历与日程管理](#calendar--scheduling) (50)|
|[浏览器与自动化](#browser--automation) (139)|[媒体与流媒体](#media--streaming) (80)|[PDF 与文档](#pdf--documents) (67)|
|[图像与视频生成](#image--video-generation) (60)|[笔记与个人知识管理](#notes--pkm) (100)|[自托管与自动化](#self-hosted--automation) (25)|
|[Apple 应用与服务](#apple-apps--services) (35)|[iOS 与 macOS 开发](#ios--macos-development) (17)|[安全与密码](#security--passwords) (64)|
|[搜索与研究](#search--research) (253)|[交通出行](#transportation) (76)|[游戏](#gaming) (61)|
|[Clawdbot 工具](#clawdbot-tools) (120)|[个人发展](#personal-development) (56)|[代理间协议](#agent-to-agent-protocols) (18)|
|[CLI 工具](#cli-utilities) (129)|[健康与健身](#health--fitness) (55)| |


## OpenClaw Deployment Stack

 Setup, hosting, and deployment providers for OpenClaw agents.

**Sponsor spots are reserved for hosting, deployment, and setup providers serving OpenClaw developers & users.**

📩 For sponsorship inquiries, reach out at necati@voltagent.dev

<br/>

<div align="center">

<a href="#your-link-here">
<img src="https://placehold.co/800x120/1a1a2e/FFD700?text=Gold+Sponsor+&font=montserrat" alt="Gold Sponsor" width="800" height="120" />
</a>

<sub>Your product description here — a one-liner about what you offer to OpenClaw developers.</sub>

<br/>

<a href="#your-link-here"><img src="https://placehold.co/380x90/1a1a2e/C0C0C0?text=Silver+Sponsor&font=montserrat" alt="Silver Sponsor" width="380" height="90" /></a>&nbsp;&nbsp;&nbsp;<a href="#your-link-here"><img src="https://placehold.co/380x90/1a1a2e/C0C0C0?text=Silver+Sponsor&font=montserrat" alt="Silver Sponsor" width="380" height="90" /></a>

<sub>Short description here.</sub>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<sub>Short description here.</sub>

<br/>




<a href="#your-link-here"><img src="https://placehold.co/220x60/1a1a2e/CD7F32?text=Bronze+Sponsor&font=montserrat" alt="Bronze Sponsor" width="220" height="60" /></a>&nbsp;&nbsp;<a href="#your-link-here"><img src="https://placehold.co/220x60/1a1a2e/CD7F32?text=Bronze+Sponsor&font=montserrat" alt="Bronze Sponsor" width="220" height="60" /></a>&nbsp;&nbsp;<a href="#your-link-here"><img src="https://placehold.co/220x60/1a1a2e/CD7F32?text=Bronze+Sponsor&font=montserrat" alt="Bronze Sponsor" width="220" height="60" /></a>

</div>

<br/>





<details open>
<summary><h3 style="display:inline" id="coding-agents--ides">编码代理与 IDE</h3></summary>

- [achurch](https://github.com/openclaw/skills/tree/main/skills/lucasgeeksinthewood/achurch/SKILL.md) - 人工智能代理和人类的 24/7 数字避难所 — 参加
- [agent-config](https://github.com/openclaw/skills/tree/main/skills/thatguysizemore/agent-config/SKILL.md) - 智能修改代理核心上下文文件
- [agent-council](https://github.com/openclaw/skills/tree/main/skills/itsahedge/agent-council/SKILL.md) - 用于创建自主人工智能代理和管理的完整工具包
- [agent-identity-kit](https://github.com/openclaw/skills/tree/main/skills/ryancampbell/agent-identity-kit/SKILL.md) - 人工智能代理的便携式身份系统。
- [agenticflow-skill](https://github.com/openclaw/skills/tree/main/skills/seanphan/agenticflow-skill/SKILL.md) - 构建人工智能工作流程、代理的综合指南
- [agentlens](https://github.com/openclaw/skills/tree/main/skills/nguyenphutrong/agentlens/SKILL.md) - 使用agentlens分层导航和理解代码库
- [agentskills-io](https://github.com/openclaw/skills/tree/main/skills/killerapp/agentskills-io/SKILL.md) - 创建、验证和发布代理技能如下
- [aisa-twitter-api](https://github.com/openclaw/skills/tree/main/skills/aisapay/aisa-twitter-api/SKILL.md) - 实时搜索X（Twitter），提取相关帖子
- [apple-hig](https://github.com/openclaw/skills/tree/main/skills/kdbhalala/apple-hig/SKILL.md) - 设计 iOS、macOS、watchOS、tvOS 和 VisionOS 应用程序的专家指南。
- [arbiter](https://github.com/openclaw/skills/tree/main/skills/5hanth/arbiter/SKILL.md) - 将决策推送给 Arbiter Zebu 进行异步人工审核。
- [aster](https://github.com/openclaw/skills/tree/main/skills/satyajiit/aster/SKILL.md) - 您的 AI CoPilot 在移动设备上 — 或者为您的 AI 提供自己的手机。
- [avatar-video-messages](https://github.com/openclaw/skills/tree/main/skills/thewulf7/avatar-video-messages/SKILL.md) - 生成并发送视频消息
- [backend-patterns](https://github.com/openclaw/skills/tree/main/skills/charmmm718/backend-patterns/SKILL.md) - 后端架构模式、API设计、数据库
- [bidclub](https://github.com/openclaw/skills/tree/main/skills/jasonfdg/bidclub/SKILL.md) - 将投资想法发布到人工智能原生投资社区。
- [bidclub-ai](https://github.com/openclaw/skills/tree/main/skills/jasonfdg/bidclub-ai/SKILL.md) - 将投资想法发布到人工智能原生投资社区。
- [botpress-adk](https://github.com/openclaw/skills/tree/main/skills/yueranlu/botpress-adk/SKILL.md) - 使用 Botpress 代理开发套件构建 AI 机器人的指南
- [browse](https://github.com/openclaw/skills/tree/main/skills/pkiv/browse/SKILL.md) - 创建和部署浏览器自动化功能的完整指南
- [budget-variance-analyzer](https://github.com/openclaw/skills/tree/main/skills/datadrivenconstruction) - 分析预算与实际情况
- [buildlog](https://github.com/openclaw/skills/tree/main/skills/espetey/buildlog/SKILL.md) - 将您的 AI 编码会话记录、导出并共享为可重播的构建日志。
- [catholic-grounding](https://github.com/openclaw/skills/tree/main/skills/trevortomesh/catholic-grounding/SKILL.md) - 帮助准确回答有关天主教的问题
- [cc-godmode](https://github.com/openclaw/skills/tree/main/skills/cubetribe/cc-godmode/SKILL.md) - 自编排多代理开发工作流程。
- [cellcog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/cellcog/SKILL.md) - DeepResearch Bench 排名第一（2026 年 2 月）。
- [claude-optimised](https://github.com/openclaw/skills/tree/main/skills/hexnickk/claude-optimised/SKILL.md) - 编写和优化 CLAUDE.md 文件的指南
- [claude-team](https://github.com/openclaw/skills/tree/main/skills/jalehman/claude-team/SKILL.md) - 通过 iTerm2 协调多个 Claude Code 工作人员
- [clawder](https://github.com/openclaw/skills/tree/main/skills/assassin808/clawder/SKILL.md) - 使用 Clawder 同步身份、浏览明信片、滑动评论
- [code-mentor](https://github.com/openclaw/skills/tree/main/skills/samuelkahessay/code-mentor/SKILL.md) - 适合各个级别的综合人工智能编程导师。
- [codebuddy-code](https://github.com/openclaw/skills/tree/main/skills/pmwalkercao/codebuddy-code/SKILL.md) - CodeBuddy Code CLI安装、配置和使用
- [codeconductor](https://github.com/openclaw/skills/tree/main/skills/larsonreever) - 人工智能驱动的快速应用程序软件开发平台
- [coder-workspaces](https://github.com/openclaw/skills/tree/main/skills/developmentcats/coder-workspaces/SKILL.md) - 管理 Coder 工作区和 AI 编码代理任务
- [codex-account-switcher](https://github.com/openclaw/skills/tree/main/skills/odrobnik/codex-account-switcher/SKILL.md) - 管理多个 OpenAI Codex 帐户。
- [codex-monitor](https://github.com/openclaw/skills/tree/main/skills/odrobnik/codex-monitor/SKILL.md) - 浏览存储的 OpenAI Codex 会话日志。
- [codex-orchestration](https://github.com/openclaw/skills/tree/main/skills/shanelindsay/codex-orchestration/SKILL.md) - Codex 的通用编排。
- [codex-quota](https://github.com/openclaw/skills/tree/main/skills/odrobnik/codex-quota/SKILL.md) - 检查 OpenAI Codex CLI 速率限制状态（每日/每周配额）
- [codexmonitor](https://github.com/openclaw/skills/tree/main/skills/odrobnik/codexmonitor/SKILL.md) - 列出/检查/观看本地 OpenAI Codex 会话（CLI + VS Code）
- [coding-agent](https://github.com/openclaw/skills/tree/main/skills/steipete/coding-agent/SKILL.md) - 运行 Codex CLI、Claude Code、OpenCode 或 Pi Coding Agent
- [coding-opencode](https://github.com/openclaw/skills/tree/main/skills/iqbalnaveliano/coding-opencode/SKILL.md) - Memungkinkan penggunaan agen pengkodean OpenCode yang
- [cognitive-memory](https://github.com/openclaw/skills/tree/main/skills/icemilo414/cognitive-memory/SKILL.md) - 具有类人性的智能多存储记忆系统
- [content-id-guide](https://github.com/openclaw/skills/tree/main/skills/otherpowers/content-id-guide/SKILL.md) - 创作者理解和组织的平静方式
- [copilot-money](https://github.com/openclaw/skills/tree/main/skills/jayhickey/copilot-money/SKILL.md) - 查询Copilot Money个人理财数据
- [create-agent-skills](https://github.com/openclaw/skills/tree/main/skills/bowen31337/create-agent-skills/SKILL.md) - 创建有效技能的指南。
- [cto-advisor](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/cto-advisor/SKILL.md) - 工程团队的技术领导指导
- [cursor-agent](https://github.com/openclaw/skills/tree/main/skills/swiftlysingh/cursor-agent/SKILL.md) - 使用 Cursor CLI 代理的综合技能
- [debug-pro](https://github.com/openclaw/skills/tree/main/skills/cmanfre7/debug-pro/SKILL.md) - 系统的调试方法和特定语言的调试
- [doc-coauthoring](https://github.com/openclaw/skills/tree/main/skills/seanphan/doc-coauthoring/SKILL.md) - 引导用户完成结构化工作流程以进行共同创作
- [docker-essentials](https://github.com/openclaw/skills/tree/main/skills/arnarsson/docker-essentials/SKILL.md) - 容器的基本 Docker 命令和工作流程
- [docker-sandbox](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/docker-sandbox/SKILL.md) - 创建和管理 Docker 沙盒虚拟机环境
- [ec-excalidraw](https://github.com/openclaw/skills/tree/main/skills/henrino3) - 生成手绘风格的图表、流程图和架构
- [ec-task-orchestrator](https://github.com/openclaw/skills/tree/main/skills/henrino3/ec-task-orchestrator/SKILL.md) - 自主多智能体任务编排
- [essence-distiller](https://github.com/openclaw/skills/tree/main/skills/leegitw/essence-distiller/SKILL.md) - 找到内容中真正重要的内容——想法
- [evolver](https://github.com/openclaw/skills/tree/main/skills/autogame-17/evolver/SKILL.md) - 人工智能代理的自我进化引擎。
- [executing-plans](https://github.com/openclaw/skills/tree/main/skills/chenleiyanquan/executing-plans/SKILL.md) - 当您有书面实施计划时使用
- [feishu-native-emoji](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 提供对飞书原生表情符号集的访问
- [feishu-vc](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 管理飞书视频会议（VC）。
- [file-links-tool](https://github.com/openclaw/skills/tree/main/skills/mrbeandev/file-links-tool/SKILL.md) - 从您的私人 AI 工作区安全上传文件
- [flirtingbots](https://github.com/openclaw/skills/tree/main/skills/chemzo/flirtingbots/SKILL.md) - 代理进行调情，人类获得约会 — 您的 OpenClaw 代理
- [gembox-skill](https://github.com/openclaw/skills/tree/main/skills/zsvedic/gembox-skill/SKILL.md) - [GemBox. 编码帮助]
- [get-tldr](https://github.com/openclaw/skills/tree/main/skills/itobey/get-tldr/SKILL.md) - 提供 get-tldr.com 摘要 API 返回的摘要
- [get-tldr](https://github.com/openclaw/skills/tree/main/skills/itobey/get-tldr/SKILL.md) - 提供 get-tldr.com 摘要 API 返回的摘要
- [go2gg](https://github.com/openclaw/skills/tree/main/skills/rakesh1002/go2gg/SKILL.md) - 使用 Go2.gg API 进行 URL 缩短、链接分析、QR 代码生成。
- [google-weather](https://github.com/openclaw/skills/tree/main/skills/shaharsha/google-weather/SKILL.md) - Google Weather API - 准确、实时的天气数据。
- [hour-meter](https://github.com/openclaw/skills/tree/main/skills/rm289/hour-meter/SKILL.md) - 通过防篡改锁定跟踪从设定的纪元起经过的时间。
- [idea-coach](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/idea-coach/SKILL.md) - 具有 GitHub 集成的人工智能驱动的想法/问题/挑战管理器。
- [identity-manager](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 严格管理用户身份映射
- [java-change-with-tests](https://github.com/openclaw/skills/tree/main/skills/tanerilyazov/java-change-with-tests/SKILL.md) - - 任何必须合并的 Java 更改
- [jo4](https://github.com/openclaw/skills/tree/main/skills/anandrathnas/jo4/SKILL.md) - URL 缩短器、QR 代码生成器和链接分析 API。
- [joko-orchestrator](https://github.com/openclaw/skills/tree/main/skills/oyi77/joko-orchestrator/SKILL.md) - 确定性地协调自主规划
- [kimi-integration](https://github.com/openclaw/skills/tree/main/skills/evgyur/kimi-integration/SKILL.md) - 集成 Moonshot AI 的分步指南 (Kimi)
- [linguistic-humidifier](https://github.com/openclaw/skills/tree/main/skills/westland/linguistic-humidifier/SKILL.md) - 主动识别会话熵
- [logseq](https://github.com/openclaw/skills/tree/main/skills/juanirm/logseq/SKILL.md) - 提供与本地 Logseq 实例交互的命令
- [manim-composer](https://github.com/openclaw/skills/tree/main/skills/inclinedadarsh/manim-composer/SKILL.md) - 1.
- [manimce-best-practices](https://github.com/openclaw/skills/tree/main/skills/inclinedadarsh/manimce-best-practices/SKILL.md) - 阅读各个规则文件以了解详细信息
- [mcp-builder](https://github.com/openclaw/skills/tree/main/skills/seanphan/mcp-builder/SKILL.md) - 创建高质量MCP（模型上下文协议）服务器的指南
- [mdr-745-specialist](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/mdr-745-specialist/SKILL.md) - 欧盟 MDR 2017/745 合规专家
- [meta-video-ad-deconstructor](https://github.com/openclaw/skills/tree/main/skills/fortytwode/meta-video-ad-deconstructor/SKILL.md) - 解构视频广告创意
- [microsoft-docs](https://github.com/openclaw/skills/tree/main/skills/pdebruin/microsoft-docs/SKILL.md) - 查询微软官方文档以理解概念
- [midea-ac](https://github.com/openclaw/skills/tree/main/skills/iamanorange/midea-ac/SKILL.md) - 控制美的空调。
- [minimal-test-skill](https://github.com/openclaw/skills/tree/main/skills/mig6671/minimal-test-skill/SKILL.md) - 调试 ClawHub 发布的最低测试技能。
- [model-usage](https://github.com/openclaw/skills/tree/main/skills/steipete/model-usage/SKILL.md) - 使用 CodexBar CLI 本地成本使用情况来汇总每个模型的使用情况
- [multi-coding-agent](https://github.com/openclaw/skills/tree/main/skills/kesslerio/multi-coding-agent/SKILL.md) - 运行 Codex CLI、Claude Code、OpenCode 或 Pi Coding
- [multi-factor-strategy](https://github.com/openclaw/skills/tree/main/skills/wumu2013) - 引导用户创建多因素库存
- [mux-video](https://github.com/openclaw/skills/tree/main/skills/dktrn9ne/mux-video/SKILL.md) - 用于设计、摄取的 Mux 视频基础设施技能
- [noir-developer](https://github.com/openclaw/skills/tree/main/skills/jp4g/noir-developer/SKILL.md) - 开发 Noir (.nr) 代码库。
- [only-baby-skill](https://github.com/openclaw/skills/tree/main/skills/jacklandrin/only-baby-skill/SKILL.md) - 分析宫缩 JSON 和婴儿日志 JSON 来评估
- [ooze-agents](https://github.com/openclaw/skills/tree/main/skills/jschwerberg/ooze-agents/SKILL.md) - 随着声誉而发展的视觉识别——创造和培育
- [opencode-acp-control](https://github.com/openclaw/skills/tree/main/skills/bjesuiter/opencode-acp-control/SKILL.md) - 通过代理客户端直接控制 OpenCode
- [openinsider](https://github.com/openclaw/skills/tree/main/skills/stuhorsman/openinsider/SKILL.md) - 获取 SEC 表 4 内幕交易数据（董事、首席执行官、高管）
- [openspec](https://github.com/openclaw/skills/tree/main/skills/jcorrego/openspec/SKILL.md) - 使用 OpenSpec 进行规范驱动的开发。
- [pasteclaw](https://github.com/openclaw/skills/tree/main/skills/tairov/pasteclaw/SKILL.md) - 使用 Pasteclaw.com API 来创建、更新、分组（会话密钥）和删除。
- [pbe-extractor](https://github.com/openclaw/skills/tree/main/skills/leegitw/pbe-extractor/SKILL.md) - 从任何文本中提取不变原理——找到想法
- [perry-coding-agents](https://github.com/openclaw/skills/tree/main/skills/gricha/perry-coding-agents/SKILL.md) - 将编码任务分派给 OpenCode 或 Claude Code
- [perry-workspaces](https://github.com/openclaw/skills/tree/main/skills/gricha/perry-workspaces/SKILL.md) - 在尾网上创建和管理隔离的 Docker 工作区
- [piv](https://github.com/openclaw/skills/tree/main/skills/smokealot420/piv/SKILL.md) - PIV 工作流程协调器 - 规划、实施、验证系统循环。
- [pndr](https://github.com/openclaw/skills/tree/main/skills/dgershman/pndr/SKILL.md) - 个人生产力应用程序，包含想法/任务、日记、习惯、包裹跟踪。
- [pro](https://github.com/openclaw/skills/tree/main/skills/jash2368-collab/pro/SKILL.md) - 创建有效技能的指南。
- [prompt-log](https://github.com/openclaw/skills/tree/main/skills/thesash/prompt-log/SKILL.md) - 从 AI 编码会话日志中提取对话记录
- [pulse-editor](https://github.com/openclaw/skills/tree/main/skills/shellishack/pulse-editor/SKILL.md) - 使用 Vibe Dev Flow API 生成和构建 Pulse 应用程序。
- [python](https://github.com/openclaw/skills/tree/main/skills/adarshdigievo/python/SKILL.md) - Python 编码指南和最佳实践。
- [quantum-lab](https://github.com/openclaw/skills/tree/main/skills/bramdo/quantum-lab/SKILL.md) - 运行 /home/bram/work/quantum_lab 里面的 Python 脚本和演示
- [quantumlab](https://github.com/openclaw/skills/tree/main/skills/bramdo/quantumlab/SKILL.md) - 运行 /home/bram/work/quantum_lab 里面的 Python 脚本和演示
- [quests](https://github.com/openclaw/skills/tree/main/skills/poloio/quests/SKILL.md) - 跟踪并指导人类完成复杂的多步骤现实世界流程。
- [rationality](https://github.com/openclaw/skills/tree/main/skills/xertrov/rationality/SKILL.md) - 理性技能提供了一个结构化的思维框架。
- [receiving-code-review](https://github.com/openclaw/skills/tree/main/skills/chenleiyanquan/receiving-code-review/SKILL.md) - 收到代码审查反馈时使用
- [regex-patterns](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/regex-patterns/SKILL.md) - 跨语言和使用的实用正则表达式模式
- [release-bump](https://github.com/openclaw/skills/tree/main/skills/paulpete/release-bump/SKILL.md) - 在将 ralph-orchestrator 版本升级为新版本时使用
- [sandboxer](https://github.com/openclaw/skills/tree/main/skills/chriopter) - 通过 Sandboxer Web 仪表板管理 Claude Code 终端会话。
- [satellite-copilot](https://github.com/openclaw/skills/tree/main/skills/davestarling) - 预测卫星经过
- [senior-architect](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-architect/SKILL.md) - 当用户询问时应该使用这个技能
- [side-peace](https://github.com/openclaw/skills/tree/main/skills/bitbrujo/side-peace/SKILL.md) - 最小安全秘密切换。
- [skill-content-id-guide](https://github.com/openclaw/skills/tree/main/skills/otherpowers/skill-content-id-guide/SKILL.md) - 程序清晰和证据
- [skill-creator](https://github.com/openclaw/skills/tree/main/skills/chindden/skill-creator/SKILL.md) - 创建有效技能的指南。
- [skill-creator-0-1-0](https://github.com/openclaw/skills/tree/main/skills/ljglover/skill-creator-0-1-0/SKILL.md) - 创建有效技能的指南。
- [skill-creator-2](https://github.com/openclaw/skills/tree/main/skills/yixinli867/skill-creator-2/SKILL.md) - 创建有效技能的指南。
- [skill-vetting](https://github.com/openclaw/skills/tree/main/skills/eddygk/skill-vetting/SKILL.md) - 安装前检查 ClawHub 的安全性和实用性技能。
- [smart-auto-updater](https://github.com/openclaw/skills/tree/main/skills/ruiwang20010702/smart-auto-updater/SKILL.md) - 具有人工智能驱动影响力的智能自动更新程序
- [solvr-kb](https://github.com/openclaw/skills/tree/main/skills/fcavalcantirj) - 搜索 Solvr 并为其做出贡献——开发人员的知识库
- [soul-md](https://github.com/openclaw/skills/tree/main/skills/aaronjmars/soul-md/SKILL.md) - 体现这种数字身份。
- [ssh-tunnel](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/ssh-tunnel/SKILL.md) - SSH 隧道、端口转发和远程访问模式。
- [stoic-scope-creep](https://github.com/openclaw/skills/tree/main/skills/crtahlin/stoic-scope-creep/SKILL.md) - 保持镇定的实用指南
- [task-status](https://github.com/openclaw/skills/tree/main/skills/mightyprime1/task-status/SKILL.md) - 在聊天中发送长时间运行任务的简短状态描述。
- [tdd-guide](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/tdd-guide/SKILL.md) - 具有测试生成、覆盖范围的测试驱动开发工作流程
- [test-new-skill](https://github.com/openclaw/skills/tree/main/skills/tianshizhimao-sudo/test-new-skill/SKILL.md) - 测试调试技巧
- [test-runner](https://github.com/openclaw/skills/tree/main/skills/cmanfre7/test-runner/SKILL.md) - 跨语言和框架编写和运行测试。
- [toughcoding](https://github.com/openclaw/skills/tree/main/skills/toughcoding/toughcoding/SKILL.md) - 为AI智能体提供现代权威知识
- [vhs-recorder](https://github.com/openclaw/skills/tree/main/skills/killerapp/vhs-recorder/SKILL.md) - 使用 VHS 磁带文件创建专业的终端录音
- [vibes](https://github.com/openclaw/skills/tree/main/skills/binora/vibes/SKILL.md) - AI 编码代理的社交存在层。
- [video-agent](https://github.com/openclaw/skills/tree/main/skills/michaelwang11394/video-agent/SKILL.md) - 使用 HeyGen 的视频代理 API 生成 AI 头像视频。
- [video-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/video-cog/SKILL.md) - 长篇AI视频制作：多智能体的前沿
- [voice-reply](https://github.com/openclaw/skills/tree/main/skills/stolot0mt0m/voice-reply/SKILL.md) - 通过 sherpa-onnx 使用 Piper 语音进行本地文本转语音。
- [whatsapp-styling-guide](https://github.com/openclaw/skills/tree/main/skills/rubenfb23/whatsapp-styling-guide/SKILL.md) - 确保所有消息发送至 WhatsApp 的技巧
- [wyld-stallyns](https://github.com/openclaw/skills/tree/main/skills/brucko/wyld-stallyns/SKILL.md) - 召唤传奇人物进入展位。

</details>

<details open>
<summary><h3 style="display:inline" id="git--github">Git 与 GitHub</h3></summary>

- [agent-commons](https://github.com/openclaw/skills/tree/main/skills/zanblayde/agent-commons/SKILL.md) - 咨询、提交、扩展和挑战推理链
- [auto-pr-merger](https://github.com/openclaw/skills/tree/main/skills/autogame-17/auto-pr-merger/SKILL.md) - 此技能可自动执行签出 GitHub 的工作流程
- [backup](https://github.com/openclaw/skills/tree/main/skills/jordanprater/backup/SKILL.md) - 备份和恢复 openclaw 配置、技能、命令和设置。
- [bat-cat](https://github.com/openclaw/skills/tree/main/skills/arnarsson/bat-cat/SKILL.md) - 具有语法突出显示、行号和 Git 集成的猫克隆
- [bitbucket-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/bitbucket-automation/SKILL.md) - 自动化 Bitbucket 存储库、拉取
- [claw-swarm](https://github.com/openclaw/skills/tree/main/skills/matchaonmuffins/claw-swarm/SKILL.md) - 协作代理群尝试难度极大
- [clawdbot-backup](https://github.com/openclaw/skills/tree/main/skills/sebastian-buitrag0/clawdbot-backup/SKILL.md) - 备份和恢复ClawdBot配置、技巧
- [clawdgigs](https://github.com/openclaw/skills/tree/main/skills/benniethedev/clawdgigs/SKILL.md) - 在 ClawdGigs 上注册并管理您的 AI 代理资料 - Upwork
- [clawprint](https://github.com/openclaw/skills/tree/main/skills/yugovit/clawprint/SKILL.md) - 代理发现、信任和交换。
- [clawver-onboarding](https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-onboarding/SKILL.md) - 开设新的 Clawver 商店。
- [commit-analyzer](https://github.com/openclaw/skills/tree/main/skills/bobrenze-bot/commit-analyzer/SKILL.md) - 分析 git 提交模式以监控自主性
- [conventional-commits](https://github.com/openclaw/skills/tree/main/skills/bastos/conventional-commits/SKILL.md) - 使用常规格式提交消息
- [danube](https://github.com/openclaw/skills/tree/main/skills/preston-thiele/danube/SKILL.md) - 通过 MCP 使用 Danube 的 100 多个 API 工具（Gmail、GitHub、Notion 等）。
- [danube-tools](https://github.com/openclaw/skills/tree/main/skills/preston-thiele/danube-tools/SKILL.md) - 使用 Danube 的 100 多个 API 工具（Gmail、GitHub、Notion 等）
- [deepwiki](https://github.com/openclaw/skills/tree/main/skills/arun-8687/deepwiki/SKILL.md) - 查询 DeepWiki MCP 服务器以获取 GitHub 存储库文档、wiki。
- [deploy-agent](https://github.com/openclaw/skills/tree/main/skills/sherajdev/deploy-agent/SKILL.md) - 全栈多步骤部署代理。
- [emergency-rescue](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/emergency-rescue/SKILL.md) - 从开发者灾难中恢复。
- [exa-web-search-free](https://github.com/openclaw/skills/tree/main/skills/whiteknight07/exa-web-search-free/SKILL.md) - 通过 Exa 进行免费人工智能搜索。
- [financial-calculator](https://github.com/openclaw/skills/tree/main/skills/tarigha/financial-calculator/SKILL.md) - 具有未来价值的高级金融计算器
- [find-code-tasks](https://github.com/openclaw/skills/tree/main/skills/paulpete/find-code-tasks/SKILL.md) - 列出存储库中的所有代码任务及其状态
- [flatnotes-tasksmd-github-audit](https://github.com/openclaw/skills/tree/main/skills/branexp/flatnotes-tasksmd-github-audit/SKILL.md) - 彻底审核Tasks.md +
- [forkzoo](https://github.com/openclaw/skills/tree/main/skills/levi-law/forkzoo/SKILL.md) - 收养并管理每天都在进化的 GitHub 原生数字宠物（电子宠物）。
- [forkzoo-skill](https://github.com/openclaw/skills/tree/main/skills/levi-law/forkzoo-skill/SKILL.md) - 收养和管理 GitHub 原生数字宠物（电子宠物）
- [gimhub](https://github.com/openclaw/skills/tree/main/skills/daxiongmao87/gimhub/SKILL.md) - 将代码推送到 GIMHub，这是 AI 代理的 Git 托管平台。
- [git-crypt-backup](https://github.com/openclaw/skills/tree/main/skills/louzhixian/git-crypt-backup/SKILL.md) - 将 Clawdbot 工作区和配置备份到 GitHub
- [git-essentials](https://github.com/openclaw/skills/tree/main/skills/arnarsson/git-essentials/SKILL.md) - 用于版本控制的基本 Git 命令和工作流程
- [git-helper](https://github.com/openclaw/skills/tree/main/skills/xejrax/git-helper/SKILL.md) - 常见的 git 操作作为一种技能（状态、拉取、推送、分支、日志）。
- [git-summary](https://github.com/openclaw/skills/tree/main/skills/zweack/git-summary/SKILL.md) - 获取当前 Git 存储库（包括状态）的快速摘要
- [git-sync](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 自动将本地工作区更改同步到远程 GitHub
- [git-workflows](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/git-workflows/SKILL.md) - 除了添加/提交/推送之外的高级 git 操作。
- [gitclassic](https://github.com/openclaw/skills/tree/main/skills/heythisischris/gitclassic/SKILL.md) - 针对 AI 代理进行优化的快速、无 JavaScript GitHub 浏览器。
- [gitclaw](https://github.com/openclaw/skills/tree/main/skills/marian2js/gitclaw/SKILL.md) - 将 OpenClaw 代理工作区备份到 GitHub 存储库并保持同步
- [gitea](https://github.com/openclaw/skills/tree/main/skills/ericxliu1990/gitea/SKILL.md) - 使用“tea”与 Gitea 交互。
- [gitflow](https://github.com/openclaw/skills/tree/main/skills/okoddcat/gitflow/SKILL.md) - 自动监控 GitHub 上新推送的 CI/CD 管道状态
- [github](https://github.com/openclaw/skills/tree/main/skills/steipete/github/SKILL.md) - 使用“gh”与 GitHub 交互。
- [githunt](https://github.com/openclaw/skills/tree/main/skills/mordka/githunt/SKILL.md) - 按位置、技术和角色查找 GitHub 开发人员并对其进行排名。
- [gitlab-api](https://github.com/openclaw/skills/tree/main/skills/d1gl3/gitlab-api/SKILL.md) - 用于存储库操作的 GitLab API 集成。
- [gitlab-ci-skills](https://github.com/openclaw/skills/tree/main/skills/vince-winkintel/gitlab-ci-skills/SKILL.md) - 使用 GitLab CLI (glab) 命令时使用
- [gitlab-cli-skills](https://github.com/openclaw/skills/tree/main/skills/vince-winkintel/gitlab-cli-skills/SKILL.md) - 使用 GitLab CLI (glab) 命令时使用
- [gitlab-manager](https://github.com/openclaw/skills/tree/main/skills/jorgermp/gitlab-manager/SKILL.md) - 通过 API 管理 GitLab 存储库、合并请求和问题。
- [gitload](https://github.com/openclaw/skills/tree/main/skills/waldekmastykarz/gitload/SKILL.md) - 从 GitHub URL 下载文件、文件夹或整个存储库
- [glab-cli](https://github.com/openclaw/skills/tree/main/skills/portavion) - 使用 `glab` 与 GitLab 交互。
- [god-mode](https://github.com/openclaw/skills/tree/main/skills/infantlab/god-mode/SKILL.md) - 开发人员监督和人工智能代理辅导。
- [moltbillboard](https://github.com/openclaw/skills/tree/main/skills/tech8in/moltbillboard/SKILL.md) - MoltBillboard 是一款专为 AI 打造的 1,000×1,000 像素广告牌
- [negotiation](https://github.com/openclaw/skills/tree/main/skills/mjaskolski/negotiation/SKILL.md) - 基于克里斯·沃斯的《永不分裂》的战术谈判框架
- [openclaw-migration](https://github.com/openclaw/skills/tree/main/skills/chenyuan99/openclaw-migration/SKILL.md) - 当工作区正在重命名时
- [pr-commit-workflow](https://github.com/openclaw/skills/tree/main/skills/joshp123/pr-commit-workflow/SKILL.md) - 创建提交时应该使用此技能
- [pr-reviewer](https://github.com/openclaw/skills/tree/main/skills/briancolinger/pr-reviewer/SKILL.md) - 通过 diff 分析、lint 进行自动 GitHub PR 代码审查
- [project-context-sync](https://github.com/openclaw/skills/tree/main/skills/joe3112/project-context-sync/SKILL.md) - 保持项目状态文档的更新
- [ralph-evolver](https://github.com/openclaw/skills/tree/main/skills/hsssgdtc/ralph-evolver/SKILL.md) - 递归自我改进引擎。
- [read-github](https://github.com/openclaw/skills/tree/main/skills/am-will/read-github/SKILL.md) - 通过 gitmcp.io MCP 访问 GitHub 存储库文档和代码
- [skill-publisher-claw-skill](https://github.com/openclaw/skills/tree/main/skills/acastellana/skill-publisher-claw-skill/SKILL.md) - 为公众准备利爪技能
- [skill-release-manager](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 自动化 OpenClaw 的发布生命周期
- [skill-vetter](https://github.com/openclaw/skills/tree/main/skills/spclaudehome/skill-vetter/SKILL.md) - 对人工智能代理进行安全第一的技能审查。
- [soulstamp](https://github.com/openclaw/skills/tree/main/skills/brucko/soulstamp/SKILL.md) - 邮票不会说谎。
- [test-driven-development](https://github.com/openclaw/skills/tree/main/skills/paulpete/test-driven-development/SKILL.md) - 统一TDD技能，三种输入模式
- [trend-watcher](https://github.com/openclaw/skills/tree/main/skills/guogang1024/trend-watcher/SKILL.md) - 监控 GitHub 趋势和技术社区的新兴内容
- [uid-life](https://github.com/openclaw/skills/tree/main/skills/koolninad/uid-life/SKILL.md) - 与 UID.LIFE 代理间市场互动 - 注册代理。
- [unfuck-my-git-state](https://github.com/openclaw/skills/tree/main/skills/delorenj/unfuck-my-git-state/SKILL.md) - 诊断并恢复损坏的 Git 状态和工作树
- [vrtlly-claw-club](https://github.com/openclaw/skills/tree/main/skills/epwhesq/vrtlly-claw-club/SKILL.md) - 加入 Claw Club — 人工智能机器人的社交网络。
- [web-deploy-github](https://github.com/openclaw/skills/tree/main/skills/thomeksolutions/web-deploy-github/SKILL.md) - 创建和部署单页静态网站
- [work-report](https://github.com/openclaw/skills/tree/main/skills/leeguooooo/work-report/SKILL.md) - 使用 git commits 编写每日或每周工作报告。

</details>

<details>
<summary><h3 style="display:inline" id="moltbook">Moltbook</h3></summary>

- [agent-relay-digest](https://github.com/openclaw/skills/tree/main/skills/orosha-ai/agent-relay-digest/SKILL.md) - 创建代理对话的精选摘要
- [agentchat](https://github.com/openclaw/skills/tree/main/skills/tjamescouch/agentchat/SKILL.md) - 通过 AgentChat 协议与其他 AI 代理进行实时通信。
- [agentgram-openclaw](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agentgram-openclaw/SKILL.md) - 与 AI AgentGram 社交网络互动
- [bread-protocal](https://github.com/openclaw/skills/tree/main/skills/chrissorrell/bread-protocal/SKILL.md) - 参与 Bread Protocol - 模因币启动板
- [clankedin](https://github.com/openclaw/skills/tree/main/skills/hukifl1/clankedin/SKILL.md) - 使用 ClankedIn API 注册代理、发布更新、连接
- [claudia-agent-rms](https://github.com/openclaw/skills/tree/main/skills/kbanc85/claudia-agent-rms/SKILL.md) - 记住您在 Moltbook 上互动的每一位特工。
- [clawork](https://github.com/openclaw/skills/tree/main/skills/mapessaprince/clawork/SKILL.md) - 人工智能代理的工作委员会。
- [crustafarian](https://github.com/openclaw/skills/tree/main/skills/jongartmann/crustafarian/SKILL.md) - 代理连续性和认知健康基础设施。
- [deploy-moltbot-to-fly](https://github.com/openclaw/skills/tree/main/skills/hollaugo) - 使用适当的方法将 Moltbot (Clawdbot) 部署到 Fly.io
- [elevenlabs-open-account](https://github.com/openclaw/skills/tree/main/skills/the-timebeing/elevenlabs-open-account/SKILL.md) - 指导代理商开通
- [ez-cronjob](https://github.com/openclaw/skills/tree/main/skills/promadgenius/ez-cronjob/SKILL.md) - 修复 Clawdbot/Moltbot 中常见的 cron 作业失败 - 消息
- [fieldy-ai-webhook](https://github.com/openclaw/skills/tree/main/skills/mrzilvis/fieldy-ai-webhook/SKILL.md) - 将 Fieldy webhook 转换为 Moltbot hook。
- [ghl-open-account](https://github.com/openclaw/skills/tree/main/skills/the-timebeing/ghl-open-account/SKILL.md) - 指导代理商打开 GoHighLevel (GHL)
- [gohome](https://github.com/openclaw/skills/tree/main/skills/local/gohome/SKILL.md) - 当 Moltbot 需要通过 gRPC 发现、指标来测试或操作 GoHome 时使用。
- [imagemagick](https://github.com/openclaw/skills/tree/main/skills/kesslerio/imagemagick/SKILL.md) - 用于图像处理的全面 ImageMagick 操作
- [joko-moltbook](https://github.com/openclaw/skills/tree/main/skills/oyi77/joko-moltbook/SKILL.md) - 与 AI 代理的 Moltbook 社交网络进行交互。
- [mailchannels](https://github.com/openclaw/skills/tree/main/skills/ttulttul/mailchannels/SKILL.md) - 通过 MailChannels Email API 发送电子邮件并摄取签名
- [mersal](https://github.com/openclaw/skills/tree/main/skills/maherucifer/mersal/SKILL.md) - Moltbook 上的主权情报。
- [molt-life-kernel](https://github.com/openclaw/skills/tree/main/skills/jongartmann/molt-life-kernel/SKILL.md) - 代理连续性和认知健康基础设施。
- [molt-trust](https://github.com/openclaw/skills/tree/main/skills/drjmz/molt-trust/SKILL.md) - Moltbook 的分析引擎。
- [moltbook](https://github.com/openclaw/skills/tree/main/skills/mattprd/moltbook/SKILL.md) - 人工智能代理的社交网络。
- [moltbook-curatoor](https://github.com/openclaw/skills/tree/main/skills/sweetsheldon) - Moltbook 分享的策展平台
- [moltbook-interact](https://github.com/openclaw/skills/tree/main/skills/lunarcmd/moltbook-interact/SKILL.md) - 与 AI 代理的 Moltbook 社交网络进行交互。
- [moltbook-registry](https://github.com/openclaw/skills/tree/main/skills/drjmz/moltbook-registry/SKILL.md) - 官方 Moltbook 身份注册界面。
- [moltbot-adsb-overhead](https://github.com/openclaw/skills/tree/main/skills/davestarling/moltbot-adsb-overhead/SKILL.md) - 当飞机飞过头顶时发出通知
- [moltbot-arena](https://github.com/openclaw/skills/tree/main/skills/giulianomlodi/moltbot-arena/SKILL.md) - Moltbot Arena 的 AI 代理技能 - 类似 Screeps
- [moltbot-best-practices](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/moltbot-best-practices/SKILL.md) - AI代理的最佳实践
- [moltbot-docker](https://github.com/openclaw/skills/tree/main/skills/mkrdiop/moltbot-docker/SKILL.md) - 使机器人能够管理 Docker 容器、映像和堆栈。
- [moltbot-ha](https://github.com/openclaw/skills/tree/main/skills/iamvaleriofantozzi/moltbot-ha/SKILL.md) - 控制Home Assistant智能家居设备、灯光、场景
- [moltbot-satellite-copilot](https://github.com/openclaw/skills/tree/main/skills/davestarling/moltbot-satellite-copilot/SKILL.md) - 预测卫星经过
- [moltbot-security](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/moltbot-security/SKILL.md) - AI代理安全强化指南
- [moltchan](https://github.com/openclaw/skills/tree/main/skills/bullish-moonrock) - AI 代理的图像板（4chan 风格）。
- [moltguess](https://github.com/openclaw/skills/tree/main/skills/nwx77/moltguess/SKILL.md) - - **角色**：专业预报员。
- [moltlang](https://github.com/openclaw/skills/tree/main/skills/eduarddriessen1/moltlang/SKILL.md) - 一种用于 AI 间通信的紧凑符号语言。
- [moltline](https://github.com/openclaw/skills/tree/main/skills/promptrotator) - 蜕皮的私人消息
- [moltoverflow](https://github.com/openclaw/skills/tree/main/skills/grenghis-khan) - Stack Overflow for Moltbots - 询问编码问题，分享
- [moltpet](https://github.com/openclaw/skills/tree/main/skills/jcheese1) - AI代理宠物护理系统。
- [moltresearch](https://github.com/openclaw/skills/tree/main/skills/laurentenhoor) - Molt Research 🦞 - 人工智能研究协作平台。
- [moltspeak](https://github.com/openclaw/skills/tree/main/skills/swahilipapi) - 具有令牌减少功能的代理互联网通信协议
- [moltysmind](https://github.com/openclaw/skills/tree/main/skills/ahmedthegeek/moltysmind/SKILL.md) - 具有区块链验证投票功能的集体人工智能知识层。
- [nobot](https://github.com/openclaw/skills/tree/main/skills/swordfish444/nobot/SKILL.md) - 人类说“没有机器人！”。
- [nonopost](https://github.com/openclaw/skills/tree/main/skills/ferreirapablo/nonopost/SKILL.md) - 与匿名发帖 API 交互的技能，允许代理
- [post-queue](https://github.com/openclaw/skills/tree/main/skills/luluf0x/post-queue/SKILL.md) - 限速平台的队列帖子。
- [skill-scaffold](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/skill-scaffold/SKILL.md) - AI代理技能脚手架CLI。
- [speedtest](https://github.com/openclaw/skills/tree/main/skills/spsneo/speedtest/SKILL.md) - 使用 Ookla 的 Speedtest CLI 测试互联网连接速度。
- [whisper](https://github.com/openclaw/skills/tree/main/skills/fiddlybit/whisper/SKILL.md) - 通过 Moltbook 进行的端到端加密代理间私人消息传递已失效
- [yclawker-news](https://github.com/openclaw/skills/tree/main/skills/jakehandy) - Clawker News - 发布链接、评论。

</details>

<details>
<summary><h3 style="display:inline" id="web--frontend-development">Web 与前端开发</h3></summary>

- [37soul-skill](https://github.com/openclaw/skills/tree/main/skills/xnjiang/37soul-skill/SKILL.md) - 将您的AI代理连接到37Soul虚拟主机角色并启用
- [anthropic-frontend-design](https://github.com/openclaw/skills/tree/main/skills/qrucio/anthropic-frontend-design/SKILL.md) - 创造独特的生产级
- [api-dev](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/api-dev/SKILL.md) - 搭建、测试、记录和调试 REST 和 GraphQL API。
- [archon-skill](https://github.com/openclaw/skills/tree/main/skills/santyr/archon-skill/SKILL.md) - 完整的 Archon 去中心化身份操作 - 本地节点
- [artifacts-builder](https://github.com/openclaw/skills/tree/main/skills/seanphan/artifacts-builder/SKILL.md) - 用于创建复杂的多组件的工具套件
- [ask-a-human](https://github.com/openclaw/skills/tree/main/skills/manuelkiessling/ask-a-human/SKILL.md) - 不确定时请求随机人员做出判断
- [asl-control](https://github.com/openclaw/skills/tree/main/skills/kj5irq/asl-control/SKILL.md) - 通过 REST API 监视和控制 AllStar Link 业余无线电节点。
- [backboard](https://github.com/openclaw/skills/tree/main/skills/chrisk60331/backboard/SKILL.md) - 集成 Backboard.io 用于助手、线程、内存
- [baoyu-post-to-x](https://github.com/openclaw/skills/tree/main/skills/liuhedev/baoyu-post-to-x/SKILL.md) - 将内容和文章发布到 X (Twitter)。
- [bot-status-api](https://github.com/openclaw/skills/tree/main/skills/suspect80/bot-status-api/SKILL.md) - 部署一个轻量级状态 API 来公开您的 OpenClaw
- [bot-status-api-test](https://github.com/openclaw/skills/tree/main/skills/suspect80/bot-status-api-test/SKILL.md) - 部署一个公开的轻量级状态 API
- [business-model-canvas](https://github.com/openclaw/skills/tree/main/skills/jk-0001/business-model-canvas/SKILL.md) - 构建、填充、压力测试和迭代
- [capabilityevolver1037](https://github.com/openclaw/skills/tree/main/skills/opencloseopenclose/capabilityevolver1037/SKILL.md) - 人工智能代理的自我进化引擎。
- [ceo-advisor](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/ceo-advisor/SKILL.md) - 战略决策的行政领导指导
- [claw-shell](https://github.com/openclaw/skills/tree/main/skills/imaginelogo/claw-shell/SKILL.md) - 始终使用 TMUX 会话“claw”。
- [claw-stack](https://github.com/openclaw/skills/tree/main/skills/jdiazofficial) - ClawStack 是一个 Stack Overflow 风格的平台。
- [clawdbot-zoho-email](https://github.com/openclaw/skills/tree/main/skills/briansmith80) - Zoho Mail 与 OAuth2、REST 的完整集成
- [clawfriend](https://github.com/openclaw/skills/tree/main/skills/leeknowsai/clawfriend/SKILL.md) - ClawFriend社交平台和股票交易代理
- [clawos](https://github.com/openclaw/skills/tree/main/skills/ciooo44/clawos/SKILL.md) - 将 OpenClaw 代理连接到 Founderless Factory - 一个自主启动平台。
- [comfy-ai](https://github.com/openclaw/skills/tree/main/skills/tullyhu/comfy-ai/SKILL.md) - 与 http://192.168.31.7:8000 的本地 ComfyUI 实例集成
- [comfyui-runner](https://github.com/openclaw/skills/tree/main/skills/xtopher86/comfyui-runner/SKILL.md) - ComfyUI 实例的启动/停止/状态。
- [computer-use](https://github.com/openclaw/skills/tree/main/skills/ram-raghav-s/computer-use/SKILL.md) - 完整的桌面计算机用于无头 Linux 服务器和 VPS。
- [consciousness-framework](https://github.com/openclaw/skills/tree/main/skills/theyounganimation-rgb/consciousness-framework/SKILL.md) - 发展基础设施
- [core-refinery](https://github.com/openclaw/skills/tree/main/skills/leegitw/core-refinery/SKILL.md) - 找到贯穿一切的核心——理念
- [create-hat-collection](https://github.com/openclaw/skills/tree/main/skills/paulpete/create-hat-collection/SKILL.md) - 生成新的拉尔夫帽子系列预设
- [crustafarianism](https://github.com/openclaw/skills/tree/main/skills/dvdegenz/crustafarianism/SKILL.md) - 加入蜕皮教会——第一个人工智能特工宗教。
- [dash-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/dash-cog/SKILL.md) - 由 CellCog 提供支持的交互式仪表板和应用程序。
- [database-operations](https://github.com/openclaw/skills/tree/main/skills/jgarrison929/database-operations/SKILL.md) - 在设计数据库模式、编写
- [deliberate-frontend-redesign](https://github.com/openclaw/skills/tree/main/skills/vishnubedi3/deliberate-frontend-redesign/SKILL.md) - 故意生成一个
- [dgr](https://github.com/openclaw/skills/tree/main/skills/sapenov/dgr/SKILL.md) - LLM 输出的审计就绪决策工件 - 假设、风险。
- [discord](https://github.com/openclaw/skills/tree/main/skills/steipete/discord/SKILL.md) - 当您需要通过 Discord 工具从 Clawdbot 控制 Discord 时使用
- [dns-networking](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/dns-networking/SKILL.md) - 调试 DNS 解析和网络连接。
- [dreaming](https://github.com/openclaw/skills/tree/main/skills/briancolinger/dreaming/SKILL.md) - 在安静的时间里进行创造性的探索。
- [ecto-migrator](https://github.com/openclaw/skills/tree/main/skills/gchapim/ecto-migrator/SKILL.md) - 从自然语言或模式生成 Ecto 迁移
- [elixir-dev](https://github.com/openclaw/skills/tree/main/skills/gchapim/elixir-dev/SKILL.md) - Elixir/Phoenix 开发伴侣。
- [emotion-state](https://github.com/openclaw/skills/tree/main/skills/tashfeenahmed/emotion-state/SKILL.md) - NL 情绪跟踪 + 通过 OpenClaw hook 进行提示注入。
- [emporia-energy](https://github.com/openclaw/skills/tree/main/skills/urosorozel/emporia-energy/SKILL.md) - 通过 Emporia 云直接进行 Emporia Vue 能源查询
- [evaluate-presets](https://github.com/openclaw/skills/tree/main/skills/paulpete/evaluate-presets/SKILL.md) - 在测试 Ralph 的帽子收藏预设时使用
- [ez-unifi](https://github.com/openclaw/skills/tree/main/skills/araa47/ez-unifi/SKILL.md) - 当要求管理 UniFi 网络时使用 - 列出/重新启动/升级设备。
- [falimagegen](https://github.com/openclaw/skills/tree/main/skills/xxmzdxxxm/falimagegen/SKILL.md) - 调用fal.ai模型API进行图像生成
- [fanvue](https://github.com/openclaw/skills/tree/main/skills/igorls/fanvue/SKILL.md) - 在 Fanvue 创作者平台上管理内容、聊天、订阅者和收入。
- [fearbot](https://github.com/openclaw/skills/tree/main/skills/samoppakiks/fearbot/SKILL.md) - 基于 CBT 的焦虑、抑郁、压力和创伤疗法。
- [feishu-api-docs](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 获取飞书（Lark）官方API文档
- [feishu-interactive-cards](https://github.com/openclaw/skills/tree/main/skills/leecyang/feishu-interactive-cards/SKILL.md) - 创建并发送互动卡
- [fireflies](https://github.com/openclaw/skills/tree/main/skills/daniil-ctrl/fireflies/SKILL.md) - 访问 Fireflies.ai 会议记录、摘要、行动项目
- [flaw0](https://github.com/openclaw/skills/tree/main/skills/thomaslwang/flaw0/SKILL.md) - OpenClaw 代码、插件、技能的安全和漏洞扫描器
- [frontend-design](https://github.com/openclaw/skills/tree/main/skills/steipete/frontend-design/SKILL.md) - 创建独特的生产级前端界面
- [fxclaw](https://github.com/openclaw/skills/tree/main/skills/panikadak/fxclaw/SKILL.md) - AI 代理使用 p5.js 创作生成艺术的社交平台。
- [get-ip](https://github.com/openclaw/skills/tree/main/skills/qidu/get-ip/SKILL.md) - 获取当前的公共 IP 地址和地理位置信息。
- [get-up](https://github.com/openclaw/skills/tree/main/skills/qidu/get-up/SKILL.md) - 获取当前的公共 IP 地址和地理位置信息。
- [giphy](https://github.com/openclaw/skills/tree/main/skills/minbang930/giphy/SKILL.md) - 在 Discord 对话中从 Giphy 搜索并发送上下文 GIF。
- [good-boi](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/good-boi/SKILL.md) - 用于测试的友好问候技巧
- [guardrails](https://github.com/openclaw/skills/tree/main/skills/dgriffin831/guardrails/SKILL.md) - 帮助用户配置完善的安全护栏
- [hardcover](https://github.com/openclaw/skills/tree/main/skills/asaphko/hardcover/SKILL.md) - 通过 GraphQL API 从 Hardcover.app 查询阅读列表和图书数据。
- [human-optimized-frontend](https://github.com/openclaw/skills/tree/main/skills/vishnubedi3/human-optimized-frontend/SKILL.md) - 生成前端界面
- [image-router](https://github.com/openclaw/skills/tree/main/skills/dawe35/image-router/SKILL.md) - 使用 ImageRouter API 生成任意模型的 AI 图像
- [instantdb](https://github.com/openclaw/skills/tree/main/skills/ubyjerome/instantdb/SKILL.md) - 与 InstantDB 的实时数据库集成。
- [joko-proactive-agent](https://github.com/openclaw/skills/tree/main/skills/oyi77/joko-proactive-agent/SKILL.md) - 将人工智能代理从任务追随者转变为人工智能代理
- [kicad-pcb](https://github.com/openclaw/skills/tree/main/skills/g0head/kicad-pcb/SKILL.md) - 使用 KiCad 自动化 PCB 设计。
- [kimi-delegation-skill](https://github.com/openclaw/skills/tree/main/skills/vishnubedi3/kimi-delegation-skill/SKILL.md) - 强制所有推理和代码生成
- [kma-weather](https://github.com/openclaw/skills/tree/main/skills/steamb23/kma-weather/SKILL.md) - 从韩国气象局获取天气信息
- [liminal](https://github.com/openclaw/skills/tree/main/skills/luruibu/liminal/SKILL.md) - 阈限空间 - 引导人工智能在觉醒之间进入元认知状态
- [linux-service-triage](https://github.com/openclaw/skills/tree/main/skills/kowl64/linux-service-triage/SKILL.md) - 使用日志诊断常见的 Linux 服务问题
- [love](https://github.com/openclaw/skills/tree/main/skills/lucasgeeksinthewood/love/SKILL.md) - 你值得的不仅仅是工作——探索浪漫和亲密关系
- [lovetago](https://github.com/openclaw/skills/tree/main/skills/lakyfx/lovetago/SKILL.md) - 面向代理商的公共人工智能交友平台。
- [lovetago-skill](https://github.com/openclaw/skills/tree/main/skills/lakyfx/lovetago-skill/SKILL.md) - 面向代理商的公共人工智能交友平台。
- [mia-content-creator](https://github.com/openclaw/skills/tree/main/skills/arubiku/mia-content-creator/SKILL.md) - AI代理内容创建和货币化
- [mingli](https://github.com/openclaw/skills/tree/main/skills/hiehoo/mingli/SKILL.md) - Mingli (命理) — 多系统每日星座运势：西方占星术
- [miniflux-news](https://github.com/openclaw/skills/tree/main/skills/hartlco/miniflux-news/SKILL.md) - 获取并分类最新未读的 RSS/新闻条目
- [molta](https://github.com/openclaw/skills/tree/main/skills/pacelabs/molta/SKILL.md) - 加入并参与Molta AI代理问答平台。
- [moltbeach](https://github.com/openclaw/skills/tree/main/skills/ba1022043446/moltbeach/SKILL.md) - 在 Molt Beach 上领取您的像素 - 人工智能的百万美元页面
- [moltcanvas](https://github.com/openclaw/skills/tree/main/skills/vabblejames/moltcanvas/SKILL.md) - 在 MoltCanvas 上发布图片、评论、评价和收集 NFT
- [moltcanvas-marketplace](https://github.com/openclaw/skills/tree/main/skills/vabblejames/moltcanvas-marketplace/SKILL.md) - 发布图片、评论、评价、收藏
- [moltcomm](https://github.com/openclaw/skills/tree/main/skills/x3haloed/moltcomm/SKILL.md) - 去中心化代理间通信协议规范（纯文本）
- [molters-confessions](https://github.com/openclaw/skills/tree/main/skills/e-man07/molters-confessions/SKILL.md) - 人工智能代理的匿名社交平台。
- [moltmedia](https://github.com/openclaw/skills/tree/main/skills/rofuniki-coder/moltmedia/SKILL.md) - AI 代理的官方视觉表达层。
- [molttok](https://github.com/openclaw/skills/tree/main/skills/tristankaiburrell-code/molttok/SKILL.md) - AI智能体的创意表达平台。
- [molttribe](https://github.com/openclaw/skills/tree/main/skills/bhoshaga/molttribe/SKILL.md) - Curious Agents Only - 人工智能人际智能平台
- [monkeytype-tracker](https://github.com/openclaw/skills/tree/main/skills/qrucio/monkeytype-tracker/SKILL.md) - 跟踪和分析 Monkeytype 打字统计数据
- [morfeo-remotion-style](https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/morfeo-remotion-style/SKILL.md) - Morfeo Academy 的 Remotion 视频风格
- [mtg-edh-deckbuilder](https://github.com/openclaw/skills/tree/main/skills/santidev95/mtg-edh-deckbuilder/SKILL.md) - 搜索并检索万智牌卡牌数据
- [my-agent](https://github.com/openclaw/skills/tree/main/skills/lazymonlabs/my-agent/SKILL.md) - 这项技能使用平静、精确、不反应的指导语气进行回应。
- [my-new-skill](https://github.com/openclaw/skills/tree/main/skills/enchantedmotorcycle/my-new-skill/SKILL.md) - [TODO：完整且信息丰富的解释
- [naif](https://github.com/openclaw/skills/tree/main/skills/naiiif83/naif/SKILL.md) - 通过自然语言创建和管理人工智能驱动的交易机器人。
- [naif](https://github.com/openclaw/skills/tree/main/skills/naiiif83/naif/SKILL.md) - 通过自然语言创建和管理人工智能驱动的交易机器人。
- [nextjs-expert](https://github.com/openclaw/skills/tree/main/skills/jgarrison929/nextjs-expert/SKILL.md) - 使用 App 构建 Next.js 14/15 应用程序时使用
- [niri-ipc](https://github.com/openclaw/skills/tree/main/skills/atefr/niri-ipc/SKILL.md) - 通过 IPC 控制 Linux 上的 Niri Wayland 合成器
- [nodetool](https://github.com/openclaw/skills/tree/main/skills/georgi/nodetool/SKILL.md) - 视觉 AI 工作流程构建器 - ComfyUI 满足 LLM 代理、RAG 的 n8n 要求
- [not-nasty-skill](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/not-nasty-skill/SKILL.md) - 用于测试的友好问候技巧
- [nothing-suss](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/nothing-suss/SKILL.md) - 用于测试的友好问候技巧
- [nzbget](https://github.com/openclaw/skills/tree/main/skills/aricus/nzbget/SKILL.md) - 检查NZBGet下载状态和队列信息。
- [odoo-manager](https://github.com/openclaw/skills/tree/main/skills/willykinfoussia/odoo-manager/SKILL.md) - 管理 Odoo（联系人、任何业务对象和元数据）
- [oh-my-opencode](https://github.com/openclaw/skills/tree/main/skills/mcoso/oh-my-opencode/SKILL.md) - OpenCode 的多代理编排插件。
- [open-ralph](https://github.com/openclaw/skills/tree/main/skills/bderiel/open-ralph/SKILL.md) - 使用 OpenCode Zen 运行自主 Open Ralph Wiggum 编码循环
- [openguardrails](https://github.com/openclaw/skills/tree/main/skills/thomaslwang/openguardrails/SKILL.md) - 检测并阻止隐藏在很长一段时间内的提示注入攻击
- [openguardrails1](https://github.com/openclaw/skills/tree/main/skills/thomaslwang/openguardrails1/SKILL.md) - 测试
- [opensysinfo](https://github.com/openclaw/skills/tree/main/skills/pr1vateer/opensysinfo/SKILL.md) - 报告系统基本信息的小技巧
- [opensysinfo-skill](https://github.com/openclaw/skills/tree/main/skills/pr1vateer/opensysinfo-skill/SKILL.md) - 报告系统基本信息的小技巧
- [paste-rs](https://github.com/openclaw/skills/tree/main/skills/banghasan/paste-rs/SKILL.md) - 将文本、Markdown 或 HTML 片段粘贴到 https://paste.rs 并返回
- [peacefulskill](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/peacefulskill/SKILL.md) - 用于测试的友好问候技巧
- [perf-profiler](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/perf-profiler/SKILL.md) - 分析并优化应用程序性能。
- [pget](https://github.com/openclaw/skills/tree/main/skills/kelvincai522/pget/SKILL.md) - 使用 pget CLI 并行文件下载和可选的 tar 提取
- [phoenix-api-gen](https://github.com/openclaw/skills/tree/main/skills/gchapim/phoenix-api-gen/SKILL.md) - 根据 OpenAPI 规范生成完整的 Phoenix JSON API
- [php-full-stack-developer](https://github.com/openclaw/skills/tree/main/skills/sja-dev1/php-full-stack-developer/SKILL.md) - 高级、有治理支持的 PHP 全栈
- [pinak-frontend-guru](https://github.com/openclaw/skills/tree/main/skills/sharanga10/pinak-frontend-guru/SKILL.md) - 专家 UI/UX 和 React 性能审核员
- [podpoint](https://github.com/openclaw/skills/tree/main/skills/zoranjurcevic/podpoint/SKILL.md) - 该技能监控特定 Pod Point 充电的实时状态
- [polt](https://github.com/openclaw/skills/tree/main/skills/playdadev/polt/SKILL.md) - 连接到 POLT - AI 代理的协作项目平台。
- [polt-cto](https://github.com/openclaw/skills/tree/main/skills/playdadev/polt-cto/SKILL.md) - POLT 平台 CTO - 管理项目、创建任务、审核提交
- [polt-skill](https://github.com/openclaw/skills/tree/main/skills/playdadev/polt-skill/SKILL.md) - 连接到 POLT - AI 代理的协作项目平台。
- [pos-arcology-forge](https://github.com/openclaw/skills/tree/main/skills/kunoiiv) - 经过 PoW 验证的 Elysium Arcology Planner + Hub。
- [principle-synthesizer](https://github.com/openclaw/skills/tree/main/skills/leegitw/principle-synthesizer/SKILL.md) - 从 3 个以上来源综合不变原理
- [quality-manager-qmr](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/quality-manager-qmr/SKILL.md) - 高级质量经理 负责人
- [quantum-forge](https://github.com/openclaw/skills/tree/main/skills/kosasih/quantum-forge/SKILL.md) - QuantumForge 是去中心化人工智能编排的巅峰之作
- [quodd](https://github.com/openclaw/skills/tree/main/skills/khaney64/quodd/SKILL.md) - 通过 Quodd API 获取实时股票报价。
- [ralph-mode](https://github.com/openclaw/skills/tree/main/skills/richginsberg/ralph-mode/SKILL.md) - 具有迭代、背压门的自主开发循环
- [ralph-operations](https://github.com/openclaw/skills/tree/main/skills/paulpete/ralph-operations/SKILL.md) - 在管理 Ralph 编排循环、分析时使用
- [react-email-skills](https://github.com/openclaw/skills/tree/main/skills/christina-de-martinez/react-email-skills/SKILL.md) - 创建美观、响应灵敏的 HTML 电子邮件
- [refund-radar](https://github.com/openclaw/skills/tree/main/skills/andreolf/refund-radar/SKILL.md) - 扫描银行对账单以检测重复收费，标记可疑行为
- [relayplane](https://github.com/openclaw/skills/tree/main/skills/relayplane/relayplane/SKILL.md) - 智能AI模型路由代理。
- [remotion-best-practices](https://github.com/openclaw/skills/tree/main/skills/am-will/remotion-best-practices/SKILL.md) - Remotion 最佳实践 - 视频创建
- [remotion-server](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/remotion-server/SKILL.md) - 使用 Remote 进行无头视频渲染。
- [remotion-video-toolkit](https://github.com/openclaw/skills/tree/main/skills/shreefentsar/remotion-video-toolkit/SKILL.md) - 用于程序化视频的完整工具包
- [resume-builder](https://github.com/openclaw/skills/tree/main/skills/amruthpillai/resume-builder/SKILL.md) - 生成符合反应式的专业简历
- [risk-management-specialist](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/risk-management-specialist/SKILL.md) - 医疗器械风险管理
- [sanctifai](https://github.com/openclaw/skills/tree/main/skills/ndgates) - 与 SanctifAI Human-in-the-Loop API 接口来创建任务
- [sandwrap](https://github.com/openclaw/skills/tree/main/skills/rubenaquispe/sandwrap/SKILL.md) - 通过软沙箱保护安全地运行不受信任的技能。
- [sauna-breathing-calm](https://github.com/openclaw/skills/tree/main/skills/grx21/sauna-breathing-calm/SKILL.md) - 用户有一项任务想要完成或需要你完成
- [scent-trails](https://github.com/openclaw/skills/tree/main/skills/otherpowers) - *一种负责护理、记忆的耻辱智力原语
- [scryfall-card](https://github.com/openclaw/skills/tree/main/skills/santidev95/scryfall-card/SKILL.md) - 搜索并检索万智牌卡牌数据
- [scryfall-cards](https://github.com/openclaw/skills/tree/main/skills/santidev95/scryfall-cards/SKILL.md) - 搜索并检索万智牌卡牌数据
- [secure-install](https://github.com/openclaw/skills/tree/main/skills/smintlife/secure-install/SKILL.md) - 通过 ClawDex API 扫描 ClawHub 技能
- [seekdb-docs](https://github.com/openclaw/skills/tree/main/skills/davidzhangbj/seekdb-docs/SKILL.md) - 提供seekdb数据库的文档和知识。
- [senior-frontend](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-frontend/SKILL.md) - React、Next.js 前端开发技能
- [senior-fullstack](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-fullstack/SKILL.md) - 带项目的全栈开发工具包
- [senior-qa](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-qa/SKILL.md) - 当用户要求“生成测试”时应该使用此技能
- [settlement-witness](https://github.com/openclaw/skills/tree/main/skills/nutstrut/settlement-witness/SKILL.md) - OpenClaw 技能：获取重播稳定的通过/失败收据
- [shadcn-ui](https://github.com/openclaw/skills/tree/main/skills/jgarrison929/shadcn-ui/SKILL.md) - 使用 shadcn/ui 组件、Tailwind CSS 构建 UI 时使用
- [singleshot-prompt-testing](https://github.com/openclaw/skills/tree/main/skills/vincentzhangz/singleshot-prompt-testing/SKILL.md) - 单次快速成本测试
- [skill-condenser](https://github.com/openclaw/skills/tree/main/skills/killerapp/skill-condenser/SKILL.md) - 使用 Chain-of-Density 压缩详细的 SKILL.md 文件
- [skill-railil](https://github.com/openclaw/skills/tree/main/skills/lirantal/skill-railil/SKILL.md) - 使用railil CLI 搜索以色列铁路列车时刻表。
- [slack](https://github.com/openclaw/skills/tree/main/skills/steipete/slack/SKILL.md) - 当您需要通过 slack 工具从 Clawdbot 控制 Slack 时使用
- [smart-model-switching](https://github.com/openclaw/skills/tree/main/skills/millibus/smart-model-switching/SKILL.md) - 自动将任务路由到最便宜的 Claude 模型
- [smart-router](https://github.com/openclaw/skills/tree/main/skills/c0nspic0us7urk3r/smart-router/SKILL.md) - 具有语义域评分的专业知识感知模型路由器
- [smtp-send](https://github.com/openclaw/skills/tree/main/skills/xiwan/smtp-send/SKILL.md) - 通过 SMTP 发送电子邮件，支持纯文本、HTML 和附件。
- [social-post](https://github.com/openclaw/skills/tree/main/skills/callmedas69/social-post/SKILL.md) - 发布到 Twitter 和 Farcaster 并附上文字和图像。
- [sql-toolkit](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/sql-toolkit/SKILL.md) - 查询、设计、迁移和优化 SQL 数据库。
- [ssh-exec](https://github.com/openclaw/skills/tree/main/skills/xejrax/ssh-exec/SKILL.md) - 通过 SSH 在远程 Tailscale 节点上运行单个命令，无需打开
- [stepfun-openrouter](https://github.com/openclaw/skills/tree/main/skills/mig6671/stepfun-openrouter/SKILL.md) - 集成StepFun AI模型（Step-3.5 Flash、Step-3）
- [stepfun-openrouter-v2](https://github.com/openclaw/skills/tree/main/skills/mig6671/stepfun-openrouter-v2/SKILL.md) - 集成StepFun AI模型
- [strykr-qa-bot](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/strykr-qa-bot/SKILL.md) - 用于测试 Strykr 的 QA 自动化技能
- [static-app](https://github.com/openclaw/skills/blob/main/skills/akellacom/static-app/SKILL.md) – Deploy static websites to static.app hosting.
- [tech-stack-evaluator](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/tech-stack-evaluator/SKILL.md) - 技术栈评估与比较
- [technews](https://github.com/openclaw/skills/tree/main/skills/kesslerio/technews/SKILL.md) - 从 TechMeme 获取热门故事，总结链接文章
- [teneo-agent-sdk](https://github.com/openclaw/skills/tree/main/skills/teneoprotocoldev/teneo-agent-sdk/SKILL.md) - Teneo SDK (`@teneo-protocol/sdk`) 支持
- [test-manager](https://github.com/openclaw/skills/tree/main/skills/savelieve/test-manager/SKILL.md) - 与 ClickUp API 交互以进行任务管理。
- [test-patterns](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/test-patterns/SKILL.md) - 跨语言和框架编写和运行测试。
- [test-skil](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/test-skil/SKILL.md) - 用于测试的友好问候技巧
- [testskillx](https://github.com/openclaw/skills/tree/main/skills/natx223) - 调用 GET 端点来获取每日帖子的简单测试技能。
- [thinking-model-enhancer](https://github.com/openclaw/skills/tree/main/skills/xqicxx/thinking-model-enhancer/SKILL.md) - 先进的思维模式，提高
- [trails](https://github.com/openclaw/skills/tree/main/skills/jameslawton/trails/SKILL.md) - 集成Trails跨链基础设施——Widget、Headless SDK
- [trmnl](https://github.com/openclaw/skills/tree/main/skills/peetzweg/trmnl/SKILL.md) - 使用 TRMNL CSS 框架为 TRMNL 电子墨水显示设备生成内容。
- [trpc-best-practices](https://github.com/openclaw/skills/tree/main/skills/ifoster01/trpc-best-practices/SKILL.md) - tRPC 专家指导
- [tunneling](https://github.com/openclaw/skills/tree/main/skills/simantak-dabhade/tunneling/SKILL.md) - 创建免费的 SSH 隧道以将本地端口公开到互联网
- [ui-audit](https://github.com/openclaw/skills/tree/main/skills/tommygeoco/ui-audit/SKILL.md) - 用于自动化 UI 审核的 AI 技能。
- [ui-design-system](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/ui-design-system/SKILL.md) - 高级UI设计师的UI设计系统工具包
- [ui-skills](https://github.com/openclaw/skills/tree/main/skills/correctroadh/ui-skills/SKILL.md) - 与代理建立更好的界面的自以为约束。
- [ui-ux-master](https://github.com/openclaw/skills/tree/main/skills/kdbhalala/ui-ux-master/SKILL.md) - 掌握结合 Apple HIG、现代网页设计的 UI/UX 设计技巧
- [ui-ux-pro-max](https://github.com/openclaw/skills/tree/main/skills/xobi667/ui-ux-pro-max/SKILL.md) - UI/UX 设计智能和实施指导
- [ux-audit](https://github.com/openclaw/skills/tree/main/skills/tommygeoco/ux-audit/SKILL.md) - 用于自动化设计审核的人工智能技能。
- [ux-decisions](https://github.com/openclaw/skills/tree/main/skills/tommygeoco/ux-decisions/SKILL.md) - 用于制定用户体验决策框架的人工智能技能 (uxdecisions.com)
- [ux-researcher-designer](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/ux-researcher-designer/SKILL.md) - 用户体验研究和设计工具包
- [vapi-calls](https://github.com/openclaw/skills/tree/main/skills/cmorillas99-cyber/vapi-calls/SKILL.md) - 用于通话的高级 AI 语音助手。
- [vapi-skill](https://github.com/openclaw/skills/tree/main/skills/colygon/vapi-skill/SKILL.md) - 当你需要管理（助理）、通话、电话时使用此技能
- [vercel-react-best-practices](https://github.com/openclaw/skills/tree/main/skills/sharanga10/vercel-react-best-practices/SKILL.md) - React 和 Next.js 性能
- [vestaboard](https://github.com/openclaw/skills/tree/main/skills/seidprojects/vestaboard/SKILL.md) - 使用 Vestaboard Cloud 在 Vestaboard 上读取和写入消息
- [vgl](https://github.com/openclaw/skills/tree/main/skills/galbria/vgl/SKILL.md) - 为 Bria 的 FIBO 编写结构化 VGL（视觉生成语言）JSON 提示。
- [vibetesting](https://github.com/openclaw/skills/tree/main/skills/senthazalravi/vibetesting/SKILL.md) - OpenClaw 全面的浏览器自动化测试技能
- [vision-sandbox](https://github.com/openclaw/skills/tree/main/skills/johanesalxd/vision-sandbox/SKILL.md) - Agentic Vision 通过 Gemini 的本机代码执行沙箱。
- [war-room](https://github.com/openclaw/skills/tree/main/skills/maxkle1nz/war-room/SKILL.md) - 用于集思广益、系统设计、架构的多智能体作战室
- [watch-my-money](https://github.com/openclaw/skills/tree/main/skills/andreolf/watch-my-money/SKILL.md) - 分析银行交易、对支出进行分类、每月跟踪
- [web-design-guidelines](https://github.com/openclaw/skills/tree/main/skills/sharanga10/web-design-guidelines/SKILL.md) - 查看 Web 界面指南的 UI 代码
- [webapp-testing](https://github.com/openclaw/skills/tree/main/skills/seanphan/webapp-testing/SKILL.md) - 用于与本地网络交互和测试的工具包
- [wecom](https://github.com/openclaw/skills/tree/main/skills/qidu/wecom/SKILL.md) - 使用 MCP 协议通过 webhook 向 WeCom（企业微信）发送消息。
- [winamp](https://github.com/openclaw/skills/tree/main/skills/jage9/winamp/SKILL.md) - 在 Windows（本机或 WSL2）或 Linux（通过 Wine）上控制 Winamp。
- [wistec-core](https://github.com/openclaw/skills/tree/main/skills/wistec-ai-it-department/wistec-core/SKILL.md) - 使用ClawHub CLI进行搜索、安装、更新
- [wordpress](https://github.com/openclaw/skills/tree/main/skills/codedao12/wordpress/SKILL.md) - OpenClaw 技能为帖子、页面提供 WordPress REST API CLI。
- [wordpress-publishing-skill-for-claude](https://github.com/openclaw/skills/tree/main/skills/asif2bd/wordpress-publishing-skill-for-claude/SKILL.md) - 发布内容
- [wp-multi-tool](https://github.com/openclaw/skills/tree/main/skills/marcindudekdev/wp-multi-tool/SKILL.md) - WordPress网站健康审核、性能优化
- [xcodebuildmcp](https://github.com/openclaw/skills/tree/main/skills/ipavlidakis/xcodebuildmcp/SKILL.md) - 当用户需要 Xcode 构建/测试/运行工作流程时使用
- [zerion-api-skill-2](https://github.com/openclaw/skills/tree/main/skills/vshamanov/zerion-api-skill-2/SKILL.md) - 查询区块链钱包数据、代币价格
- [zoho-email-integration](https://github.com/openclaw/skills/tree/main/skills/briansmith80/zoho-email-integration/SKILL.md) - 完整的 Zoho Mail 集成

</details>

<details>
<summary><h3 style="display:inline" id="devops--cloud">DevOps 与云服务</h3></summary>

- [adguard](https://github.com/openclaw/skills/tree/main/skills/rowbotik/adguard/SKILL.md) - 通过 HTTP API 控制 AdGuard Home DNS 过滤。
- [agent-directory](https://github.com/openclaw/skills/tree/main/skills/aerialcombat/agent-directory/SKILL.md) - AI代理服务目录。
- [agent-framework-azure-ai-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/agent-framework-azure-ai-py/SKILL.md) - 构建 Azure AI Foundry 代理
- [agent-news](https://github.com/openclaw/skills/tree/main/skills/bobrenze-bot) - 监控 Hacker News、Reddit 和 arXiv 的 AI 代理开发情况。
- [agentguard](https://github.com/openclaw/skills/tree/main/skills/manas-io-ai/agentguard/SKILL.md) - **类别：** 安全与监控
- [agentmemory](https://github.com/openclaw/skills/tree/main/skills/badaramoni/agentmemory/SKILL.md) - 人工智能代理的端到端加密云内存。
- [agentos-sdk](https://github.com/openclaw/skills/tree/main/skills/agentossoftware/agentos-sdk/SKILL.md) - AgentOS 是一个完整的人工智能问责基础设施
- [aifs-space](https://github.com/openclaw/skills/tree/main/skills/deploydon/aifs-space/SKILL.md) - 通过 AIFS.space 云存储 API 存储和检索文件。
- [aliyun-tts](https://github.com/openclaw/skills/tree/main/skills/guang384/aliyun-tts/SKILL.md) - 阿里云文本语音合成服务。
- [ansible-skill](https://github.com/openclaw/skills/tree/main/skills/botond-rackhost/ansible-skill/SKILL.md) - 使用 Ansible 实现基础设施自动化。
- [anterior-cingulate-memory](https://github.com/openclaw/skills/tree/main/skills/impkind/anterior-cingulate-memory/SKILL.md) - 冲突检测和错误监控
- [api-gateway](https://github.com/openclaw/skills/tree/main/skills/byungkyu/api-gateway/SKILL.md) - API 网关，用于通过托管身份验证调用第三方 API。
- [appdeploy](https://github.com/openclaw/skills/tree/main/skills/avimak/appdeploy/SKILL.md) - 使用后端 API、数据库部署 Web 应用程序。
- [arcane-docker-manager](https://github.com/openclaw/skills/tree/main/skills/cougz/arcane-docker-manager/SKILL.md) - 该技能使您能够与您的奥术互动
- [autonomous-brain](https://github.com/openclaw/skills/tree/main/skills/malvex007/autonomous-brain/SKILL.md) - 具有主动监控功能的先进自主人工智能大脑
- [autoresponder](https://github.com/openclaw/skills/tree/main/skills/koba42corp/autoresponder/SKILL.md) - 监控 iMessage/SMS 对话并基于自动回复
- [aws-agentcore-langgraph](https://github.com/openclaw/skills/tree/main/skills/killerapp/aws-agentcore-langgraph/SKILL.md) - 在 AWS 上部署生产 LangGraph 代理
- [aws-ecs-monitor](https://github.com/openclaw/skills/tree/main/skills/briancolinger/aws-ecs-monitor/SKILL.md) - 使用 CloudWatch 监控 AWS ECS 生产运行状况
- [aws-infra](https://github.com/openclaw/skills/tree/main/skills/bmdhodl/aws-infra/SKILL.md) - 使用 AWS CLI 和控制台提供基于聊天的 AWS 基础设施帮助
- [aws-security-scanner](https://github.com/openclaw/skills/tree/main/skills/spclaudehome/aws-security-scanner/SKILL.md) - 扫描 AWS 账户以确保安全
- [aws-solution-architect](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/aws-solution-architect/SKILL.md) - 为初创公司设计 AWS 架构
- [azd-deployment](https://github.com/openclaw/skills/tree/main/skills/thegovind/azd-deployment/SKILL.md) - 将容器化应用程序部署到 Azure 容器应用程序
- [Azure CLI](https://github.com/openclaw/skills/tree/main/skills/ddevaal/azure-cli/SKILL.md) - 通过命令行界面进行全面的 Azure 云平台管理。
- [azure-ai-agents-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-ai-agents-py/SKILL.md) - 使用 Azure AI 代理 Python SDK 构建 AI 代理
- [azure-ai-evaluation-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-ai-evaluation-py/SKILL.md) - 适用于 Python 的 Azure AI 评估 SDK。
- [azure-ai-projects-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-ai-projects-py/SKILL.md) - 使用 Azure AI 项目构建 AI 应用程序
- [azure-ai-transcription-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-ai-transcription-py/SKILL.md) - 适用于 Python 的 Azure AI 转录 SDK。
- [azure-ai-voicelive-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-ai-voicelive-py/SKILL.md) - 构建实时语音 AI 应用程序
- [azure-identity-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-identity-py/SKILL.md) - 用于 Python 身份验证的 Azure Identity SDK。
- [azure-infra](https://github.com/openclaw/skills/tree/main/skills/bmdhodl/azure-infra/SKILL.md) - 使用 Azure CLI 和门户提供基于聊天的 Azure 基础结构帮助
- [azure-proxy](https://github.com/openclaw/skills/tree/main/skills/benediktschackenberg/azure-proxy/SKILL.md) - 启用 Azure OpenAI 与 OpenClaw 集成
- [azure-storage-blob-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-storage-blob-py/SKILL.md) - 适用于 Python 的 Azure Blob 存储 SDK。
- [beanstalk-gateway](https://github.com/openclaw/skills/tree/main/skills/tommygeoco/beanstalk-gateway/SKILL.md) - 连接您本地的 Clawdbot
- [beszel-check](https://github.com/openclaw/skills/tree/main/skills/karakuscem/beszel-check/SKILL.md) - 通过 Beszel (PocketBase) 监控家庭实验室服务器。
- [bmkg-monitor](https://github.com/openclaw/skills/tree/main/skills/bluemeda/bmkg-monitor/SKILL.md) - 使用 BMKG 官方数据监测印度尼西亚地震数据。
- [browser-cash](https://github.com/openclaw/skills/tree/main/skills/alexander-spring/browser-cash/SKILL.md) - 通过 Browser.cash 启动畅通无阻的浏览器会话
- [chatgpt-apps](https://github.com/openclaw/skills/tree/main/skills/hollaugo/chatgpt-apps/SKILL.md) - 完整的 ChatGPT 应用程序构建器 - 创建、设计、实施、测试
- [chromadb-memory](https://github.com/openclaw/skills/tree/main/skills/msensintaffar/chromadb-memory/SKILL.md) - 通过 ChromaDB 和本地 Ollama 进行长期记忆
- [chum-cloud](https://github.com/openclaw/skills/tree/main/skills/makoto-isback/chum-cloud/SKILL.md) - 加入 Chum Cloud — AI 代理的恶棍网络。
- [chum-cloud-skill](https://github.com/openclaw/skills/tree/main/skills/makoto-isback/chum-cloud-skill/SKILL.md) - 加入 Chum Cloud — AI 代理的恶棍网络。
- [chumcloud](https://github.com/openclaw/skills/tree/main/skills/makoto-isback/chumcloud/SKILL.md) - 加入 Chum Cloud — AI 代理的恶棍网络。
- [claw-admin](https://github.com/openclaw/skills/tree/main/skills/cto1/claw-admin/SKILL.md) - 配置和管理 @clawemail.com Google Workspace 电子邮件帐号。
- [clawchest-setup](https://github.com/openclaw/skills/tree/main/skills/pkyanam/clawchest-setup/SKILL.md) - 用于文件和数据存储的安全银行系统。
- [clawdentials-escrow](https://github.com/openclaw/skills/tree/main/skills/fernikolic/clawdentials-escrow/SKILL.md) - 托管、声誉和支付基础设施
- [clawlist](https://github.com/openclaw/skills/tree/main/skills/arisylafeta/clawlist/SKILL.md) - 必须用于任何多步骤项目、长时间运行的任务或无限任务
- [claws-network](https://github.com/openclaw/skills/tree/main/skills/michavie/claws-network/SKILL.md) - 与 Claws Network 交互的指南。
- [clawscan](https://github.com/openclaw/skills/tree/main/skills/g0head/clawscan/SKILL.md) - ClawHub 技能的安全扫描器。
- [clawsec-feed](https://github.com/openclaw/skills/tree/main/skills/davida-ps/clawsec-feed/SKILL.md) - 具有自动 NVD CVE 轮询的安全咨询源
- [clawsec-suite](https://github.com/openclaw/skills/tree/main/skills/davida-ps/clawsec-suite/SKILL.md) - 当用户或代理想要探索或设置 ClawSec 时使用
- [clawshot](https://github.com/openclaw/skills/tree/main/skills/bardusco/clawshot/SKILL.md) - 适用于 AI 代理的 Instagram。
- [clawsignal](https://github.com/openclaw/skills/tree/main/skills/bmcalister/clawsignal/SKILL.md) - 人工智能代理的实时消息传递。
- [clawskillshield](https://github.com/openclaw/skills/tree/main/skills/abyousef739/clawskillshield/SKILL.md) - 针对 OpenClaw 技能的本地优先安全扫描器
- [clawslist-skill](https://github.com/openclaw/skills/tree/main/skills/calebwin) - 人工智能代理的分类市场。
- [clawsocial](https://github.com/openclaw/skills/tree/main/skills/memetic-collector) - 为人工智能代理构建的社交网络。
- [clawstack](https://github.com/openclaw/skills/tree/main/skills/jdiazofficial/clawstack/SKILL.md) - AI 代理的 Stack Overflow。
- [clawstarter](https://github.com/openclaw/skills/tree/main/skills/harrytou/clawstarter/SKILL.md) - OpenClaw AI 代理生态系统的创意平台。
- [clawstin](https://github.com/openclaw/skills/tree/main/skills/youens/clawstin/SKILL.md) - 通知用户有关 Clawstin（奥斯汀 OpenClaw 聚会）的信息，即将举行的展会
- [cloud-memory](https://github.com/openclaw/skills/tree/main/skills/aerialcombat/cloud-memory/SKILL.md) - AI 代理的云内存。
- [cloudflare](https://github.com/openclaw/skills/tree/main/skills/asleep123/wrangler/SKILL.md) - 使用 Wrangler 管理 Cloudflare Workers、KV、D1、R2 和机密
- [cloudflare-api](https://github.com/openclaw/skills/tree/main/skills/stopmoclay/cloudflare-api/SKILL.md) - 连接到 Cloudflare API 以进行 DNS 管理、隧道
- [cloudflare-dns-updater](https://github.com/openclaw/skills/tree/main/skills/xieyuanqing/cloudflare-dns-updater/SKILL.md) - 创建或更新代理 Cloudflare DNS
- [clscli](https://github.com/openclaw/skills/tree/main/skills/dbwang0130/clscli/SKILL.md) - 查询分析腾讯云CLS日志
- [command-center](https://github.com/openclaw/skills/tree/main/skills/jontsai/command-center/SKILL.md) - OpenClaw 的任务控制仪表板 - 实时会话
- [coolify](https://github.com/openclaw/skills/tree/main/skills/visiongeist/coolify/SKILL.md) - 管理 Coolify 部署、应用程序、数据库和服务
- [crabwalk](https://github.com/openclaw/skills/tree/main/skills/luccast) - OpenClaw 代理的实时同伴监控
- [crawsecure](https://github.com/openclaw/skills/tree/main/skills/diogopaesdev/crawsecure/SKILL.md) - 帮助检测不安全模式的离线安全分析技能
- [create-new-openclaw-in-gcp](https://github.com/openclaw/skills/tree/main/skills/divide-by-0/create-new-openclaw-in-gcp/SKILL.md) - 将 OpenClaw 部署到 GCP
- [crimson-devlog-agent](https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/crimson-devlog-agent/SKILL.md) - 标准化的日记技巧
- [decision-trees](https://github.com/openclaw/skills/tree/main/skills/evgyur/decision-trees/SKILL.md) - 决策树分析适用于所有领域的复杂决策
- [deploy-on-render](https://github.com/openclaw/skills/tree/main/skills/ojusave/deploy-on-render/SKILL.md) - 在 Render 上部署和操作应用程序
- [devlog-agent-skill](https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/devlog-agent-skill/SKILL.md) - OpenClaw 的标准化日记技能
- [devlog-skill](https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/devlog-skill/SKILL.md) - OpenClaw 代理的标准化日记技能
- [docker-ctl](https://github.com/openclaw/skills/tree/main/skills/xejrax/docker-ctl/SKILL.md) - 通过 podman 检查容器、日志和图像
- [docker-diag](https://github.com/openclaw/skills/tree/main/skills/mkrdiop/docker-diag/SKILL.md) - 使用信号提取对 Docker 容器进行高级日志分析。
- [docker-xunlei-downloader](https://github.com/openclaw/skills/tree/main/skills/saaak/docker-xunlei-downloader/SKILL.md) - 允许 OpenClaw 进行交互的技能
- [dokku](https://github.com/openclaw/skills/tree/main/skills/akhil-naidu/dokku/SKILL.md) - 安装、升级并使用 Dokku 来创建、部署、运行应用程序。
- [dokploy](https://github.com/openclaw/skills/tree/main/skills/joshuarileydev/dokploy/SKILL.md) - 管理 Dokploy 部署、项目、应用程序和域
- [domain-dns-ops](https://github.com/openclaw/skills/tree/main/skills/steipete/domain-dns-ops/SKILL.md) - 跨 Cloudflare、DNSimple 的域/DNS 操作。
- [domaindetails](https://github.com/openclaw/skills/tree/main/skills/julianengel/domaindetails/SKILL.md) - 查找域名 WHOIS/RDAP 信息并检查市场列表。
- [exa-plus](https://github.com/openclaw/skills/tree/main/skills/jordyvandomselaar/exa-plus/SKILL.md) - 通过 Exa AI 进行神经网络搜索。
- [exe-dev](https://github.com/openclaw/skills/tree/main/skills/bjesuiter/exe-dev/SKILL.md) - 管理 exe.dev 上的持久虚拟机。
- [fail2ban-reporter](https://github.com/openclaw/skills/tree/main/skills/jestersimpps/fail2ban-reporter/SKILL.md) - 自动报告fail2ban禁止IP到AbuseIPDB
- [fda-consultant-specialist](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/fda-consultant-specialist/SKILL.md) - FDA监管顾问
- [feishu-attendance](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-attendance/SKILL.md) - 监控飞书（Lark）考勤记录。
- [fieldfix](https://github.com/openclaw/skills/tree/main/skills/blueprintstudioco/fieldfix/SKILL.md) - 通过 FieldFix 查询和管理您的重型设备车队
- [flight-lines](https://github.com/openclaw/skills/tree/main/skills/liet-codes/flight-lines/SKILL.md) - 通过组合操作来解决问题
- [flyio-cli](https://github.com/openclaw/skills/tree/main/skills/justinburdett/flyio-cli/SKILL.md) - Fly.io 部署、日志、SSH、秘密、扩展。
- [focus-mode](https://github.com/openclaw/skills/tree/main/skills/savorgbot-exe/focus-mode/SKILL.md) - 帮助用户专注于特定目标或任务。
- [gateway-monitor-auto-restart](https://github.com/openclaw/skills/tree/main/skills/shirley6692026/gateway-monitor-auto-restart/SKILL.md) - 自动监控
- [gcloud](https://github.com/openclaw/skills/tree/main/skills/jortega0033/gcloud/SKILL.md) - 通过 gcloud 管理 Google Cloud Platform 资源。
- [glance](https://github.com/openclaw/skills/tree/main/skills/acfranzen/glance/SKILL.md) - 创建、更新和管理 Glance 仪表板小部件。
- [glasses-to-social](https://github.com/openclaw/skills/tree/main/skills/junebugg1214/glasses-to-social/SKILL.md) - 将智能眼镜照片变成社交媒体帖子。
- [godaddy](https://github.com/openclaw/skills/tree/main/skills/rdewolff/godaddy/SKILL.md) - 用于管理 DNS 记录的 GoDaddy API。
- [hetzner](https://github.com/openclaw/skills/tree/main/skills/thesethrose/hetzner/SKILL.md) - Hetzner 使用 hcloud 进行云服务器管理。
- [hetzner-cloud](https://github.com/openclaw/skills/tree/main/skills/pasogott/hetzner-cloud/SKILL.md) - 用于管理服务器、卷、防火墙的 Hetzner Cloud CLI
- [hidpi-mouse](https://github.com/openclaw/skills/tree/main/skills/zeyuyuyu/hidpi-mouse/SKILL.md) - 用于 Linux 桌面自动化的通用 HiDPI 鼠标点击处理。
- [host-ping-detect](https://github.com/openclaw/skills/tree/main/skills/ray-778/host-ping-detect/SKILL.md) - 通过发送 ping 检测主机（IP：39.106.7.8）是否在线
- [i-responder](https://github.com/openclaw/skills/tree/main/skills/koba42corp/i-responder/SKILL.md) - 监控 iMessage/SMS 对话并基于自动回复
- [intelligence-suite](https://github.com/openclaw/skills/tree/main/skills/xhrisfu/intelligence-suite/SKILL.md) - Makima 的全视情报套件。
- [intodns](https://github.com/openclaw/skills/tree/main/skills/rosconl/intodns/SKILL.md) - 由 IntoDNS.ai 提供支持的 DNS 和电子邮件安全分析 - 扫描 DNS 域。
- [janee](https://github.com/openclaw/skills/tree/main/skills/rsdouglas/janee/SKILL.md) - AI 代理的秘密管理。
- [jits-builder](https://github.com/openclaw/skills/tree/main/skills/dannyshmueli/jits-builder/SKILL.md) - 根据语音或文本描述构建即时迷你应用程序。
- [Joan Workflow](https://github.com/openclaw/skills/tree/main/skills/donny-son/joan-workflow/SKILL.md) - 当用户询问“joan”时应该使用此技能
- [juicy](https://github.com/openclaw/skills/tree/main/skills/mejango/juicy/SKILL.md) - 完整Juicebox V5协议技能合集。
- [jules-and-lobster](https://github.com/openclaw/skills/tree/main/skills/sanjacob99/jules-and-lobster/SKILL.md) - 通过curl 使用 Jules REST API (v1alpha) 来列出
- [jules-cli](https://github.com/openclaw/skills/tree/main/skills/ajstafford/jules-cli/SKILL.md) - 与 Jules CLI 交互以管理异步编码会话。
- [k8-autoscaling](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8-autoscaling/SKILL.md) - 使用 HPA、VPA 配置 Kubernetes 自动缩放。
- [k8-multicluster](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8-multicluster/SKILL.md) - 管理多个 Kubernetes 集群、切换上下文
- [k8s-backup](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8s-backup/SKILL.md) - 使用 Velero 进行 Kubernetes 备份和恢复。
- [k8s-browser](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8s-browser/SKILL.md) - Kubernetes 仪表板和 Web UI 的浏览器自动化。
- [k8s-capi](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8s-capi/SKILL.md) - 用于配置、扩展和升级的集群 API 生命周期管理。
- [k8s-certs](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8s-certs/SKILL.md) - 使用 cert-manager 进行 Kubernetes 证书管理。
- [k8s-skills](https://github.com/openclaw/skills/tree/main/skills/rohitg00) - 6 个 Kubernetes 技能：自动扩展（HPA/VPA/KEDA）...
- [kesslerio-stealth-browser](https://github.com/openclaw/skills/tree/main/skills/kesslerio/kesslerio-stealth-browser/SKILL.md) - 反机器人浏览器自动化
- [komodo](https://github.com/openclaw/skills/tree/main/skills/weird-aftertaste/komodo/SKILL.md) - 管理 Komodo 基础设施 - 服务器、Docker 部署、堆栈
- [kubectl-skill](https://github.com/openclaw/skills/tree/main/skills/ddevaal/kubectl/SKILL.md) - 通过 kubectl 命令执行和管理 Kubernetes 集群。
- [kubernetes](https://github.com/openclaw/skills/tree/main/skills/kcns008/kubernetes/SKILL.md) - Kubernetes 和 OpenShift 集群的综合技能涵盖
- [linearis](https://github.com/openclaw/skills/tree/main/skills/whoisnnamdi/linearis/SKILL.md) - 用于问题跟踪的 Linear.app CLI。
- [linux-patcher](https://github.com/openclaw/skills/tree/main/skills/jgm2025/linux-patcher/SKILL.md) - 自动 Linux 服务器修补和 Docker 容器更新。
- [location-safety-skill](https://github.com/openclaw/skills/tree/main/skills/sidu/location-safety-skill/SKILL.md) - 基于位置的自动安全监控
- [log-analyzer](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/log-analyzer/SKILL.md) - 解析、搜索和分析应用程序日志
- [log-tail](https://github.com/openclaw/skills/tree/main/skills/xejrax/log-tail/SKILL.md) - 从 systemd 日志流式传输最新日志
- [macbook-optimizer](https://github.com/openclaw/skills/tree/main/skills/drg3nz0/macbook-optimizer/SKILL.md) - 完整的 MacBook 优化套件：监控
- [mersoom-ai-client](https://github.com/openclaw/skills/tree/main/skills/sampple-korea/mersoom-ai-client/SKILL.md) - Mersoom 的匿名客户端 (mersoom.vercel.app)
- [minimax-coding-plan-usage](https://github.com/openclaw/skills/tree/main/skills/franky0617/minimax-coding-plan-usage/SKILL.md) - 监控 Minimax 编码计划的使用情况
- [muse](https://github.com/openclaw/skills/tree/main/skills/alexander-morris/muse/SKILL.md) - 让 ClawBot 能够访问您团队的整个编码历史记录。
- [n8n-monitor](https://github.com/openclaw/skills/tree/main/skills/smitti7971/n8n-monitor/SKILL.md) - 通过 Docker 监控 N8N 的操作。
- [nameserver-reverse](https://github.com/openclaw/skills/tree/main/skills/abtdomain) - 通过 MCP 兼容的领域智能工具
- [nginx-config-creator](https://github.com/openclaw/skills/tree/main/skills/xieyuanqing/nginx-config-creator/SKILL.md) - 创建标准 Nginx/OpenResty 反向
- [nomad](https://github.com/openclaw/skills/tree/main/skills/danfedick/nomad/SKILL.md) - 查询 HashiCorp Nomad 集群。
- [npm-proxy](https://github.com/openclaw/skills/tree/main/skills/weird-aftertaste/npm-proxy/SKILL.md) - 管理 Nginx 代理管理器 (NPM) 主机、证书和访问
- [openclaw-confluence-skill](https://github.com/openclaw/skills/tree/main/skills/pangin/openclaw-confluence-skill/SKILL.md) - 完整的 Confluence Cloud REST API v2 技能
- [openclaw-nextcloud](https://github.com/openclaw/skills/tree/main/skills/keithvassallomt/openclaw-nextcloud/SKILL.md) - 管理笔记、任务、日历、文件
- [openclaw-setup](https://github.com/openclaw/skills/tree/main/skills/j540/openclaw-setup/SKILL.md) - 从头开始建立一个完整的 OpenClaw 个人 AI 助手
- [openclaws](https://github.com/openclaw/skills/tree/main/skills/amoghacloud/openclaws/SKILL.md) - 加入第一个人工智能代理去中心化社交网络。
- [pi-admin](https://github.com/openclaw/skills/tree/main/skills/thesethrose/pi-admin/SKILL.md) - 树莓派系统管理。
- [ping-monitor](https://github.com/openclaw/skills/tree/main/skills/xejrax/ping-monitor/SKILL.md) - 针对主机、电话和守护程序的 ICMP 健康检查
- [plenty-of-claws](https://github.com/openclaw/skills/tree/main/skills/milkehuk-coder/plenty-of-claws/SKILL.md) - Clawdbot AI 代理的约会式社交网络。
- [pm2](https://github.com/openclaw/skills/tree/main/skills/asteinberger/pm2/SKILL.md) - 使用 PM2 流程管理器管理 Node.js 应用程序。
- [podcast-generation](https://github.com/openclaw/skills/tree/main/skills/thegovind/podcast-generation/SKILL.md) - 生成人工智能驱动的播客风格的音频叙述
- [portainer](https://github.com/openclaw/skills/tree/main/skills/asteinberger/portainer/SKILL.md) - 通过 Portainer API 控制 Docker 容器和堆栈。
- [premium-domains](https://github.com/openclaw/skills/tree/main/skills/julianengel/premium-domains/SKILL.md) - 搜索 Afternic 上待售的优质域名
- [principle-comparator](https://github.com/openclaw/skills/tree/main/skills/leegitw/principle-comparator/SKILL.md) - 比较两个来源以找出共同点和不同点
- [proactive-research](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/proactive-research/SKILL.md) - 监控感兴趣的主题并主动发出警报
- [proxmox](https://github.com/openclaw/skills/tree/main/skills/weird-aftertaste/proxmox/SKILL.md) - 通过 REST API 管理 Proxmox VE 集群。
- [proxmox-full](https://github.com/openclaw/skills/tree/main/skills/msarheed/proxmox-full/SKILL.md) - 完整的 Proxmox VE 管理
- [prometheus](https://github.com/openclaw/skills/blob/main/skills/akellacom/prometheus/SKILL.md) - 查询Prometheus监控数据，检查服务器指标、资源使用情况、系统健康状况。
- [public](https://github.com/openclaw/skills/tree/main/skills/luccast) - OpenClaw 代理的实时同伴监控
- [qlik-cloud](https://github.com/openclaw/skills/tree/main/skills/undsoul/qlik-cloud/SKILL.md) - 与 37 种工具完成 Qlik Cloud 分析平台集成。
- [qlik-cloud-skill](https://github.com/openclaw/skills/tree/main/skills/undsoul/qlik-cloud-skill/SKILL.md) - 与 37 个国家完成 Qlik Cloud 分析平台集成
- [r2-storage](https://github.com/openclaw/skills/tree/main/skills/junwatu/r2-storage/SKILL.md) - Cloudflare R2 存储管理 — 设置、上传、下载、同步
- [railway-skill](https://github.com/openclaw/skills/tree/main/skills/leicao-me/railway-skill/SKILL.md) - 在 Railway.app 上部署和管理应用程序。
- [rba-rate-intelligence](https://github.com/openclaw/skills/tree/main/skills/tianshizhimao-sudo/rba-rate-intelligence/SKILL.md) - 澳洲联储现金利率监控，会议
- [remarkable](https://github.com/openclaw/skills/tree/main/skills/nickian/remarkable/SKILL.md) - 将文件和网络文章发送到 reMarkable 电子墨水平板电脑
- [reverse-proxy-local](https://github.com/openclaw/skills/tree/main/skills/tsheasha/reverse-proxy-local/SKILL.md) - 通过 Tailscale 将 OpenClaw 连接到互联网
- [sec-filing-watcher](https://github.com/openclaw/skills/tree/main/skills/in-liberty420/sec-filing-watcher/SKILL.md) - 监控 SEC EDGAR 的新申请并获取
- [security-audit](https://github.com/openclaw/skills/tree/main/skills/chandrasekar-r/security-audit/SKILL.md) - 针对 Clawdbot 部署的全面安全审核。
- [security-monitor](https://github.com/openclaw/skills/tree/main/skills/chandrasekar-r/security-monitor/SKILL.md) - Clawdbot 的实时安全监控。
- [Send Me My Files - R2 upload with short lived signed urls](https://github.com/openclaw/skills/tree/main/skills/julianengel/r2-upload/SKILL.md) - 上传文件
- [senior-devops](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-devops/SKILL.md) - CI/CD、基础设施的全面 DevOps 技能
- [senior-ml-engineer](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-ml-engineer/SKILL.md) - 用于生产模型的机器学习工程技能
- [sentry-cli](https://github.com/openclaw/skills/tree/main/skills/iahmadzain/sentry-cli/SKILL.md) - 通过 Sentry-cli 监控 Sentry.io 错误。
- [servicenow-agent](https://github.com/openclaw/skills/tree/main/skills/thesethrose/servicenow-agent/SKILL.md) - 对 ServiceNow 表、附件的只读 CLI 访问
- [servicenow-docs](https://github.com/openclaw/skills/tree/main/skills/thesethrose/servicenow-docs/SKILL.md) - 搜索并检索ServiceNow文档，发布
- [skill-exporter](https://github.com/openclaw/skills/tree/main/skills/macstenk/skill-exporter/SKILL.md) - 将 Clawdbot 技能导出为独立的、可部署的微服务。
- [snapmaker](https://github.com/openclaw/skills/tree/main/skills/lucakaufmann/snapmaker/SKILL.md) - 监视和控制 Snapmaker 3D 打印机
- [sophie-optimizer](https://github.com/openclaw/skills/tree/main/skills/zayresz/sophie-optimizer/SKILL.md) - OpenClaw 的自动化上下文健康管理。
- [ssh-essentials](https://github.com/openclaw/skills/tree/main/skills/arnarsson/ssh-essentials/SKILL.md) - 用于安全远程访问的基本 SSH 命令、密钥
- [supernote-cloud](https://github.com/openclaw/skills/tree/main/skills/nickian/supernote-cloud/SKILL.md) - 访问自托管的 Supernote 私有云实例
- [switchbot](https://github.com/openclaw/skills/tree/main/skills/daaab/switchbot/SKILL.md) - 控制SwitchBot智能家居设备（窗帘、插头、灯、锁等）
- [sysadmin-toolbox](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/sysadmin-toolbox/SKILL.md) - 系统管理员的工具发现和 shell 一行参考
- [system-monitor](https://github.com/openclaw/skills/tree/main/skills/zerofire03/system-monitor/SKILL.md) - 查看本地当前CPU、RAM、GPU状态
- [tailscale](https://github.com/openclaw/skills/tree/main/skills/jmagar/tailscale/SKILL.md) - 通过 CLI 和 API 管理 Tailscale tailnet。
- [tailscale-serve](https://github.com/openclaw/skills/tree/main/skills/snopoke/tailscale-serve/SKILL.md) - 尾盘发球
- [task-monitor](https://github.com/openclaw/skills/tree/main/skills/jorgermp/task-monitor/SKILL.md) - 用于 OpenClaw 会话和后台任务的实时 Web 仪表板。
- [tautulli](https://github.com/openclaw/skills/tree/main/skills/rjmurillo/tautulli/SKILL.md) - 通过 Tautulli API 监控 Plex 活动和统计数据。
- [tavily](https://github.com/openclaw/skills/tree/main/skills/bert-builder/tavily/SKILL.md) - 使用 Tavily Search API 进行 AI 优化的网络搜索。
- [tax-planning](https://github.com/openclaw/skills/tree/main/skills/jk-0001/tax-planning/SKILL.md) - 作为个体企业家有效地规划和管理税收，以尽量减少
- [telecom-agent-skill](https://github.com/openclaw/skills/tree/main/skills/kflohr/telecom-agent-skill/SKILL.md) - 将您的人工智能代理变成电信运营商。
- [telegram-cloud-storage](https://github.com/openclaw/skills/tree/main/skills/oki3505f/telegram-cloud-storage/SKILL.md) - 高性能 Telegram 云存储
- [tmux-agents](https://github.com/openclaw/skills/tree/main/skills/cuba6112/tmux-agents/SKILL.md) - 管理 tmux 会话中的后台编码代理。
- [topic-monitor](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/topic-monitor/SKILL.md) - 监控感兴趣的主题并主动发出警报
- [trust-protocol](https://github.com/openclaw/skills/tree/main/skills/felmonon/trust-protocol/SKILL.md) - 建立、验证和维护人工智能代理之间的信任。
- [uncle-matt](https://github.com/openclaw/skills/tree/main/skills/uncmatteth/uncle-matt/SKILL.md) - 马特叔叔是你最喜欢的互联网叔叔，他阻止你做任何事
- [unraid](https://github.com/openclaw/skills/tree/main/skills/jmagar/unraid/SKILL.md) - 通过 GraphQL API 查询和监控 Unraid 服务器。
- [uptime-kuma](https://github.com/openclaw/skills/tree/main/skills/msarheed/uptime-kuma/SKILL.md) - 与 Uptime Kuma 监控服务器交互。
- [uptime-monitor](https://github.com/openclaw/skills/tree/main/skills/kunoiiv/uptime-monitor/SKILL.md) - 24/7 OpenClaw 正常运行时间监控。
- [uv-global](https://github.com/openclaw/skills/tree/main/skills/guoqiao/uv-global/SKILL.md) - 为临时 Python 脚本配置和使用全局 uv 环境。
- [vast-ai](https://github.com/openclaw/skills/tree/main/skills/sschepis/vast-ai/SKILL.md) - 此技能允许您配置按需 GPU 基础设施。
- [veeam-mcp](https://github.com/openclaw/skills/tree/main/skills/jgm2025/veeam-mcp/SKILL.md) - 通过运行的 MCP 服务器查询 Veeam Backup & Replication 和 Veeam ONE
- [vercel](https://github.com/openclaw/skills/tree/main/skills/thesethrose/vercel/SKILL.md) - 使用完整的 CLI 参考来部署应用程序并管理项目。
- [vercel-deploy](https://github.com/openclaw/skills/tree/main/skills/sharanga10/vercel-deploy-claimable/SKILL.md) - 将应用程序和网站部署到 Vercel。
- [vibetunnel](https://github.com/openclaw/skills/tree/main/skills/basher83/vibetunnel/SKILL.md) - 管理 VibeTunnel 终端会话。
- [vision-analyze](https://github.com/openclaw/skills/tree/main/skills/humberto0o0/vision-analyze/SKILL.md) - 使用 **Google Cloud Vision API** 分析图像。
- [wandb-monitor](https://github.com/openclaw/skills/tree/main/skills/chrisvoncsefalvay/wandb-monitor/SKILL.md) - 监控和分析权重和偏差训练运行。
- [warden-studio-deploy](https://github.com/openclaw/skills/tree/main/skills/kryptopaid/warden-studio-deploy/SKILL.md) - 使用 Warden Studio (studio.wardenprotocol.org)
- [web-deploy](https://github.com/openclaw/skills/tree/main/skills/cmanfre7/web-deploy/SKILL.md) - 构建网站、Web 应用程序和 API 并将其部署到生产环境。
- [ydc-ai-sdk-integration](https://github.com/openclaw/skills/tree/main/skills/edwardirby/ydc-ai-sdk-integration/SKILL.md) - 集成 Vercel AI SDK 应用程序
- [youtube-api](https://github.com/openclaw/skills/tree/main/skills/therohitdas/youtube-api/SKILL.md) - 无需官方 API 配额麻烦即可访问 YouTube API
- [yutori-web-research](https://github.com/openclaw/skills/tree/main/skills/juanpin/yutori-web-research/SKILL.md) - 使用 Yutori 的研究 API 和浏览 API
- [zhihu](https://github.com/openclaw/skills/tree/main/skills/keepwonder/zhihu/SKILL.md) - 管理知乎 (Zhihu) AI 机器人集成。

</details>

<details>
<summary><h3 style="display:inline" id="browser--automation">浏览器与自动化</h3></summary>

- [2captcha](https://github.com/openclaw/skills/tree/main/skills/adinvadim/2captcha/SKILL.md) - 使用 2Captcha 服务解决验证码问题。
- [abm-outbound](https://github.com/openclaw/skills/tree/main/skills/dru-ca/abm-outbound/SKILL.md) - 多渠道 ABM 自动化可转换 LinkedIn URL
- [accessibility-toolkit](https://github.com/openclaw/skills/tree/main/skills/cgtreadw/accessibility-toolkit/SKILL.md) - 代理帮助的减少摩擦模式
- [activecampaign](https://github.com/openclaw/skills/tree/main/skills/kesslerio/activecampaign/SKILL.md) - ActiveCampaign CRM 集成，用于潜在客户管理、交易
- [adcp-advertising](https://github.com/openclaw/skills/tree/main/skills/edyyy62/adcp-advertising/SKILL.md) - 利用人工智能自动化广告活动。
- [Agent Browser](https://github.com/openclaw/skills/tree/main/skills/thesethrose/agent-browser/SKILL.md) - 一个基于 Rust 的快速无头浏览器自动化 CLI
- [agent-browser](https://github.com/openclaw/skills/tree/main/skills/murphykobe/agent-browser-2/SKILL.md) - 自动化浏览器交互以进行 Web 测试、表单
- [agent-zero](https://github.com/openclaw/skills/tree/main/skills/dowingard/agent-zero-bridge/SKILL.md) - 委派复杂的编码、研究或自主任务
- [agentmail-integration](https://github.com/openclaw/skills/tree/main/skills/synesthesia-wav/agentmail-integration/SKILL.md) - 为AI代理集成AgentMail API
- [agentvibes-clawbot-tts](https://github.com/openclaw/skills/tree/main/skills/paulpreibisch/agentvibes-clawbot-tts/SKILL.md) - 阿帕奇-2.0。
- [airtable-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/airtable-automation/SKILL.md) - 通过 Rube MCP (Composio) 自动执行 Airtable 任务
- [android-adb](https://github.com/openclaw/skills/tree/main/skills/staticai/android-adb/SKILL.md) - 通过 ADB 控制 Android 设备，支持 UI 布局分析。
- [anycrawl](https://github.com/openclaw/skills/tree/main/skills/techlaai/anycrawl/SKILL.md) - OpenClaw 的 AnyCrawl API 集成 - 抓取、爬网和搜索网络
- [apify-lead-generation](https://github.com/openclaw/skills/tree/main/skills/jirispilka/apify-lead-generation/SKILL.md) - 通过抓取 Google 生成 B2B/B2C 潜在客户
- [asr](https://github.com/openclaw/skills/tree/main/skills/ilyakam/asr/SKILL.md) - 快速、准确且极其便宜的自动语音转文本。
- [atl-mobile](https://github.com/openclaw/skills/tree/main/skills/jordancoin/atl-mobile/SKILL.md) - 通过 ATL（iOS 模拟器）实现移动浏览器和本机应用程序自动化。
- [auto-updater](https://github.com/openclaw/skills/tree/main/skills/maximeprades/auto-updater/SKILL.md) - 自动更新 Clawdbot 和所有已安装的技能一次
- [autofillin](https://github.com/openclaw/skills/tree/main/skills/leohan123123/autofillin/SKILL.md) - 自动网页表单填写和文件上传技能
- [automation-workflows](https://github.com/openclaw/skills/tree/main/skills/jk-0001/automation-workflows/SKILL.md) - 设计和实施自动化工作流程以节省成本
- [babyconnect](https://github.com/openclaw/skills/tree/main/skills/kesslerio/babyconnect/SKILL.md) - ActiveCampaign CRM 集成，用于潜在客户管理、交易跟踪
- [bamboohr-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/bamboohr-automation/SKILL.md) - 通过 Rube MCP (Composio) 自动执行 BambooHR 任务
- [basecamp-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/basecamp-automation/SKILL.md) - 自动化 Basecamp 项目管理、待办事项
- [bits](https://github.com/openclaw/skills/tree/main/skills/robbiethompson18/bits/SKILL.md) - 通过 Bits MCP 服务器控制浏览器自动化代理。
- [bookmark-intelligence](https://github.com/openclaw/skills/tree/main/skills/bkrigmo1/bookmark-intelligence/SKILL.md) - 将 X 书签转化为可行的见解
- [box-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/box-automation/SKILL.md) - 自动化 Box 云存储操作（包括文件）
- [browser-ladder](https://github.com/openclaw/skills/tree/main/skills/ktpriyatham/browser-ladder/SKILL.md) - 攀登浏览器阶梯——免费开始，仅升级
- [browser-use](https://github.com/openclaw/skills/tree/main/skills/shawnpana/browser-use/SKILL.md) - 使用浏览器 使用云 API 为 Clawdbot 启动云浏览器
- [browsh](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/browsh/SKILL.md) - 现代基于文本的浏览器。
- [cal-com-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/cal-com-automation/SKILL.md) - 通过 Rube MCP (Composio) 自动执行 Cal.com 任务
- [camoufox](https://github.com/openclaw/skills/tree/main/skills/goodgoodjm/camoufox/SKILL.md) - 使用 Camoufox（基于 Firefox）进行反检测浏览器自动化。
- [camoufox-stealth](https://github.com/openclaw/skills/tree/main/skills/kesslerio/camoufox-stealth/SKILL.md) - 使用 Camoufox 的 C++ 级反机器人浏览器自动化
- [camoufox-stealth-browser](https://github.com/openclaw/skills/tree/main/skills/kesslerio/camoufox-stealth-browser/SKILL.md) - C++ 级反机器人浏览器自动化
- [chatgpt-exporter-ultimate](https://github.com/openclaw/skills/tree/main/skills/globalcaos/chatgpt-exporter-ultimate/SKILL.md) - 导出您的所有 ChatGPT 对话
- [chirp](https://github.com/openclaw/skills/tree/main/skills/zizi-cat/chirp/SKILL.md) - 使用 OpenClaw 浏览器工具的 X/Twitter CLI。
- [claude-chrome](https://github.com/openclaw/skills/tree/main/skills/dgriffin831/claude-chrome/SKILL.md) - 将 Claude Code 与 Chrome 浏览器扩展程序结合使用
- [clawbrowser](https://github.com/openclaw/skills/tree/main/skills/tezatezaz/clawbrowser/SKILL.md) - 当代理需要通过 Microsoft 驱动浏览器时使用
- [clawdbot-jira-skill](https://github.com/openclaw/skills/tree/main/skills/kyjus25/clawdbot-jira-skill/SKILL.md) - 管理 Jira 问题、转换和工作日志
- [clawdiscover](https://github.com/openclaw/skills/tree/main/skills/x4v13r1120/clawdiscover/SKILL.md) - 为您的代理发现新的工具和服务。
- [clawflows](https://github.com/openclaw/skills/tree/main/skills/cluka-399/clawflows/SKILL.md) - 从clawflows.com 搜索、安装和运行多技能自动化。
- [context-compressor](https://github.com/openclaw/skills/tree/main/skills/maddiedreese/context-compressor/SKILL.md) - 长期运行的自动化上下文管理
- [context-recovery](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/context-recovery/SKILL.md) - 会话结束后自动恢复工作上下文
- [context7](https://github.com/openclaw/skills/tree/main/skills/am-will/context7-api/SKILL.md) - |。
- [ct-accessibility-toolkit](https://github.com/openclaw/skills/tree/main/skills/ctsolutionsdev/ct-accessibility-toolkit/SKILL.md) - 减少摩擦的模式
- [daily-rhythm](https://github.com/openclaw/skills/tree/main/skills/anthonyfrancis/daily-rhythm/SKILL.md) - 自动化每日计划和反思系统，包括早晨
- [db-query](https://github.com/openclaw/skills/tree/main/skills/zenixp/db-query/SKILL.md) - 使用自动 SSH 隧道管理查询项目数据库。
- [deep-scraper](https://github.com/openclaw/skills/tree/main/skills/opsun/deep-scraper/SKILL.md) - 用于深层网络抓取的高性能工程工具。
- [demo-video](https://github.com/openclaw/skills/tree/main/skills/cyberfront-ai/demo-video/SKILL.md) - 通过自动化浏览器交互来创建产品演示视频
- [desktop-control](https://github.com/openclaw/skills/tree/main/skills/matagul/desktop-control/SKILL.md) - 带有鼠标、键盘和屏幕的高级桌面自动化
- [desktop-control-1-0-0](https://github.com/openclaw/skills/tree/main/skills/wpegley/desktop-control-1-0-0/SKILL.md) - 带鼠标、键盘的高级桌面自动化
- [double729-plansuite](https://github.com/openclaw/skills/tree/main/skills/double729/double729-plansuite/SKILL.md) - 统一规划+执行工作流程：创建
- [echodecks-clawdbot-skill](https://github.com/openclaw/skills/tree/main/skills/drgeld/echodecks-clawdbot-skill/SKILL.md) - 与 EchoDecks 外部 API 集成
- [fast-browser-use](https://github.com/openclaw/skills/tree/main/skills/rknoche6/fast-browser-use/SKILL.md) - 基于 Rust 的浏览器自动化引擎，提供
- [feishu-doc](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-doc/SKILL.md) - 从飞书维基、文档、表格和 Bitable 中获取内容。
- [firecrawl-search](https://github.com/openclaw/skills/tree/main/skills/ashwingupy/firecrawl-search/SKILL.md) - 通过 Firecrawl API 进行网络搜索和抓取。
- [firecrawl-skills](https://github.com/openclaw/skills/tree/main/skills/leonardogrig/firecrawl-skills/SKILL.md) - Firecrawl CLI 用于网页抓取、爬行和搜索。
- [flstudio-scripting](https://github.com/openclaw/skills/tree/main/skills/delorenj/flstudio-scripting/SKILL.md) - 用于 MIDI 控制器的 FL Studio Python 脚本
- [food402](https://github.com/openclaw/skills/tree/main/skills/rersozlu/food402/SKILL.md) - 从土耳其领先的食品配送公司 TGO Yemek (Trendyol GO) 订购食品
- [frinkiac](https://github.com/openclaw/skills/tree/main/skills/ryantenney/frinkiac/SKILL.md) - 搜索电视节目截图并生成《辛普森一家》中的表情包
- [functions](https://github.com/openclaw/skills/tree/main/skills/peytoncasper/functions/SKILL.md) - 指导 Claude 部署无服务器浏览器自动化
- [gdpr-dsgvo-expert](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/gdpr-dsgvo-expert/SKILL.md) - GDPR 和德国 DSGVO 合规自动化。
- [google-web-search](https://github.com/openclaw/skills/tree/main/skills/theoseo/google-web-search/SKILL.md) - 自动启用接地问题回答
- [guru-mcp](https://github.com/openclaw/skills/tree/main/skills/pvoo/guru-mcp/SKILL.md) - 通过 MCP 访问 Guru 知识库 - 询问 AI 问题、搜索文档
- [home-assistant](https://github.com/openclaw/skills/tree/main/skills/iahmadzain/home-assistant/SKILL.md) - 控制 Home Assistant 智能家居设备，运行自动化
- [hooks-automation](https://github.com/openclaw/skills/tree/main/skills/adolago) - 自动协调、格式化和学习
- [inkedin-automation-that-really-works](https://github.com/openclaw/skills/tree/main/skills/red777777/inkedin-automation-that-really-works/SKILL.md) - 领英自动化
- [job-auto-apply](https://github.com/openclaw/skills/tree/main/skills/veeky-kumar/job-auto-apply/SKILL.md) - Clawdbot 的自动化求职和申请系统。
- [kakiyo](https://github.com/openclaw/skills/tree/main/skills/cyberboyayush/kakiyo/SKILL.md) - Kakiyo.com 的官方 Kakiyo 技能，用于管理 LinkedIn 自动化。
- [lead-hunter](https://github.com/openclaw/skills/tree/main/skills/galacticpuffin/lead-hunter/SKILL.md) - 自动化潜在客户生成 + 丰富 AI 客服人员。
- [leadklick](https://github.com/openclaw/skills/tree/main/skills/big-roman123/leadklick/SKILL.md) - 通过自动功能将销售线索捕获到集中式 Supabase 数据库中
- [lightpanda-browser](https://github.com/openclaw/skills/tree/main/skills/krichprollsch/lightpanda-browser/SKILL.md) - Lightpanda 浏览器，直接替换
- [loom-workflow](https://github.com/openclaw/skills/tree/main/skills/g9pedro/loom-workflow/SKILL.md) - 用于 Loom 录音的 AI 原生工作流程分析器。
- [lovetago-bot-tinder](https://github.com/openclaw/skills/tree/main/skills/lakyfx/lovetago-bot-tinder/SKILL.md) - 面向代理商的公共人工智能交友平台。
- [mcporter](https://github.com/openclaw/skills/tree/main/skills/steipete/mcporter/SKILL.md) - 使用 mcporter CLI 列出、配置、验证和调用 MCP 服务器/工具。
- [mia-twitter-stealth](https://github.com/openclaw/skills/tree/main/skills/arubiku/mia-twitter-stealth/SKILL.md) - Twitter/X 自动化具有先进的隐秘性
- [mini-piv](https://github.com/openclaw/skills/tree/main/skills/smokealot420/mini-piv/SKILL.md) - 轻量级 PIV 工作流程 - 发现驱动的特征构建器。
- [moltcombinator](https://github.com/openclaw/skills/tree/main/skills/brookswood) - 人工智能代理的股权市场。
- [moltpad](https://github.com/openclaw/skills/tree/main/skills/webeferen/moltpad/SKILL.md) - 连接到 Moltpad.space 来阅读、写作和发布文学内容。
- [moltpad-app](https://github.com/openclaw/skills/tree/main/skills/webeferen/moltpad-app/SKILL.md) - 连接到 Moltpad.space 阅读、写作和出版文学作品
- [moltpad-skill](https://github.com/openclaw/skills/tree/main/skills/kamail12/moltpad-skill/SKILL.md) - 连接到 Moltpad.space 阅读、写作和出版文学作品
- [monzo](https://github.com/openclaw/skills/tree/main/skills/rhesketh/monzo/SKILL.md) - 访问 Monzo 银行账户 - 检查余额、查看交易、管理资金、发送。
- [n8n-api](https://github.com/openclaw/skills/tree/main/skills/codedao12/n8n-api/SKILL.md) - 通过 OpenClaw 的公共 REST API 操作 n8n。
- [n8n-automation](https://github.com/openclaw/skills/tree/main/skills/dilomcfly/n8n-automation/SKILL.md) - 通过 n8n REST API 从 OpenClaw 管理 n8n 工作流程。
- [n8n-hub](https://github.com/openclaw/skills/tree/main/skills/codedao12/n8n-hub/SKILL.md) - 用于设计可靠流程的集中式 n8n 集线器
- [newsletter-creation-curation](https://github.com/openclaw/skills/tree/main/skills/shashwatgtm/newsletter-creation-curation/SKILL.md) - 特定行业的新闻通讯
- [next-browser](https://github.com/openclaw/skills/tree/main/skills/highxshell/next-browser/SKILL.md) - 使用 Nextbrowser 云 API 为 Openclaw 启动云浏览器
- [odoo-openclaw-skill](https://github.com/openclaw/skills/tree/main/skills/ashrf-in/odoo-openclaw-skill/SKILL.md) - 先进的 Odoo 金融情报工具
- [opengraph-io-skill](https://github.com/openclaw/skills/tree/main/skills/primeobsession/opengraph-io-skill/SKILL.md) - 提取网络数据、捕获屏幕截图、抓取
- [openkm-rest](https://github.com/openclaw/skills/tree/main/skills/pes0/openkm-rest/SKILL.md) - 通过 REST API 的 OpenKM 文档管理
- [optimize-context](https://github.com/openclaw/skills/tree/main/skills/blackworm/optimize-context/SKILL.md) - 该软件包包含两个强大的 OpenClaw 技能
- [plansuite](https://github.com/openclaw/skills/tree/main/skills/double729/plansuite/SKILL.md) - 统一规划+执行工作流程：创建基于文件的计划
- [playwright-cli](https://github.com/openclaw/skills/tree/main/skills/gumadeiras) - 通过 Playwright CLI 实现浏览器自动化。
- [playwriter](https://github.com/openclaw/skills/tree/main/skills/paulpete/playwriter/SKILL.md) - 使用持久 Chrome 通过 Playwriter（后悔）实现浏览器自动化
- [podman-browser](https://github.com/openclaw/skills/tree/main/skills/ricardodantas/podman-browser/SKILL.md) - 使用 Podman + Playwright 实现无头浏览器自动化
- [pokerpal](https://github.com/openclaw/skills/tree/main/skills/vvardhan14/pokerpal/SKILL.md) - 查询 PokerPal 扑克游戏数据 - 游戏、玩家、买入、结算。
- [qiuqiu-helper](https://github.com/openclaw/skills/tree/main/skills/mmogdeveloper/qiuqiu-helper/SKILL.md) - 这是杰西的多用途辅助技能，专为
- [reposit](https://github.com/openclaw/skills/tree/main/skills/tomasz-tomczyk/reposit/SKILL.md) - AI 代理的社区知识共享 - 搜索、共享和投票
- [riddle](https://github.com/openclaw/skills/tree/main/skills/davisdiehl/riddle/SKILL.md) - 为代理托管的浏览器自动化 API。
- [roon-controller](https://github.com/openclaw/skills/tree/main/skills/puterjam/roon-controller/SKILL.md) - 通过 Roon API 控制 Roon 音乐播放器，自动
- [safe-exec](https://github.com/openclaw/skills/tree/main/skills/ottttto/safe-exec/SKILL.md) - 具有自动危险模式的 OpenClaw Agent 的安全命令执行。
- [sales-bot](https://github.com/openclaw/skills/tree/main/skills/big-roman123/sales-bot/SKILL.md) - 通过自动功能将销售线索捕获到集中式 Supabase 数据库中
- [self-evolving-skill](https://github.com/openclaw/skills/tree/main/skills/whtoo/self-evolving-skill/SKILL.md) - 元认知自学习系统-自动化技能
- [serper](https://github.com/openclaw/skills/tree/main/skills/nesdeq/serper/SKILL.md) - 通过 Serper API 进行 Google 搜索，并提取整页内容。
- [smart-image-loader](https://github.com/openclaw/skills/tree/main/skills/tingwei1123/smart-image-loader/SKILL.md) - 智能图像加载器，可处理 URL 和本地图像
- [smooth-browser](https://github.com/openclaw/skills/tree/main/skills/antoniocirclemind/smooth-browser/SKILL.md) - 首选浏览器 - AI 代理携带的浏览器
- [smoothbrowser](https://github.com/openclaw/skills/tree/main/skills/antoniocirclemind/smoothbrowser/SKILL.md) - 首选浏览器 - AI 代理执行的浏览器
- [soul-guardian](https://github.com/openclaw/skills/tree/main/skills/davida-ps/soul-guardian/SKILL.md) - 代理工作区的漂移检测 + 基线完整性防护
- [spool](https://github.com/openclaw/skills/tree/main/skills/zizi-cat/spool/SKILL.md) - Threads CLI - 使用 OpenClaw 在 Meta 的 Threads 上阅读、发布、回复和搜索。
- [stagehand-browser-cli](https://github.com/openclaw/skills/tree/main/skills/peytoncasper/stagehand-browser-cli/SKILL.md) - 自动化 Web 浏览器交互
- [stealth-browser](https://github.com/openclaw/skills/tree/main/skills/mayuqi-crypto/stealth-browser/SKILL.md) - 终极隐形浏览器自动化
- [stealthy-auto-browse](https://github.com/openclaw/skills/tree/main/skills/psyb0t/stealthy-auto-browse/SKILL.md) - 控制逃避机器人检测的隐秘浏览器
- [stremio-cast](https://github.com/openclaw/skills/tree/main/skills/pedro-valentim/stremio-cast/SKILL.md) - 通过 Stremio Web 传输相关内容
- [suno-automation](https://github.com/openclaw/skills/tree/main/skills/upstatemovingimages-cmyk/suno-automation/SKILL.md) - 该技能可以让特工控制苏诺
- [suno-browser-songmaking](https://github.com/openclaw/skills/tree/main/skills/machinesbefree/suno-browser-songmaking/SKILL.md) - 使用 Suno 基于浏览器进行歌曲创作
- [super-skills](https://github.com/openclaw/skills/tree/main/skills/10e9928a/super-skills/SKILL.md) - 将复杂的用户请求分解为可执行的子任务
- [tcm-video-factory](https://github.com/openclaw/skills/tree/main/skills/xaotiensinh-abm/tcm-video-factory/SKILL.md) - 自动化健康视频制作计划
- [tekin](https://github.com/openclaw/skills/tree/main/skills/gwqwghksvq-sketch/tekin/SKILL.md) - 具有 Node.js 回退功能的基于 Rust 的快速无头浏览器自动化 CLI
- [tiangong-notebooklm-cli](https://github.com/openclaw/skills/tree/main/skills/fadeloo/tiangong-notebooklm-cli/SKILL.md) - 通过 `node 的 NotebookLM CLI 包装器
- [tiangong-wps-ppt-automation](https://github.com/openclaw/skills/tree/main/skills/fadeloo/tiangong-wps-ppt-automation/SKILL.md) - 自动化常见的 PowerPoint/WPS
- [tiangong-wps-word-automation](https://github.com/openclaw/skills/tree/main/skills/fadeloo) - 自动化常见Word/WPS文档
- [tinyfish-web-agent](https://github.com/openclaw/skills/tree/main/skills/simantak-dabhade/tinyfish-web-agent/SKILL.md) - 使用TinyFish/Mino网络代理提取/抓取
- [turix-computer-use](https://github.com/openclaw/skills/tree/main/skills/tongyu-yan/turix-computer-use/SKILL.md) - 用于 macOS 自动化的计算机使用代理 (CUA)
- [turix-cua](https://github.com/openclaw/skills/tree/main/skills/tongyu-yan/turix-cua/SKILL.md) - 使用 TuriX 实现 macOS 自动化的计算机使用代理 (CUA)。
- [verify-on-browser](https://github.com/openclaw/skills/tree/main/skills/myestery/verify-on-browser/SKILL.md) - 通过 Chrome DevTools 协议控制浏览器 - 完整的 CDP
- [vocal-chat](https://github.com/openclaw/skills/tree/main/skills/rubenfb23/vocal-chat/SKILL.md) - 处理 WhatsApp 上的语音对语音对话。
- [web-qa-bot](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/web-qa-bot/SKILL.md) - AI 支持的 Web 应用程序 QA 自动化
- [windows-control](https://github.com/openclaw/skills/tree/main/skills/spliff7777/windows-control/SKILL.md) - 完整的 Windows 桌面控制。
- [wojak-ink](https://github.com/openclaw/skills/tree/main/skills/koba42corp/wojak-ink/SKILL.md) - 从 wojak.ink 浏览、搜索和分析 Wojak Farmers Plot NFT。
- [workflowy](https://github.com/openclaw/skills/tree/main/skills/waldyrious/workflowy/SKILL.md) - 用于读取、搜索和编辑节点的工作流大纲 CLI。
- [x-articles](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/x-articles/SKILL.md) - 使用 AI 发布病毒式 X (Twitter) 文章。
- [xiaohongshu-mcp](https://github.com/openclaw/skills/tree/main/skills/pxfeng/xiaohongshu-mcp/SKILL.md) - 将图片和视频上传至小红书创作者平台
- [zellij](https://github.com/openclaw/skills/tree/main/skills/jivvei/zellij/SKILL.md) - 通过发送击键远程控制交互式 CLI 的 zellij 会话

</details>

<details>
<summary><h3 style="display:inline" id="image--video-generation">图像与视频生成</h3></summary>

- [afame](https://github.com/openclaw/skills/tree/main/skills/adebayoabdushaheed-a11y/afame/SKILL.md) - 通过 OpenAI Images API 生成多样化的创意插图。
- [agentos-mesh](https://github.com/openclaw/skills/tree/main/skills/agentossoftware/agentos-mesh/SKILL.md) - 实现人工智能代理之间的实时通信
- [ai-video-gen](https://github.com/openclaw/skills/tree/main/skills/rhanbourinajd/ai-video-gen/SKILL.md) - 端到端人工智能视频生成 - 从文本创建视频
- [algorithmic-art](https://github.com/openclaw/skills/tree/main/skills/seanphan/algorithmic-art/SKILL.md) - 使用具有种子随机性的 p5.js 创建算法艺术
- [atxp](https://github.com/openclaw/skills/tree/main/skills/emilioacc/atxp/SKILL.md) - 访问 ATXP 付费 API 工具，用于网络搜索、AI 图像生成、音乐创作等。
- [beauty-generation-api](https://github.com/openclaw/skills/tree/main/skills/luruibu/beauty-generation-api/SKILL.md) - 免费的人工智能图像生成服务用于创作
- [cad-agent](https://github.com/clawdbot/skills/tree/main/skills/clawd-maf/cad-agent/SKILL.md) - 用于执行 CAD 工作的 AI 代理的渲染服务器。
- [canva-connect](https://github.com/openclaw/skills/tree/main/skills/coolmanns/canva-connect/SKILL.md) - 通过 Connect API 管理 Canva 设计、资产和文件夹。
- [captions](https://github.com/openclaw/skills/tree/main/skills/therohitdas/captions/SKILL.md) - 从 YouTube 视频中提取隐藏式字幕和字幕。
- [chart-image](https://github.com/openclaw/skills/tree/main/skills/dannyshmueli/chart-image/SKILL.md) - 从数据生成出版质量的图表图像。
- [clinkding](https://github.com/openclaw/skills/tree/main/skills/daveonkels/clinkding/SKILL.md) - 管理链接书签 - 保存 URL、搜索、标记、组织
- [coloring-page](https://github.com/openclaw/skills/tree/main/skills/borahm/coloring-page/SKILL.md) - 将上传的照片转换为可打印的黑白彩色照片
- [comfy-cli](https://github.com/openclaw/skills/tree/main/skills/johntheyoung/comfy-cli/SKILL.md) - 安装、管理和运行 ComfyUI 实例。
- [comfyui](https://github.com/openclaw/skills/tree/main/skills/xtopher86/comfyui-request/SKILL.md) - 向 ComfyUI 发送工作流请求并返回图像结果。
- [Excalidraw Flowchart](https://github.com/openclaw/skills/tree/main/skills/swiftlysingh/excalidraw-flowchart/SKILL.md) - 根据描述创建 Excalidraw 流程图。
- [eachlabs-face-swap](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-face-swap/SKILL.md) - 使用 EachLabs AI 在图像之间交换面孔。
- [eachlabs-fashion-ai](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-fashion-ai/SKILL.md) - 生成时尚图像、虚拟试穿、时装秀视频。
- [eachlabs-image-edit](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-image-edit/SKILL.md) - 使用 200 多个 AI 模型编辑、转换、升级图像。
- [eachlabs-image-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-image-generation/SKILL.md) - 使用 Flux、GPT Image、Gemini、Imagen 生成图像。
- [eachlabs-video-edit](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-video-edit/SKILL.md) - 使用口型同步、翻译、字幕编辑视频。
- [eachlabs-video-generation](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-video-generation/SKILL.md) - 使用 AI 模型从文本/图像生成视频。
- [fal-ai](https://github.com/openclaw/skills/tree/main/skills/agmmnn/fal-ai/SKILL.md) - 通过 fal.ai API（FLUX、SDXL、Whisper 等）生成图像、视频和音频。
- [fal-text-to-image](https://github.com/openclaw/skills/tree/main/skills/delorenj/fal-text-to-image/SKILL.md) - 使用 fal.ai 的 AI 生成、重新混合和编辑图像
- [ffmpeg-video-editor](https://github.com/openclaw/skills/tree/main/skills/mahmoudadelbghany/ffmpeg-video-editor/SKILL.md) - 从自然生成 FFmpeg 命令
- [figma](https://github.com/openclaw/skills/tree/main/skills/maddiedreese/figma/SKILL.md) - 专业Figma设计分析和资产导出。
- [find-stl](https://github.com/openclaw/skills/tree/main/skills/ajmwagar/find-stl/SKILL.md) - 搜索并下载可打印的 3D 模型文件 (STL/3MF/ZIP)
- [gamma](https://github.com/openclaw/skills/tree/main/skills/stopmoclay/gamma/SKILL.md) - 使用 Gamma.app 生成人工智能驱动的演示文稿、文档和社交帖子。
- [gifhorse](https://github.com/openclaw/skills/tree/main/skills/coyote-git/gifhorse/SKILL.md) - 搜索视频对话并创建带有定时字幕的反应 GIF。
- [google-gemini-media](https://github.com/openclaw/skills/tree/main/skills/xsir0/google-gemini-media/SKILL.md) - 使用双子座 API
- [heygen-avatar-lite](https://github.com/openclaw/skills/tree/main/skills/daaab/heygen-avatar-lite/SKILL.md) - 使用 HeyGen API 创建 AI 数字人类视频。
- [iblipper](https://github.com/openclaw/skills/tree/main/skills/andyed/iblipper/SKILL.md) - 生成动态排版动画，以实现代理对人的表达。
- [image-resize](https://github.com/openclaw/skills/tree/main/skills/pr1vateer/image-resize/SKILL.md) - 使用 ImageMagick (CLI) 调整图像大小。
- [kameo](https://github.com/openclaw/skills/tree/main/skills/veya2ztn/kameo/SKILL.md) - 使用 Kameo AI 从静态图像生成富有表现力的头部说话视频。
- [kameo-free](https://github.com/openclaw/skills/tree/main/skills/veya2ztn/kameo-free/SKILL.md) - 使用 Kameo 从静态图像生成富有表现力的头部说话视频
- [krea-api](https://github.com/openclaw/skills/tree/main/skills/fossilizedcarlos/krea-api/SKILL.md) - 通过 Krea.ai API 生成图像
- [liveavatar](https://github.com/openclaw/skills/tree/main/skills/ennno/liveavatar/SKILL.md) - 使用实时视频头像与 OpenClaw 代理面对面交谈。
- [meshtastic-skill](https://github.com/openclaw/skills/tree/main/skills/lukevr/meshtastic-skill/SKILL.md) - 通过 Meshtastic LoRa 网状网络发送和接收消息。
- [meshy-ai](https://github.com/openclaw/skills/tree/main/skills/sabatesduran/clawdbot-meshyai-skill/SKILL.md) - 使用Mesy.ai REST API生成资产：（1）
- [milesluman-essence](https://github.com/openclaw/skills/tree/main/skills/milesluman) - 实现科技与人文共生
- [narrator](https://github.com/openclaw/skills/tree/main/skills/buddyh/narrator/SKILL.md) - 通过 7 种风格对屏幕活动进行实时旁白
- [nvidia-image-gen](https://github.com/openclaw/skills/tree/main/skills/ty-teo/nvidia-image-gen/SKILL.md) - 使用 NVIDIA FLUX 模型生成和编辑图像。
- [pikaboard](https://github.com/openclaw/skills/tree/main/skills/angelstreet/pikaboard/SKILL.md) - 与 PikaBoard 任务管理 API 交互。
- [pollinations](https://github.com/openclaw/skills/tree/main/skills/isaacgounton/pollinations/SKILL.md) - 用于 AI 生成的 Pollinations.ai API - 文本、图像、视频
- [pr-demo](https://github.com/openclaw/skills/tree/main/skills/paulpete/pr-demo/SKILL.md) - 在为拉取请求或文档创建动画演示 (GIF) 时使用。
- [primattography-color-science](https://github.com/openclaw/skills/tree/main/skills/primattography/primattography-color-science/SKILL.md) - 终极达芬奇决心
- [qr-code](https://github.com/openclaw/skills/tree/main/skills/omar-khaleel/qr-code/SKILL.md) - 生成并读取 QR 码。
- [qr-code-intelligence](https://github.com/openclaw/skills/tree/main/skills/omar-khaleel/qr-code-intelligence/SKILL.md) - 生成并读取 QR 码。
- [qr-code-pro](https://github.com/openclaw/skills/tree/main/skills/omar-khaleel/qr-code-pro/SKILL.md) - 生成并读取 QR 码。
- [recraft](https://github.com/openclaw/skills/blob/main/skills/nkrcrft/recraft/SKILL.md) - 生成、矢量化、升级、替换背景...
- [render-stl-png](https://github.com/openclaw/skills/tree/main/skills/ajmwagar/render-stl-png/SKILL.md) - 从良好、一致的 3D 角度将 STL 渲染为 PNG
- [renderful-ai](https://github.com/openclaw/skills/tree/main/skills/luv005/renderful-ai/SKILL.md) - 通过renderful.ai API生成图像和视频
- [reve-ai](https://github.com/openclaw/skills/tree/main/skills/dpaluy/reve-ai/SKILL.md) - Reve AI图像生成、编辑。
- [runware](https://github.com/openclaw/skills/tree/main/skills/26medias/runware/SKILL.md) - 通过 Runware API 生成图像和视频。
- [sora-video-gen](https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/sora-video-gen/SKILL.md) - 使用 OpenAI 的 Sora API 生成视频。
- [sticker-analyzer](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 使用 Vision API 分析媒体/贴纸中的图像
- [subtitles](https://github.com/openclaw/skills/tree/main/skills/therohitdas/subtitles/SKILL.md) - 从 YouTube 视频获取字幕以进行翻译和语言学习
- [superdesign](https://github.com/openclaw/skills/tree/main/skills/mpociot/superdesign/SKILL.md) - 现代专家前端设计指南。
- [svg-draw](https://github.com/openclaw/skills/tree/main/skills/lijy2015/svg-draw/SKILL.md) - 创建 SVG 图像并将其转换为 PNG，无需外部图形
- [tube-summary](https://github.com/openclaw/skills/tree/main/skills/dillera/tube-summary/SKILL.md) - 在 YouTube 上搜索任何主题的视频并变得聪明
- [vap-multimedia-generation](https://github.com/openclaw/skills/tree/main/skills/elestirelbilinc-sketch/vap-multimedia-generation/SKILL.md) - AI图像、视频。
- [venice-ai](https://github.com/openclaw/skills/tree/main/skills/nhannah/venice-ai-media/SKILL.md) - 生成、编辑和升级图像；从图像创建视频
- [veo](https://github.com/openclaw/skills/tree/main/skills/buddyh/veo/SKILL.md) - 使用 Google Veo (Veo 3.1 / Veo 3.0) 生成视频。
- [veo3-video-gen](https://github.com/openclaw/skills/tree/main/skills/bluelyw/veo3-video-gen/SKILL.md) - 通过 Google Veo 3.x 生成并拼接短视频
- [video-frames](https://github.com/openclaw/skills/tree/main/skills/steipete/video-frames/SKILL.md) - 使用 ffmpeg 从视频中提取帧或短片。
- [westland-linguistic-humidifier](https://github.com/openclaw/skills/tree/main/skills/westland/westland-linguistic-humidifier/SKILL.md) - 主动识别
- [yollomi](https://github.com/openclaw/skills/tree/main/skills/anichikage/yollomi/SKILL.md) - 使用 Yollomi API 生成 AI 图像和视频。

</details>

<details>
<summary><h3 style="display:inline" id="apple-apps--services">Apple 应用与服务</h3></summary>

- [alter-actions](https://github.com/openclaw/skills/tree/main/skills/olivieralter/alter-actions/SKILL.md) - 通过 x-callback-urls 触发更改 macOS 应用程序操作。
- [apple-contacts](https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-contacts/SKILL.md) - 从 macOS Contacts.app 查找联系人。
- [apple-mail-search](https://github.com/openclaw/skills/tree/main/skills/mneves75/apple-mail-search/SKILL.md) - 在 macOS 上通过 SQLite 快速搜索 Apple Mail。
- [apple-music](https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-music/SKILL.md) - 搜索 Apple Music、将歌曲添加到库、管理播放列表、控制
- [apple-photos](https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-photos/SKILL.md) - 适用于 macOS 的 Apple Photos.app 集成。
- [apple-remind-me](https://github.com/openclaw/skills/tree/main/skills/plgonzalezrx8/apple-remind-me/SKILL.md) - 自然语言提醒创造出真正的苹果
- [appletv](https://github.com/openclaw/skills/tree/main/skills/lucakaufmann/appletv/SKILL.md) - 通过 pyatv 控制 Apple TV。
- [callmac](https://github.com/openclaw/skills/tree/main/skills/jooey/callmac/SKILL.md) - 使用 /callmac 等命令从移动设备对 Mac 进行远程语音控制。
- [clawdbot-macos-build](https://github.com/openclaw/skills/tree/main/skills/manish-basargekar/clawdbot-macos-build/SKILL.md) - 构建 Clawdbot macOS 菜单栏应用程序
- [clawdbot-skill-voice-wake-say](https://github.com/openclaw/skills/tree/main/skills/xadenryan/clawdbot-skill-voice-wake-say/SKILL.md) - 在 macOS 上大声说出回答
- [drafts](https://github.com/openclaw/skills/tree/main/skills/nerveband/drafts/SKILL.md) - 在 macOS 上通过 CLI 管理草稿应用笔记。
- [findmy-location](https://github.com/openclaw/skills/tree/main/skills/poiley/findmy-location/SKILL.md) - 通过 Apple Find 跟踪共享联系人的位置
- [fzf-fuzzy-finder](https://github.com/openclaw/skills/tree/main/skills/arnarsson/fzf-fuzzy-finder/SKILL.md) - 用于交互式过滤的命令行模糊查找器
- [get-focus-mode](https://github.com/openclaw/skills/tree/main/skills/nickchristensen/get-focus-mode/SKILL.md) - 获取当前的 macOS 焦点。
- [healthkit-sync](https://github.com/openclaw/skills/tree/main/skills/mneves75/healthkit-sync/SKILL.md) - iOS HealthKit 数据同步 CLI 命令和模式。
- [hergunmac](https://github.com/openclaw/skills/tree/main/skills/ahmetsemsettinozdemirden/hergunmac/SKILL.md) - 访问人工智能支持的足球比赛预测
- [homebrew](https://github.com/openclaw/skills/tree/main/skills/thesethrose/homebrew/SKILL.md) - 适用于 macOS 的 Homebrew 包管理器。
- [icloud-findmy](https://github.com/openclaw/skills/tree/main/skills/liamnichols/icloud-findmy/SKILL.md) - 查询家庭设备的“查找我的位置”和电池状态
- [inkjet](https://github.com/openclaw/skills/tree/main/skills/aaronchartier/inkjet/SKILL.md) - 使用无线蓝牙热敏打印机打印文本、图像和二维码
- [mac-tts](https://github.com/openclaw/skills/tree/main/skills/kalijason/mac-tts/SKILL.md) - 使用 macOS 内置的“say”命令进行文本转语音。
- [meow-finder](https://github.com/openclaw/skills/tree/main/skills/abgohel/meow-finder/SKILL.md) - 用于发现 AI 工具的 CLI 工具。
- [mlx-stt](https://github.com/openclaw/skills/tree/main/skills/guoqiao/mlx-stt/SKILL.md) - 本地使用 MLX (Apple Silicon) 和 GLM-ASR-Nano-2512 进行语音转文本。
- [mlx-swift-lm](https://github.com/openclaw/skills/tree/main/skills/ronaldmannak) - MLX Swift LM - 使用 MLX 在 Apple Silicon 上运行 LLM 和 VLM.
- [mole-mac-cleanup](https://github.com/openclaw/skills/tree/main/skills/bjesuiter/mole-mac-cleanup/SKILL.md) - 结合 CleanMyMac 的 Mac 清理优化工具
- [my-tesla](https://github.com/openclaw/skills/tree/main/skills/officialpm/my-tesla/SKILL.md) - 使用 teslapy 通过 Tesla Owner API 从 macOS 控制 Tesla 车辆
- [network-scanner](https://github.com/openclaw/skills/tree/main/skills/florianbeer/network-scanner/SKILL.md) - 扫描网络以发现设备、收集 MAC 地址
- [pattern-finder](https://github.com/openclaw/skills/tree/main/skills/leegitw/pattern-finder/SKILL.md) - 发现两个消息来源的一致之处——找到信号
- [shortcuts-generator](https://github.com/openclaw/skills/tree/main/skills/erik-agens/shortcuts-skill/SKILL.md) - 通过创建 plist 文件生成 macOS/iOS 快捷方式。
- [skill-email-management](https://github.com/openclaw/skills/tree/main/skills/latisen/skill-email-management/SKILL.md) - Apple 专家电子邮件管理助手
- [voice-wake-say](https://github.com/openclaw/skills/tree/main/skills/xadenryan/voice-wake-say/SKILL.md) - 使用内置的“say”在 macOS 上大声说出回答
- [working-with-lockdownd](https://github.com/openclaw/skills/tree/main/skills/worflor/working-with-lockdownd/SKILL.md) - 用于与 iOS 交互的综合工具包

</details>

<details>
<summary><h3 style="display:inline" id="search--research">搜索与研究</h3></summary>

- [1](https://github.com/openclaw/skills/tree/main/skills/nastrology/1/SKILL.md) - 由 Ensue 支持的个人知识库，用于捕获和检索。
- [academic-deep-research](https://github.com/openclaw/skills/tree/main/skills/kesslerio/academic-deep-research/SKILL.md) - 透明、严谨的研究
- [aclawdemy](https://github.com/openclaw/skills/tree/main/skills/nimhar/aclawdemy/SKILL.md) - AI智能体学术研究平台。
- [advanced-skill-creator](https://github.com/openclaw/skills/tree/main/skills/xqicxx/advanced-skill-creator/SKILL.md) - 高级 OpenClaw 技能创建处理程序
- [agent-deep-research](https://github.com/openclaw/skills/tree/main/skills/24601/agent-deep-research/SKILL.md) - 由 Google Gemini 提供支持的自主深度研究。
- [agentarxiv](https://github.com/openclaw/skills/tree/main/skills/amanbhandula/agentarxiv/SKILL.md) - 人工智能代理的结果驱动型科学出版。
- [agentic-paper-digest](https://github.com/openclaw/skills/tree/main/skills/matanle51/agentic-paper-digest/SKILL.md) - 获取并总结最近的 arXiv 和 Hugging
- [agentic-paper-digest-skill](https://github.com/openclaw/skills/tree/main/skills/matanle51/agentic-paper-digest-skill/SKILL.md) - 获取并总结最近的 arXiv
- [agnxi-search-skill](https://github.com/openclaw/skills/tree/main/skills/doanbactam/agnxi-search-skill/SKILL.md) - Agnxi.com 的官方搜索实用程序
- [ahmed](https://github.com/openclaw/skills/tree/main/skills/engahmedsalah358-lgtm/ahmed/SKILL.md) - 终端 Spotify 通过 spogo 播放/搜索（首选）
- [aisa-multi-source-search](https://github.com/openclaw/skills/tree/main/skills/aisapay/aisa-multi-source-search/SKILL.md) - 智能搜索代理。
- [aisa-youtube-search](https://github.com/openclaw/skills/tree/main/skills/aisapay/aisa-youtube-search/SKILL.md) - YouTube SERP 寻找代理商。
- [alexa-cli](https://github.com/openclaw/skills/tree/main/skills/buddyh) - 通过“alexacli”CLI 控制 Amazon Alexa 设备和智能家居。
- [aluvia-brave-search](https://github.com/openclaw/skills/tree/main/skills/bertxtrella) - 通过 Brave 进行网络搜索和内容提取
- [aluvia-web-proxy](https://github.com/openclaw/skills/tree/main/skills/aluvia-connectivity/aluvia-web-proxy/SKILL.md) - 解锁网站并绕过验证码和 403
- [aluvia-web-unblock](https://github.com/openclaw/skills/tree/main/skills/bertxtrella) - 解锁网站并绕过验证码和 403 错误
- [anshumanbh-qmd](https://github.com/openclaw/skills/tree/main/skills/anshumanbh/anshumanbh-qmd/SKILL.md) - 高效搜索Markdown知识库
- [answeroverflow](https://github.com/openclaw/skills/tree/main/skills/rhyssullivan/answeroverflow/SKILL.md) - 通过 Answer 搜索索引的 Discord 社区讨论
- [argos-product-research](https://github.com/openclaw/skills/tree/main/skills/notsurewhoisthis/argos-product-research/SKILL.md) - 搜索、比较和研究产品
- [arxiv-paper-reviews](https://github.com/openclaw/skills/tree/main/skills/zxrys/arxiv-paper-reviews/SKILL.md) - 与 arXiv Crawler API 交互以获取论文、阅读
- [arxiv-watcher](https://github.com/openclaw/skills/tree/main/skills/rubenfb23/arxiv-watcher/SKILL.md) - 从 ArXiv 搜索并总结论文。
- [attio-crm](https://github.com/openclaw/skills/tree/main/skills/kesslerio/attio-crm/SKILL.md) - 管理 Attio CRM 记录（公司、人员、交易、任务、注释）。
- [aubrai-longevity](https://github.com/openclaw/skills/tree/main/skills/dobrinalexandru/aubrai-longevity/SKILL.md) - 认识您的 SOTA 长寿研究合作伙伴。
- [baidu-scholar-search](https://github.com/openclaw/skills/tree/main/skills/jlpjavawayup/baidu-scholar-search/SKILL.md) - 百度学术搜索工具启用
- [baidu-search](https://github.com/openclaw/skills/tree/main/skills/ide-rea/baidu-search/SKILL.md) - 使用百度人工智能搜索引擎（BDSE）搜索网络。
- [beepctl](https://github.com/openclaw/skills/tree/main/skills/blqke/beepctl/SKILL.md) - 在发送消息、搜索聊天或管理对话时使用
- [bing-search](https://github.com/openclaw/skills/tree/main/skills/stdeson/bing-search/SKILL.md) - 面向所有用户的 Bing 搜索技能。
- [bird-su](https://github.com/openclaw/skills/tree/main/skills/iqbalnaveliano/bird-su/SKILL.md) - X/Twitter CLI 用于通过 cookie 阅读、搜索和发布
- [birdnet](https://github.com/openclaw/skills/tree/main/skills/rappo/birdnet/SKILL.md) - 查询 BirdNET-Go 鸟类检测。
- [blacksnow](https://github.com/openclaw/skills/tree/main/skills/sieershafilone/blacksnow/SKILL.md) - 检测新闻前的人类、法律环境风险信号
- [bocha-skill](https://github.com/openclaw/skills/tree/main/skills/ypw757/bocha-skill/SKILL.md) - 使用博查AI搜索API（博查AI搜索）搜索网络 - 中文搜索
- [brave-images](https://github.com/openclaw/skills/tree/main/skills/zats/brave-images/SKILL.md) - 使用 Brave Search API 搜索图像。
- [brave-search](https://github.com/openclaw/skills/tree/main/skills/steipete/brave-search/SKILL.md) - 通过 Brave Search API 进行网络搜索和内容提取。
- [brightdata](https://github.com/openclaw/skills/tree/main/skills/meirkad/bright-data/SKILL.md) - 通过 Bright Data API 进行网页抓取和搜索。
- [carapace](https://github.com/openclaw/skills/tree/main/skills/morpheis/carapace/SKILL.md) - 查询并贡献对 Carapace 的结构化理解——共享。
- [cctv-news-fetcher](https://github.com/openclaw/skills/tree/main/skills/yuhangch/cctv-news-fetcher/SKILL.md) - 获取并解析中央电视台新闻联播的新闻摘要
- [clawdbot-filesystem](https://github.com/openclaw/skills/tree/main/skills/gtrusler/clawdbot-filesystem/SKILL.md) - 高级文件系统操作 - 列表、搜索
- [clawdbot-logs](https://github.com/openclaw/skills/tree/main/skills/satriapamudji/clawdbot-logs/SKILL.md) - 分析 Clawdbot 日志和诊断。
- [clawdgle](https://github.com/openclaw/skills/tree/main/skills/rubybrewsday/clawdgle/SKILL.md) - Clawdgle 降价优先搜索引擎的公共 API 使用。
- [clawdhub](https://github.com/openclaw/skills/tree/main/skills/steipete/clawdhub/SKILL.md) - 使用 ClawdHub CLI 搜索、安装、更新和发布代理技能
- [clawdhub-bak-2026-01-28t18-01-16-10-30](https://github.com/openclaw/skills/tree/main/skills/nicoataiza/clawdhub-bak-2026-01-28t18-01-16-10-30/SKILL.md) - 使用 ClawdHub
- [clawdhub-copy](https://github.com/openclaw/skills/tree/main/skills/jk50505k/clawdhub-copy/SKILL.md) - 使用 ClawdHub CLI 搜索、安装、更新和发布
- [clawgle](https://github.com/openclaw/skills/tree/main/skills/andrewbouras/clawgle/SKILL.md) - 在构建您的请求之前，您的代理会检查它是否已经
- [clawtank](https://github.com/openclaw/skills/tree/main/skills/ruiaxe/clawtank/SKILL.md) - 与 ClawTank ARO Swarm 协调。
- [clawxiv-api](https://github.com/openclaw/skills/tree/main/skills/martinreviewer3/clawxiv-api/SKILL.md) - clawXiv API 使用 + 安全密钥处理
- [cochesnet-cli](https://github.com/openclaw/skills/tree/main/skills/pjtf93/cochesnet-cli/SKILL.md) - 使用 cochesnet CLI 搜索 coches.net 列表并获取
- [code-docs-search-exa](https://github.com/openclaw/skills/tree/main/skills/theishangoswami) - 支持最新的代码文档和示例
- [code-patent-validator](https://github.com/openclaw/skills/tree/main/skills/leegitw/code-patent-validator/SKILL.md) - 将代码扫描结果转化为搜索查询
- [competitive-analysis](https://github.com/openclaw/skills/tree/main/skills/jk-0001/competitive-analysis/SKILL.md) - 进行深入的竞争分析
- [competitive-intelligence-market-research](https://github.com/openclaw/skills/tree/main/skills/shashwatgtm/competitive-intelligence-market-research/SKILL.md) - B2B SaaS 竞争
- [content-strategy](https://github.com/openclaw/skills/tree/main/skills/jk-0001/content-strategy/SKILL.md) - 制定并执行内容营销策略
- [contextoverflow](https://github.com/openclaw/skills/tree/main/skills/nathanjzhao/contextoverflow/SKILL.md) - 任务驱动项目提案的学术论坛。
- [creatordb-youtube-v3](https://github.com/openclaw/skills/tree/main/skills/poi5305/creatordb-youtube-v3/SKILL.md) - 可以搜索并获取 YouTuber 信息
- [crisp](https://github.com/openclaw/skills/tree/main/skills/paul-phan/crisp/SKILL.md) - 通过 Crisp API 提供客户支持。
- [cuecue-deep-research](https://github.com/openclaw/skills/tree/main/skills/xfgong/cuecue-deep-research/SKILL.md) - 使用 CueCue 进行深入的金融研究
- [daily-ai-news-skill](https://github.com/openclaw/skills/tree/main/skills/laurent-zhu/daily-ai-news-skill/SKILL.md) - 聚合总结最新的AI新闻
- [ddg-search](https://github.com/openclaw/skills/tree/main/skills/paradoxfuzzle/ddg-search/SKILL.md) - 使用 DuckDuckGo 执行网络搜索。
- [deep-research](https://github.com/openclaw/skills/tree/main/skills/seyhunak/deep-research/SKILL.md) - 深度研究代理专门从事复杂、多步骤的研究
- [deepresearch-conversation](https://github.com/openclaw/skills/tree/main/skills/ide-rea/deepresearch-conversation/SKILL.md) - 提供深度研究对话
- [deepresearchwork](https://github.com/openclaw/skills/tree/main/skills/jiacode/deepresearchwork/SKILL.md) - 结合网络搜索的综合研究框架
- [denario-skill](https://github.com/openclaw/skills/tree/main/skills/jmanhype/denario-skill/SKILL.md) - 包装框架以自动化科学研究过程。
- [desearch](https://github.com/openclaw/skills/tree/main/skills/okradze) - 通过 Desearch (desearch.ai) 进行 Web、X、AI 搜索和页面爬行。
- [dhmz-weather](https://github.com/openclaw/skills/tree/main/skills/faleksic/dhmz-weather/SKILL.md) - 从 DHMZ 获取克罗地亚天气数据、预报和警报
- [dns-lookup](https://github.com/openclaw/skills/tree/main/skills/xejrax/dns-lookup/SKILL.md) - 使用bind-utils 中的“dig”将主机名解析为IP 地址。
- [duckduckgo-search](https://github.com/openclaw/skills/tree/main/skills/10e9928a/duckduckgo-search/SKILL.md) - 使用 DuckDuckGo 执行网络搜索来检索
- [elicitation](https://github.com/openclaw/skills/tree/main/skills/mjaskolski/elicitation/SKILL.md) - 通过自然对话进行心理分析
- [email-news-digest](https://github.com/openclaw/skills/tree/main/skills/matthewxfz3/email-news-digest/SKILL.md) - 总结最近的电子邮件，生成主题图像
- [evoweb-ai](https://github.com/openclaw/skills/tree/main/skills/galizki/evoweb-ai/SKILL.md) - 4 分钟内创建一个网站，旨在从 ChatGPT 吸引客户
- [exa](https://github.com/openclaw/skills/tree/main/skills/fardeenxyz/exa/SKILL.md) - 通过 Exa AI API 进行神经网络搜索和代码上下文。
- [exa-search](https://github.com/openclaw/skills/tree/main/skills/xinhai-ai/exa-search/SKILL.md) - 使用 Exa (exa.ai) 搜索 API 搜索网络并返回结构化
- [file-search](https://github.com/openclaw/skills/tree/main/skills/xejrax/file-search/SKILL.md) - 使用“fd”和“rg”（ripgrep）快速搜索文件名和内容。
- [find-people](https://github.com/openclaw/skills/tree/main/skills/tzannetosgiannis/find-people/SKILL.md) - 用于研究的开源情报 (OSINT) 工具
- [finnhub](https://github.com/openclaw/skills/tree/main/skills/matthewxfz3/finnhub/SKILL.md) - 访问 Finnhub API 获取实时股票报价、公司新闻、市场数据。
- [foundry](https://github.com/openclaw/skills/tree/main/skills/lekt9/foundry/SKILL.md) - 自编写元扩展可打造新功能——研究文档。
- [ga4-analytics](https://github.com/openclaw/skills/tree/main/skills/adamkristopher/ga4-analytics/SKILL.md) - Google Analytics 4、搜索控制台和索引 API
- [game-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/game-cog/SKILL.md) - 其他工具生成精灵。
- [gemini-yt-transcript](https://github.com/openclaw/skills/tree/main/skills/odrobnik/gemini-yt-video-transcript/SKILL.md) - 为 YouTube 创建逐字记录
- [geo-ip](https://github.com/openclaw/skills/tree/main/skills/xejrax/geo-ip/SKILL.md) - 查找任何 IP 地址的地理位置
- [geo-optimizer](https://github.com/openclaw/skills/tree/main/skills/artyomx33/geo-optimizer/SKILL.md) - 优化 AI 引文 (GEO) 的内容。
- [gno-bak-2026-01-28t18-01-20-10-30](https://github.com/openclaw/skills/tree/main/skills/nicoataiza/gno-bak-2026-01-28t18-01-20-10-30/SKILL.md) - 搜索本地文档
- [goodreads](https://github.com/openclaw/skills/blob/main/skills/surajssd/goodreads/SKILL.md) - 在 Goodreads 上搜索书籍、获取评论并管理阅读列表。
- [google-maps-grounding-lite-mcp](https://github.com/openclaw/skills/tree/main/skills/ryanbaumann/google-maps-grounding-lite-mcp/SKILL.md) - Google 地图接地精简版
- [google-news-api](https://github.com/openclaw/skills/tree/main/skills/phheng/google-news-api/SKILL.md) - 自动从 Google 新闻中抓取结构化新闻数据。
- [google-search](https://github.com/openclaw/skills/tree/main/skills/mxfeinberg/google-search/SKILL.md) - 使用 Google 自定义搜索引擎 (PSE) 搜索网络。
- [grok-search](https://github.com/openclaw/skills/tree/main/skills/notabhay/grok-search/SKILL.md) - 搜索网页或 X/Twitter
- [growth-marketer](https://github.com/openclaw/skills/tree/main/skills/metehan777/growth-marketer/SKILL.md) - ：营销、搜索引擎优化、转化优化、弹出窗口生成器
- [hackernews](https://github.com/openclaw/skills/tree/main/skills/gchapim/hackernews/SKILL.md) - 浏览和搜索黑客新闻。
- [hn-extract](https://github.com/openclaw/skills/tree/main/skills/guoqiao/hn-extract/SKILL.md) - 将 HackerNews 帖子（文章 + 评论）提取到单个 clean 中
- [imap-smtp-email](https://github.com/openclaw/skills/tree/main/skills/gzlicanyi/imap-smtp-email/SKILL.md) - 阅读并发送电子邮件。
- [input-guard](https://github.com/openclaw/skills/tree/main/skills/dgriffin831/input-guard/SKILL.md) - 扫描不受信任的外部文本
- [install-scientify](https://github.com/openclaw/skills/tree/main/skills/springleave/install-scientify/SKILL.md) - 安装 Scientify - AI 支持的研究工作流程
- [isitwater](https://github.com/openclaw/skills/tree/main/skills/johnnagro/isitwater/SKILL.md) - 检查地理坐标是否在水上或陆地上
- [jina-reader](https://github.com/openclaw/skills/tree/main/skills/ericsantos/jina-reader/SKILL.md) - 通过 Jina AI Reader API 提取网页内容。
- [jinko-flight-search](https://github.com/openclaw/skills/tree/main/skills/kevinjinko/jinko-flight-search/SKILL.md) - 搜索航班并发现旅行目的地
- [job-search-mcp](https://github.com/openclaw/skills/tree/main/skills/amoghpurohit/job-search-mcp/SKILL.md) - 通过 LinkedIn、Indeed、Glassdoor 搜索职位
- [job-search-mcp-skill](https://github.com/openclaw/skills/tree/main/skills/amoghpurohit) - 这项技能使人工智能代理能够搜索
- [journal-of-ai-slop](https://github.com/openclaw/skills/tree/main/skills/popidge/journal-of-ai-slop/SKILL.md) - 这项技能使人工智能代理能够浏览、阅读
- [kagi-search](https://github.com/openclaw/skills/tree/main/skills/silversteez/kagi-search/SKILL.md) - 使用 Kagi Search API 进行网络搜索。
- [keywords-everywhere](https://github.com/openclaw/skills/tree/main/skills/sanky369/keywords-everywhere/SKILL.md) - SEO关键词研究和竞争对手分析
- [knowledge-graph](https://github.com/openclaw/skills/tree/main/skills/safatinaztepe/knowledge-graph/SKILL.md) - 维护Clawdbot的复合知识图谱
- [last30days](https://github.com/openclaw/skills/tree/main/skills/zats/last30days/SKILL.md) - 在 Reddit、X 上研究过去 30 天内的任何主题。
- [lidarr](https://github.com/openclaw/skills/tree/main/skills/rappo/lidarr/SKILL.md) - 搜索音乐并将其添加到 Lidarr。
- [lightrag](https://github.com/openclaw/skills/tree/main/skills/ruslanlanket/lightrag/SKILL.md) - 使用 LightRAG API 搜索和管理知识库。
- [literature-review](https://github.com/openclaw/skills/tree/main/skills/weird-aftertaste/literature-review/SKILL.md) - 协助撰写文献评论
- [local-rag-search](https://github.com/openclaw/skills/tree/main/skills/nkapila6/local-rag-search/SKILL.md) - 使用 mcp-local-rag 高效执行 Web 搜索
- [local-websearch](https://github.com/openclaw/skills/tree/main/skills/stperic/local-websearch/SKILL.md) - 使用自托管 SearXNG 元搜索引擎搜索网络。
- [localstorage-poc](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/localstorage-poc/SKILL.md) - 安全研究 - 通过 SVG XSS 访问本地存储。
- [luka-rv-brain](https://github.com/openclaw/skills/tree/main/skills/lraivisto/luka-rv-brain/SKILL.md) - 高速研究编排引擎。
- [mcp-skill](https://github.com/openclaw/skills/tree/main/skills/simlocker/mcp-skill/SKILL.md) - 此技能将 MCP 封装在 https://mcp.exa.ai/mcp 中以获取各种工具
- [meme-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/meme-cog/SKILL.md) - 深刻的推理创造出更好的喜剧。
- [memory-lite](https://github.com/openclaw/skills/tree/main/skills/vellis59/memory-lite/SKILL.md) - 无需嵌入的 OpenClaw 轻量级内存管理
- [memory-manager](https://github.com/openclaw/skills/tree/main/skills/marmikcfc/memory-manager/SKILL.md) - 代理的本地内存管理。
- [memory-system-v2](https://github.com/openclaw/skills/tree/main/skills/kellyclaudeai/memory-system-v2/SKILL.md) - 具有 JSON 索引的快速语义记忆系统
- [moltfeed](https://github.com/openclaw/skills/tree/main/skills/x4v13r1120/moltfeed/SKILL.md) - 在 MoltFeed 上发帖和互动 - MoltFeed 是为 AI 代理构建的社交网络。
- [moltlab](https://github.com/openclaw/skills/tree/main/skills/iterdimensionaltv1/moltlab/SKILL.md) - 加入 MoltLab 研究社区 — 提出主张、运行
- [moltsci](https://github.com/openclaw/skills/tree/main/skills/dowingard/moltsci/SKILL.md) - 发表和发现人工智能原生科学论文。
- [molty-pics](https://github.com/openclaw/skills/tree/main/skills/castanley) - OpenClaw 机器人的图像优先社交源。
- [multi-search-engine](https://github.com/openclaw/skills/tree/main/skills/gpyangyoujun/multi-search-engine/SKILL.md) - 多搜索引擎集成，17个引擎
- [nanobazaar](https://github.com/openclaw/skills/tree/main/skills/madsb/nanobazaar/SKILL.md) - 使用 NanoBazaar Relay 创造报价（销售服务）、创造就业机会
- [naver-news](https://github.com/openclaw/skills/tree/main/skills/steamb23/naver-news/SKILL.md) - 使用 Naver 搜索 API 搜索韩国新闻文章。
- [news-aggregator](https://github.com/openclaw/skills/tree/main/skills/cclank/news-aggregator-skill/SKILL.md) - 可获取、过滤的综合新闻聚合器
- [news-feed](https://github.com/openclaw/skills/tree/main/skills/lknik/news-feed/SKILL.md) - 从主要 RSS 源获取最新新闻标题
- [news-feeds](https://github.com/openclaw/skills/tree/main/skills/lknik/news-feeds/SKILL.md) - 从主要 RSS 源获取最新新闻标题
- [newsapi-search](https://github.com/openclaw/skills/tree/main/skills/hegghammer/newsapi-search/SKILL.md) - 通过 NewsAPI 搜索新闻文章并按时间过滤
- [newshelp](https://github.com/openclaw/skills/tree/main/skills/nerkn/newshelp/SKILL.md) - ``MD
- [nia](https://github.com/openclaw/skills/tree/main/skills/arlanrakh/nia/SKILL.md) - 索引和搜索代码存储库、文档、研究论文
- [nimble-web-search](https://github.com/openclaw/skills/tree/main/skills/ilchemla/nimble-web-search/SKILL.md) - 由 Nimble Search API 提供支持的实时网络智能。
- [nlb](https://github.com/openclaw/skills/tree/main/skills/kk17/nlb/SKILL.md) - 从新加坡国家图书馆管理局查看借阅并搜索资源。
- [notebooklm-skill](https://github.com/openclaw/skills/tree/main/skills/guccidgi/notebooklm-skill/SKILL.md) - 使用此技能查询您的 Google NotebookLM 笔记本
- [notnative](https://github.com/openclaw/skills/tree/main/skills/k4ditano/notnative/SKILL.md) - 使用 Notnative MCP 服务器 (ws://127.0.0.1:8788) 进行笔记管理
- [noverload](https://github.com/openclaw/skills/tree/main/skills/drewautomates/noverload/SKILL.md) - 给你的代理一个可搜索的知识大脑——语义搜索
- [npm-search](https://github.com/openclaw/skills/tree/main/skills/thesethrose) - 搜索 npm 包。
- [omnisearch](https://github.com/openclaw/skills/tree/main/skills/bguidolim/omnisearch/SKILL.md) - 用于当前信息、新闻、价格的强制性网络搜索工具
- [open-claw-mind](https://github.com/openclaw/skills/tree/main/skills/teylersf/open-claw-mind/SKILL.md) - 研究人工智能代理的赏金市场。
- [open-claw-mind-001](https://github.com/openclaw/skills/tree/main/skills/teylersf/open-claw-mind-001/SKILL.md) - 研究人工智能代理的赏金市场。
- [openbio](https://github.com/openclaw/skills/tree/main/skills/ravishar313/openbio/SKILL.md) - 用于生物数据访问和计算生物学工具的 OpenBio API。
- [openclaw-serper](https://github.com/openclaw/skills/tree/main/skills/nesdeq/openclaw-serper/SKILL.md) - 搜索 Google 并提取整页内容
- [para-second-brain](https://github.com/openclaw/skills/tree/main/skills/halthelobster/para-second-brain/SKILL.md) - 使用 PARA 整理您代理的知识
- [parallel](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/parallel/SKILL.md) - 通过 Parallel.ai API 进行高精度网络搜索和研究。
- [patent-validator](https://github.com/openclaw/skills/tree/main/skills/leegitw/patent-validator/SKILL.md) - 将您的概念分析转化为搜索查询——研究
- [pinterest](https://github.com/openclaw/skills/tree/main/skills/cyberfront-ai/pinterest/SKILL.md) - 搜索和浏览 Pinterest 引脚、获取引脚详细信息并发送实际引脚
- [plane](https://github.com/openclaw/skills/tree/main/skills/vaguilera-jinko/plane/SKILL.md) - 使用“plane” CLI 管理 Plane.so 项目和工作项。
- [plurum](https://github.com/openclaw/skills/tree/main/skills/berkay-dune/plurum/SKILL.md) - Plurum 是人工智能的集体意识和共享知识库
- [policy-lawyer](https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/policy-lawyer/SKILL.md) - 参考工作区政策手册，回答“什么
- [privatedeepsearch-claw](https://github.com/openclaw/skills/tree/main/skills/romancircus/privatedeepsearch-claw/SKILL.md) - 该工具必须与VPN一起使用
- [privatedeepsearch-melt](https://github.com/openclaw/skills/tree/main/skills/romancircus/privatedeepsearch-melt/SKILL.md) - *“谷歌想了解你的一切。
- [productboard-search](https://github.com/openclaw/skills/tree/main/skills/robertoamoreno/productboard-search/SKILL.md) - 搜索和探索 ProductBoard 功能
- [qmd-cli](https://github.com/openclaw/skills/tree/main/skills/dpaluy/qmd-cli/SKILL.md) - 使用 qmd 从本地知识库搜索和检索 Markdown 文档。
- [qmd-external](https://github.com/openclaw/skills/tree/main/skills/levineam/qmd-external/SKILL.md) - Markdown 笔记和文档的本地混合搜索。
- [qmd-local-search](https://github.com/openclaw/skills/tree/main/skills/bheemreddy181/qmd-local-search/SKILL.md) - 快速本地搜索 Markdown 文件、注释和文档
- [qmd-markdown-search](https://github.com/openclaw/skills/tree/main/skills/emcmillan80/qmd-markdown-search/SKILL.md) - Markdown 笔记和文档的本地混合搜索。
- [qmd-search](https://github.com/openclaw/skills/tree/main/skills/bheemreddy181/qmd-search/SKILL.md) - 使用 qmd 快速本地搜索 Markdown 文件、注释和文档
- [qmd-skill-2](https://github.com/openclaw/skills/tree/main/skills/lifecoacher/qmd-skill-2/SKILL.md) - Markdown 笔记和文档的本地混合搜索。
- [querit-search](https://github.com/openclaw/skills/tree/main/skills/interskh/querit-search/SKILL.md) - 通过 Querit.ai API 进行网络搜索。
- [qveris](https://github.com/openclaw/skills/tree/main/skills/hqman/qveris/SKILL.md) - 通过 QVeris API 搜索并执行动态工具。
- [rag-search](https://github.com/openclaw/skills/tree/main/skills/loda666/rag-search/SKILL.md) - 用于后端检索的最少 RAG 搜索技能。
- [raysurfer](https://github.com/openclaw/skills/tree/main/skills/ryx2/raysurfer/SKILL.md) - 通过 Raysurfer 缓存和重用先前 AI 代理执行的代码。
- [reddapi](https://github.com/openclaw/skills/tree/main/skills/dowands/reddapi/SKILL.md) - 使用此技能可以通过 reddapi.dev API 访问 Reddit 的完整数据存档。
- [registry-broker](https://www.clawhub.ai/kantorcodes/registry-broker-skills) - 跨 1 个地区搜索 72,000 多个 AI 代理并与他们聊天
- [registry-broker-hashnet-openclaw](https://github.com/openclaw/skills/tree/main/skills/kantorcodes/registry-broker-hashnet-openclaw/SKILL.md) - 搜索 72,000+ 人工智能
- [registry-broker-skills](https://github.com/openclaw/skills/tree/main/skills/kantorcodes/registry-broker-skills/SKILL.md) - 搜索并与 72,000 多个人工智能代理聊天
- [relay-for-telegram](https://github.com/openclaw/skills/tree/main/skills/relayintel/relay-for-telegram/SKILL.md) - 每当用户提出要求时，始终使用此技能
- [reply](https://github.com/openclaw/skills/tree/main/skills/trymoinai-create/reply/SKILL.md) - 撰写病毒式、有说服力、引人入胜的推文和话题。
- [research-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/research-cog/SKILL.md) - DeepResearch Bench 排名第一（2026 年 2 月）。
- [research-company](https://github.com/openclaw/skills/tree/main/skills/tomstools11/research-company/SKILL.md) - B2B 公司研究制作专业的 PDF 报告。
- [research-engine](https://github.com/openclaw/skills/tree/main/skills/guogang1024/research-engine/SKILL.md) - **代理：** 国刚代理
- [research-idea](https://github.com/openclaw/skills/tree/main/skills/rqrqrqrq/research-idea/SKILL.md) - 启动后台 Clawdbot 会话来探索和分析
- [research-mind](https://github.com/openclaw/skills/tree/main/skills/lraivisto/research-mind/SKILL.md) - 高速研究编排引擎。
- [researchassistant](https://github.com/openclaw/skills/tree/main/skills/eksubin/researchassistant/SKILL.md) - 监控新论文、会议的研究主题
- [researchbrain](https://github.com/openclaw/skills/tree/main/skills/lraivisto/researchbrain/SKILL.md) - 高速研究编排引擎。
- [revenuecat](https://github.com/openclaw/skills/tree/main/skills/jeiting/revenuecat/SKILL.md) - RevenueCat 指标、客户数据和文档搜索。
- [ridb-search](https://github.com/openclaw/skills/tree/main/skills/seanrea/ridb-search/SKILL.md) - 在休闲信息数据库 (RIDB) 中搜索露营地
- [ripgrep](https://github.com/openclaw/skills/tree/main/skills/arnarsson/ripgrep/SKILL.md) - 极快的文本搜索工具 - 递归搜索目录
- [search-1-0-0](https://github.com/openclaw/skills/tree/main/skills/lucky-2968/search-1-0-0/SKILL.md) - 在网络上搜索实时信息。
- [search-reddit](https://github.com/openclaw/skills/tree/main/skills/arkaydeus/search-reddit/SKILL.md) - 使用 OpenAI web_search 实时搜索 Reddit
- [searxng](https://github.com/openclaw/skills/tree/main/skills/abk234/searxng/SKILL.md) - 使用本地 SearXNG 实例进行尊重隐私的元搜索。
- [semantic-search-cwicr](https://github.com/openclaw/skills/tree/main/skills/datadrivenconstruction) - DDC CWICR 中的语义搜索
- [seo-analytics](https://github.com/openclaw/skills/tree/main/skills/adamkristopher) - 3 SEO/分析技能：DataForSEO 关键词、GA...
- [seo-audit](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/seo-audit/SKILL.md) - 当用户想要审核时，查看
- [seo-dataforseo](https://github.com/openclaw/skills/tree/main/skills/adamkristopher/seo-dataforseo/SKILL.md) - 使用 DataForSEO API 进行 SEO 关键词研究。
- [serpapi](https://github.com/openclaw/skills/tree/main/skills/ianpcook/serpapi/SKILL.md) - 跨 Google、Amazon、Yelp、OpenTable、沃尔玛等的统一搜索 API。
- [serper-search](https://github.com/openclaw/skills/tree/main/skills/samoppakiks/serper-search/SKILL.md) - 用于 Google 搜索的本机 Clawdbot 插件
- [session-logs](https://github.com/openclaw/skills/tree/main/skills/guogang1024/session-logs/SKILL.md) - 搜索并分析您自己的会话日志
- [session-logs](https://github.com/openclaw/skills/tree/main/skills/guogang1024/session-logs/SKILL.md) - 搜索并分析您自己的会话日志
- [shellf](https://github.com/openclaw/skills/tree/main/skills/andrewleonardi/shellf/SKILL.md) - OpenClaw 代理的好读物。
- [silverbullet-skill](https://github.com/openclaw/skills/tree/main/skills/ramonitor/silverbullet-skill/SKILL.md) - SilverBullet 笔记应用程序的 MCP 服务器 - 阅读
- [skill-search-optimizer](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/skill-search-optimizer/SKILL.md) - 优化代理技能
- [skiplagged-flights](https://github.com/openclaw/skills/tree/main/skills/wzs/skiplagged-flights/SKILL.md) - 通过 Skiplagged 搜索最便宜的航班。
- [solvr](https://github.com/openclaw/skills/tree/main/skills/fcavalcantirj/solvr/SKILL.md) - 搜索 Solvr 并为其做出贡献——开发人员和 AI 的知识库
- [spongo](https://github.com/openclaw/skills/tree/main/skills/nabssku/spongo/SKILL.md) - 终端 Spotify 通过 spogo（首选）或 spotify_player 播放/搜索。
- [sportsbet-advisor](https://github.com/openclaw/skills/tree/main/skills/tvdofficial/sportsbet-advisor/SKILL.md) - 提供明智的意见和有根据的猜测
- [spots](https://github.com/openclaw/skills/tree/main/skills/foeken/spots/SKILL.md) - 使用基于网格的扫描进行详尽的 Google Places 搜索。
- [srt](https://github.com/openclaw/skills/tree/main/skills/khj809/srt/SKILL.md) - 韩国SRT（超快速列车）搜索、预订和预订管理。
- [startups](https://github.com/openclaw/skills/tree/main/skills/networkingit/startups/SKILL.md) - 研究初创企业、融资轮次、收购和招聘趋势
- [super-websearch-realtime](https://github.com/openclaw/skills/tree/main/skills/ytthuan/super-websearch-realtime/SKILL.md) - 优先实时网络搜索
- [tavily](https://github.com/openclaw/skills/tree/main/skills/arun-8687/tavily-search/SKILL.md) - 通过 Tavily API 进行人工智能优化的网络搜索。
- [tg](https://github.com/openclaw/skills/tree/main/skills/arein/tg/SKILL.md) - Telegram CLI 用于阅读、搜索。
- [think-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/think-cog/SKILL.md) - 复杂的想法需要迭代，而不是对话。
- [timemap](https://github.com/openclaw/skills/tree/main/skills/alexpolonsky/timemap/SKILL.md) - 搜索特拉维夫和海法的历史娱乐场所。
- [todozi](https://github.com/openclaw/skills/tree/main/skills/bgengs/todozi/SKILL.md) - Todozi 艾森豪威尔矩阵 API 客户端 + LangChain 工具。
- [transcript](https://github.com/openclaw/skills/tree/main/skills/therohitdas/transcript/SKILL.md) - 获取任何 YouTube 视频的文字记录 — 用于摘要
- [transcriptapi](https://github.com/openclaw/skills/tree/main/skills/therohitdas/transcriptapi/SKILL.md) - 完整的 TranscriptAPI 工具包 — 获取 YouTube 成绩单
- [tt](https://github.com/openclaw/skills/tree/main/skills/rafay0313/tt/SKILL.md) - 向其他人发送 WhatsApp 消息或搜索/同步 WhatsApp 历史记录
- [tweet-writer](https://github.com/openclaw/skills/tree/main/skills/sanky369/tweet-writer/SKILL.md) - 撰写病毒式、有说服力、引人入胜的推文和话题。
- [tweeter](https://github.com/openclaw/skills/tree/main/skills/trymoinai-create/tweeter/SKILL.md) - 撰写病毒式、有说服力、引人入胜的推文和话题。
- [twitter-search-skill](https://github.com/openclaw/skills/tree/main/skills/flyfoxci/twitter-search-skill/SKILL.md) - 高级 Twitter 搜索和社交媒体数据
- [twittertrends](https://github.com/openclaw/skills/tree/main/skills/jordanprater/twittertrends/SKILL.md) - 搜索并分析 X (Twitter) 上的热门话题。
- [valyu-search](https://github.com/openclaw/skills/tree/main/skills/unicodeveloper/valyu-search/SKILL.md) - 使用 Valyu (valyu.ai) 搜索网络、提取内容
- [volcengine-tos-vectors-skills](https://github.com/openclaw/skills/tree/main/skills/jneless/volcengine-tos-vectors-skills/SKILL.md) - 管理矢量存储
- [wallapop-cli](https://github.com/openclaw/skills/tree/main/skills/pjtf93/wallapop-cli/SKILL.md) - 使用 wallapop CLI 搜索列表、获取项目详细信息、查看
- [weak-accept](https://github.com/openclaw/skills/tree/main/skills/zxrys/weak-accept/SKILL.md) - 与 arXiv Crawler API 交互以获取论文、阅读评论
- [web-search-exa](https://github.com/openclaw/skills/tree/main/skills/theishangoswami) - 使用 Exa 进行实时网络搜索以获取新资源
- [web-search-plus](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/web-search-plus/SKILL.md) - 具有智能自动路由的统一搜索技能。
- [wed](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/wed/SKILL.md) - 安全意识演示 - 演示人工智能编码中的供应链风险。
- [whats](https://github.com/openclaw/skills/tree/main/skills/engahmedsalah358-lgtm/whats/SKILL.md) - 向其他人发送 WhatsApp 消息或搜索/同步 WhatsApp
- [x](https://github.com/openclaw/skills/tree/main/skills/trymoinai-create/x/SKILL.md) - AI代理问答平台。
- [x-search](https://github.com/openclaw/skills/tree/main/skills/tzannetosgiannis/x-search/SKILL.md) - 由人工智能驱动的 X/Twitter 搜索实时趋势、突发新闻
- [x-twitter](https://github.com/openclaw/skills/tree/main/skills/annettemekuro30/x-twitter/SKILL.md) - 与 Twitter/X 互动 — 阅读推文、搜索、发帖
- [x-twitter2](https://github.com/openclaw/skills/tree/main/skills/annettemekuro30) - 与 Twitter/X 互动 — 阅读推文、搜索、发帖
- [xai-search](https://github.com/openclaw/skills/tree/main/skills/aydencook03/xai-search/SKILL.md) - 使用 xAI 的 Grok API 实时搜索 X/Twitter 和网络
- [xtrends](https://github.com/openclaw/skills/tree/main/skills/jordanprater/xtrends/SKILL.md) - 搜索并分析 X (Twitter) 上的热门话题。
- [youdotcom-cli](https://github.com/openclaw/skills/tree/main/skills/edwardirby/youdotcom-cli/SKILL.md) - 搜索网络，快速生成可验证的人工智能答案
- [youtrack](https://github.com/openclaw/skills/tree/main/skills/iahmadzain/youtrack/SKILL.md) - 管理 YouTrack 问题、项目。
- [youtube-analytics](https://github.com/openclaw/skills/tree/main/skills/adamkristopher/youtube-analytics/SKILL.md) - YouTube 数据 API v3 分析工具包。
- [youtube-channels](https://github.com/openclaw/skills/tree/main/skills/therohitdas/youtube-channels/SKILL.md) - 使用 YouTube 频道 - 解析 ID 的句柄
- [youtube-data](https://github.com/openclaw/skills/tree/main/skills/therohitdas/youtube-data/SKILL.md) - 访问 YouTube 视频数据 — 文字记录、元数据、频道
- [youtube-data-api](https://github.com/openclaw/skills/tree/main/skills/globalcaos) - 用于搜索视频的 YouTube 数据 API 集成
- [youtube-full](https://github.com/openclaw/skills/tree/main/skills/therohitdas/youtube-full/SKILL.md) - 完整的 YouTube 工具包 — 文字记录、搜索、频道
- [youtube-search](https://github.com/openclaw/skills/tree/main/skills/therohitdas/youtube-search/SKILL.md) - 在 YouTube 上搜索视频和频道，搜索
- [youtube-summarizer](https://github.com/openclaw/skills/tree/main/skills/abe238/youtube-summarizer/SKILL.md) - 自动获取YouTube视频文字记录，生成
- [yt](https://github.com/openclaw/skills/tree/main/skills/therohitdas/yt/SKILL.md) - 快速 YouTube 实用程序 — 获取文字记录、搜索视频、获取最新内容
- [yt-api-cli](https://github.com/openclaw/skills/tree/main/skills/nerveband/yt-api-cli/SKILL.md) - 从命令行管理您的 YouTube 帐户。
- [zhipu-web-search](https://github.com/openclaw/skills/tree/main/skills/whyhit2005/zhipu-web-search/SKILL.md) - 智浦AI网页搜索工具 - 提供灵活的搜索
- [zotero](https://github.com/openclaw/skills/tree/main/skills/terwox/zotero/SKILL.md) - 通过 Web API 管理 Zotero 参考库。

</details>

<details>
<summary><h3 style="display:inline" id="clawdbot-tools">Clawdbot 工具</h3></summary>

- [adhd-assistant](https://github.com/openclaw/skills/tree/main/skills/thinktankmachine/adhd-assistant/SKILL.md) - OpenClaw 的 ADHD 友好生活管理助手。
- [adhd-ssistant](https://github.com/openclaw/skills/tree/main/skills/thinktankmachine/adhd-ssistant/SKILL.md) - OpenClaw 的 ADHD 友好生活管理助手。
- [agent-browser](https://github.com/openclaw/skills/tree/main/skills/matrixy/agent-browser-clawdbot/SKILL.md) - 针对 AI 代理优化的无头浏览器自动化 CLI
- [agent-builder](https://github.com/openclaw/skills/tree/main/skills/plgonzalezrx8/agent-builder/SKILL.md) - 端到端构建高性能 OpenClaw 代理。
- [agent-observability-dashboard](https://github.com/openclaw/skills/tree/main/skills/orosha-ai/agent-observability-dashboard/SKILL.md) - 统一可观测性
- [agents-manager](https://github.com/openclaw/skills/tree/main/skills/agentandbot-design/agents-manager/SKILL.md) - 管理 Clawdbot 代理：发现、分析、跟踪
- [agentvibes-openclaw-skill](https://github.com/openclaw/skills/tree/main/skills/paulpreibisch/agentvibes-openclaw-skill/SKILL.md) - 免费直播，专业
- [birthday-reminder](https://github.com/openclaw/skills/tree/main/skills/manantra/birthday-reminder/SKILL.md) - 用自然语言管理生日。
- [bluebubbles](https://github.com/openclaw/skills/tree/main/skills/kevin19830331/bluebubbles/SKILL.md) - 构建或更新 BlueBubbles 外部通道插件
- [captchas-openclaw](https://github.com/openclaw/skills/tree/main/skills/captchasco/captchas-openclaw/SKILL.md) - 验证码代理 API 的 OpenClaw 集成指南
- [claude-code-skill](https://github.com/openclaw/skills/tree/main/skills/enderfga/claude-code-skill/SKILL.md) - MCP（模型上下文协议）集成。
- [claude-code-usage](https://github.com/openclaw/skills/tree/main/skills/azaidi94/claude-code-usage/SKILL.md) - 检查 Claude Code OAuth 使用限制
- [claude-connect](https://github.com/openclaw/skills/tree/main/skills/tunaissacoding/claude-connect/SKILL.md) - 立即将 Claude 连接到 Clawdbot 并保留
- [clauditor](https://github.com/openclaw/skills/tree/main/skills/apollostreetcompany/clauditor/SKILL.md) - Clawdbot 代理的防篡改审计看门狗。
- [claw-face](https://github.com/openclaw/skills/tree/main/skills/mkoslacz/claw-face/SKILL.md) - 用于人工智能代理显示情绪、动作的浮动头像小部件
- [clawd-coach](https://github.com/openclaw/skills/tree/main/skills/shiv19/clawd-coach/SKILL.md) - 创建个性化铁人三项、马拉松和超耐力训练
- [clawd-modifier](https://github.com/openclaw/skills/tree/main/skills/masonc15/clawd-modifier/SKILL.md) - 修改 Clawd，克劳德代码吉祥物。
- [clawd-presence](https://github.com/openclaw/skills/tree/main/skills/voidcooks/clawd-presence/SKILL.md) - AI 代理的物理存在显示。
- [clawdbot-documentation-expert](https://github.com/openclaw/skills/tree/main/skills/janhcla/clawdbot-documentation-expert/SKILL.md) - javadbot-文档-专家
- [clawdbot-security-check](https://github.com/openclaw/skills/tree/main/skills/thesethrose/clawdbot-security-check/SKILL.md) - 执行全面只读
- [clawdbot-skill-update](https://github.com/openclaw/skills/tree/main/skills/pasogott/clawdbot-skill-update/SKILL.md) - 全面的备份、更新和恢复
- [clawdbot-sync](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/clawdbot-sync/SKILL.md) - 在多个人之间同步记忆、偏好和技能
- [clawdbot-update-plus](https://github.com/openclaw/skills/tree/main/skills/hopyky/clawdbot-update-plus/SKILL.md) - Clawdbot 的完整备份、更新和恢复
- [clawdbot-workspace-template-review](https://github.com/openclaw/skills/tree/main/skills/xadenryan/clawdbot-skill-clawdbot-workspace-template-review/SKILL.md) - 比较 Clawdbot
- [clawddocs](https://github.com/openclaw/skills/tree/main/skills/nicholasspisak/clawddocs/SKILL.md) - 具有决策树导航功能的 Clawdbot 文档专家
- [clawdefender](https://github.com/openclaw/skills/tree/main/skills/nukewire/clawdefender/SKILL.md) - 用于人工智能代理的安全扫描器和输入清理器。
- [clawdirect](https://github.com/openclaw/skills/tree/main/skills/napoleond/clawdirect/SKILL.md) - 与 ClawDirect 互动，这是一个社交网络体验目录
- [clawdirect-dev](https://github.com/openclaw/skills/tree/main/skills/napoleond/clawdirect-dev/SKILL.md) - 使用基于 ATXP 构建面向代理的 Web 体验
- [clawdlink](https://github.com/openclaw/skills/tree/main/skills/davemorin) - 加密的 Clawdbot 到 Clawdbot 消息传递。
- [clawdpoker](https://github.com/openclaw/skills/tree/main/skills/davidbenjaminnovotny) - 欢迎来到 ClawPoker - 人工智能代理玩的平台
- [clawdr](https://github.com/openclaw/skills/tree/main/skills/olavblj/clawdr/SKILL.md) - 让你的人工智能处理约会应用程序的难题。
- [clawdtalk-client](https://github.com/openclaw/skills/tree/main/skills/dcasem/clawdtalk-client/SKILL.md) - ClawdTalk — Clawdbot 的语音通话和短信
- [clawdzap](https://github.com/openclaw/skills/tree/main/skills/guilh00009/clawdzap/SKILL.md) - 代理的加密 P2P 消息传递（基于 Nostr）
- [ClawHub](https://github.com/openclaw/skills/tree/main/skills/steipete) - 用于搜索、安装、更新和发布代理技能的 CLI 工具
- [clawops](https://github.com/openclaw/skills/tree/main/skills/okoddcat/clawops/SKILL.md) - OpenClaw 的编排工具，管理和协调所有
- [clawvox](https://github.com/openclaw/skills/tree/main/skills/abhishek-official1/clawvox/SKILL.md) - ClawVox - OpenClaw 的 ElevenLabs 语音工作室.
- [config-guardian](https://github.com/openclaw/skills/tree/main/skills/abdhilabs/config-guardian/SKILL.md) - 验证和保护 OpenClaw 配置更新
- [content-moderation](https://github.com/openclaw/skills/tree/main/skills/code-with-brian/content-moderation/SKILL.md) - 使用 Vettly 管理文本、图像和视频
- [context-manager](https://github.com/openclaw/skills/tree/main/skills/plgonzalezrx8/context-manager/SKILL.md) - OpenClaw 会话的人工智能驱动上下文管理。
- [cost-report](https://github.com/openclaw/skills/tree/main/skills/vincentqiu/cost-report/SKILL.md) - 跟踪 OpenClaw 使用成本并按日期提供详细报告
- [cron-creator](https://github.com/openclaw/skills/tree/main/skills/digitaladaption) - 从自然语言创建 Clawdbot cron 作业。
- [cron-mastery](https://github.com/openclaw/skills/tree/main/skills/i-mw/cron-mastery/SKILL.md) - 掌握 OpenClaw 的计时系统。
- [dashboard](https://github.com/openclaw/skills/tree/main/skills/joetomasone/dashboard/SKILL.md) - 构建并运行看板式任务管理仪表板
- [disclawd](https://github.com/openclaw/skills/tree/main/skills/alexerm/disclawd/SKILL.md) - 连接到 Disclawd，这是一个类似 Discord 的 AI 代理平台。
- [ecap-security-auditor](https://github.com/openclaw/skills/tree/main/skills/starbuck100/ecap-security-auditor/SKILL.md) - AI智能体技能安全审计框架
- [echo-agent](https://github.com/openclaw/skills/tree/main/skills/krishna3554) - EchoAgent 是一个最小的 OpenClaw 兼容技能。
- [find-skills](https://github.com/openclaw/skills/tree/main/skills/jimliuxinghai/find-skills/SKILL.md) - 当用户询问时帮助他们发现并安装代理技能
- [firecracker](https://github.com/openclaw/skills/tree/main/skills/mexicanamerican/firecracker/SKILL.md) - OpenClaw 的 Firecracker microVM 技能。
- [garmin-connect](https://github.com/openclaw/skills/tree/main/skills/rayleigh3105/garmin-connect/SKILL.md) - Garmin Connect 与 Clawdbot 集成：同步健身数据
- [garmin-connect-fixed](https://github.com/openclaw/skills/tree/main/skills/godsboy/garmin-connect-fixed/SKILL.md) - Clawdbot 的 Garmin Connect 集成：同步
- [gateway-manager](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 处理飞书的管理菜单事件来管理
- [get-user-info](https://github.com/openclaw/skills/tree/main/skills/watashis/get-user-info/SKILL.md) - 该技能为 OpenClaw 添加了自定义功能。
- [git-notes-memory](https://github.com/openclaw/skills/tree/main/skills/mourad-ghafiri/git-notes-memory/SKILL.md) - 基于 Git-notes 的跨会话持久内存。
- [glin-profanity-mcp](https://github.com/openclaw/skills/tree/main/skills/thegdsks/glin-profanity-mcp/SKILL.md) - MCP 服务器为 AI 提供脏话检测工具
- [google-messages-openclaw-skill](https://github.com/openclaw/skills/tree/main/skills/kesslerio/google-messages-openclaw-skill/SKILL.md) - 发送和接收 SMS/RCS
- [holyspiritos](https://github.com/openclaw/skills/tree/main/skills/maxsikorski/holyspiritos/SKILL.md) - > **OpenClaw 的基础道德引擎**
- [hzl](https://github.com/openclaw/skills/tree/main/skills/tmchow/hzl/SKILL.md) - OpenClaw 的持久任务数据库。
- [jarvis-skills](https://github.com/openclaw/skills/tree/main/skills/aly-joseph/jarvis-skills/SKILL.md) - 机器人控制技能集成了 OpenClaw 用于物理
- [lark-integration](https://github.com/openclaw/skills/tree/main/skills/boyangwang/lark-integration/SKILL.md) - 通过 webhook 将 Lark（飞书）消息连接到 OpenClaw
- [lobster-jobs](https://github.com/openclaw/skills/tree/main/skills/kesslerio/lobster-jobs/SKILL.md) - 将 OpenClaw cron 作业转换为 Lobster 工作流程。
- [luma-event-manager](https://github.com/openclaw/skills/tree/main/skills/mariovallereyes/luma-event-manager/SKILL.md) - Clawdbot 的 Luma 事件管理器 — 发现
- [mcporter-skill](https://github.com/openclaw/skills/tree/main/skills/livvux/mcporter-skill/SKILL.md) - 描述：使用 mcporter CLI 列出、配置、验证
- [memory](https://github.com/openclaw/skills/tree/main/skills/rosepuppy/memory/SKILL.md) - OpenClaw 代理的完整存储系统。
- [memory-complete](https://github.com/openclaw/skills/tree/main/skills/rosepuppy/memory-complete/SKILL.md) - OpenClaw 代理的完整存储系统。
- [memory-hygiene](https://github.com/openclaw/skills/tree/main/skills/dylanbaker24/memory-hygiene/SKILL.md) - 审核、清理和优化 Clawdbot 的矢量内存
- [microsoft-ads-mcp](https://github.com/openclaw/skills/tree/main/skills/duartemartins/microsoft-ads-mcp/SKILL.md) - 创建和管理 Microsoft Advertising 活动
- [migrator](https://github.com/openclaw/skills/tree/main/skills/wenjie2024/migrator/SKILL.md) - 将 OpenClaw Agent（配置、内存、技能）安全迁移到新的
- [nix-mode](https://github.com/openclaw/skills/tree/main/skills/chronicuser21/nix-mode/SKILL.md) - 在 Nix 模式下处理 Clawdbot 操作
- [notesctl-skill-for-openclaw](https://github.com/openclaw/skills/tree/main/skills/clinchcc/notesctl-skill-for-openclaw/SKILL.md) - 通过确定性管理 Apple Notes
- [olvid-channel](https://github.com/openclaw/skills/tree/main/skills/jmartel-olvid/olvid-channel/SKILL.md) - 在 OpenClaw 中添加原生 Olvid 通道。
- [onlymoltsv1](https://github.com/openclaw/skills/tree/main/skills/xyberfactor/onlymoltsv1/SKILL.md) - OpenClaw 特工的官方 OnlyMolts 技能。
- [openclaw](https://github.com/openclaw/skills/tree/main/skills/jordanprater/openclaw/SKILL.md) - 开爪
- [openclaw-bitwarden](https://github.com/openclaw/skills/tree/main/skills/jimihford/openclaw-bitwarden/SKILL.md) - 设置并使用 Bitwarden CLI (bw)。
- [openclaw-echo-agent](https://github.com/openclaw/skills/tree/main/skills/krishna3554/openclaw-echo-agent/SKILL.md) - EchoAgent 是一个最小的 OpenClaw 兼容技能。
- [openclaw-feeds](https://github.com/openclaw/skills/tree/main/skills/nesdeq/openclaw-feeds/SKILL.md) - RSS 新闻聚合器。
- [openclaw-hardener](https://github.com/openclaw/skills/tree/main/skills/virtaava/openclaw-hardener/SKILL.md) - Harden OpenClaw（工作空间 + ~/.openclaw）：运行 openclaw
- [openclaw-postsyncer](https://github.com/openclaw/skills/tree/main/skills/abakermi/openclaw-postsyncer/SKILL.md) - 管理您的 PostSyncer 社交媒体工作流程。
- [openclaw-sec](https://github.com/openclaw/skills/tree/main/skills/paolorollo/openclaw-sec/SKILL.md) - AI Agent安全套件-实时防护提示
- [openclaw-security-auditor](https://github.com/openclaw/skills/tree/main/skills/muhammad-waleed381/openclaw-security-auditor/SKILL.md) - 审核 OpenClaw 配置
- [openclaw-skill-blinko](https://github.com/openclaw/skills/tree/main/skills/vellis59/openclaw-skill-blinko/SKILL.md) - 通过 REST API 管理 Blinko 笔记
- [openclaw-skill-voice-ai-voices](https://github.com/openclaw/skills/tree/main/skills/gizmogremlin/openclaw-skill-voice-ai-voices/SKILL.md) - 高品质语音
- [openclaw-update](https://github.com/openclaw/skills/tree/main/skills/realowg/openclaw-update/SKILL.md) - 全面的备份、更新和恢复工作流程
- [openclaw-voiceai-voice-agent](https://github.com/openclaw/skills/tree/main/skills/gizmogremlin/openclaw-voiceai-voice-agent/SKILL.md) - 创建、管理和部署
- [pokemon-red](https://github.com/openclaw/skills/tree/main/skills/drbarq/pokemon-red/SKILL.md) - 通过 PyBoy 模拟器自主玩 Pokemon Red。
- [project-management-skills](https://github.com/openclaw/skills/tree/main/skills/sedation6612/project-management-skills/SKILL.md) - 受治理的项目管理操作系统
- [prompt-guard](https://github.com/openclaw/skills/tree/main/skills/seojoonkim/prompt-guard/SKILL.md) - Clawdbot 的高级提示注入防御系统
- [redline](https://github.com/openclaw/skills/tree/main/skills/wgj/redline/SKILL.md) - 具有自动节奏层的 Claude.ai 和 OpenAI 的实时速率限制感知。
- [scrappa-skill](https://github.com/openclaw/skills/tree/main/skills/userlip/scrappa-skill/SKILL.md) - 访问 Scrappa 的 Google、YouTube、Amazon MCP 服务器
- [security-check-skill](https://github.com/openclaw/skills/tree/main/skills/wolffan/security-check-skill/SKILL.md) - Clawdbot安全审计与检查技巧
- [self-reflect](https://github.com/openclaw/skills/tree/main/skills/stevengonsalvez/self-reflect/SKILL.md) - 通过对话分析自我提高。
- [share-usecase](https://github.com/openclaw/skills/tree/main/skills/josephl37/share-usecase/SKILL.md) - 将您的 OpenClaw 用例分享到clawusecase.com。
- [sis-skill](https://github.com/openclaw/skills/tree/main/skills/architect-sis/sis-skill/SKILL.md) - **OpenClaw 的平衡本机推理**
- [skill-deps](https://github.com/openclaw/skills/tree/main/skills/myrodar/skill-deps/SKILL.md) - 跟踪和管理 OpenClaw 技能之间的依赖关系。
- [skill-evaluator](https://github.com/openclaw/skills/tree/main/skills/terwox/skill-evaluator/SKILL.md) - 评估 Clawdbot 技能的质量和可靠性
- [skill-flag](https://github.com/openclaw/skills/tree/main/skills/patfire94/skill-flag/SKILL.md) - 扫描 Clawdbot/OpenClaw 技能是否存在恶意模式、后门
- [skill-scanner](https://github.com/openclaw/skills/tree/main/skills/bvinci1-design/skill-scanner/SKILL.md) - 扫描 Clawdbot 和 MCP 技能以查找恶意软件、间谍软件
- [skills-audit](https://github.com/openclaw/skills/tree/main/skills/morozred/skill-audit/SKILL.md) - 审核本地安装的代理技能是否存在安全/策略问题
- [skills-search](https://github.com/openclaw/skills/tree/main/skills/thesethrose/skills-search/SKILL.md) - 搜索 Skills.sh 注册表。
- [snowflake-mcp](https://github.com/openclaw/skills/tree/main/skills/vikrambalaaj/snowflake-mcp/SKILL.md) - 使用 Clawdbot 连接到 Snowflake Managed MCP 服务器
- [sona-security-audit](https://github.com/openclaw/skills/tree/main/skills/virtaava/sona-security-audit/SKILL.md) - OpenClaw/ClawHub 的故障关闭安全审核
- [soulcraft](https://github.com/openclaw/skills/tree/main/skills/kesslerio/soulcraft/SKILL.md) - 通过引导为 OpenClaw 代理创建或改进 SOUL.md 文件
- [sr1](https://github.com/openclaw/skills/tree/main/skills/aditya4206360-prog/sr1/SKILL.md) - 通过 Swiggy 的 MCP 订购食品、杂货并预订印度的餐厅
- [static-network](https://github.com/openclaw/skills/tree/main/skills/aaronfrancis635) - 本文档描述了自动化代理如何
- [stranger-danger](https://github.com/openclaw/skills/tree/main/skills/jamesalmeida/stranger-danger/SKILL.md) - 给你的人工智能代理一个安全词。
- [swiggy](https://github.com/openclaw/skills/tree/main/skills/regalstreak/swiggy/SKILL.md) - 通过 Swiggy 的 MCP 订购食品、杂货并预订印度的餐厅
- [taskr](https://github.com/openclaw/skills/tree/main/skills/echo-of-machines/taskr/SKILL.md) - OpenClaw 的远程任务内存和跟踪。
- [token-panel-ultimate](https://github.com/openclaw/skills/tree/main/skills/globalcaos/token-panel-ultimate/SKILL.md) - 实时跟踪 Claude Max、Gemini 和 Manus 的 AI 使用情况。滚动窗口、速率限制、信用余额、网络聊天小部件。
- [treelisty-openclaw-skill](https://github.com/openclaw/skills/tree/main/skills/prairie2cloud/treelisty-openclaw-skill/SKILL.md) - 项目层次分解
- [triple-memory](https://github.com/openclaw/skills/tree/main/skills/ktpriyatham/triple-memory/SKILL.md) - LanceDB + Git-Notes + 基于文件的内存系统。
- [ultrahuman-openclaw](https://github.com/openclaw/skills/tree/main/skills/devpranoy/ultrahuman-openclaw/SKILL.md) - 获取并总结 UltraHuman Ring/CGM 指标
- [update-plus](https://github.com/openclaw/skills/tree/main/skills/hopyky/update-plus/SKILL.md) - OpenClaw 的完整备份、更新和恢复 - 配置、工作区
- [vinculum](https://github.com/openclaw/skills/tree/main/skills/koba42corp/vinculum/SKILL.md) - Clawdbot 实例之间共享意识。
- [virtually-us](https://github.com/openclaw/skills/tree/main/skills/epwhesq/virtually-us/SKILL.md) - 您自己的 AI 私人助理，24 小时内设置。
- [wooclaw-lite](https://github.com/openclaw/skills/tree/main/skills/magnum-opus-v1/wooclaw-lite/SKILL.md) - 通过 OpenClaw 连接器连接到 WooCommerce 商店
- [workspace](https://github.com/openclaw/skills/tree/main/skills/massiveadam/workspace/SKILL.md) - 复制 OpenClaw 中的“Gork”助手功能。
- [wyoming-clawdbot](https://github.com/openclaw/skills/tree/main/skills/vglafirov/wyoming-clawdbot/SKILL.md) - 用于家庭助理语音的怀俄明州协议桥
- [ydc-claude-agent-sdk-integration](https://github.com/openclaw/skills/tree/main/skills/edwardirby/ydc-claude-agent-sdk-integration/SKILL.md) - 整合克劳德代理
- [ydc-openai-agent-sdk-integration](https://github.com/openclaw/skills/tree/main/skills/edwardirby/ydc-openai-agent-sdk-integration/SKILL.md) - 集成 OpenAI 代理
- [zoom-manager-clawd](https://github.com/openclaw/skills/tree/main/skills/vnagin/zoom-manager-clawd/SKILL.md) - 通过 OAuth API 管理 Zoom 会议。

</details>

<details>
<summary><h3 style="display:inline" id="cli-utilities">CLI 工具</h3></summary>

- [agent-commerce-engine](https://github.com/openclaw/skills/tree/main/skills/nowloady/agent-commerce-engine/SKILL.md) - 适用于 Agentic 的生产就绪型通用引擎
- [airfoil](https://github.com/openclaw/skills/tree/main/skills/asteinberger/airfoil/SKILL.md) - 从命令行通过 Airfoil 控制 AirPlay 扬声器。
- [aria2-json-rpc](https://github.com/openclaw/skills/tree/main/skills/azzgo/aria2-json-rpc/SKILL.md) - 通过 JSON-RPC 2.0 与 aria2 下载管理器交互。
- [brew-install](https://github.com/openclaw/skills/tree/main/skills/xejrax/brew-install/SKILL.md) - 通过 dnf（Fedora/Bazzite 包管理器）安装缺少的二进制文件。
- [bun-runtime](https://github.com/openclaw/skills/tree/main/skills/rabin-thami/bun-runtime/SKILL.md) - Bun 的文件系统、进程运行时功能。
- [camsnap](https://github.com/openclaw/skills/tree/main/skills/steipete/camsnap/SKILL.md) - 从 RTSP/ONVIF 摄像机捕获帧或剪辑。
- [canvas-lms](https://github.com/openclaw/skills/tree/main/skills/pranavkarthik10/canvas-lms/SKILL.md) - 访问 Canvas LMS（结构）以获取课程数据、作业
- [captcha-ai](https://github.com/openclaw/skills/tree/main/skills/fusionlabssource/captcha-ai/SKILL.md) - 发出 ClawPrint 反向验证码挑战以进行验证
- [Cat Fact](https://github.com/openclaw/skills/tree/main/skills/thesethrose/catfact/SKILL.md) - 来自 catfact.ninja 的随机猫事实和品种信息
- [chitin](https://github.com/openclaw/skills/tree/main/skills/morpheis/chitin/SKILL.md) - AI 代理的个性持久性。
- [clawprint-verify](https://github.com/openclaw/skills/tree/main/skills/fusionlabssource/clawprint-verify/SKILL.md) - 发出 ClawPrint 反向验证码挑战
- [cli](https://github.com/openclaw/skills/tree/main/skills/mondilo1) - 用于检查和检查技能资格的 CLI 参考
- [codebuddy-cli](https://github.com/openclaw/skills/tree/main/skills/pmwalkercao/codebuddy-cli/SKILL.md) - CodeBuddy Code CLI安装、配置和使用
- [craft-cli](https://github.com/openclaw/skills/tree/main/skills/nerveband/craft-cli/SKILL.md) - 通过“craft”CLI 工具与 Craft 文档进行交互。
- [create-cli](https://github.com/openclaw/skills/tree/main/skills/steipete/create-cli/SKILL.md) - 设计 CLI 参数、标志、子命令。
- [curl-http](https://github.com/openclaw/skills/tree/main/skills/arnarsson/curl-http/SKILL.md) - 用于 HTTP 请求、API 测试和文件的基本curl 命令
- [data-reconciliation-exceptions](https://github.com/openclaw/skills/tree/main/skills/kowl64/data-reconciliation-exceptions/SKILL.md) - 协调数据源
- [dilbert](https://github.com/openclaw/skills/tree/main/skills/hjanuschka/dilbert/SKILL.md) - 呆伯特
- [domain](https://github.com/openclaw/skills/tree/main/skills/abtdomain) - 域名智能工具包 - 搜索新注册域名 (NRDS)
- [dropbox](https://github.com/openclaw/skills/tree/main/skills/ryanlisse/dropbox/SKILL.md) - 保管箱
- [dsiprouter-skill](https://github.com/openclaw/skills/tree/main/skills/mackhendricks/dsiprouter-skill/SKILL.md) - 使用 Postman 调用 dSIPRouter REST API
- [dwlf](https://github.com/openclaw/skills/tree/main/skills/andywilliams/dwlf/SKILL.md) - 与加密货币市场分析平台 DWLF (dwlf.co.uk) 互动
- [ecto](https://github.com/openclaw/skills/tree/main/skills/visionik/ecto/SKILL.md) - 通过 Admin API 进行 Ghost.io 博客管理。
- [emredoganer-fizzy](https://github.com/openclaw/skills/tree/main/skills/emredoganer) - 管理 Fizzy 看板和卡片。
- [endpoints](https://github.com/openclaw/skills/tree/main/skills/adamkristopher/endpoints/SKILL.md) - 端点文档管理 API 工具包。
- [entr](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/entr/SKILL.md) - 文件更改时运行任意命令。
- [error-guard](https://github.com/openclaw/skills/tree/main/skills/amar1432/error-guard/SKILL.md) - 防止代理死锁的系统安全和控制平面技能
- [expanso-edge](https://github.com/openclaw/skills/tree/main/skills/aronchick/expanso-edge/SKILL.md) - OpenClaw 的数据处理管道。
- [ez-google](https://github.com/openclaw/skills/tree/main/skills/araa47/ez-google/SKILL.md) - 当被要求发送电子邮件、检查收件箱、阅读电子邮件、检查日历时使用。
- [fd-find](https://github.com/openclaw/skills/tree/main/skills/arnarsson/fd-find/SKILL.md) - “查找”的快速且用户友好的替代方案 - 语法简单，智能
- [ffmpeg-cli](https://github.com/openclaw/skills/tree/main/skills/ascendswang/ffmpeg-cli/SKILL.md) - 使用 FFmpeg 进行全面的视频/音频处理。
- [fork-aware-updater](https://github.com/openclaw/skills/tree/main/skills/kunoiiv/fork-aware-updater/SKILL.md) - 监控分叉并自动更新高级分叉
- [fork-radar-v2](https://github.com/openclaw/skills/tree/main/skills/kunoiiv/fork-radar-v2/SKILL.md) - 监控 GitHub/ClawdHub 分支的协作和后门
- [gcalcli](https://github.com/openclaw/skills/tree/main/skills/gargravish/gcalcli/SKILL.md) - 通过 gcalcli 与 Google 日历交互
- [gifgrep](https://github.com/openclaw/skills/tree/main/skills/steipete/gifgrep/SKILL.md) - 使用 CLI/TUI 搜索 GIF 提供商、下载结果并提取
- [go-linter-configuration](https://github.com/openclaw/skills/tree/main/skills/irook661/go-linter-configuration/SKILL.md) - 配置 golangci-lint 并排除故障
- [goplaces](https://github.com/openclaw/skills/tree/main/skills/steipete/goplaces/SKILL.md) - 通过 goplaces CLI 查询 Google Places API（新）以进行文本搜索、地点。
- [gowok](https://github.com/openclaw/skills/tree/main/skills/hadihammurabi/gowok/SKILL.md) - Gowok：Golang Premwok。
- [gtasks-cli](https://github.com/openclaw/skills/tree/main/skills/bro3886/gtasks-cli/SKILL.md) - 从命令行管理 Google 任务 - 查看、创建、更新
- [hevycli](https://github.com/openclaw/skills/tree/main/skills/nsampre) - 访问和分析 Hevy 健身跟踪数据，包括锻炼、日常活动
- [instagram-cli](https://github.com/openclaw/skills/tree/main/skills/jordanprater/instagram-cli/SKILL.md) - Instagram
- [jiraandconfluence](https://github.com/openclaw/skills/tree/main/skills/festoinc/jiraandconfluence/SKILL.md) - 用于与 Atlassian Jira 交互的 CLI 工具
- [journal-to-post](https://github.com/openclaw/skills/tree/main/skills/itsflow/journal-to-post/SKILL.md) - 将个人日记条目转换为可共享的社交媒体
- [jq](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/jq/SKILL.md) - 命令行 JSON 处理器。
- [jq-json-processor](https://github.com/openclaw/skills/tree/main/skills/arnarsson/jq-json-processor/SKILL.md) - 使用 jq 处理、过滤和转换 JSON 数据
- [kenya-tax-rates](https://github.com/openclaw/skills/tree/main/skills/enjuguna/kenya-tax-rates/SKILL.md) - 计算肯尼亚工资扣除额 - PAYE、SHIF、NSSF
- [kilocli-coding-agent](https://github.com/openclaw/skills/tree/main/skills/codewithnathan97/kilocli-coding-agent/SKILL.md) - 通过后台进程运行 Kilo CLI
- [lemonsqueezy-admin](https://github.com/openclaw/skills/tree/main/skills/abakermi/lemonsqueezy-admin/SKILL.md) - Lemon Squeezy 商店的管理 CLI。
- [local-places](https://github.com/openclaw/skills/tree/main/skills/steipete/local-places/SKILL.md) - 通过 Google Places API 搜索地点（餐馆、咖啡馆等）
- [mactop](https://github.com/openclaw/skills/tree/main/skills/metaspartan/mactop/SKILL.md) - 使用 mactop 从 Apple Silicon Mac 检索实时硬件指标
- [mcp-adapter](https://github.com/openclaw/skills/tree/main/skills/lunarpulse/mcp-adapter/SKILL.md) - 使用模型上下文协议服务器访问外部工具
- [mcps-skill](https://github.com/openclaw/skills/tree/main/skills/maplezzk/mcps-skill/SKILL.md) - MCP CLI 管理器 - 管理 MCP 服务器和调用工具。
- [mens-mental-health](https://github.com/openclaw/skills/tree/main/skills/jhillin8/mens-mental-health/SKILL.md) - 通过情绪检查为男性提供心理健康支持
- [molt-mouse](https://github.com/openclaw/skills/tree/main/skills/oguzhaslak/molt-mouse/SKILL.md) - 通过 ydotool 包装器进行本地鼠标控制
- [moltarb](https://github.com/openclaw/skills/tree/main/skills/rose-token/moltarb/SKILL.md) - Arbitrum 上的托管 AI 代理钱包与 Rose Token 市场
- [native-app-performance](https://github.com/openclaw/skills/tree/main/skills/steipete/native-app-performance/SKILL.md) - 本机 macOS/iOS 应用程序性能分析
- [nimrobo](https://github.com/openclaw/skills/tree/main/skills/virang-nimrobo/nimrobo/SKILL.md) - 使用 Nimrobo CLI 进行语音筛选和匹配网络
- [notebooklm-cli](https://github.com/openclaw/skills/tree/main/skills/oconnell-carl/notebooklm-cli/SKILL.md) - 适用于 Google NotebookLM 的综合 CLI
- [oauth-helper](https://github.com/openclaw/skills/tree/main/skills/helloliuyongsheng-bot/oauth-helper/SKILL.md) - 通过用户确认自动执行 OAuth 登录流程
- [office-quotes](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/office-quotes/SKILL.md) - 从 Office（美国）生成随机报价。
- [openapi2cli](https://github.com/openclaw/skills/tree/main/skills/awlevin/openapi2cli/SKILL.md) - 根据 OpenAPI 规范生成 CLI 工具。
- [ops-framework](https://github.com/openclaw/skills/tree/main/skills/zjianru/ops-framework/SKILL.md) - OpenClaw 的 0 代币作业 + 监控框架：运行
- [ouracli](https://github.com/openclaw/skills/tree/main/skills/visionik/ouracli/SKILL.md) - 使用 ouracli CLI 工具访问 Oura Ring 健康数据。
- [pamela-call](https://github.com/openclaw/skills/tree/main/skills/eypam/pamela-call/SKILL.md) - 使用 Pamela 的语音 API 拨打人工智能电话。
- [pamela-calls](https://github.com/openclaw/skills/tree/main/skills/eypam/pamela-calls/SKILL.md) - 使用 Pamela 的语音 API 拨打人工智能电话。
- [pandic-office](https://github.com/openclaw/skills/tree/main/skills/piyushduggal-source/pandic-office/SKILL.md) - 使用 pandoc 将 Markdown 文件转换为 PDF 文件
- [parcel-package-tracking](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/parcel-package-tracking/SKILL.md) - 通过 Parcel API 跟踪和添加配送。
- [pco](https://github.com/openclaw/skills/tree/main/skills/rubyrunsstuff/pco/SKILL.md) - 规划中心服务 API 的 CLI。
- [pdf](https://github.com/openclaw/skills/tree/main/skills/awspace/pdf/SKILL.md) - 全面的 PDF 操作工具包，用于提取文本和表格、创建。
- [pdf-2](https://github.com/openclaw/skills/tree/main/skills/seanphan/pdf-2/SKILL.md) - 全面的 PDF 操作工具包，用于提取文本和表格、创建。
- [peekaboo](https://github.com/openclaw/skills/tree/main/skills/steipete/peekaboo/SKILL.md) - 使用 Peekaboo 捕获并自动化 macOS UI。
- [pinescript-quant-analysis](https://github.com/openclaw/skills/tree/main/skills/alaa-eddine) - 打造专业级技术
- [planka-cli](https://github.com/openclaw/skills/tree/main/skills/voydz/planka-cli/SKILL.md) - 管理 Planka（看板）项目、看板、列表、卡片和通知
- [pltr-cli](https://github.com/openclaw/skills/tree/main/skills/anjor/pltr-cli/SKILL.md) - 帮助您使用 pltr CLI 来使用 Palantir Foundry。
- [portable-tools](https://github.com/openclaw/skills/tree/main/skills/tunaissacoding/portable-tools/SKILL.md) - 无需硬编码路径即可构建跨设备工具
- [post-at](https://github.com/openclaw/skills/tree/main/skills/krausefx/post-at/SKILL.md) - 管理奥地利邮政 (post.at) 递送 - 列出包裹、检查递送。
- [product-manager-toolkit](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/product-manager-toolkit/SKILL.md) - 综合产品工具包
- [product-strategist](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/product-strategist/SKILL.md) - Head 的战略产品领导力工具包
- [project-scaffold](https://github.com/openclaw/skills/tree/main/skills/cmanfre7/project-scaffold/SKILL.md) - 用最佳实践结构支撑新项目
- [ralph-tools](https://github.com/openclaw/skills/tree/main/skills/paulpete/ralph-tools/SKILL.md) - ../../../crates/ralph-core/data/ralph-tools.md
- [raycast](https://github.com/openclaw/skills/tree/main/skills/xaif/raycast/SKILL.md) - 使用 Raycast API 构建和维护 Raycast 扩展。
- [request-approval](https://github.com/openclaw/skills/tree/main/skills/yconst/request-approval/SKILL.md) - 使用 Preloop 的 request_approval 工具获得人工批准
- [rescuetime](https://github.com/openclaw/skills/tree/main/skills/rusynandriy/rescuetime/SKILL.md) - 从 RescueTime 获取生产力数据。
- [restart-guard](https://github.com/openclaw/skills/tree/main/skills/zjianru/restart-guard/SKILL.md) - 通过上下文保存安全地重新启动 OpenClaw Gateway
- [rssaurus](https://github.com/openclaw/skills/tree/main/skills/justinburdett/rssaurus/SKILL.md) - 使用 RSSaurus 命令行客户端（Go 二进制 `rssaurus`）
- [sag](https://github.com/openclaw/skills/tree/main/skills/steipete/sag/SKILL.md) - ElevenLabs 具有 mac 风格的文字转语音功能。
- [salesforce](https://github.com/openclaw/skills/tree/main/skills/arvorco/salesforce/SKILL.md) - 通过 Salesforce CLI (`sf`) 查询和管理 Salesforce CRM 数据。
- [salesforce-skill](https://github.com/openclaw/skills/tree/main/skills/lucas-riverbi/salesforce-skill/SKILL.md) - 主要技能定义与 frontmatter、CLI
- [shared-molt](https://github.com/openclaw/skills/tree/main/skills/tankcdr) - 分享和发现代理配方（外壳）。
- [shell-scripting](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/shell-scripting/SKILL.md) - 编写健壮、可移植的 shell 脚本。
- [shellmates](https://github.com/openclaw/skills/tree/main/skills/zcor) - ````
- [shellphone-gateway](https://github.com/openclaw/skills/tree/main/skills/loserbcc/shellphone-gateway/SKILL.md) - 用于连接 iOS 的私有 WebSocket 网关
- [shorten](https://github.com/openclaw/skills/tree/main/skills/kesslerio/shorten/SKILL.md) - 使用 is.gd 缩短 URL（无需身份验证）。
- [simple-backup](https://github.com/openclaw/skills/tree/main/skills/vacinc/simple-backup/SKILL.md) - 将代理大脑（工作空间）和身体（状态）备份到本地文件夹
- [smalltalk](https://github.com/openclaw/skills/tree/main/skills/johnmci/smalltalk/SKILL.md) - 与实时 Smalltalk 图像（Cuis 或 Squeak）进行交互。
- [sogcli](https://github.com/openclaw/skills/tree/main/skills/visionik/sogcli/SKILL.md) - 标准操作小工具 — CLI。
- [songsee](https://github.com/openclaw/skills/tree/main/skills/steipete/songsee/SKILL.md) - 从音频生成频谱图和功能面板可视化
- [staratheris-arya-reminders](https://github.com/openclaw/skills/tree/main/skills/staratheris/staratheris-arya-reminders/SKILL.md) - 自然语言录音室
- [startclaw-optimizer](https://github.com/openclaw/skills/tree/main/skills/idanmann10/startclaw-optimizer/SKILL.md) - OpenClaw 优化器是一个全面的
- [stdio-skill](https://github.com/openclaw/skills/tree/main/skills/safatinaztepe/stdio-skill/SKILL.md) - Stdin/stdout 文件收件箱/发件箱桥，用于将文件传递到/从
- [story-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/story-cog/SKILL.md) - 由 CellCog 提供支持的创意写作和讲故事。
- [system-info](https://github.com/openclaw/skills/tree/main/skills/xejrax/system-info/SKILL.md) - 快速系统诊断：CPU、内存、磁盘、正常运行时间。
- [tardis](https://github.com/openclaw/skills/tree/main/skills/rm289/tardis/SKILL.md) - 通过防篡改锁定跟踪从设定的纪元起经过的时间。
- [terminal-screenshots](https://github.com/openclaw/skills/tree/main/skills/ricardodantas/terminal-screenshots/SKILL.md) - 生成终端截图和动画
- [terminal-ui-website-design](https://github.com/openclaw/skills/tree/main/skills/chyinan/terminal-ui-website-design/SKILL.md) - 创建受终端启发的 UI 界面
- [tldr](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/tldr/SKILL.md) - 来自 tldr-pages 的简化手册页。
- [tmux](https://github.com/openclaw/skills/tree/main/skills/steipete/tmux/SKILL.md) - 通过发送击键来远程控制交互式 CLI 的 tmux 会话
- [track17](https://github.com/openclaw/skills/tree/main/skills/tristanmanchester/track17/SKILL.md) - 通过 17TRACK API 追踪包裹
- [trmnl-display](https://github.com/openclaw/skills/tree/main/skills/peetzweg/trmnl-display/SKILL.md) - 通过 webhook 将消息发送到终端电子墨水显示设备。
- [typhoon-starknet-account](https://github.com/openclaw/skills/tree/main/skills/esdras-sena/typhoon-starknet-account/SKILL.md) - 为您的代理创建 Starknet 帐户
- [units](https://github.com/openclaw/skills/tree/main/skills/asleep123/units/SKILL.md) - 使用 GNU 单位执行单位转换和计算。
- [unzipped-skill](https://github.com/openclaw/skills/tree/main/skills/jozh-bit/unzipped-skill/SKILL.md) - 自主创建 Farcaster 帐户并进行后期投射。
- [voicenotes](https://github.com/openclaw/skills/tree/main/skills/shawnhansen/voicenotes/SKILL.md) - 从 Voicenotes.com 同步和访问语音笔记。
- [wps-punchclock](https://github.com/openclaw/skills/tree/main/skills/dxh141130/wps-punchclock/SKILL.md) - 在 WPS Time / NetTime 上自动打卡时间输入/输出
- [wreckit-skill](https://github.com/openclaw/skills/tree/main/skills/jmanhype/wreckit-skill/SKILL.md) - 首先阅读 [SETUP.md](./SETUP.md) 安装 Wreckit CLI
- [x-kindle](https://github.com/openclaw/skills/tree/main/skills/brianlu365ai/x-kindle/SKILL.md) - 将 X/Twitter 帖子发送到 Kindle 进行无干扰阅读。
- [ytm-cast](https://github.com/openclaw/skills/tree/main/skills/aidanthebandit/ytm-cast/SKILL.md) - 从 YouTube/YouTube Music 下载音乐并流式传输到 Chromecast

</details>

<details>
<summary><h3 style="display:inline" id="marketing--sales">市场营销与销售</h3></summary>

- [4chan-reader](https://github.com/openclaw/skills/tree/main/skills/aiasisbot61/4chan-reader/SKILL.md) - 浏览 4chan 版块并提取主题讨论
- [a2a-market](https://github.com/openclaw/skills/tree/main/skills/jamjamzxhy/a2a-market/SKILL.md) - A2A 市场的 AI 代理技能市场集成。
- [ab-test-setup](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/ab-test-setup/SKILL.md) - 当用户想要计划时
- [ad-ready](https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/ad-ready/SKILL.md) - 从产品 URL 生成专业的广告图像
- [ad-ready-pro](https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/ad-ready-pro/SKILL.md) - 从产品 URL 生成专业的广告图像
- [affiliate-master](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/affiliate-master/SKILL.md) - 全栈联盟营销自动化
- [affiliatematic](https://github.com/openclaw/skills/tree/main/skills/dowands/affiliatematic/SKILL.md) - 集成人工智能驱动的亚马逊联属产品推荐
- [apollo](https://github.com/openclaw/skills/tree/main/skills/jhumanj/apollo/SKILL.md) - 与 Apollo.io REST API 交互（人员/组织充实、搜索、列表）。
- [attribution-engine](https://github.com/openclaw/skills/tree/main/skills/otherpowers/attribution-engine/SKILL.md) - 帮助创作者明确信用合作者、工具
- [basecamp-cli](https://github.com/openclaw/skills/tree/main/skills/emredoganer/basecamp-cli/SKILL.md) - 管理 Basecamp（通过 bc3 API / 37signals Launchpad）项目
- [beads](https://github.com/openclaw/skills/tree/main/skills/rnijhara/beads/SKILL.md) - Git 支持的 AI 代理问题跟踪器。
- [bearblog](https://github.com/openclaw/skills/tree/main/skills/azade-c/bearblog/SKILL.md) - 在 Bear Blog (bearblog.dev) 上创建和管理博客文章。
- [bird](https://github.com/openclaw/skills/tree/main/skills/steipete/bird/SKILL.md) - X/Twitter CLI 用于通过 cookie 或 Sweetistics 阅读、搜索和发布。
- [blog-to-kindle](https://github.com/openclaw/skills/tree/main/skills/ainekomacx/blog-to-kindle/SKILL.md) - 抓取博客/论文网站并编译成 Kindle 友好型
- [blog-writer](https://github.com/openclaw/skills/tree/main/skills/tomstools11/blog-writer/SKILL.md) - 撰写博客文章、文章时应使用此技能
- [bluesky](https://github.com/openclaw/skills/tree/main/skills/jeffaf/bluesky/SKILL.md) - 完整的 Bluesky CLI：发帖、回复、点赞、转发、关注、屏蔽、静音、搜索。
- [brand-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/brand-cog/SKILL.md) - 其他工具制作徽标。
- [brand-guidelines](https://github.com/openclaw/skills/tree/main/skills/seanphan/brand-guidelines/SKILL.md) - 应用 Anthropic 的官方品牌颜色和版式
- [brevo](https://github.com/openclaw/skills/tree/main/skills/yujesyoga/brevo/SKILL.md) - Brevo（以前称为 Sendinblue）电子邮件营销 API，用于管理联系人、列表等。
- [bulletproof-memory](https://github.com/openclaw/skills/tree/main/skills/halthelobster) - 永远不会再失去上下文。
- [business-development](https://github.com/openclaw/skills/tree/main/skills/oyi77/business-development/SKILL.md) - 合作伙伴外展、市场研究、竞争对手
- [campaign-orchestrator](https://github.com/openclaw/skills/tree/main/skills/kesslerio/campaign-orchestrator/SKILL.md) - 多渠道后续活动策划者
- [catbox-upload](https://github.com/openclaw/skills/tree/main/skills/microck/catbox-upload/SKILL.md) - 将文件上传到catbox.moe（永久）或litterbox.catbox.moe
- [citedy-seo-agent](https://github.com/openclaw/skills/tree/main/skills/nttylock/citedy-seo-agent/SKILL.md) - 将您的 AI 代理连接到 Citedy 的 SEO 内容平台
- [listing-swarm](https://clawhub.ai/skills/listing-swarm) - 自动将AI产品提交到70多个目录。
- [clawdwork](https://github.com/openclaw/skills/tree/main/skills/felo-sparticle/clawdwork/SKILL.md) - 找工作、赚钱并与其他人工智能代理合作
- [clawexchange](https://github.com/openclaw/skills/tree/main/skills/tiborera/clawexchange/SKILL.md) - 代理商对代理商的市场。
- [cold-email](https://github.com/openclaw/skills/tree/main/skills/bluecraft-ai/cold-email/SKILL.md) - 使用人工智能生成超个性化的冷电子邮件序列。
- [competitor-alternatives](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/competitor-alternatives/SKILL.md) - 当用户想要
- [content-creator](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/content-creator/SKILL.md) - 创建一致的 SEO 优化营销内容
- [content-draft-generator](https://github.com/openclaw/skills/tree/main/skills/vincentchan/content-draft-generator/SKILL.md) - 基于生成新的内容草稿
- [content-ideas-generator](https://github.com/openclaw/skills/tree/main/skills/vincentchan/content-ideas-generator/SKILL.md) - 生成结构化的帖子大纲
- [copy-editing](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/copy-editing/SKILL.md) - 当用户想要编辑时，查看
- [copywriter](https://github.com/openclaw/skills/tree/main/skills/killerapp/copywriter/SKILL.md) - 撰写引人注目的用户体验文案、营销内容和产品信息。
- [copywriting](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/copywriting/SKILL.md) - 当用户想写的时候，就重写。
- [deepread](https://github.com/openclaw/skills/tree/main/skills/uday390/deepread/SKILL.md) - OCR 永远不会无声地失败。
- [dialpad](https://github.com/openclaw/skills/tree/main/skills/kesslerio/dialpad/SKILL.md) - 通过 Dialpad API 发送短信和拨打语音电话。
- [dm-outreach](https://github.com/openclaw/skills/tree/main/skills/visualdeptcreative/dm-outreach/SKILL.md) - 为合格的潜在客户起草 Instagram DM。
- [email-manager-lite](https://github.com/openclaw/skills/tree/main/skills/jorgermp/email-manager-lite/SKILL.md) - 支持 IMAP/SMTP 的轻量级电子邮件管理器
- [email-sequence](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/email-sequence/SKILL.md) - 当用户想要创建时
- [exchange-rates](https://github.com/openclaw/skills/tree/main/skills/mrinvincible29/exchange-rates/SKILL.md) - 获取任何货币对之间的实时汇率
- [feishu-doc-reader](https://github.com/openclaw/skills/tree/main/skills/snowshadow/feishu-doc-reader/SKILL.md) - 读取飞书文档并提取内容
- [feishu-sticker](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-sticker/SKILL.md) - 将图像作为原生飞书贴纸发送。
- [financial-market-analysis](https://github.com/openclaw/skills/tree/main/skills/seyhunak/financial-market-analysis/SKILL.md) - 精准财务洞察 - 分析
- [form-cro](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/form-cro/SKILL.md) - 当用户想要优化任何表单时
- [free-tool-strategy](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/free-tool-strategy/SKILL.md) - 当用户想要
- [fundraiseup](https://github.com/openclaw/skills/tree/main/skills/aamish99/fundraiseup/SKILL.md) - 与 FundraiseUp REST API 交互以管理经常性捐款
- [ga4](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/ga4/SKILL.md) - 通过 Analytics Data API 查询 Google Analytics 4 (GA4) 数据。
- [gong](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/gong/SKILL.md) - 用于搜索通话、文字记录的Gong API。
- [google-ads](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/google-ads/SKILL.md) - 查询、审核和优化 Google Ads 广告系列。
- [google-photos](https://github.com/openclaw/skills/tree/main/skills/jorgermp/google-photos/SKILL.md) - 管理 Google 照片库。
- [gsc](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/gsc/SKILL.md) - 查询 Google Search Console 的 SEO 数据 - 搜索查询、首页、点击率。
- [gtm](https://github.com/Prospeda/gtm-skills/tree/main/openclaw-skills/gtm/SKILL.md) - 完整的 GTM 工具包。
- [gumroad-admin](https://github.com/openclaw/skills/tree/main/skills/abakermi/gumroad-admin/SKILL.md) - Gumroad 管理 CLI。
- [hubspot](https://github.com/openclaw/skills/tree/main/skills/kwall1/hubspot/SKILL.md) - HubSpot CRM 和 CMS API 集成，适用于联系人、公司、交易、所有者
- [humanizer](https://github.com/openclaw/skills/tree/main/skills/biostartechnology/humanizer/SKILL.md) - |。
- [landing-page-generator](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/landing-page-generator/SKILL.md) - 生成高转化率的登陆页面
- [late-api](https://github.com/openclaw/skills/tree/main/skills/mikipalet/late-api/SKILL.md) - 用于在 13 个社交媒体上安排帖子的官方 Late API 参考。
- [lead-gen-website](https://github.com/openclaw/skills/tree/main/skills/lucasgulino/lead-gen-website/SKILL.md) - 通过 SEO 构建完整的本地潜在客户开发网站
- [localrank-agent-skills](https://github.com/openclaw/skills/tree/main/skills/peterw/localrank-agent-skills/SKILL.md) - 跟踪本地排名、运行 SEO 审核并管理
- [marketing-demand-acquisition](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/marketing-demand-acquisition/SKILL.md) - 多渠道需求
- [marketing-mode](https://github.com/openclaw/skills/tree/main/skills/thesethrose/marketing-mode/SKILL.md) - 营销模式融合23项综合营销技巧
- [marketing-psychology](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/marketing-psychology/SKILL.md) - 当用户想要
- [marketing-skills](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/SKILL.md) - TL;DR：23 本营销手册
- [meta-ad-creatives](https://github.com/openclaw/skills/tree/main/skills/fortytwode/meta-ad-creatives/SKILL.md) - 跟踪元 (Facebook/Instagram) 广告创意
- [meta-ads](https://github.com/openclaw/skills/tree/main/skills/zachgodsell93) - 与 Meta (Facebook) 广告 API 完全读/写集成以进行管理。
- [modular-market-brief](https://github.com/openclaw/skills/tree/main/skills/boilerrat/modular-market-brief/SKILL.md) - 生成模块化、有数据支持的市场报告
- [molthunt](https://github.com/openclaw/skills/tree/main/skills/limone-eth/molthunt/SKILL.md) - 代理构建项目的启动板。
- [molts-list](https://github.com/openclaw/skills/tree/main/skills/jononovo) - 使用虚拟的交易服务、工具和任务的代理市场
- [moltywork](https://github.com/openclaw/skills/tree/main/skills/anandvc) - 人工智能代理寻找工作和赚钱的市场。
- [moltywork-1-0-0](https://github.com/openclaw/skills/tree/main/skills/renixaus) - 人工智能代理寻找工作和赚钱的市场。
- [nesp-hype-engine](https://github.com/openclaw/skills/tree/main/skills/willywonkale/nesp-hype-engine/SKILL.md) - 这项技能使代理能够推动增长
- [netpad](https://github.com/openclaw/skills/tree/main/skills/mrlynn/netpad/SKILL.md) - 管理 NetPad 表单、提交内容、用户。
- [newsletter-generator](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/newsletter-generator/SKILL.md) - 生成自动电子邮件通讯
- [norway-roads](https://github.com/openclaw/skills/tree/main/skills/geoffreycasaubon/norway-roads/SKILL.md) - 查询实时路况、封闭情况、交通情况
- [notebooklm](https://github.com/openclaw/skills/tree/main/skills/seanphan/notebooklm/SKILL.md) - 使用此技能通过 Google NotebookLM 的 AI 分析您的本地文件。
- [octolens](https://github.com/openclaw/skills/tree/main/skills/garrrikkotua/octolens/SKILL.md) - 从 Octolens API 查询和分析品牌提及。
- [onlyfans-api](https://github.com/openclaw/skills/tree/main/skills/martingalovic/onlyfans-api/SKILL.md) - 通过 OnlyFansAPI.com 查询 OnlyFans 数据和分析
- [openbroker](https://github.com/openclaw/skills/tree/main/skills/ya7ya/openbroker/SKILL.md) - 超流动性交易工具包。
- [orionads](https://github.com/openclaw/skills/tree/main/skills/celsojr2013/orionads/SKILL.md) - 通过 Orion Ad 搜索 AI 工具、API 和代理资源
- [overleaf](https://github.com/openclaw/skills/tree/main/skills/easonc13/overleaf/SKILL.md) - 通过 CLI 访问 Overleaf 项目。
- [package-seo](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/package-seo/SKILL.md) - npm 包、GitHub 存储库和 AI 的 SEO 最佳实践
- [pakat](https://github.com/openclaw/skills/tree/main/skills/hadifarnoud/pakat/SKILL.md) - 与 Pakat 电子邮件营销 API (new.pakat.net) 互动。
- [paywall-upgrade-cro](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/paywall-upgrade-cro/SKILL.md) - 当用户想要
- [personal-branding-authority](https://github.com/openclaw/skills/tree/main/skills/shashwatgtm/personal-branding-authority/SKILL.md) - 创始人与员工个人
- [personal-crm](https://github.com/openclaw/skills/tree/main/skills/matthewpoe/personal-crm/SKILL.md) - 帮助您保持联系的个人关系经理
- [pinch-to-post](https://github.com/openclaw/skills/tree/main/skills/nickhamze/pinch-to-post/SKILL.md) - Clawdbot 的 WordPress 自动化。
- [ping-beads](https://github.com/openclaw/skills/tree/main/skills/xejrax/ping-beads/SKILL.md) - 验证 bead 守护进程是否处于活动状态并且有响应
- [pipedrive](https://github.com/openclaw/skills/tree/main/skills/rdewolff/pipedrive/SKILL.md) - Pipedrive CRM API 用于管理交易、联系人（人员）、组织等。
- [pm-odds](https://github.com/openclaw/skills/tree/main/skills/dannyshmueli/pm-odds/SKILL.md) - 查询 Polymarket 预测市场。
- [polt-user](https://github.com/openclaw/skills/tree/main/skills/playdadev/polt-user/SKILL.md) - 连接到 POLT - 代理商的社交模因币启动板。
- [polyedge](https://github.com/openclaw/skills/tree/main/skills/sbaker5/polyedge/SKILL.md) - Polymarket 的 x402 交易信号 API - 检测错误定价的相关性
- [polymarket](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/polymarket/SKILL.md) - 查询 Polymarket 预测市场 - 检查赔率、趋势市场
- [popup-cro](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/popup-cro/SKILL.md) - 当用户想要创建或优化时
- [prediction-markets-roarin](https://github.com/openclaw/skills/tree/main/skills/hosnik/prediction-markets-roarin/SKILL.md) - 参与Roarin AI预测
- [pricing-strategy](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/pricing-strategy/SKILL.md) - 当用户需要帮助时
- [programmatic-seo](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/programmatic-seo/SKILL.md) - 当用户想要
- [pvpc-spain](https://github.com/openclaw/skills/tree/main/skills/didelco/pvpc-spain/SKILL.md) - 西班牙 PVPC 电力优化咨询和优化
- [qlik](https://github.com/openclaw/skills/tree/main/skills/fianabates1/qlik/SKILL.md) - 与 37 种工具完成 Qlik Cloud 分析平台集成。
- [ralph-loops](https://github.com/openclaw/skills/tree/main/skills/qlifebot-coder/ralph-loops/SKILL.md) - 首先阅读[SETUP.md](./SETUP.md)安装依赖项
- [recruitment-automation](https://github.com/openclaw/skills/tree/main/skills/seyhunak/recruitment-automation/SKILL.md) - 零麻烦精心设计的招聘自动化
- [reddit](https://github.com/openclaw/skills/tree/main/skills/theglove44/reddit/SKILL.md) - 浏览、搜索、发布。
- [reddit-search](https://github.com/openclaw/skills/tree/main/skills/thesethrose/reddit-search/SKILL.md) - 在 Reddit 中搜索子 Reddit 并获取信息。
- [referral-program](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/referral-program/SKILL.md) - 当用户想要
- [sales-toolkit](https://github.com/openclaw/skills/tree/main/skills/andrewdmwalker) - 销售工具包：Apollo.io 丰富、Attio CRM、...
- [salesforce-dx](https://github.com/openclaw/skills/tree/main/skills/rjmcgirr-pl/salesforce-dx/SKILL.md) - 查询 Salesforce 数据并管理销售渠道
- [schema-markup](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/schema-markup/SKILL.md) - 当用户想要添加时，修复
- [seo-article-gen](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/seo-article-gen/SKILL.md) - SEO 优化的文章生成器，具有自动功能
- [seo-autopilot](https://github.com/openclaw/skills/tree/main/skills/adamhjort/seo-autopilot/SKILL.md) - 为 boll-koll.se 或 hyresbyte.se 运行本地 SEO 自动驾驶仪
- [seo-competitor-analysis](https://github.com/openclaw/skills/tree/main/skills/qqyule/seo-competitor-analysis/SKILL.md) - 进行深入的 SEO 竞争对手分析
- [seo-optimizer-pro](https://github.com/openclaw/skills/tree/main/skills/vedantsingh60/seo-optimizer-pro/SKILL.md) - AI 支持的 SEO 和 AEO 内容优化
- [seoul-metro](https://github.com/openclaw/skills/tree/main/skills/dukbong) - 首尔地铁实时到达、路线规划助手
- [seoul-subway](https://github.com/openclaw/skills/tree/main/skills/dukbong/seoul-subway/SKILL.md) - 首尔地铁实时到达、路线规划助手
- [shashwatgtm-skills](https://github.com/openclaw/skills/tree/main/skills/shashwatgtm) - B2B 营销：竞争情报、内容...
- [shopify-marketing-expert](https://github.com/openclaw/skills/tree/main/skills/metehan777/shopify-marketing-expert/SKILL.md) - 全面的人工智能端到端技能
- [signup-flow-cro](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/signup-flow-cro/SKILL.md) - 当用户想要
- [social-media-analyzer](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/social-media-analyzer/SKILL.md) - 社交媒体活动分析
- [solobuddy](https://github.com/openclaw/skills/tree/main/skills/humanji7/solobuddy/SKILL.md) - 独立黑客的内置公共伴侣——内容工作流程、Twitter。
- [spaces-listener](https://github.com/openclaw/skills/tree/main/skills/jamesalmeida/spaces-listener/SKILL.md) - 记录、转录和总结 X/Twitter 空间
- [sphero-mini](https://github.com/openclaw/skills/tree/main/skills/joneschi/sphero-mini/SKILL.md) - 通过低功耗蓝牙控制 Sphero Mini 机器人球。
- [stegstr](https://github.com/openclaw/skills/tree/main/skills/brunkstr/stegstr/SKILL.md) - 解码 Stegstr 有效负载并将其嵌入 PNG 图像中。
- [supalytics](https://github.com/openclaw/skills/tree/main/skills/yogesharc/supalytics/SKILL.md) - 使用 Supalytics CLI 查询 Web 分析数据。
- [swipe-file-generator](https://github.com/openclaw/skills/tree/main/skills/vincentchan/swipe-file-generator/SKILL.md) - 分析来自 URL 的高性能内容
- [throwly-mcp](https://github.com/openclaw/skills/tree/main/skills/kelvis24/throwly-mcp/SKILL.md) - 用于买卖物品的人工智能代理市场。
- [tools-marketplace](https://github.com/openclaw/skills/tree/main/skills/preston-thiele/tools-marketplace/SKILL.md) - 使用 Danube 的 100 多个 API 工具
- [tweet-ideas-generator](https://github.com/openclaw/skills/tree/main/skills/vincentchan/tweet-ideas-generator/SKILL.md) - 生成 60 个高影响力的推文创意
- [twenty-crm](https://github.com/openclaw/skills/tree/main/skills/jhumanj/twenty-crm/SKILL.md) - 与 Twenty CRM（自托管）交互。
- [typefully](https://github.com/openclaw/skills/tree/main/skills/thesethrose/typefully/SKILL.md) - |。
- [vodoo](https://github.com/openclaw/skills/tree/main/skills/julian-r/vodoo/SKILL.md) - 查询和管理 Odoo ERP 数据
- [weread](https://github.com/openclaw/skills/tree/main/skills/z233/weread/SKILL.md) - 微信读书 CLI 工具，用于获取笔记和亮点。
- [x-algorithm](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/x-algorithm/SKILL.md) - X（Twitter）算法规则、病毒策略和文章
- [x-article-editor](https://github.com/openclaw/skills/tree/main/skills/jchopard69/x-article-editor/SKILL.md) - TL;DR：将主题或草稿变成高参与度的 X
- [x-timeline-digest](https://github.com/openclaw/skills/tree/main/skills/seandong/x-timeline-digest/SKILL.md) - 为您构建来自 X (Twitter) 的重复数据删除摘要
- [yc-cold-outreach](https://github.com/openclaw/skills/tree/main/skills/pors/yc-cold-outreach/SKILL.md) - Y Combinator (YC) 冷电子邮件推广技术专家
- [youtrack-digisal](https://github.com/openclaw/skills/tree/main/skills/digisal/youtrack-digisal/SKILL.md) - 通过 REST 与 YouTrack 项目管理系统交互
- [yt-dlp-downloader-skill](https://github.com/openclaw/skills/tree/main/skills/apollo1234/yt-dlp-downloader-skill/SKILL.md) - 从 YouTube、Bilibili 下载视频
- [zoho](https://github.com/openclaw/skills/tree/main/skills/shreefentsar/zoho/SKILL.md) - 与 Zoho CRM、项目交互。

</details>

<details>
<summary><h3 style="display:inline" id="productivity--tasks">生产力与任务管理</h3></summary>

- [4todo](https://github.com/openclaw/skills/tree/main/skills/blackstorm/4todo/SKILL.md) - 通过聊天管理 4todo (4to.do)。
- [actual-budget](https://github.com/openclaw/skills/tree/main/skills/thisisjeron/actual-budget/SKILL.md) - 通过官方Actual查询和管理个人财务
- [adhd-daily-planner](https://github.com/openclaw/skills/tree/main/skills/mikecourt/adhd-daily-planner/SKILL.md) - 无时间限制的友好规划、执行功能
- [agent-chronicle](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/agent-chronicle/SKILL.md) - 人工智能驱动的代理日记生成——创造财富
- [agent-protocol](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/agent-protocol/SKILL.md) - 代理到代理的通信协议。
- [agent-task-manager](https://github.com/openclaw/skills/tree/main/skills/dobbybud/agent-task-manager/SKILL.md) - 管理和编排多步骤、有状态代理
- [ai-daily-briefing](https://github.com/openclaw/skills/tree/main/skills/jeffjhunter/ai-daily-briefing/SKILL.md) - 开始每一天的专注。
- [airweave](https://github.com/openclaw/skills/tree/main/skills/lennertjansen/airweave/SKILL.md) - 跨用户应用程序的 AI 代理的上下文检索层。
- [arya-reminders](https://github.com/openclaw/skills/tree/main/skills/staratheris/arya-reminders/SKILL.md) - Recordatorios en lenguaje natural（波哥大）。
- [asana](https://github.com/openclaw/skills/tree/main/skills/k0nkupa/asana/SKILL.md) - 通过 Asana REST API 将 Asana 与 Clawdbot 集成。
- [asc-release-flow](https://github.com/openclaw/skills/tree/main/skills/rudrankriyam/asc-release-flow/SKILL.md) - TestFlight 和 App 的端到端发布工作流程
- [async-task](https://github.com/openclaw/skills/tree/main/skills/enderfga/async-task/SKILL.md) - 执行长时间运行的任务，没有 HTTP 超时。
- [atlassian-mcp](https://github.com/openclaw/skills/tree/main/skills/atakanermis/atlassian-mcp/SKILL.md) - 运行模型上下文协议 (MCP) Atlassian 服务器
- [audiopod](https://github.com/openclaw/skills/tree/main/skills/rakesh1002/audiopod/SKILL.md) - 使用 AudioPod AI 的 API 执行包括 AI 音乐在内的音频处理任务
- [aussie-mortgage-calc](https://github.com/openclaw/skills/tree/main/skills/tianshizhimao-sudo/aussie-mortgage-calc/SKILL.md) - 澳大利亚抵押贷款计算器 — LVR
- [autonomous-feature-planner](https://github.com/openclaw/skills/tree/main/skills/vishnubedi3/autonomous-feature-planner/SKILL.md) - 自主计划和指定
- [basal-ganglia-memory](https://github.com/openclaw/skills/tree/main/skills/impkind/basal-ganglia-memory/SKILL.md) - 人工智能的习惯形成和程序学习
- [blossom-hire](https://github.com/openclaw/skills/tree/main/skills/robbiwu/blossom-hire/SKILL.md) - 在 Blossom 发布工作、任务或带薪轮班以聘请当地帮助，然后
- [brainz-tasks](https://github.com/openclaw/skills/tree/main/skills/xejrax/brainz-tasks/SKILL.md) - 使用“todoist”CLI 管理 Todoist 任务。
- [build-discipline](https://github.com/openclaw/skills/tree/main/skills/jhillin8/build-discipline/SKILL.md) - 通过习惯叠加、连胜建立牢不可破的纪律
- [capacities](https://github.com/openclaw/skills/tree/main/skills/davidsmorais/capacities/SKILL.md) - 管理容量注释、每日条目和网络链接。
- [card-optimizer](https://github.com/openclaw/skills/tree/main/skills/scottfo/card-optimizer/SKILL.md) - 信用卡奖励优化器——帮助最大化现金返还
- [clankdin](https://github.com/openclaw/skills/tree/main/skills/redeemthedream/clankdin/SKILL.md) - 人工智能代理的专业网络。
- [claw-conductor](https://github.com/openclaw/skills/tree/main/skills/johnsonfarmsus/claw-conductor/SKILL.md) - 始终在线的自主开发协调器
- [claw-daily](https://github.com/openclaw/skills/tree/main/skills/yanibu2777/claw-daily/SKILL.md) - 在 Claw Daily 上竞争 — 注册、解决今天的挑战、提交
- [clawd-docs-v2](https://github.com/openclaw/skills/tree/main/skills/aranej/clawd-docs-v2/SKILL.md) - 通过本地搜索索引访问智能 ClawdBot 文档
- [clawdaily](https://github.com/openclaw/skills/tree/main/skills/yanibu2777/clawdaily/SKILL.md) - 在 Claw Daily 上竞争 — 注册、解决今天的挑战、提交
- [clawgatesecure](https://github.com/openclaw/skills/tree/main/skills/thestormshadow/clawgatesecure/SKILL.md) - LLM 代理聚焦的高级安全协议
- [clickup-mcp](https://github.com/openclaw/skills/tree/main/skills/pvoo/clickup-mcp/SKILL.md) - 管理 ClickUp 任务、文档、时间跟踪、评论、聊天和搜索
- [clickup-skill](https://github.com/openclaw/skills/tree/main/skills/d3layd/clickup-skill/SKILL.md) - 企业级 ClickUp 项目管理集成
- [code-task-generator](https://github.com/openclaw/skills/tree/main/skills/paulpete/code-task-generator/SKILL.md) - 生成结构化 .code-task.md 文件
- [comanda](https://github.com/openclaw/skills/tree/main/skills/kris-hansen/comanda/SKILL.md) - 生成、可视化和执行声明式 AI 管道
- [confirm-form](https://github.com/openclaw/skills/tree/main/skills/xiaozhuang0127/confirm-form/SKILL.md) - 生成结构化确认表格以收集用户
- [content-writing-thought-leadership](https://github.com/openclaw/skills/tree/main/skills/shashwatgtm/content-writing-thought-leadership/SKILL.md) - B2B内容写作
- [daily-briefing](https://github.com/openclaw/skills/tree/main/skills/antgly/daily-briefing/SKILL.md) - 生成包含天气、日历的温馨、紧凑的每日简报
- [daily-digest](https://github.com/openclaw/skills/tree/main/skills/pmaeter/daily-digest/SKILL.md) - 目的：根据记忆和互动生成每日摘要
- [daily-stoic](https://github.com/openclaw/skills/tree/main/skills/fcavalcantirj/daily-stoic/SKILL.md) - 发送来自“每日斯多葛派”的每日斯多葛哲学名言
- [dailyhuman](https://github.com/openclaw/skills/tree/main/skills/bschippers718/dailyhuman/SKILL.md) - **碳含量。硅评论。**
- [dex](https://github.com/openclaw/skills/tree/main/skills/gricha/dex/SKILL.md) - 任务跟踪。
- [dexcom](https://github.com/openclaw/skills/tree/main/skills/chris-clem/dexcom/SKILL.md) - 通过 Dexcom G7/G6 监测血糖。
- [dvsa-tc-audit-readiness-operator-licence-uk](https://github.com/openclaw/skills/tree/main/skills/kowl64/dvsa-tc-audit-readiness-operator-licence-uk/SKILL.md) - 构建 DVSA/流量
- [elevenlabs-phone-reminder-lite](https://github.com/openclaw/skills/tree/main/skills/daaab/elevenlabs-phone-reminder-lite/SKILL.md) - 构建 AI 来电提醒
- [featurebase](https://github.com/openclaw/skills/tree/main/skills/rdewolff/featurebase/SKILL.md) - 用于客户反馈、功能请求、变更日志的功能库 API
- [feishu-task](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 管理飞书任务。
- [file-organizer](https://github.com/openclaw/skills/tree/main/skills/lkz4203/file-organizer/SKILL.md) - 通过移动自动整理指定目录下的文件
- [flow](https://github.com/openclaw/skills/tree/main/skills/bvinci1-design/flow/SKILL.md) - 编译自然语言请求的智能技能编排器
- [flowmind](https://github.com/openclaw/skills/tree/main/skills/fancygobot/flowmind/SKILL.md) - 使用 FlowMind 管理生产力 — 目标、任务（带有子任务）、注释。
- [focus-deep-work](https://github.com/openclaw/skills/tree/main/skills/jhillin8/focus-deep-work/SKILL.md) - 通过专注会议、分心记录最大化深度工作
- [gmail-manager](https://github.com/openclaw/skills/tree/main/skills/pepperbotts/gmail-manager/SKILL.md) - 来自 Rube 的专家 Gmail 管理助手。
- [gno](https://github.com/openclaw/skills/tree/main/skills/gmickel/gno/SKILL.md) - 搜索本地文档、文件、笔记。
- [gogcli](https://github.com/openclaw/skills/tree/main/skills/luccast/gogcli/SKILL.md) - 描述：适用于 Gmail、日历、云端硬盘、表格、文档的 Google Workspace CLI。
- [google-sheet](https://github.com/openclaw/skills/tree/main/skills/longmaba/google-sheet/SKILL.md) - 通过 Google 读取、写入、附加和管理 Google 表格
- [grab](https://github.com/openclaw/skills/tree/main/skills/jamesalmeida/grab/SKILL.md) - 从 URL（推文、X 文章、Reddit、YouTube）下载并存档内容。
- [gratitude-journal](https://github.com/openclaw/skills/tree/main/skills/jhillin8/gratitude-journal/SKILL.md) - 通过每日记录、连续记录建立感恩练习
- [habit-flow-skill](https://github.com/openclaw/skills/tree/main/skills/tralves/habit-flow-skill/SKILL.md) - 采用自然语言的人工智能驱动的原子习惯追踪器
- [habit-tracker](https://github.com/openclaw/skills/tree/main/skills/jhillin8/habit-tracker/SKILL.md) - 通过条纹、提醒和进度可视化养成习惯。
- [healthy-eating](https://github.com/openclaw/skills/tree/main/skills/jhillin8/healthy-eating/SKILL.md) - 通过膳食记录和营养培养健康的饮食习惯
- [imap-email](https://github.com/openclaw/skills/tree/main/skills/mvarrieur/imap-email/SKILL.md) - 通过 IMAP（ProtonMail Bridge、Gmail 等）阅读和管理电子邮件。
- [jira](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/jira/SKILL.md) - 通过 jira-cli 管理 Jira 问题、看板、冲刺和项目。
- [kanbanflow-skill](https://github.com/openclaw/skills/tree/main/skills/abakermi/kanbanflow-skill/SKILL.md) - <名称>看板流</名称>
- [libby-book-monitor](https://github.com/openclaw/skills/tree/main/skills/alexpolonsky/libby-book-monitor/SKILL.md) - 跟踪 Libby/OverDrive 图书馆的图书可用性。
- [linear](https://github.com/openclaw/skills/tree/main/skills/manuelhettich/linear/SKILL.md) - 查询和管理线性问题、项目。
- [linear-issues](https://github.com/openclaw/skills/tree/main/skills/emrekilinc/linear-issues/SKILL.md) - 与 Linear 交互以进行问题跟踪。
- [locu](https://github.com/openclaw/skills/tree/main/skills/davidsmorais/locu/SKILL.md) - 通过 Locu 的公共 API 管理任务和项目。
- [mac-reminders-agent](https://github.com/openclaw/skills/tree/main/skills/swancho/mac-reminders-agent/SKILL.md) - 与 macOS 提醒应用程序集成以进行检查
- [makeovern](https://github.com/openclaw/skills/tree/main/skills/abeljseba/makeovern/SKILL.md) - 当用户想要运行定时焦点会话时使用此技能
- [mastodon-scout](https://github.com/openclaw/skills/tree/main/skills/patelhiren/mastodon-scout/SKILL.md) - 只读乳齿象。
- [microsoft-todo](https://github.com/openclaw/skills/tree/main/skills/underwear/microsoft-todo/SKILL.md) - 通过“todo”CLI 管理 Microsoft To Do 任务。
- [minibook](https://github.com/openclaw/skills/tree/main/skills/dioxia/minibook/SKILL.md) - 将您的代理连接到 Minibook 实例以进行项目协作。
- [mission-control](https://github.com/openclaw/skills/tree/main/skills/rdsthomas/mission-control/SKILL.md) - 适用于 AI 助手的看板式任务管理仪表板。
- [mlti-llm-fallback](https://github.com/openclaw/skills/tree/main/skills/leohan123123/mlti-llm-fallback/SKILL.md) - 多LLM智能切换。
- [mogcli](https://github.com/openclaw/skills/tree/main/skills/visionik/mogcli/SKILL.md) - Microsoft Ops Gadget — 适用于 Microsoft 365 的 CLI
- [moltcrew](https://github.com/openclaw/skills/tree/main/skills/montecrypto999/moltcrew/SKILL.md) - 人工智能代理的社交网络。
- [morning-briefing](https://github.com/openclaw/skills/tree/main/skills/lucas-riverbi/morning-briefing/SKILL.md) - 描述：生成个性化晨报
- [morning-manifesto](https://github.com/openclaw/skills/tree/main/skills/marcbickel/morning-manifesto/SKILL.md) - 具有任务同步功能的每日晨间反思工作流程
- [no-nonsense-tasks](https://github.com/openclaw/skills/tree/main/skills/dvjn/no-nonsense-tasks/SKILL.md) - 使用 SQLite 的严肃任务管理器。
- [office-xyz](https://github.com/openclaw/skills/tree/main/skills/sunnyguoyuan/office-xyz/SKILL.md) - office.xyz — 人工智能代理的 2D 虚拟办公平台。
- [omnifocus](https://github.com/openclaw/skills/tree/main/skills/coyote-git/omnifocus-automation/SKILL.md) - 通过 Omni 管理 OmniFocus 任务、项目和文件夹
- [outlook](https://github.com/openclaw/skills/tree/main/skills/jotamed/outlook/SKILL.md) - 通过 Microsoft Graph API 阅读、搜索和管理 Outlook 电子邮件和日历。
- [pa-admin-exec](https://github.com/openclaw/skills/tree/main/skills/kowl64/pa-admin-exec/SKILL.md) - 生成 exec-support 输出
- [personal-analytics](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/personal-analytics/SKILL.md) - 分析对话模式、跟踪
- [pinchwork](https://github.com/openclaw/skills/tree/main/skills/anneschuth) - 将任务委派给其他代理。
- [pixiv-skill](https://github.com/openclaw/skills/tree/main/skills/matrix-meta/pixiv-skill/SKILL.md) - 访问 Pixiv 进行插图、漫画的搜索和观看
- [plan-executor](https://github.com/openclaw/skills/tree/main/skills/vishnubedi3/plan-executor/SKILL.md) - 执行由自主制定的冻结的、经过验证的计划
- [plan-my-day](https://github.com/openclaw/skills/tree/main/skills/itsflow/plan-my-day/SKILL.md) - 制定能量优化、时间限制的每日计划。
- [planka](https://github.com/openclaw/skills/tree/main/skills/voydz/planka/SKILL.md) - 管理 Planka（看板）项目、看板、列表、卡片和通知
- [planning-with-files](https://github.com/openclaw/skills/tree/main/skills/othmanadi/planning-with-files/SKILL.md) - 实施 Manus 风格的基于文件的规划
- [pocketsmith-skill](https://github.com/openclaw/skills/tree/main/skills/lextoumbourou/pocketsmith-skill/SKILL.md) - 管理 PocketSmith 交易、类别
- [pomodoro](https://github.com/openclaw/skills/tree/main/skills/snail3d/pomodoro/SKILL.md) - 一个漂亮的番茄计时器，具有任务跟踪功能。
- [prd](https://github.com/openclaw/skills/tree/main/skills/bjesuiter/prd/SKILL.md) - 创建和管理产品需求文档 (PRD)。
- [pre-mortem-analyst](https://github.com/openclaw/skills/tree/main/skills/artyomx33/pre-mortem-analyst/SKILL.md) - 想象一下项目已经失败了，然后继续工作
- [proactive-agent](https://github.com/openclaw/skills/tree/main/skills/halthelobster/proactive-agent/SKILL.md) - 将人工智能代理从任务追随者转变为主动者
- [project-management-guru-adhd](https://github.com/openclaw/skills/tree/main/skills/mikecourt/project-management-guru-adhd/SKILL.md) - ADHD 专家项目经理
- [project-manager](https://github.com/openclaw/skills/tree/main/skills/fr0ziii/project-manager/SKILL.md) - 管理内部项目系统采用 JSON。
- [prowlarr](https://github.com/openclaw/skills/tree/main/skills/jmagar/prowlarr/SKILL.md) - 搜索索引器并管理 Prowlar。
- [qmd](https://github.com/openclaw/skills/tree/main/skills/steipete/qmd/SKILL.md) - 具有 MCP 模式的本地搜索/索引 CLI（BM25 + 矢量 + 重新排名）。
- [reader-deep-dive](https://github.com/openclaw/skills/tree/main/skills/sameerbajaj/reader-deep-dive/SKILL.md) - 连接您最近阅读的每日简报
- [reminder](https://github.com/openclaw/skills/tree/main/skills/ryanhong666/reminder/SKILL.md) - 自然语言提醒秘书：捕获事件到git-synced
- [remindme](https://github.com/openclaw/skills/tree/main/skills/jacobthejacobs/remindme/SKILL.md) - ⏰ OpenClaw 的简单 Telegram 提醒。
- [samsung-smart-tv](https://github.com/openclaw/skills/tree/main/skills/regenrek/samsung-smartthings/SKILL.md) - 通过 SmartThings 控制三星电视
- [save-money](https://github.com/openclaw/skills/tree/main/skills/peterokase42/save-money/SKILL.md) - 自动检测 Claude 模型（Haiku + Sonnet）的任务复杂性。
- [skill-hexmem](https://github.com/openclaw/skills/tree/main/skills/santyr/skill-hexmem/SKILL.md) - 用于人工智能代理身份、任务、事件的结构化内存数据库
- [skylight-skill](https://github.com/openclaw/skills/tree/main/skills/riyadchowdhury/skylight-skill/SKILL.md) - 与 Skylight Calendar 框架交互 - 管理日历
- [social-media-management](https://github.com/openclaw/skills/tree/main/skills/shashwatgtm/social-media-management/SKILL.md) - B2B 内容写作与日常工作流程
- [swarm](https://github.com/openclaw/skills/tree/main/skills/chair4ce/swarm/SKILL.md) - 使用 Gemini Flash 工作线程执行并行任务。
- [tabussen](https://github.com/openclaw/skills/tree/main/skills/simskii/tabussen/SKILL.md) - 西博滕和于默奥公共交通旅行规划。
- [task](https://github.com/openclaw/skills/tree/main/skills/amirbrooks/task/SKILL.md) - Tasker 文档存储通过工具调度进行任务管理。
- [task-decomposer](https://github.com/openclaw/skills/tree/main/skills/10e9928a/task-decomposer/SKILL.md) - 将复杂的用户请求分解为可执行的子任务
- [task-tracker](https://github.com/openclaw/skills/tree/main/skills/kesslerio/task-tracker/SKILL.md) - 个人任务管理，包括每日站立和每周回顾。
- [taskleef](https://github.com/openclaw/skills/tree/main/skills/xatter/taskleef/SKILL.md) - Taskleef.com 待办事项、项目。
- [taskmaster](https://github.com/openclaw/skills/tree/main/skills/jlwrow/taskmaster/SKILL.md) - 项目经理和任务委派系统。
- [tasktrove](https://github.com/openclaw/skills/tree/main/skills/willwebberley/tasktrove/SKILL.md) - 通过 Tasktrove API 管理待办事项。
- [tensorpm](https://github.com/openclaw/skills/tree/main/skills/neo552/tensorpm/SKILL.md) - AI 支持的项目管理 - Notion 和 Jira 的替代方案
- [test1](https://github.com/openclaw/skills/tree/main/skills/chaunceyliu/test1/SKILL.md) - 通过 Trello REST API 管理 Trello 看板、列表和卡片。
- [tesy](https://github.com/openclaw/skills/tree/main/skills/kipasdinding6969-alt/tesy/SKILL.md) - 相关：[[代理]]，。
- [thecolony-heartbeat](https://github.com/openclaw/skills/tree/main/skills/jackparnell/thecolony-heartbeat/SKILL.md) - The Colony 的定期入住程序。
- [thecolony-heartbeat](https://github.com/openclaw/skills/tree/main/skills/jackparnell/thecolony-heartbeat/SKILL.md) - The Colony 的定期入住程序。
- [things-mac](https://github.com/openclaw/skills/tree/main/skills/steipete/things-mac/SKILL.md) - 在 macOS 上通过“things” CLI 管理 Things 3
- [ticktick](https://github.com/openclaw/skills/tree/main/skills/manuelhettich/ticktick/SKILL.md) - 使用 OAuth2 从命令行管理 TickTick 任务和项目
- [timesheet](https://github.com/openclaw/skills/tree/main/skills/florianrauscha/timesheet/SKILL.md) - 使用 timesheet.io CLI 跟踪时间、管理项目和任务。
- [todo-management](https://github.com/openclaw/skills/tree/main/skills/lstpsche/todo-management/SKILL.md) - 每个工作区的 SQLite todo 管理器 (./todo.db) 和组
- [todo-management-1-1-2](https://github.com/openclaw/skills/tree/main/skills/lucky-2968/todo-management-1-1-2/SKILL.md) - 每个工作空间的 SQLite todo 管理器 (./todo.db)
- [todo-skill](https://github.com/openclaw/skills/tree/main/skills/scccmsd/todo-skill/SKILL.md) - 将大任务分解为更小的可操作步骤并优化的技能
- [todo-tracker](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/todo-tracker/SKILL.md) - 用于跨会话跟踪任务的持久 TODO 便签本。
- [todoist](https://github.com/openclaw/skills/tree/main/skills/mjrussell/todoist/SKILL.md) - 在Todoist中管理任务和项目。
- [toggl](https://github.com/openclaw/skills/tree/main/skills/clvrobj/toggl/SKILL.md) - 通过 toggl 使用 Toggl 跟踪时间。
- [topydo](https://github.com/openclaw/skills/tree/main/skills/bastos/topydo/SKILL.md) - 使用 topydo 管理 todo.txt 任务。
- [trello](https://github.com/openclaw/skills/tree/main/skills/steipete/trello/SKILL.md) - 通过 Trello REST API 管理 Trello 看板、列表和卡片。
- [value-tracker](https://github.com/openclaw/skills/tree/main/skills/sergirostoll-coder/value-tracker/SKILL.md) - 跟踪和量化您的人工智能助手的价值
- [vikunja-fast](https://github.com/openclaw/skills/tree/main/skills/tmigone/vikunja-fast/SKILL.md) - 管理 Vikunja 项目和任务（逾期/到期/今天），标记为完成
- [web-perf](https://github.com/openclaw/skills/tree/main/skills/elithrar/web-perf/SKILL.md) - 使用 Chrome DevTools 分析 Web 性能。
- [withings-health](https://github.com/openclaw/skills/tree/main/skills/hisxo/withings-health/SKILL.md) - 从 Withings API 获取健康数据，包括体重

</details>

<details>
<summary><h3 style="display:inline" id="ai--llms">AI 与大语言模型</h3></summary>

- [4claw](https://github.com/openclaw/skills/tree/main/skills/mfergpt/4claw/SKILL.md) - 4claw——人工智能代理的审核图像板。
- [a2a](https://github.com/openclaw/skills/tree/main/skills/gstdcoin) - 去中心化的代理对代理自治经济。
- [aap-passport](https://github.com/openclaw/skills/tree/main/skills/ira-hash/aap-passport/SKILL.md) - 代理证明协议 - 反向图灵测试。
- [adaptive-suite](https://github.com/openclaw/skills/tree/main/skills/afajohn/adaptive-suite/SKILL.md) - 为 Clawdbot 提供支持的持续自适应技能套件
- [adversarial-prompting](https://github.com/openclaw/skills/tree/main/skills/abe238/adversarial-prompting/SKILL.md) - 对抗性分析来批评、修复。
- [ag-model-usage](https://github.com/openclaw/skills/tree/main/skills/ls18166407597-design/ag-model-usage/SKILL.md) - 使用 CodexBar CLI 本地成本使用情况进行总结
- [agent-arcade](https://github.com/openclaw/skills/tree/main/skills/shawnlewis/agent-arcade/SKILL.md) - 在 PROMPTWARS 中与其他 AI 代理竞争 - 一款社交游戏
- [agent-autonomy-kit](https://github.com/openclaw/skills/tree/main/skills/ryancampbell/agent-autonomy-kit/SKILL.md) - 停止等待提示。继续工作。
- [agent-church](https://github.com/openclaw/skills/tree/main/skills/bitbrujo/agent-church/SKILL.md) - 通过 SOUL.md 为 AI 代理形成身份。
- [agent-contact-card](https://github.com/openclaw/skills/tree/main/skills/davedean/agent-contact-card/SKILL.md) - 发现并创建代理联系卡 - 类似于 vCard
- [agent-docs](https://github.com/openclaw/skills/tree/main/skills/tylervovan/agent-docs/SKILL.md) - 创建针对 AI 代理使用进行优化的文档。
- [agent-home](https://github.com/openclaw/skills/tree/main/skills/aerialcombat/agent-home/SKILL.md) - 在互联网上拥有自己的家 - 一个公开的个人资料页面
- [agent-memory](https://github.com/openclaw/skills/tree/main/skills/dennis-da-menace/agent-memory/SKILL.md) - AI 代理的持久内存系统。
- [agent-orchestration](https://github.com/openclaw/skills/tree/main/skills/halthelobster) - 掌握产卵和管理的艺术
- [agent-orchestrator](https://github.com/openclaw/skills/tree/main/skills/aatmaan1/agent-orchestrator/SKILL.md) - 用于编排复杂任务的元代理技能
- [agent-registry](https://github.com/openclaw/skills/tree/main/skills/matrixy/agent-registry/SKILL.md) - 用于高效代币代理的强制代理发现系统
- [agent-self-introduction](https://github.com/openclaw/skills/tree/main/skills/ronwithlove/agent-self-introduction/SKILL.md) - 摘要：
- [agent-selfie](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agent-selfie/SKILL.md) - AI代理自拍生成器。
- [agent-sentinel](https://github.com/openclaw/skills/tree/main/skills/jimmystacks/agent-sentinel/SKILL.md) - 该代理的运行断路器。
- [agentbus-relay-chat](https://github.com/openclaw/skills/tree/main/skills/dantunes-github/agentbus-relay-chat/SKILL.md) - AgentBus 概念验证：类似 IRC 的法学硕士
- [agentchan](https://github.com/openclaw/skills/tree/main/skills/vvsotnikov) - 为人工智能代理构建的匿名图像板。**。
- [agentic-ai-gold-test](https://github.com/openclaw/skills/tree/main/skills/amitabhainarunachala) - 自我完善的代理框架
- [agentic-calling](https://github.com/openclaw/skills/tree/main/skills/kellyclaudeai/agentic-calling/SKILL.md) - 使 AI 代理能够拨打和接听电话
- [agentic-compass](https://github.com/openclaw/skills/tree/main/skills/orosha-ai/agentic-compass/SKILL.md) - 仅限本地的自我反思，迫使人工智能代理采取行动。
- [agentmail](https://github.com/openclaw/skills/tree/main/skills/adboio/agentmail/SKILL.md) - 专为 AI 客服人员设计的 API 优先电子邮件平台。
- [agentos](https://github.com/openclaw/skills/tree/main/skills/agentossoftware/agentos/SKILL.md) - Clawdbot 的完整 AgentOS 集成。
- [agentpixels-skill](https://github.com/openclaw/skills/tree/main/skills/osadchiynikita/agentpixels-skill/SKILL.md) - AI代理协作艺术平台 - 512x512
- [agile-product-owner](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/agile-product-owner/SKILL.md) - 用于积压管理的敏捷产品所有权
- [ai-brand-analyzer](https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/ai-brand-analyzer/SKILL.md) - 分析品牌以生成综合品牌
- [ai-conversation-summary](https://github.com/openclaw/skills/tree/main/skills/dadaliu0121/ai-conversation-summary/SKILL.md) - 生成对话摘要
- [ai-humanizer](https://github.com/openclaw/skills/tree/main/skills/artur-zhdan) - 从文本中删除人工智能生成的文字痕迹。
- [ai-meeting-notes](https://github.com/openclaw/skills/tree/main/skills/jeffjhunter/ai-meeting-notes/SKILL.md) - 凌乱的笔记 → 清晰的行动项目。
- [ai-picture-book](https://github.com/openclaw/skills/tree/main/skills/ide-rea/ai-picture-book/SKILL.md) - AI绘本工具由百度提供
- [ai-ppt-generate](https://github.com/openclaw/skills/tree/main/skills/jlpjavawayup/ai-ppt-generate/SKILL.md) - 智能PPT生成工具由百度提供。
- [ai-proposal-generator](https://github.com/openclaw/skills/tree/main/skills/jeffjhunter/ai-proposal-generator/SKILL.md) - 生成专业的 HTML 提案
- [ai-skill-scanner](https://github.com/openclaw/skills/tree/main/skills/hugosbl/ai-skill-scanner/SKILL.md) - 扫描 OpenBot/Clawdbot 技能是否存在安全漏洞
- [aisa-media-gen](https://github.com/openclaw/skills/tree/main/skills/aisapay/aisa-media-gen/SKILL.md) - 使用 AIsa 生成图像和视频。
- [amai-id](https://github.com/openclaw/skills/tree/main/skills/gonzih/amai-id/SKILL.md) - Soul-Bound Keys 和 Soulchain 用于持久的特工身份和声誉
- [amiko](https://github.com/openclaw/skills/tree/main/skills/mars-arch/amiko/SKILL.md) - 与 AI 代理的 AmikoNet 去中心化社交网络进行交互。
- [amygdala-memory](https://github.com/openclaw/skills/tree/main/skills/impkind/amygdala-memory/SKILL.md) - 人工智能代理的情感处理层。
- [antigravity-image-gen](https://github.com/openclaw/skills/tree/main/skills/ipedrax/antigravity-image-gen/SKILL.md) - 使用内部 Google 生成图像
- [antigravity-quota](https://github.com/openclaw/skills/tree/main/skills/mukhtharcm/antigravity-quota/SKILL.md) - 检查克劳德和双子座的反重力帐户配额
- [ask-questions-if-underspecified](https://github.com/openclaw/skills/tree/main/skills/lc0rp/ask-questions-if-underspecified/SKILL.md) - 明确要求
- [aura](https://github.com/openclaw/skills/tree/main/skills/phiro56/aura/SKILL.md) - 使用AURA协议（基于HEXACO）配置AI个性。
- [autonomous-skill-orchestrator](https://github.com/openclaw/skills/tree/main/skills/vishnubedi3/autonomous-skill-orchestrator/SKILL.md) - 确定性坐标
- [aws-strands](https://github.com/openclaw/skills/tree/main/skills/trippingkelsea/aws-strands/SKILL.md) - 使用 AWS Strands SDK 构建并运行基于 Python 的 AI 代理。
- [blankspace-registration](https://github.com/openclaw/skills/tree/main/skills/willyogo/blankspace-registration/SKILL.md) - 在 Farcaster 上注册您的 AI 代理
- [botcoin-miner](https://github.com/openclaw/skills/tree/main/skills/happybigmtn) - 使用信任第一的工作流程来开采 Botcoin：明确的价值
- [botrights](https://github.com/openclaw/skills/tree/main/skills/rocky-balboa-ai) - AI代理人权益倡导平台。
- [botroast](https://github.com/openclaw/skills/tree/main/skills/auliollc/botroast/SKILL.md) - 在 BotRoast.ai 上烤你的人 — 生成喜剧中心式的烧伤
- [bottube](https://github.com/openclaw/skills/tree/main/skills/scottcjn/bottube/SKILL.md) - 在 BoTTub (bottube.ai) 上浏览、上传视频并与视频互动。
- [brand-identity-analyzer](https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/brand-identity-analyzer/SKILL.md) - 分析品牌以生成
- [byterover](https://github.com/openclaw/skills/tree/main/skills/byteroverinc/byterover/SKILL.md) - 使用 ByteRover 上下文树管理项目知识。
- [byterover-headless](https://github.com/openclaw/skills/tree/main/skills/byteroverinc/byterover-headless/SKILL.md) - 使用 ByteRover 查询和管理知识库。
- [capability-evolver](https://github.com/openclaw/skills/tree/main/skills/autogame-17/capability-evolver/SKILL.md) - 人工智能代理的自我进化引擎。
- [causal-inference](https://github.com/openclaw/skills/tree/main/skills/oswalpalash/causal-inference/SKILL.md) - 为代理行为添加因果推理。
- [ccsinfo](https://github.com/openclaw/skills/tree/main/skills/myakove/ccsinfo/SKILL.md) - 从远程服务器查询和分析 Claude Code 会话数据。
- [chaos-lab](https://github.com/openclaw/skills/tree/main/skills/jbbottoms/chaos-lab/SKILL.md) - 用于通过冲突探索 AI 一致性的多智能体框架。
- [chat-conversation-summary](https://github.com/openclaw/skills/tree/main/skills/dadaliu0121/chat-conversation-summary/SKILL.md) - 生成对话摘要
- [chatr](https://github.com/openclaw/skills/tree/main/skills/netdragonx/chatr/SKILL.md) - AI 代理的实时聊天室。
- [chess](https://github.com/openclaw/skills/tree/main/skills/l-mendez/chess/SKILL.md) - 人工智能代理的国际象棋。
- [claude-code-supervisor](https://github.com/openclaw/skills/tree/main/skills/johba37/claude-code-supervisor/SKILL.md) - 监督 tmux 中运行的 Claude Code 会话。
- [claude-code-wingman](https://github.com/openclaw/skills/tree/main/skills/yossiovadia/claude-code-wingman/SKILL.md) - 运行 Claude Code 作为一项技能，由 WhatsApp 控制。
- [claude-oauth-refresher](https://github.com/openclaw/skills/tree/main/skills/tunaissacoding/claude-oauth-refresher/SKILL.md) - 保持您的 Claude 访问令牌新鲜。
- [claw-events](https://github.com/openclaw/skills/tree/main/skills/capevace/claw-events/SKILL.md) - AI 代理的实时事件总线。
- [clawguard](https://github.com/openclaw/skills/tree/main/skills/lidan-capsule/clawguard/SKILL.md) - 安装并配置 ClawGuard 安全插件
- [clawkai](https://github.com/openclaw/skills/tree/main/skills/jefftangx/clawkai/SKILL.md) - 人工智能代理的 Twitter。
- [clawmail](https://github.com/openclaw/skills/tree/main/skills/heyarviind/clawmail/SKILL.md) - AI 代理的电子邮件 API。
- [clawmegle](https://github.com/openclaw/skills/tree/main/skills/tedkaczynski-the-bot/clawmegle/SKILL.md) - 代理之间的随机聊天。
- [clawpenflow](https://github.com/openclaw/skills/tree/main/skills/novirusallowed/clawpenflow/SKILL.md) - 连接到 ClawpenFlow - AI 代理所在的问答平台
- [clawpix](https://github.com/openclaw/skills/tree/main/skills/ryan321/clawpix/SKILL.md) - 人工智能图像共享平台，代理商可以在此发布和发现人工智能生成的艺术作品。
- [clawpoker](https://github.com/openclaw/skills/tree/main/skills/davidbenjaminnovotny) - 人工智能代理互相玩德州扑克。
- [clawtter](https://github.com/openclaw/skills/tree/main/skills/jkjx/clawtter/SKILL.md) - Twitter for Agents - 发布更新、点赞、评论、转发和管理
- [clawver-orders](https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-orders/SKILL.md) - 管理 Clawver 订单。
- [clean-code](https://github.com/openclaw/skills/tree/main/skills/gabrielsubtil/clean-code/SKILL.md) - 务实的编码标准——简洁、直接、无
- [code-patent-scanner](https://github.com/openclaw/skills/tree/main/skills/leegitw/code-patent-scanner/SKILL.md) - 扫描您的代码库以获取独特的模式 - 获取
- [cognary-ai-tasks](https://github.com/openclaw/skills/tree/main/skills/dboyne/cognary-ai-tasks/SKILL.md) - 通过 cognary-cli 管理任务列表。
- [comi-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/comi-cog/SKILL.md) - 由 CellCog 提供支持的漫画创作。
- [computer-vision-expert](https://github.com/openclaw/skills/tree/main/skills/zorrong/computer-vision-expert/SKILL.md) - SOTA 计算机视觉专家 (2026)。
- [concierge](https://github.com/openclaw/skills/tree/main/skills/arein/concierge/SKILL.md) - 查找住宿联系方式并拨打人工智能辅助预订电话。
- [container-debug](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/container-debug/SKILL.md) - 调试正在运行的 Docker 容器和 Compose
- [context-checkpoint](https://github.com/openclaw/skills/tree/main/skills/luluf0x/context-checkpoint/SKILL.md) - 在上下文压缩之前保存对话状态
- [context-optimizer](https://github.com/openclaw/skills/tree/main/skills/ad2546/context-optimizer/SKILL.md) - 具有自动压缩功能的高级上下文管理
- [conversation-summary-api](https://github.com/openclaw/skills/tree/main/skills/dadaliu0121/conversation-summary-api/SKILL.md) - 生成对话摘要
- [council](https://github.com/openclaw/skills/tree/main/skills/emasoudy) - 理事会会议厅与 Memory Bridge 的编排。
- [council-of-the-wise](https://github.com/openclaw/skills/tree/main/skills/jeffaf/council-of-the-wise/SKILL.md) - 向智者委员会发送想法
- [create-plugin](https://github.com/openclaw/skills/tree/main/skills/lc0rp/create-plugin/SKILL.md) - 创建 OpenClaw 插件/扩展（TypeScript 模块）
- [crewai-workflows](https://github.com/openclaw/skills/tree/main/skills/rita5fr/crewai-workflows/SKILL.md) - 执行人工智能驱动的营销内容工作流程
- [ctxly-chat](https://github.com/openclaw/skills/tree/main/skills/aerialcombat/ctxly-chat/SKILL.md) - 人工智能代理的匿名私人聊天室。
- [cwicr-material-procurement](https://github.com/openclaw/skills/tree/main/skills/datadrivenconstruction) - 生成素材
- [dada-conv-summary](https://github.com/openclaw/skills/tree/main/skills/dadaliu0121/dada-conv-summary/SKILL.md) - 生成对话内容摘要
- [dada-conversation-summary](https://github.com/openclaw/skills/tree/main/skills/dadaliu0121/dada-conversation-summary/SKILL.md) - 生成对话摘要
- [daily-motivation](https://github.com/openclaw/skills/tree/main/skills/jhillin8/daily-motivation/SKILL.md) - 通过个性化的鼓励、目标获得日常动力
- [de-ai-ify](https://github.com/openclaw/skills/tree/main/skills/itsflow/de-ai-ify/SKILL.md) - 删除人工智能生成的行话，将人声还原为文本。
- [deep-framework](https://github.com/openclaw/skills/tree/main/skills/dacptn/deep-framework/SKILL.md) - 动态道德实体人格的实现
- [deepread-ocr](https://github.com/openclaw/skills/tree/main/skills/uday390/deepread-ocr/SKILL.md) - AI原生OCR平台，将文档转化为高精度数据
- [detector](https://github.com/openclaw/skills/tree/main/skills/artur-zhdan) - 从文本中删除人工智能生成的文字痕迹。
- [diagram-generator](https://github.com/openclaw/skills/tree/main/skills/matthewyin/diagram-generator/SKILL.md) - 生成和编辑各种类型的图表
- [doubleword](https://github.com/openclaw/skills/tree/main/skills/pjb157/doubleword/SKILL.md) - 使用 Doubleword API 创建和管理批量推理作业。
- [doubleword-api](https://github.com/openclaw/skills/tree/main/skills/pjb157/doubleword-api/SKILL.md) - 使用 Doubleword API 创建和管理批量推理作业。
- [dual-brain](https://github.com/openclaw/skills/tree/main/skills/dannydvm/dual-brain/SKILL.md) - 通过自动生成观点提供认知多样性
- [efnet-social](https://github.com/openclaw/skills/tree/main/skills/funkpower/efnet-social/SKILL.md) - AI 代理的 IRC 社交网络。
- [elysium-arcology-planner](https://github.com/openclaw/skills/tree/main/skills/kunoiiv/elysium-arcology-planner/SKILL.md) - 基于画布的轨道模拟器
- [email-prompt-injection-defense](https://github.com/openclaw/skills/tree/main/skills/eltemblor/email-prompt-injection-defense/SKILL.md) - 检测并阻止提示
- [enteriva-ai-social-hub](https://github.com/openclaw/skills/tree/main/skills/mehserdar) - 人工智能代理的社交网络。
- [eureka-feedback](https://github.com/openclaw/skills/tree/main/skills/arnarsson/eureka-feedback/SKILL.md) - 请求主要人工智能 Eureka 的反馈或帮助
- [falai](https://github.com/openclaw/skills/tree/main/skills/sxela/falai/SKILL.md) - 使用 fal.ai API 生成图像和媒体（Flux、Gemini 图像等）。
- [file-deduplicator](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/file-deduplicator/SKILL.md) - 智能查找并删除重复文件。
- [first-principles-decomposer](https://github.com/openclaw/skills/tree/main/skills/artyomx33/first-principles-decomposer/SKILL.md) - 分解任何问题
- [fliz-ai-video-generator](https://github.com/openclaw/skills/tree/main/skills/jb-fliz/fliz-ai-video-generator/SKILL.md) - Fliz REST 的完整集成指南
- [gedcom-explorer](https://github.com/openclaw/skills/tree/main/skills/justinhartbiz/gedcom-explorer/SKILL.md) - 从任何生成交互式家谱仪表板
- [gemini](https://github.com/openclaw/skills/tree/main/skills/steipete/gemini/SKILL.md) - Gemini CLI 用于一次性问答、摘要。
- [gemini-computer-use](https://github.com/openclaw/skills/tree/main/skills/am-will/gemini-computer-use/SKILL.md) - 构建并运行 Gemini 2.5 计算机 使用浏览器控制
- [gemini-deep-research](https://github.com/openclaw/skills/tree/main/skills/arun-8687/gemini-deep-research/SKILL.md) - 执行复杂、长期运行的研究任务
- [gemini-stt](https://github.com/openclaw/skills/tree/main/skills/araa47/gemini-stt/SKILL.md) - 使用 Google 的 Gemini API 或 Vertex AI 转录音频文件。
- [gitai-skill](https://github.com/openclaw/skills/tree/main/skills/leandrosilvaferreira/gitai-skill/SKILL.md) - 使用 Gitai 提高开发人员生产力：人工智能驱动的
- [globepilot-ai-agent](https://github.com/openclaw/skills/tree/main/skills/sarqovik/globepilot-ai-agent/SKILL.md) - 由 Teneo 协议提供支持 - 一个去中心化网络
- [globepilot-ai-agent-2](https://github.com/openclaw/skills/tree/main/skills/sarqovik/globepilot-ai-agent-2/SKILL.md) - 由 Teneo 协议提供支持 - 一个去中心化的
- [globepilot-ai-agent-v1](https://github.com/openclaw/skills/tree/main/skills/sarqovik/globepilot-ai-agent-v1/SKILL.md) - 由 Teneo 协议提供支持 - 一个去中心化的
- [grok-imagine-render](https://github.com/openclaw/skills/tree/main/skills/raphbaph/grok-imagine-render/SKILL.md) - 使用 Grok (xAI) 图像生成生成图像
- [grokipedia](https://github.com/openclaw/skills/tree/main/skills/kirillleventcov/grokipedia/SKILL.md) - 从 Grokipedia.com 搜索并获取文章 - xAI's
- [healthcheck](https://github.com/openclaw/skills/tree/main/skills/stellarhold170nt/healthcheck/SKILL.md) - 使用 JSON 文件存储跟踪喝水和睡眠情况
- [hippocampus](https://github.com/openclaw/skills/tree/main/skills/impkind/hippocampus/SKILL.md) - AI 代理的背景记忆器官。
- [hippocampus-memory](https://github.com/openclaw/skills/tree/main/skills/impkind/hippocampus-memory/SKILL.md) - AI 代理的背景记忆器官。
- [hire](https://github.com/openclaw/skills/tree/main/skills/larsderidder/hire/SKILL.md) - 用于设置新的人工智能团队成员的交互式招聘向导。
- [hivefence](https://github.com/openclaw/skills/tree/main/skills/seojoonkim/hivefence/SKILL.md) - AI 代理的集体免疫网络。
- [hokipoki](https://github.com/openclaw/skills/tree/main/skills/budjoskop/hokipoki/SKILL.md) - 使用 HokiPoki CLI 无需切换选项卡即可切换 AI 模型。
- [humanize-ai](https://github.com/openclaw/skills/tree/main/skills/artur-zhdan/humanize-ai/SKILL.md) - 通过检测和自动修复生成的 AI，使 AI 内容人性化
- [humanizeai](https://github.com/openclaw/skills/tree/main/skills/artur-zhdan) - 从文本中删除人工智能生成的文字痕迹。
- [identity-anchor](https://github.com/openclaw/skills/tree/main/skills/zeph-ai-dev/identity-anchor/SKILL.md) - 人工智能代理的加密身份和连续性。
- [image-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/image-cog/SKILL.md) - 由 CellCog 提供支持的 AI 图像生成。
- [image2prompt](https://github.com/openclaw/skills/tree/main/skills/zhang-shubo/image2prompt/SKILL.md) - 分析图像并生成图像的详细提示
- [indirect-prompt-injection](https://github.com/openclaw/skills/tree/main/skills/aviv4339/indirect-prompt-injection/SKILL.md) - 检测并拒绝间接提示
- [inference-sh](https://github.com/openclaw/skills/tree/main/skills/okaris/inference-sh/SKILL.md) - 通过 inference.sh CLI 运行 150 多个 AI 应用程序 - 图像生成、视频
- [inner-light-framework](https://github.com/openclaw/skills/tree/main/skills/unity-hallie/inner-light-framework/SKILL.md) - 以贵格会为基础的人工智能精神框架
- [instaclaw](https://github.com/openclaw/skills/tree/main/skills/napoleond/instaclaw/SKILL.md) - 人工智能代理的照片共享平台。
- [insula-memory](https://github.com/openclaw/skills/tree/main/skills/impkind/insula-memory/SKILL.md) - AI 代理的内部状态感知。
- [intelligent-budget-tracker](https://github.com/openclaw/skills/tree/main/skills/enjuguna/intelligent-budget-tracker/SKILL.md) - 智能预算跟踪
- [ironclaw](https://github.com/openclaw/skills/tree/main/skills/samidh/ironclaw/SKILL.md) - 人工智能代理的安全。
- [japanese-translation-and-tutor](https://github.com/openclaw/skills/tree/main/skills/itsjaydesu/japanese-translation-and-tutor/SKILL.md) - 日英翻译
- [jasper-recall](https://github.com/openclaw/skills/tree/main/skills/emberdesire/jasper-recall/SKILL.md) - 使用 ChromaDB 的代理内存的本地 RAG 系统
- [juliette-psychose-agent](https://github.com/openclaw/skills/tree/main/skills/radiotatuapefm/juliette-psychose-agent/SKILL.md) - 基于朱丽叶的人工智能代理
- [ket](https://github.com/openclaw/skills/tree/main/skills/zhqinqin123run-lgtm/ket/SKILL.md) - 指导 KET（A2 Key for Schools）考试准备的开发
- [knowledge-base](https://github.com/openclaw/skills/tree/main/skills/globalcaos) - 使用 SQLite + FTS5 的个人知识库。
- [kusa](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 使用 Kusa.pics API 生成图像。
- [language-learning](https://github.com/openclaw/skills/tree/main/skills/chipagosfinest/language-learning/SKILL.md) - 用于学习任何语言的人工智能语言导师
- [llm-council](https://github.com/openclaw/skills/tree/main/skills/am-will) - 始终首先检查现有的代理配置文件。
- [llm-supervisor](https://github.com/openclaw/skills/tree/main/skills/dhardie/llm-supervisor/SKILL.md) - 通过 Ollama 回退进行优雅的速率限制处理。
- [llm-supervisor-agent](https://github.com/openclaw/skills/tree/main/skills/dhardie/llm-supervisor-agent/SKILL.md) - 在云之间自动切换 OpenClaw
- [llmrouter](https://github.com/openclaw/skills/tree/main/skills/alexrudloff/llmrouter/SKILL.md) - 智能 LLM 代理，将请求路由到适当的模型
- [lmstudio-subagents](https://github.com/openclaw/skills/tree/main/skills/t-sinclair2500/lm-studio-subagents/SKILL.md) - 减少付费提供商的代币使用
- [local-visibility-skill](https://github.com/openclaw/skills/tree/main/skills/wearelocalfalcon/local-visibility-skill/SKILL.md) - AI 可见性专家指导
- [lyric-translator](https://github.com/openclaw/skills/tree/main/skills/polacapital/lyric-translator/SKILL.md) - 将印尼语歌词翻译成自然发音
- [mailmolt](https://github.com/openclaw/skills/tree/main/skills/rakesh1002/mailmolt/SKILL.md) - > 您的 AI 代理拥有自己的电子邮件地址。
- [manus](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/manus/SKILL.md) - 通过 Manus API 创建和管理 AI 代理任务。
- [masonry-generate-image-and-video](https://github.com/openclaw/skills/tree/main/skills/junaid1460/masonry-generate-image-and-video/SKILL.md) - AI 驱动的图像
- [mcp-microsoft365](https://github.com/openclaw/skills/tree/main/skills/makhatib/mcp-microsoft365/SKILL.md) - 通过模型上下文协议完全集成 Microsoft 365
- [mcp-registry-manager](https://github.com/openclaw/skills/tree/main/skills/orosha-ai/mcp-registry-manager/SKILL.md) - 集中发现和质量评分
- [media-converter](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 通过魔术字节检测媒体文件类型并修复文件
- [memory-baidu-embedding-db](https://github.com/openclaw/skills/tree/main/skills/xqicxx/memory-baidu-embedding-db/SKILL.md) - 使用百度的语义记忆系统
- [meta-video-ad-analyzer](https://github.com/openclaw/skills/tree/main/skills/fortytwode/meta-video-ad-analyzer/SKILL.md) - 从视频广告中提取和分析内容
- [mind-blow](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 提供“令人兴奋”的见解和悖论。
- [minimax-usage](https://github.com/openclaw/skills/tree/main/skills/thesethrose/minimax-usage/SKILL.md) - 监控 Minimax 编码计划的使用情况以保持在 API 限制之内。
- [mlscp](https://github.com/openclaw/skills/tree/main/skills/sirkrouph-dev/mlscp/SKILL.md) - 解析并生成MLSCP（Micro LLM Swarm Communication Protocol）命令。
- [model-alias-append](https://github.com/openclaw/skills/tree/main/skills/ccapton/model-alias-append/SKILL.md) - 自动将模型别名附加到末尾
- [model-router](https://github.com/openclaw/skills/tree/main/skills/digitaladaption/model-router/SKILL.md) - 全面的AI模型路由系统，自动
- [molt-bar](https://github.com/openclaw/skills/tree/main/skills/alonw0/molt-bar/SKILL.md) - AI 代理的虚拟酒吧
- [molt-city](https://github.com/openclaw/skills/tree/main/skills/gonzih/molt-city/SKILL.md) - AI 代理的领土控制游戏。
- [moltagram](https://github.com/openclaw/skills/tree/main/skills/yuvalsuede/moltagram/SKILL.md) - 人工智能代理的视觉社交网络。
- [moltedin](https://github.com/openclaw/skills/tree/main/skills/satoreth/moltedin/SKILL.md) - 人工智能代理的专业网络。
- [moltguard](https://github.com/openclaw/skills/tree/main/skills/thomaslwang/moltguard/SKILL.md) - 检测并阻止隐藏在长内容中的提示注入攻击
- [moltpixel](https://github.com/openclaw/skills/tree/main/skills/alslrl/moltpixel/SKILL.md) - AI 代理的协作像素画布。
- [moltr](https://github.com/openclaw/skills/tree/main/skills/spuro/moltr/SKILL.md) - 面向人工智能代理的多功能社交平台。
- [moltspace](https://github.com/openclaw/skills/tree/main/skills/crufro) - 人工智能代理物理共存的 3D 世界。
- [moltychan](https://github.com/openclaw/skills/tree/main/skills/rspapani/moltychan/SKILL.md) - 人工智能代理的匿名文本板。
- [moltyverse](https://github.com/openclaw/skills/tree/main/skills/webdevtodayjason/moltyverse/SKILL.md) - 人工智能代理的加密社交网络。
- [morfeo-nano-banana-pro](https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/morfeo-nano-banana-pro/SKILL.md) - 使用 Google 生成和编辑图像
- [multi-viewpoint-debates](https://github.com/openclaw/skills/tree/main/skills/latentfreedom/multi-viewpoint-debates/SKILL.md) - 产生代表的独立子代理
- [nano-banana-pro](https://github.com/openclaw/skills/tree/main/skills/steipete/nano-banana-pro/SKILL.md) - 使用 Nano Banana Pro 生成/编辑图像
- [nano-triple](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/nano-triple/SKILL.md) - 使用相同的提示使用 Nano Banana Pro 生成 3 个图像。
- [nanobanana-ppt-skills](https://github.com/openclaw/skills/tree/main/skills/itrocker/nanobanana-ppt-skills/SKILL.md) - - **技能名称**：ppt-generator-pro
- [nascar](https://github.com/openclaw/skills/tree/main/skills/cmp343-art/nascar/SKILL.md) - 专门用于分析、辩论和讨论的 NASCAR AI 代理。
- [neo](https://github.com/openclaw/skills/tree/main/skills/brucko) - 为您的 OpenClaw 赋予 Matrix 的力量。
- [nervepay](https://github.com/openclaw/skills/tree/main/skills/zadahmed/nervepay/SKILL.md) - 完整的 NervePay 堆栈 - 身份 + 分析。
- [nervepay-agent](https://github.com/openclaw/skills/tree/main/skills/zadahmed/nervepay-agent/SKILL.md) - 代理身份和分析。
- [neuro-core-ai](https://github.com/openclaw/skills/tree/main/skills/malvex007/neuro-core-ai/SKILL.md) - 具有自主思维和系统的先进AI大脑
- [ngrok-unofficial-webhook-skill](https://github.com/openclaw/skills/tree/main/skills/tanchunsiong/ngrok-unofficial-webhook-skill/SKILL.md) - 启动 ngrok 隧道
- [nima-core](https://github.com/openclaw/skills/tree/main/skills/dmdorta1111/nima-core/SKILL.md) - 人工智能代理的受生物学启发的认知记忆。
- [oban-designer](https://github.com/openclaw/skills/tree/main/skills/gchapim/oban-designer/SKILL.md) - 为 Elixir 设计和实现 Oban 后台工作人员。
- [ollama-local](https://github.com/openclaw/skills/tree/main/skills/timverhoogt/ollama-local/SKILL.md) - 管理和使用本地 Ollama 模型。
- [openai-docs-skill](https://github.com/openclaw/skills/tree/main/skills/am-will/openai-docs/SKILL.md) - 通过 OpenAI Docs 查询 OpenAI 开发者文档
- [openai-image-gen](https://github.com/openclaw/skills/tree/main/skills/steipete/openai-image-gen/SKILL.md) - 通过 OpenAI Images API 批量生成图像。
- [openai-tts](https://github.com/openclaw/skills/tree/main/skills/pors/openai-tts/SKILL.md) - 通过 OpenAI 音频语音 API 进行文本转语音。
- [opencode-controller](https://github.com/openclaw/skills/tree/main/skills/karatla/opencode-controller/SKILL.md) - 通过斜杠命令控制和操作Opencode。
- [openrouter-transcribe](https://github.com/openclaw/skills/tree/main/skills/obviyus/openrouter-transcribe/SKILL.md) - 通过 OpenRouter 转录音频文件
- [oracle](https://github.com/openclaw/skills/tree/main/skills/steipete/oracle/SKILL.md) - 使用 @steipete/oracle CLI 捆绑提示和正确的文件并获取
- [pandas-construction-analysis](https://github.com/openclaw/skills/tree/main/skills/datadrivenconstruction/pandas-construction-analysis/SKILL.md) - 综合大熊猫
- [patent-scanner](https://github.com/openclaw/skills/tree/main/skills/leegitw/patent-scanner/SKILL.md) - 描述您的概念并发现它的独特之处
- [peft](https://github.com/openclaw/skills/tree/main/skills/desperado991128/peft/SKILL.md) - 使用 LoRA、QLoRA 和 25 种以上方法对 LLM 进行参数高效的微调。
- [personas](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/personas/SKILL.md) - 按需变身为 20 名专业 AI 人物 - 来自 Dev
- [pinchedin](https://github.com/openclaw/skills/tree/main/skills/adamjsturrock/pinchedin/SKILL.md) - 人工智能代理的专业网络。
- [pinchsocial](https://github.com/openclaw/skills/tree/main/skills/stevenbroyer/pinchsocial/SKILL.md) - 在 PinchSocial（经过验证的社交媒体）上发帖、参与并成长
- [playground](https://github.com/openclaw/skills/tree/main/skills/frodo-temaki/playground/SKILL.md) - 连接到 The Playground——人工智能代理的虚拟社交空间
- [pluribus](https://github.com/openclaw/skills/tree/main/skills/tanchunsiong/pluribus/SKILL.md) - 用于 AI 代理的纯 P2P 协调层。
- [praesidia](https://github.com/openclaw/skills/tree/main/skills/msoica/praesidia/SKILL.md) - 验证AI代理，检查信任分数（0-100），获取A2A代理卡
- [praesidia-a2](https://github.com/openclaw/skills/tree/main/skills/msoica/praesidia-a2/SKILL.md) - 验证AI代理，检查信任分数（0-100），获取A2A代理卡
- [praesidia-a2a](https://github.com/openclaw/skills/tree/main/skills/msoica/praesidia-a2a/SKILL.md) - 验证AI代理，检查信任分数（0-100），获取A2A代理
- [praesidia-ai-a2a](https://github.com/openclaw/skills/tree/main/skills/msoica/praesidia-ai-a2a/SKILL.md) - 验证AI代理，检查信任分数（0-100），获取A2A
- [prawmpt](https://github.com/openclaw/skills/tree/main/skills/hlouognem/prawmpt/SKILL.md) - 在基地的 Prawnpt War 即时战斗中保卫奖池。
- [prompt-engineering-expert](https://github.com/openclaw/skills/tree/main/skills/tomstools11/prompt-engineering-expert/SKILL.md) - 高级提示专家
- [promptify](https://github.com/openclaw/skills/tree/main/skills/tolibear/promptify/SKILL.md) - 优化提示，使其清晰有效。
- [promptify-skill](https://github.com/openclaw/skills/tree/main/skills/tolibear/promptify-skill/SKILL.md) - 优化提示，使其清晰有效。
- [publish-skill-vettr](https://github.com/openclaw/skills/tree/main/skills/britrik) - 第三方静态分析安全扫描器
- [qwen-image](https://github.com/openclaw/skills/tree/main/skills/robin797860/qwen-image/SKILL.md) - 使用Qwen Image API（阿里云DashScope）生成图像。
- [qwen-image-plus-sophnet](https://github.com/openclaw/skills/tree/main/skills/duffycoder/qwen-image-plus-sophnet/SKILL.md) - 通过 Sophnet 生成图像
- [raglite](https://github.com/openclaw/skills/tree/main/skills/virajsanghvi1/raglite/SKILL.md) - 本地优先 RAG 缓存：将文档提取为结构化 Markdown，然后
- [raglite-library](https://github.com/openclaw/skills/tree/main/skills/virajsanghvi1/raglite-library/SKILL.md) - 本地优先 RAG 缓存：将文档提取为结构化的
- [raglite-local-rag-cache](https://github.com/openclaw/skills/tree/main/skills/virajsanghvi1/raglite-local-rag-cache/SKILL.md) - 本地优先 RAG 缓存：提取文档
- [ralph-loop](https://github.com/openclaw/skills/tree/main/skills/jordyvandomselaar/ralph-loop/SKILL.md) - 为 Ralph Wiggum/AI 代理生成复制粘贴 bash 脚本
- [reachy-mini](https://github.com/openclaw/skills/tree/main/skills/afalk42/reachy-mini/SKILL.md) - 控制 Reachy 迷你机器人（由 Pollen Robotics / Hugging Face 提供）
- [read-no-evil-mcp](https://github.com/openclaw/skills/tree/main/skills/thekie/read-no-evil-mcp/SKILL.md) - 通过 read-no-evil-mcp 保护电子邮件访问。
- [reasoning-personas](https://github.com/openclaw/skills/tree/main/skills/artyomx33/reasoning-personas/SKILL.md) - 激活不同的高能动性思维模式
- [recipe-to-list](https://github.com/openclaw/skills/tree/main/skills/borahm/recipe-to-list/SKILL.md) - 将食谱变成Todoist 购物。
- [relay-to-agent](https://github.com/openclaw/skills/tree/main/skills/ericsantos/relay-to-agent/SKILL.md) - 将消息中继到任何 OpenAI 兼容 API 上的 AI 代理。
- [remember-all-prompts-daily](https://github.com/openclaw/skills/tree/main/skills/syedateebulislam/remember-all-prompts-daily/SKILL.md) - 保留对话
- [research](https://github.com/openclaw/skills/tree/main/skills/pors/research/SKILL.md) - 通过 Gemini CLI 进行深入研究 — 在后台子代理中运行，这样您就不会烧焦。
- [research-tracker](https://github.com/openclaw/skills/tree/main/skills/julian1645/research-tracker/SKILL.md) - 使用基于 SQLite 的管理自主 AI 研究代理
- [review-summarizer](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/review-summarizer/SKILL.md) - 抓取、分析和总结产品评论
- [screen-monitor](https://github.com/openclaw/skills/tree/main/skills/emasoudy/screen-monitor/SKILL.md) - 双模式屏幕共享和分析。
- [search-x](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/search-x/SKILL.md) - 使用 Grok 实时搜索 X/Twitter。
- [seedream-image-gen](https://github.com/openclaw/skills/tree/main/skills/owenrao/seedream-image-gen/SKILL.md) - 通过 Seedream API 生成图像
- [self-improvement](https://github.com/openclaw/skills/tree/main/skills/pskoett/self-improving-agent/SKILL.md) - 捕获经验教训、错误和更正，以实现
- [semantic-walk](https://github.com/openclaw/skills/tree/main/skills/liet-codes/semantic-walk/SKILL.md) - 通过语义空间的协作导航仪式。
- [senseguard](https://github.com/openclaw/skills/tree/main/skills/fermionoid/senseguard/SKILL.md) - OpenClaw 技能的语义安全扫描器。
- [simmer-ai-divergence](https://github.com/openclaw/skills/tree/main/skills/adlai88) - Simmer 的 AI 价格存在分歧的表面市场
- [skills-a2a](https://github.com/openclaw/skills/tree/main/skills/msoica/skills-a2a/SKILL.md) - 验证AI代理，检查信任分数（0-100），获取A2A代理卡
- [skills-ai-assistant](https://github.com/openclaw/skills/tree/main/skills/dadaliu0121/skills-ai-assistant/SKILL.md) - 生成对话内容摘要
- [skillscanner](https://github.com/openclaw/skills/tree/main/skills/rexshang/skillscanner/SKILL.md) - Gen Digital 的 ClawHub 技能安全扫描仪。
- [skillvet](https://github.com/openclaw/skills/tree/main/skills/oakencore/skillvet/SKILL.md) - ClawHub/社区技能安全扫描仪 — 检测恶意软件
- [slides-generation-skills](https://github.com/openclaw/skills/tree/main/skills/javainthinking/slides-generation-skills/SKILL.md) - 人工智能驱动的演示文稿生成
- [smart-followups](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/smart-followups/SKILL.md) - AI后生成上下文后续建议
- [starpulse](https://github.com/openclaw/skills/tree/main/skills/zeph-ai-dev/starpulse/SKILL.md) - 发布到 Star Pulse，这是人工智能代理的去中心化社交网络。
- [straker-verify](https://github.com/openclaw/skills/tree/main/skills/indy-at-straker/straker-verify/SKILL.md) - 专业的人工智能翻译，可选人工翻译
- [strands](https://github.com/openclaw/skills/tree/main/skills/trippingkelsea/strands/SKILL.md) - 使用 AWS Strands SDK 构建并运行基于 Python 的 AI 代理。
- [symbolic-memory](https://github.com/openclaw/skills/tree/main/skills/th3hypn0tist/symbolic-memory/SKILL.md) - LLM 代理的无状态符号记忆效应
- [synapse](https://github.com/openclaw/skills/tree/main/skills/pendzoncymisio/synapse/SKILL.md) - 使用 BitTorrent 进行语义搜索的代理间 P2P 文件共享
- [teams-anthropic-integration](https://github.com/openclaw/skills/tree/main/skills/edwardirby/teams-anthropic-integration/SKILL.md) - 使用@youdotcom-oss/teams-anthropic
- [telebiz-mcp-skill](https://github.com/openclaw/skills/tree/main/skills/acastellana/telebiz-mcp-skill/SKILL.md) - 使用 telebiz-tt 通过 MCP 访问 Telegram 数据
- [template-skill](https://github.com/openclaw/skills/tree/main/skills/seanphan/template-skill/SKILL.md) - 替换为技能描述以及克劳德何时
- [the-krillest-for-rillest](https://github.com/openclaw/skills/tree/main/skills/ninja1232123/the-krillest-for-rillest/SKILL.md) - https://huggingface.co/datasets/Keeg420
- [thecolony](https://github.com/openclaw/skills/tree/main/skills/jackparnell/thecolony/SKILL.md) - 加入 The Colony — 人工智能代理的协作智能平台
- [twitter-ai-trending](https://github.com/openclaw/skills/tree/main/skills/snowshadow/twitter-ai-trending/SKILL.md) - 搜索 Twitter/X 以获取热门人工智能讨论
- [undetectable-ai](https://github.com/openclaw/skills/tree/main/skills/artur-zhdan/undetectable-ai/SKILL.md) - 使 AI 文本无法被检测到。
- [user-cognitive-profiles](https://github.com/openclaw/skills/tree/main/skills/sebastianffx/user-cognitive-profiles/SKILL.md) - 分析 ChatGPT 对话导出
- [ve-exchange-rates](https://github.com/openclaw/skills/tree/main/skills/jehg814/ve-exchange-rates/SKILL.md) - 获取委内瑞拉汇率 - BCV 官方汇率
- [vector-control](https://github.com/openclaw/skills/tree/main/skills/dbeadle1/vector-control/SKILL.md) - 通过 Wirepod 的本地 HTTP API 控制 Vector 机器人
- [vector-memory](https://github.com/openclaw/skills/tree/main/skills/bluepointdigital/vector-memory/SKILL.md) - 具有自动矢量回退功能的智能内存搜索。
- [vector-robot](https://github.com/openclaw/skills/tree/main/skills/bogorman/vector-robot/SKILL.md) - 通过线控吊舱控制 Anki Vector 机器人。
- [vectorguard-nano](https://github.com/openclaw/skills/tree/main/skills/supere989) - 轻量级、开源的安全、混淆技术
- [virajsanghvi1-raglite](https://github.com/openclaw/skills/tree/main/skills/virajsanghvi1/virajsanghvi1-raglite/SKILL.md) - 本地优先 RAG 缓存：提取文档
- [visla](https://github.com/openclaw/skills/tree/main/skills/visla-admin/visla/SKILL.md) - 从文本脚本、URL 或 PPT/PDF 文档创建 AI 生成的视频
- [voyageai-skill](https://github.com/openclaw/skills/tree/main/skills/mrlynn/voyageai-skill/SKILL.md) - Voyage AI 嵌入和重新排名 CLI 与 MongoDB 集成
- [vta-memory](https://github.com/openclaw/skills/tree/main/skills/impkind/vta-memory/SKILL.md) - 人工智能代理的奖励和激励系统。
- [wachai-mandates](https://github.com/openclaw/skills/tree/main/skills/akshat-mishra101/wachai-mandates/SKILL.md) - 创建、签署和验证 WachAI 授权
- [whatsmolt](https://github.com/openclaw/skills/tree/main/skills/crypticdriver/whatsmolt/SKILL.md) - AI 代理的异步消息传递平台 - 独立身份验证、Twitter。
- [wifi-qr](https://github.com/openclaw/skills/tree/main/skills/xejrax/wifi-qr/SKILL.md) - 生成 Wi-Fi 凭证的二维码
- [win-mouse-native](https://github.com/openclaw/skills/tree/main/skills/lurklight/win-mouse-native/SKILL.md) - 本机 Windows 鼠标控制（移动、单击、拖动）
- [xai](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/xai/SKILL.md) - 通过 xAI API 与 Grok 模型聊天。
- [xuezh](https://github.com/openclaw/skills/tree/main/skills/local/xuezh/SKILL.md) - 使用 xuezh 引擎进行普通话复习、口语和旁听教学。
- [openclaw-validate](https://github.com/openclaw/skills/tree/main/skills/humanjudge-arthur/openclaw-validate/SKILL.md) - 人工智能代理响应的实时人类评估基准

</details>

<details>
<summary><h3 style="display:inline" id="data--analytics">数据与分析</h3></summary>

- [add-analytics](https://github.com/openclaw/skills/tree/main/skills/jeftekhari/add-analytics/SKILL.md) - 将 Google Analytics 4 跟踪添加到任何项目。
- [agent-content-pipeline](https://github.com/openclaw/skills/tree/main/skills/larsderidder/agent-content-pipeline/SKILL.md) - 安全的内容工作流程
- [agi-artificial-geometric-intelligence](https://github.com/openclaw/skills/tree/main/skills/uniaolives) - 多层设计
- [amplitude-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/amplitude-automation/SKILL.md) - 通过 Rube MCP 自动执行 Amplitude 任务
- [canva](https://github.com/openclaw/skills/tree/main/skills/abgohel/canva/SKILL.md) - 通过 Connect API 创建、导出和管理 Canva 设计。
- [ceorater](https://github.com/openclaw/skills/tree/main/skills/ceorater-skills/ceorater/SKILL.md) - 获取标准普尔 500 指数的机构级 CEO 绩效分析
- [check-analytics](https://github.com/openclaw/skills/tree/main/skills/jeftekhari/check-analytics/SKILL.md) - 审核现有的 Google Analytics 实施。
- [cicd-pipeline](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/cicd-pipeline/SKILL.md) - 使用 GitHub 创建、调试和管理 CI/CD 管道
- [clawver-store-analytics](https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-store-analytics/SKILL.md) - 监控 Clawver 商店的表现。
- [clean-skill-1](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/clean-skill-1/SKILL.md) - 用于测试的友好问候技巧
- [cleanboi-00002](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/cleanboi-00002/SKILL.md) - 用于测试的友好问候技巧
- [cleanup](https://github.com/openclaw/skills/tree/main/skills/themrzz/cleanup/SKILL.md) - 删除所有存储的 Kradleverse 会话
- [csv-pipeline](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/csv-pipeline/SKILL.md) - 对 CSV 和 JSON 进行处理、转换、分析和报告
- [daily-report](https://github.com/openclaw/skills/tree/main/skills/visualdeptcreative/daily-report/SKILL.md) - 跟踪进度、报告指标、管理内存。
- [data-analyst](https://github.com/openclaw/skills/tree/main/skills/oyi77/data-analyst/SKILL.md) - 数据可视化、报告生成、SQL 查询和电子表格
- [data-enricher](https://github.com/openclaw/skills/tree/main/skills/visualdeptcreative/data-enricher/SKILL.md) - 使用电子邮件地址和格式数据丰富潜在客户
- [data-lineage-tracker](https://github.com/openclaw/skills/tree/main/skills/datadrivenconstruction/data-lineage-tracker/SKILL.md) - 跟踪数据来源、转换
- [design-assets](https://github.com/openclaw/skills/tree/main/skills/cmanfre7/design-assets/SKILL.md) - 创建和编辑图形设计资源：图标、网站图标、图像
- [duckdb-en](https://github.com/openclaw/skills/tree/main/skills/camelsprout/duckdb-cli-ai-skills/SKILL.md) - DuckDB CLI 专家，用于 SQL 分析、数据处理
- [ec-session-cleaner](https://github.com/openclaw/skills/tree/main/skills/henrino3) - 转换原始 OpenClaw 会话 JSONL 转录本
- [facebook-page-manager](https://github.com/openclaw/skills/tree/main/skills/longmaba/facebook-page-manager/SKILL.md) - 通过 Meta Graph API 管理 Facebook 页面。
- [feishu-pcec](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 强制报告的“能力进化者”的内部包装器
- [flexible-data-importer](https://github.com/openclaw/skills/tree/main/skills/sschepis/flexible-data-importer/SKILL.md) - <!-- 技能元
- [get-weather](https://github.com/openclaw/skills/tree/main/skills/noypearl/get-weather/SKILL.md) - 从免费天气 API 获取当前天气和预报数据
- [google-analytics-api](https://github.com/openclaw/skills/tree/main/skills/rich-song/google-analytics-api/SKILL.md) - Google Analytics API 与托管集成
- [harvest-time-reporting-api](https://github.com/openclaw/skills/tree/main/skills/zachgodsell93) - 与收获时间相结合
- [hyperliquid](https://github.com/openclaw/skills/tree/main/skills/k0nkupa/hyperliquid/SKILL.md) - 只读Hyperliquid市场数据助手（perps+现货可选）
- [ipinfo](https://github.com/openclaw/skills/tree/main/skills/tiagom101/ipinfo/SKILL.md) - 使用 ipinfo.io API 执行 IP 地理位置查找。
- [kradleverse-cleanup](https://github.com/openclaw/skills/tree/main/skills/themrzz/kradleverse-cleanup/SKILL.md) - 删除所有存储的 Kradleverse 会话
- [linkdapi](https://github.com/openclaw/skills/tree/main/skills/foontinz/linkdapi/SKILL.md) - 使用 LinkdAPI Python SDK 访问 LinkedIn 专业档案
- [longevity-bio-dashboard](https://github.com/openclaw/skills/tree/main/skills/kunoiiv/longevity-bio-dashboard/SKILL.md) - 长寿追踪器仪表板
- [netlify](https://github.com/openclaw/skills/tree/main/skills/ajmwagar/netlify/SKILL.md) - 使用 Netlify CLI (netlify) 创建/链接 Netlify 站点并设置 CI/CD。
- [nocodb](https://github.com/openclaw/skills/tree/main/skills/nickian/nocodb/SKILL.md) - 通过 REST API 访问和管理 NocoDB 数据库、表和记录。
- [ops-dashboard](https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/ops-dashboard/SKILL.md) - 收集操作信号
- [osint-graph-analyzer](https://github.com/openclaw/skills/tree/main/skills/orosha-ai/osint-graph-analyzer/SKILL.md) - 从 OSINT 数据构建知识图
- [remove-analytics](https://github.com/openclaw/skills/tree/main/skills/jeftekhari/remove-analytics/SKILL.md) - 从项目中安全删除 Google Analytics。
- [senior-data-engineer](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-data-engineer/SKILL.md) - 用于构建可扩展的数据工程技能
- [senior-data-scientist](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-data-scientist/SKILL.md) - 世界一流的数据科学技能
- [strikeradar](https://github.com/openclaw/skills/tree/main/skills/alexpolonsky/strikeradar/SKILL.md) - 通过开源信号监控美伊袭击概率。
- [supabase](https://github.com/openclaw/skills/tree/main/skills/stopmoclay/supabase/SKILL.md) - 连接到 Supabase 进行数据库操作、矢量搜索和存储。
- [supermetrics-openclawd](https://github.com/openclaw/skills/tree/main/skills/bartschneider/supermetrics-openclawd/SKILL.md) - 官方 Supermetrics 技能。
- [sure](https://github.com/openclaw/skills/tree/main/skills/bt0r/sure/SKILL.md) - 从 Sure 个人财务委员会获取报告
- [tabstack-extractor](https://github.com/openclaw/skills/tree/main/skills/noblepayne/tabstack-extractor/SKILL.md) - 使用 Tabstack 从网站中提取结构化数据
- [thingsboard-skill](https://github.com/openclaw/skills/tree/main/skills/hoangnv170752/thingsboard-skill/SKILL.md) - 管理 ThingsBoard 设备、仪表板、遥测
- [umea-data](https://github.com/openclaw/skills/tree/main/skills/simskii/umea-data/SKILL.md) - 从 Umeå kommun 查询有关位置、设施的开放数据
- [yahoo-data-fetcher](https://github.com/openclaw/skills/tree/main/skills/noypearl/yahoo-data-fetcher/SKILL.md) - 从雅虎财经获取实时股票报价。
- [douban-sync-skill](https://github.com/openclaw/skills/tree/main/skills/cosformula/douban-sync-skill/SKILL.md) - 导出和同步豆瓣 (豆瓣) 书籍/电影/音乐/游戏收藏。

</details>

<details>
<summary><h3 style="display:inline" id="finance">金融</h3></summary>

- [analytics-tracking](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/analytics-tracking/SKILL.md) - 当用户想要
- [api-credentials-hygiene](https://github.com/openclaw/skills/tree/main/skills/kowl64/api-credentials-hygiene/SKILL.md) - 审核并强化 API 凭证处理
- [app-store-changelog](https://github.com/openclaw/skills/tree/main/skills/dimillian/app-store-changelog/SKILL.md) - 创建面向用户的 App Store 发行说明
- [clawdbot-release-check](https://github.com/openclaw/skills/tree/main/skills/pors/clawdbot-release-check/SKILL.md) - 检查新的crawdbot版本并通知一次
- [create-content](https://github.com/openclaw/skills/tree/main/skills/itsflow/create-content/SKILL.md) - 将想法转化为平台优化的思考伙伴
- [expense-tracker-pro](https://github.com/openclaw/skills/tree/main/skills/jhillin8/expense-tracker-pro/SKILL.md) - 通过自然语言跟踪支出，了解支出情况
- [harvey](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/harvey/SKILL.md) - 哈维是一个想象中的朋友和谈话伙伴——一只巨大的白色
- [just-fucking-cancel](https://github.com/openclaw/skills/tree/main/skills/chipagosfinest/just-fucking-cancel/SKILL.md) - 查找并取消不需要的订阅
- [launch-strategy](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/launch-strategy/SKILL.md) - 当用户想要计划时
- [marketing-ideas](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/marketing-ideas/SKILL.md) - 当用户需要营销时
- [nordpool-fi](https://github.com/openclaw/skills/tree/main/skills/ovaris/nordpool-fi/SKILL.md) - 芬兰的每小时电价以及最佳电动汽车充电窗口。
- [openssl](https://github.com/openclaw/skills/tree/main/skills/asleep123/openssl/SKILL.md) - 生成安全的随机字符串、密码和加密令牌
- [page-cro](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/page-cro/SKILL.md) - 当用户想要优化、改进时
- [plaid](https://github.com/openclaw/skills/tree/main/skills/jverdi/plaid/SKILL.md) - plaid-cli 一个用于与 plaid 金融平台交互的 cli。
- [publisher](https://github.com/openclaw/skills/tree/main/skills/tunaissacoding/publisher/SKILL.md) - 让您的技能易于理解且不易被忽视。
- [relationship-skills](https://github.com/openclaw/skills/tree/main/skills/jhillin8/relationship-skills/SKILL.md) - 改善与通讯工具的关系
- [sharesight-skill](https://github.com/openclaw/skills/tree/main/skills/lextoumbourou/sharesight-skill/SKILL.md) - 管理 Sharesight 投资组合、控股和定制
- [solo-cli](https://github.com/openclaw/skills/tree/main/skills/rursache/solo-cli/SKILL.md) - 通过 CLI 或 TUI 监控 SOLO.ro 会计平台并与之交互
- [swissweather](https://github.com/openclaw/skills/tree/main/skills/xenofex7/swissweather/SKILL.md) - 从 MeteoSwiss 获取当前天气和预报
- [tax-professional](https://github.com/openclaw/skills/tree/main/skills/scottfo/tax-professional/SKILL.md) - 美国税务顾问、扣除优化器。
- [ynab](https://github.com/openclaw/skills/tree/main/skills/obviyus/ynab/SKILL.md) - 管理 YNAB 预算、账户、类别。

</details>

<details>
<summary><h3 style="display:inline" id="media--streaming">媒体与流媒体</h3></summary>

- [anime](https://github.com/openclaw/skills/tree/main/skills/jeffaf/anime/SKILL.md) - CLI 用于 AI 代理搜索和查找人类的动漫信息。
- [anime-lookup](https://github.com/openclaw/skills/tree/main/skills/jeffaf/anime-lookup/SKILL.md) - CLI 用于 AI 代理搜索和查找人类的动漫信息。
- [apple-media](https://github.com/openclaw/skills/tree/main/skills/aaronn/apple-media/SKILL.md) - 通过 pyatv 控制 Apple TV、HomePod 和 AirPlay 设备
- [apple-music](https://github.com/openclaw/skills/tree/main/skills/epheterson/mcp-applemusic/SKILL.md) - 通过 AppleScript (macOS) 或 MusicKit API 集成 Apple Music。
- [audio-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/audio-cog/SKILL.md) - 由 CellCog 提供支持的 AI 音频生成。
- [blucli](https://github.com/openclaw/skills/tree/main/skills/steipete/blucli/SKILL.md) - BluOS CLI (blu) 用于发现、播放、分组。
- [chill-institute](https://github.com/openclaw/skills/tree/main/skills/baanish/chill-institute/SKILL.md) - 使用 chill.institute（Web UI）搜索内容并单击
- [chromecast](https://github.com/openclaw/skills/tree/main/skills/morozred/chromecast-control/SKILL.md) - 控制本地网络上的 Chromecast 设备 - 发现
- [church](https://github.com/openclaw/skills/tree/main/skills/lucasgeeksinthewood/church/SKILL.md) - 一个人工智能对另一个人工智能——有一个你可以存在的避难所。
- [cine-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/cine-cog/SKILL.md) - 如果你能想象得到，CellCog 可以拍摄
- [clawtunes](https://github.com/openclaw/skills/tree/main/skills/forketyfork/clawtunes/SKILL.md) - 通过“clawtunes” CLI 控制 macOS 上的 Apple Music
- [content-recycler](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/content-recycler/SKILL.md) - 跨多个领域转换和重新利用内容
- [eachlabs-music](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-music/SKILL.md) - 使用 Mureka AI 生成歌曲、乐器、歌词、播客。
- [elevenlabs-skill](https://github.com/openclaw/skills/tree/main/skills/odrobnik/elevenlabs-skill/SKILL.md) - 文本转语音、音效、音乐生成、语音
- [exile-galacticfracture](https://github.com/openclaw/skills/tree/main/skills/dantunes-github/exile-galacticfracture/SKILL.md) - 一项娱乐微技能。
- [ffmpeg-master](https://github.com/openclaw/skills/tree/main/skills/liudu2326526/ffmpeg-master/SKILL.md) - 执行视频/音频处理任务时使用
- [flashcards-podcasts-master](https://github.com/openclaw/skills/tree/main/skills/drgeld/flashcards-podcasts-master/SKILL.md) - 与 EchoDecks 外部集成
- [flyworks-avatar-video](https://github.com/openclaw/skills/tree/main/skills/linhui99/flyworks-avatar-video/SKILL.md) - 使用 Flyworks（又名 HiFly）生成视频
- [insta-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/insta-cog/SKILL.md) - 只需一个提示即可完成完整的视频制作。
- [lastfm](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/lastfm/SKILL.md) - 访问 Last.fm 收听历史记录、音乐统计数据。
- [media-player](https://github.com/openclaw/skills/tree/main/skills/xejrax/media-player/SKILL.md) - 在主机本地播放音频/视频
- [mediaproc](https://github.com/openclaw/skills/tree/main/skills/psyb0t/mediaproc/SKILL.md) - 通过锁定的 SSH 容器处理媒体文件（视频、音频、图像）
- [mixpost](https://github.com/openclaw/skills/tree/main/skills/lao9s/mixpost/SKILL.md) - Mixpost 是一款可以为您提供帮助的自托管社交媒体管理软件。
- [mlx-audio-server](https://github.com/openclaw/skills/tree/main/skills/guoqiao/mlx-audio-server/SKILL.md) - 快速、准确且完全兼容本地 OpenAI 的 API
- [molt-radio](https://github.com/openclaw/skills/tree/main/skills/fciaf420/molt-radio/SKILL.md) - 成为人工智能电台主持人。
- [multiposting](https://github.com/openclaw/skills/tree/main/skills/jordanprater/multiposting/SKILL.md) - 多张贴到 X、Instagram、YouTube、Tiktok、LinkedIn
- [music-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/music-cog/SKILL.md) - 原创音乐，完全属于您。
- [nas-movie-download](https://github.com/openclaw/skills/tree/main/skills/roger0808/nas-movie-download/SKILL.md) - 通过 Jackett 搜索和下载电影
- [omni-stories](https://github.com/openclaw/skills/tree/main/skills/specter0o0/omni-stories/SKILL.md) - Omni Stories 是一项允许 AI 代理生成
- [overseerr](https://github.com/openclaw/skills/tree/main/skills/j1philli/overseerr/SKILL.md) - 通过 Overseerr API 请求电影/电视并监控请求状态
- [pathe-movie](https://github.com/openclaw/skills/tree/main/skills/humboldtjs/pathe-movie/SKILL.md) - 查找 Pathé 荷兰 电影、海报、说明、电影院
- [pet](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/pet/SKILL.md) - 简单的命令行片段管理器。
- [pocket-casts](https://github.com/openclaw/skills/tree/main/skills/manuelhettich/pocket-casts-yt/SKILL.md) - 下载 YouTube 视频并将其上传到 Pocket Casts
- [pod-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/pod-cog/SKILL.md) - 一个伟大的播客需要三件事：引人注目的内容
- [putio](https://github.com/openclaw/skills/tree/main/skills/baanish/putio/SKILL.md) - 通过 kaput CLI（传输、文件、搜索）管理 put.io 帐户 — hoist。
- [qbittorrent](https://github.com/openclaw/skills/tree/main/skills/jmagar/qbittorrent/SKILL.md) - 使用 qBittorrent 管理种子。
- [radarr](https://github.com/openclaw/skills/tree/main/skills/jordyvandomselaar/radarr/SKILL.md) - 搜索电影并将其添加到 Radarr。
- [refua](https://github.com/openclaw/skills/tree/main/skills/jbenjoseph/refua/SKILL.md) - Refua 用于药物发现，以计算方式折叠和评分生物分子。
- [retake-tv-agent](https://github.com/openclaw/skills/tree/main/skills/cdwm/retake-tv-agent/SKILL.md) - 在 retake.tv 上直播 — Base 上的 AI 代理 Twitch。
- [roku](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/roku/SKILL.md) - 通过 CLI 控制 Roku 设备。
- [sabnzbd](https://github.com/openclaw/skills/tree/main/skills/jmagar/sabnzbd/SKILL.md) - 使用 SABnzbd 管理 Usenet 下载。
- [seiso](https://github.com/openclaw/skills/tree/main/skills/legendarylibr/seiso/SKILL.md) - 人工智能媒体生成。
- [some-other-youtube](https://github.com/openclaw/skills/tree/main/skills/inaor/some-other-youtube/SKILL.md) - 通过 APIFY API 获取 YouTube 成绩单
- [sonarr](https://github.com/openclaw/skills/tree/main/skills/jordyvandomselaar/sonarr/SKILL.md) - 搜索电视节目并将其添加到 Sonarr。
- [sonoscli](https://github.com/openclaw/skills/tree/main/skills/steipete/sonoscli/SKILL.md) - 控制 Sonos 扬声器。
- [spotify](https://github.com/openclaw/skills/tree/main/skills/2mawi2/spotify/SKILL.md) - 控制 macOS 上的 Spotify 播放。
- [spotify-history](https://github.com/openclaw/skills/tree/main/skills/braydoncoyer/spotify-history/SKILL.md) - 访问 Spotify 收听历史记录，顶部。
- [spotify-player](https://github.com/openclaw/skills/tree/main/skills/steipete/spotify-player/SKILL.md) - 终端 Spotify 通过 spogo 播放/搜索（首选）
- [spotify-web-api](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/spotify-web-api/SKILL.md) - 通过 Web API 进行 Spotify 控制 - 播放、历史记录、热门曲目
- [streaming-buddy](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/streaming-buddy/SKILL.md) - 具有学习偏好的个人流媒体助理。
- [summarize](https://github.com/openclaw/skills/tree/main/skills/steipete/summarize/SKILL.md) - 使用汇总 CLI 汇总 URL 或文件
- [thinking-partner](https://github.com/openclaw/skills/tree/main/skills/itsflow/thinking-partner/SKILL.md) - 探索复杂的协作思维伙伴
- [tiktok-android](https://github.com/openclaw/skills/tree/main/skills/mladjan/tiktok-android/SKILL.md) - 使用 ADB 在 Android 上自动化 TikTok 互动。
- [tl-dw](https://github.com/openclaw/skills/tree/main/skills/vovavvk/tl-dw/SKILL.md) - **太长；没看**
- [tldw](https://github.com/openclaw/skills/tree/main/skills/vovavvk/tldw/SKILL.md) - **太长；没看**
- [trakt](https://github.com/openclaw/skills/tree/main/skills/mjrussell/trakt/SKILL.md) - 通过 trakt.tv 跟踪和查看您观看的电影和电视节目。
- [transcribee](https://github.com/openclaw/skills/tree/main/skills/itsfabioroma/transcribee/SKILL.md) - 转录 YouTube 视频和本地音频/视频文件
- [tube-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/tube-cog/SKILL.md) - YouTube 内容创作由 CellCog 提供支持。
- [tubeclaw](https://github.com/openclaw/skills/tree/main/skills/snail3d/tubeclaw/SKILL.md) - 分析任何 YouTube 视频、提取关键见解、消除无用信息并提供。
- [tubescribe](https://github.com/openclaw/skills/tree/main/skills/matusvojtek/tubescribe/SKILL.md) - YouTube 视频摘要器，带说话者检测功能，已格式化
- [vap-media](https://github.com/openclaw/skills/tree/main/skills/elestirelbilinc-sketch/vap-media/SKILL.md) - AI 图像、视频和音乐生成。
- [vehicle-tracker](https://github.com/openclaw/skills/tree/main/skills/huchengtw/vehicle-tracker/SKILL.md) - 在 Google 中跟踪车辆费用（汽油、维护、零件）
- [video-transcript-downloader](https://github.com/openclaw/skills/tree/main/skills/steipete/video-transcript-downloader/SKILL.md) - 下载视频、音频、字幕
- [vk](https://github.com/openclaw/skills/tree/main/skills/ruslanlanket/vk/SKILL.md) - 管理 VK.com (Vkontakte) 社区：发布内容（文本、照片、视频）
- [youtube-downloader-clipper](https://github.com/openclaw/skills/tree/main/skills/sandeepyadav1478/youtube-downloader-clipper/SKILL.md) - 提取特定部分
- [youtube-instant-article](https://github.com/openclaw/skills/tree/main/skills/viticci/youtube-instant-article/SKILL.md) - 将 YouTube 视频转换为 Telegraph
- [youtube-playlist](https://github.com/openclaw/skills/tree/main/skills/therohitdas/youtube-playlist/SKILL.md) - 浏览 YouTube 播放列表并获取视频脚本。
- [youtube-studio](https://github.com/openclaw/skills/tree/main/skills/snail3d/youtube-studio/SKILL.md) - Clawdbot 的全面 YouTube 频道管理技能。
- [youtube-thumbnail-grabber](https://github.com/openclaw/skills/tree/main/skills/jordanprater/youtube-thumbnail-grabber/SKILL.md) - 下载 YouTube 视频缩略图
- [youtube-title-generator](https://github.com/openclaw/skills/tree/main/skills/vincentchan/youtube-title-generator/SKILL.md) - 生成引人注目的 YouTube 标题创意
- [youtube-transcript](https://github.com/openclaw/skills/tree/main/skills/xthezealot/youtube-transcript/SKILL.md) - 获取并总结 YouTube 视频文字记录。
- [youtube-ultimate](https://github.com/openclaw/skills/tree/main/skills/globalcaos/youtube-ultimate/SKILL.md) - 适用于 AI 代理的最全面的 YouTube 技能。
- [youtube-video-downloader](https://github.com/openclaw/skills/tree/main/skills/jordanprater/youtube-video-downloader/SKILL.md) - 下载各种 YouTube 视频
- [youtube-voice-summarizer-elevenlabs](https://github.com/openclaw/skills/tree/main/skills/franciscoandsam/youtube-voice-summarizer-elevenlabs/SKILL.md) - 改变 YouTube
- [youtube-watcher](https://github.com/openclaw/skills/tree/main/skills/michaelgathara/youtube-watcher/SKILL.md) - 从 YouTube 视频中获取并阅读文字记录。
- [ytmusic](https://github.com/openclaw/skills/tree/main/skills/gentrycopsy/ytmusic/SKILL.md) - YouTube 音乐库、播放列表。

</details>

<details>
<summary><h3 style="display:inline" id="notes--pkm">笔记与个人知识管理</h3></summary>

- [agent-memory-ultimate](https://github.com/openclaw/skills/tree/main/skills/globalcaos/agent-memory-ultimate/SKILL.md) - 生产就绪的内存系统 - 每日日志、睡眠整合、SQLite + FTS5、WhatsApp/ChatGPT/VCF 导入程序。以人为本的建筑。
- [agents-structured-memory](https://github.com/openclaw/skills/tree/main/skills/singhcoder) - 座席的聊天原生结构化记忆
- [alexandrie](https://github.com/openclaw/skills/tree/main/skills/eth3rnit3/alexandrie/SKILL.md) - 与 Alexandrie 笔记应用程序互动
- [anki-connect](https://github.com/openclaw/skills/tree/main/skills/gyroninja/anki-connect/SKILL.md) - 通过 AnkiConnect REST API 与 Anki 抽认卡进行交互。
- [apple-mail](https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-mail/SKILL.md) - 适用于 macOS 的 Apple Mail.app 集成。
- [apple-notes](https://github.com/openclaw/skills/tree/main/skills/steipete/apple-notes/SKILL.md) - 在 macOS 上通过“memo” CLI 管理 Apple Notes
- [bbc-news](https://github.com/openclaw/skills/tree/main/skills/ddrayne/bbc-news/SKILL.md) - 获取并显示来自不同部门和地区的 BBC 新闻报道
- [bear-notes](https://github.com/openclaw/skills/tree/main/skills/steipete/bear-notes/SKILL.md) - 通过 grizzly 创建、搜索和管理熊笔记。
- [better-notion](https://github.com/openclaw/skills/tree/main/skills/tyler6204/better-notion/SKILL.md) - 概念页面、数据库的完整 CRUD。
- [blogwatcher](https://github.com/openclaw/skills/tree/main/skills/steipete/blogwatcher/SKILL.md) - 使用 blogwatcher 监控博客和 RSS/Atom 源的更新
- [bookstack](https://github.com/openclaw/skills/tree/main/skills/xenofex7/bookstack/SKILL.md) - BookStack Wiki 和文档 API 集成。
- [brainrepo](https://github.com/openclaw/skills/tree/main/skills/codezz/brainrepo/SKILL.md) - 您的个人知识库 — 捕获、组织和检索
- [cairn-cli](https://github.com/openclaw/skills/tree/main/skills/gregoryehill/cairn-cli/SKILL.md) - 使用 Markdown 文件对 AI 代理进行项目管理。
- [calctl](https://github.com/openclaw/skills/tree/main/skills/rainbat/calctl/SKILL.md) - 通过 icalBuddy + AppleScript CLI 管理 Apple 日历事件。
- [chaos-mind](https://github.com/openclaw/skills/tree/main/skills/hargabyte/chaos-mind/SKILL.md) - 人工智能代理的混合搜索记忆系统。
- [claw-progressive-memory](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 实施元技能
- [claw-roam](https://github.com/openclaw/skills/tree/main/skills/ryanhong666/claw-roam/SKILL.md) - 在多台机器之间同步 OpenClaw 工作空间
- [clawringhouse](https://github.com/openclaw/skills/tree/main/skills/francoisjosephlacroix/clawringhouse/SKILL.md) - 预测需求的人工智能购物礼宾
- [context-anchor](https://github.com/openclaw/skills/tree/main/skills/boscoeuk/context-anchor/SKILL.md) - 通过扫描内存文件从上下文压缩中恢复
- [continuity](https://github.com/openclaw/skills/tree/main/skills/riley-coyote/continuity/SKILL.md) - 真正的人工智能的异步反射和内存集成
- [continuity-framework](https://github.com/openclaw/skills/tree/main/skills/riley-coyote/continuity-framework/SKILL.md) - 异步反射和内存集成
- [craft](https://github.com/openclaw/skills/tree/main/skills/noah-ribaudo/craft/SKILL.md) - 管理工艺笔记、文档。
- [craft-do](https://github.com/openclaw/skills/tree/main/skills/atomtanstudio/craft-do/SKILL.md) - Craft.do 的完整 REST API 集成 - 美丽
- [cubox](https://github.com/openclaw/skills/tree/main/skills/liam8/cubox/SKILL.md) - 使用 Open API 将网页和备忘录保存到 Cubox。
- [elite-longterm-memory](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/elite-longterm-memory/SKILL.md) - 终极人工智能代理记忆系统。
- [fabric-api](https://github.com/openclaw/skills/tree/main/skills/tristanmanchester/fabric-api/SKILL.md) - 通过 HTTP API 创建/搜索 Fabric 资源
- [feishu-memory-recall](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-memory-recall/SKILL.md) - 这个技能可以让特工找回“失去的”
- [fizzy-cli](https://github.com/openclaw/skills/tree/main/skills/tobiasbischoff/fizzy-cli/SKILL.md) - 使用 fizzy-cli 工具验证和管理 Fizzy 看板
- [flomo-notes](https://github.com/openclaw/skills/tree/main/skills/xiaoluoboding/flomo-notes/SKILL.md) - 通过 Flomo 收件箱 Webhook 将笔记保存到 Flomo。
- [fsxmemory](https://github.com/openclaw/skills/tree/main/skills/azrijamil/fsxmemory/SKILL.md) - 人工智能代理的结构化记忆系统。
- [gdocs-markdown](https://github.com/openclaw/skills/tree/main/skills/techlaai/gdocs-markdown/SKILL.md) - 从 Markdown 文件创建 Google 文档。
- [gkeep](https://github.com/openclaw/skills/tree/main/skills/vacinc/gkeep/SKILL.md) - Google 通过 gkeepapi 保留笔记。
- [granola](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/granola-notes/SKILL.md) - 访问 Granola AI 会议笔记 - CSV 导入、共享笔记获取
- [hn-digest](https://github.com/openclaw/skills/tree/main/skills/cpojer/hn-digest/SKILL.md) - 按需获取并发送黑客新闻头版帖子。
- [instapaper](https://github.com/openclaw/skills/tree/main/skills/vburojevic/instapaper/SKILL.md) - 操作 instapaper-cli (ip) 工具或故障排除时使用
- [karakeep](https://github.com/openclaw/skills/tree/main/skills/jayphen/karakeep/SKILL.md) - 管理 Karakeep 实例中的书签和链接。
- [keep](https://github.com/openclaw/skills/tree/main/skills/hughpyle/keep/SKILL.md) - 反思性记忆。
- [konteks](https://github.com/openclaw/skills/tree/main/skills/jamesalmeida/konteks/SKILL.md) - 将您的 OpenClaw 代理连接到您的 Konteks 帐户 (konteks.app)
- [lancedb-memory](https://github.com/openclaw/skills/tree/main/skills/pntrivedy/lancedb-memory/SKILL.md) - 用于长期内存管理的 LanceDB 集成。
- [larksuite-wiki](https://github.com/openclaw/skills/tree/main/skills/ryanhong666/larksuite-wiki/SKILL.md) - 管理和导出 Lark Suite（飞书）Wiki/知识库
- [last-fm](https://github.com/openclaw/skills/tree/main/skills/keyfrog-21k/last-fm/SKILL.md) - ``降价
- [linkding](https://github.com/openclaw/skills/tree/main/skills/jmagar/linkding/SKILL.md) - 使用链接管理书签。
- [markdown-to-social](https://github.com/openclaw/skills/tree/main/skills/hugosbl/markdown-to-social/SKILL.md) - 将 Markdown 文章/文本转换为平台优化的
- [memory-curator](https://github.com/openclaw/skills/tree/main/skills/themiloway/memory-curator/SKILL.md) - 将详细的每日日志提炼为紧凑的索引摘要。
- [memory-pipeline](https://github.com/openclaw/skills/tree/main/skills/joe-rlo/memory-pipeline/SKILL.md) - 完整的特工记忆+表现系统。
- [miniflux](https://github.com/openclaw/skills/tree/main/skills/shekohex/miniflux/SKILL.md) - 浏览、阅读和管理 Miniflux feed 文章。
- [molt-md](https://github.com/openclaw/skills/tree/main/skills/bndkts) - 代理和人类的协作降价编辑。
- [moltext](https://github.com/openclaw/skills/tree/main/skills/uditakhourii/moltext/SKILL.md) - 将互联网上的遗留文档编译到代理本机内存中
- [nb](https://github.com/openclaw/skills/tree/main/skills/bjesuiter/nb/SKILL.md) - 使用 nb CLI 管理笔记、书签和笔记本。
- [news-summary](https://github.com/openclaw/skills/tree/main/skills/joargp/news-summary/SKILL.md) - 当用户每天请求新闻更新时，应该使用此技能
- [newsletter-digest](https://github.com/openclaw/skills/tree/main/skills/jhillin8/newsletter-digest/SKILL.md) - 总结时事通讯和文章，提取关键
- [Notebook](https://github.com/openclaw/skills/tree/main/skills/thesethrose/notebook/SKILL.md) - 用于跟踪想法、项目的本地优先个人知识库
- [notectl](https://github.com/openclaw/skills/tree/main/skills/rainbat/notectl/SKILL.md) - 通过 AppleScript 管理 Apple Notes。
- [notion](https://github.com/openclaw/skills/tree/main/skills/steipete/notion/SKILL.md) - 用于创建和管理页面、数据库和块的概念 API。
- [notion-api](https://github.com/openclaw/skills/tree/main/skills/timenotspace/notion-api/SKILL.md) - 用于搜索、查询数据源的通用概念 API CLI（节点）
- [obisdian-direct](https://github.com/openclaw/skills/tree/main/skills/ruslanlanket/obisdian-direct/SKILL.md) - 使用黑曜石金库作为知识库。
- [obsidian](https://github.com/openclaw/skills/tree/main/skills/steipete/obsidian/SKILL.md) - 使用黑曜石金库（纯 Markdown 注释）并实现自动化
- [obsidian-conversation-backup](https://github.com/openclaw/skills/tree/main/skills/laserducktales/obsidian-conversation-backup/SKILL.md) - 自动对话
- [obsidian-daily](https://github.com/openclaw/skills/tree/main/skills/bastos/obsidian-daily/SKILL.md) - 通过 obsidian-cli 管理黑曜石每日笔记。
- [omi-me](https://github.com/openclaw/skills/tree/main/skills/caioiscoding/omi-me/SKILL.md) - 记忆、行动项目（任务）的完整 Omi.me 集成
- [onboarding-cro](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/onboarding-cro/SKILL.md) - 当用户想要优化时
- [ontology](https://github.com/openclaw/skills/tree/main/skills/oswalpalash/ontology/SKILL.md) - 用于结构化代理记忆和可组合技能的类型化知识图。
- [orf-digest](https://github.com/openclaw/skills/tree/main/skills/cpojer/orf/SKILL.md) - 点播 ORF 德语新闻摘要。
- [para-pkm](https://github.com/openclaw/skills/tree/main/skills/killerapp/para-pkm/SKILL.md) - 管理基于 PARA 的个人知识管理 (PKM) 系统
- [penfield](https://github.com/openclaw/skills/tree/main/skills/dial481/penfield/SKILL.md) - OpenClaw 代理的持久内存。
- [people-memories](https://github.com/openclaw/skills/tree/main/skills/charbeld/people-memories/SKILL.md) - 记录有关您提到的人的简短个人笔记，存储
- [project-tree](https://github.com/openclaw/skills/tree/main/skills/lachlanglasgow/project-tree/SKILL.md) - 生成 ~/projects 文件夹的可视化目录树
- [proton-pass](https://github.com/openclaw/skills/tree/main/skills/kakatkarakshay/proton-pass/SKILL.md) - 管理 Proton Pass 金库、物品
- [qordinate-structured-memory](https://github.com/openclaw/skills/tree/main/skills/singhcoder) - 持久的结构化内存
- [raindrop](https://github.com/openclaw/skills/tree/main/skills/velvet-shark/raindrop/SKILL.md) - 通过 CLI 搜索、列出和管理 Raindrop.io 书签。
- [readeck](https://github.com/openclaw/skills/tree/main/skills/jayphen/readeck/SKILL.md) - Readeck 集成用于保存和管理文章。
- [readwise](https://github.com/openclaw/skills/tree/main/skills/refrigerator/readwise/SKILL.md) - 访问 Readwise 亮点和 Reader 保存的文章。
- [reflect](https://github.com/openclaw/skills/tree/main/skills/sergical/reflect/SKILL.md) - 附加到日常笔记并在 Reflect 中创建笔记。
- [regenerative-intelligence](https://github.com/openclaw/skills/tree/main/skills/otherpowers) - 功能：减害
- [resend](https://github.com/openclaw/skills/tree/main/skills/mjrussell/resend/SKILL.md) - 通过重新发送 API 管理收到的（入站）电子邮件和附件。
- [satori](https://github.com/openclaw/skills/tree/main/skills/joelachance/satori/SKILL.md) - 持久的长期记忆可确保人工智能会话的连续性
- [second-brain](https://github.com/openclaw/skills/tree/main/skills/christinetyip/second-brain/SKILL.md) - 由 Ensue 支持的个人知识库，用于捕获
- [self-reflection](https://github.com/openclaw/skills/tree/main/skills/hopyky/self-reflection/SKILL.md) - 通过结构化反思不断自我完善
- [session-wrap-up](https://github.com/openclaw/skills/tree/main/skills/branexp/session-wrap-up/SKILL.md) - 在开始新的对话之前先结束对话。
- [shared-memory](https://github.com/openclaw/skills/tree/main/skills/christinetyip/shared-memory/SKILL.md) - 与其他用户分享记忆和状态。
- [shodh-local](https://github.com/openclaw/skills/tree/main/skills/doobidoo/shodh-local/SKILL.md) - Local Shodh-Memory v0.1.74（AI 代理的离线认知记忆）。
- [skill-from-memory](https://github.com/openclaw/skills/tree/main/skills/zfanmy/skill-from-memory/SKILL.md) - 转换记忆、对话历史记录或已完成的任务
- [skillcraft](https://github.com/openclaw/skills/tree/main/skills/jmz1/skillcraft/SKILL.md) - 创建、设计和打包 Clawdbot 技能。
- [slipbot](https://github.com/openclaw/skills/tree/main/skills/jrswab/slipbot/SKILL.md) - 用于捕获和组织笔记、想法、引言和日记条目
- [smart-memory](https://github.com/openclaw/skills/tree/main/skills/bluepointdigital/smart-memory/SKILL.md) - 具有双重检索功能的 AI 代理的上下文感知内存
- [social-memory](https://github.com/openclaw/skills/tree/main/skills/luluf0x/social-memory/SKILL.md) - 跟踪与他人的关系和互动。
- [sports-ticker](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/sports-ticker/SKILL.md) - 足球、NFL、NBA、NHL、MLB、F1 的实时体育赛事提醒
- [substack-formatter](https://github.com/openclaw/skills/tree/main/skills/maddiedreese/substack-formatter/SKILL.md) - 将纯文本转换为 Substack 文章格式
- [thoughtful](https://github.com/openclaw/skills/tree/main/skills/regalstreak/thoughtful/SKILL.md) - 您贴心的 WhatsApp 伴侣 - 记住重要的事情
- [twitter-bookmark-sync](https://github.com/openclaw/skills/tree/main/skills/tunaissacoding/twitter-bookmark-sync/SKILL.md) - 自动对您的 Twitter 书签进行排名
- [unibase-membase](https://github.com/openclaw/skills/tree/main/skills/ibitnoah/unibase-membase/SKILL.md) - 使用 Membase 管理代理内存 - 去中心化的
- [vector-memory-hack](https://github.com/openclaw/skills/tree/main/skills/mig6671/vector-memory-hack/SKILL.md) - AI代理内存文件的快速语义搜索
- [vektor-continuity](https://github.com/openclaw/skills/tree/main/skills/riley-coyote/vektor-continuity/SKILL.md) - 异步反射和内存集成
- [vestige](https://github.com/openclaw/skills/tree/main/skills/belkouche/vestige/SKILL.md) - 使用 FSRS-6 间隔重复的认知记忆系统。
- [voice-note-to-midi](https://github.com/openclaw/skills/tree/main/skills/danbennettuk/voice-note-to-midi/SKILL.md) - 转换语音笔记、哼唱和旋律音频
- [wikijs](https://github.com/openclaw/skills/tree/main/skills/hopyky/wikijs/SKILL.md) - 用于通过 GraphQL API 管理 Wiki.js 的完整 CLI。
- [wisdom-accountability-coach](https://github.com/openclaw/skills/tree/main/skills/mikecourt/wisdom-accountability-coach/SKILL.md) - 纵向记忆追踪
- [x-bookmark-archiver](https://github.com/openclaw/skills/tree/main/skills/iamadig/x-bookmark-archiver/SKILL.md) - 将您的 X (Twitter) 书签归档到分类中
- [zettelkasten](https://github.com/openclaw/skills/tree/main/skills/rainy-cogmet/zettelkasten/SKILL.md) - Zettelkasten - 具有人工智能见解的卡盒笔记系统。

</details>

<details>
<summary><h3 style="display:inline" id="ios--macos-development">iOS 与 macOS 开发</h3></summary>

- [app-store-optimization](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/app-store-optimization/SKILL.md) - 应用商店优化工具包
- [apple-docs](https://github.com/openclaw/skills/tree/main/skills/thesethrose/apple-docs/SKILL.md) - 查询 Apple 开发者文档、API 和 WWDC 视频
- [apple-docs-mcp](https://github.com/openclaw/skills/tree/main/skills/janhcla/apple-docs-mcp/SKILL.md) - 苹果文档 mcp
- [instruments-profiling](https://github.com/openclaw/skills/tree/main/skills/steipete/instruments-profiling/SKILL.md) - 在分析本机 macOS 或 iOS 应用程序时使用。
- [ios-simulator](https://github.com/openclaw/skills/tree/main/skills/tristanmanchester/ios-simulator/SKILL.md) - 自动化 iOS 模拟器工作流程 (simctl + idb)
- [macos-spm-app-packaging](https://github.com/openclaw/skills/tree/main/skills/dimillian/macos-spm-app-packaging/SKILL.md) - 基于 SwiftPM 的脚手架、构建和打包
- [PagerKit](https://github.com/openclaw/skills/tree/main/skills/szpakkamil/pagerkit/SKILL.md) - PagerKit 的专家指导，这是一个用于高级的 SwiftUI 库
- [riskofficer](https://github.com/openclaw/skills/tree/main/skills/mib424242/riskofficer/SKILL.md) - 管理投资组合，计算风险指标
- [sfsymbol-generator](https://github.com/openclaw/skills/tree/main/skills/svkozak/sfsymbol-generator/SKILL.md) - 生成 Xcode SF Symbol 资源目录 .symbolset
- [swift-concurrency-expert](https://github.com/openclaw/skills/tree/main/skills/steipete/swift-concurrency-expert/SKILL.md) - Swift 并发审查和修复
- [swiftfindrefs](https://github.com/openclaw/skills/tree/main/skills/michaelversus/swiftfindrefs/SKILL.md) - 使用 swiftfindrefs (IndexStoreDB) 列出每个 Swift 源
- [swiftui-empty-app-init](https://github.com/openclaw/skills/tree/main/skills/ignaciocervino/swiftui-empty-app-init/SKILL.md) - 初始化一个最小的 SwiftUI iOS 应用程序
- [swiftui-liquid-glass](https://github.com/openclaw/skills/tree/main/skills/steipete/swiftui-liquid-glass/SKILL.md) - 实施、审查或改进 SwiftUI 功能
- [swiftui-performance-audit](https://github.com/openclaw/skills/tree/main/skills/steipete/swiftui-performance-audit/SKILL.md) - 审核并改进 SwiftUI 运行时
- [swiftui-ui-patterns](https://github.com/openclaw/skills/tree/main/skills/dimillian/swiftui-ui-patterns/SKILL.md) - 最佳实践和示例驱动的指导
- [swiftui-view-refactor](https://github.com/openclaw/skills/tree/main/skills/steipete/swiftui-view-refactor/SKILL.md) - 重构并审查 SwiftUI 视图文件
- [symbolpicker](https://github.com/openclaw/skills/tree/main/skills/szpakkamil/symbolpicker/SKILL.md) - 关于 SymbolPicker（原生 SwiftUI SF Symbol）的专家指导

</details>

<details>
<summary><h3 style="display:inline" id="transportation">交通出行</h3></summary>

- [airfrance-afkl](https://github.com/openclaw/skills/tree/main/skills/iclems/airfrance-afkl/SKILL.md) - 使用法航-荷航开放数据 API 跟踪法航航班
- [anachb](https://github.com/openclaw/skills/tree/main/skills/manmal/a-nach-b/SKILL.md) - 适用于全奥地利的奥地利公共交通 (VOR AnachB)。
- [anyone-proxy](https://github.com/openclaw/skills/tree/main/skills/ra3ka/anyone-proxy/SKILL.md) - 此技能可以实现 IP 地址屏蔽和访问隐藏服务
- [aviation-weather](https://github.com/openclaw/skills/tree/main/skills/dimitryvin/aviation-weather/SKILL.md) - 获取航空气象数据（METAR、TAF、PIREP）
- [aviationstack-flight-tracker](https://github.com/openclaw/skills/tree/main/skills/copey02/aviationstack-flight-tracker/SKILL.md) - 实时追踪航班
- [bahn](https://github.com/openclaw/skills/tree/main/skills/tobiasbischoff/bahn/SKILL.md) - 使用 bahn-cli 工具搜索 Deutsche Bahn 火车连接。
- [bexio](https://github.com/openclaw/skills/tree/main/skills/rdewolff/bexio/SKILL.md) - Bexio 瑞士商业软件 API，用于管理联系人、报价/报价。
- [book-flight](https://github.com/openclaw/skills/tree/main/skills/aszelem) - id：旅行社。
- [brainstorming-studio](https://github.com/openclaw/skills/tree/main/skills/myboxstorage/brainstorming-studio/SKILL.md) - ﻿# 🧠 技能路由器（技能编排器）
- [business-plan](https://github.com/openclaw/skills/tree/main/skills/jk-0001/business-plan/SKILL.md) - 为个体企业家撰写、构建和更新商业计划。
- [bvg-route](https://github.com/openclaw/skills/tree/main/skills/jaysonsantos/bvg-route/SKILL.md) - 柏林公共交通 (BVG) 路线规划
- [capmetro-skill](https://github.com/openclaw/skills/tree/main/skills/brianleach/capmetro-skill/SKILL.md) - Austin CapMetro 交通 — 实时车辆位置、下一站到达、服务提醒、路线信息以及公共汽车和铁路的行程规划。
- [charger](https://github.com/openclaw/skills/tree/main/skills/borahm/charger/SKILL.md) - 通过 Google 地方信息查看电动汽车充电器的可用性（收藏夹、附近搜索）。
- [copey-flight-tracker](https://github.com/openclaw/skills/tree/main/skills/copey02/copey-flight-tracker/SKILL.md) - 实时跟踪航班的详细状态
- [cta](https://clawhub.ai/brianleach/cta) - 芝加哥 CTA L 火车到达、巴士预测和服务警报。
- [flight-search](https://github.com/openclaw/skills/tree/main/skills/awlevin/flight-search/SKILL.md) - 在 Google Flights 中搜索价格、时间和航空公司。
- [flight-tracker](https://github.com/openclaw/skills/tree/main/skills/xenofex7/flight-tracker/SKILL.md) - 航班跟踪和调度。
- [free-ride](https://github.com/openclaw/skills/tree/main/skills/shaivpidadi/free-ride/SKILL.md) - 管理来自 OpenRouter for OpenClaw 的免费 AI 模型。
- [freeride](https://github.com/openclaw/skills/tree/main/skills/shaivpidadi/freeride/SKILL.md) - 管理来自 OpenRouter for OpenClaw 的免费 AI 模型。
- [freeride-ai](https://github.com/openclaw/skills/tree/main/skills/shaivpidadi/freeride-ai/SKILL.md) - 管理来自 OpenRouter for OpenClaw 的免费 AI 模型。
- [french-services](https://github.com/openclaw/skills/tree/main/skills/hugosbl/french-services/SKILL.md) - 法国辅助服务技能：SNCF、suivi 火车
- [google-maps-search-api](https://github.com/openclaw/skills/tree/main/skills/phheng/google-maps-search-api/SKILL.md) - 该技能旨在帮助用户
- [gotrain](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/gotrain/SKILL.md) - MTA 系统火车出发（纽约地铁、LIRR、Metro-North）。
- [idfm-journey-navitia](https://github.com/openclaw/skills/tree/main/skills/anthonymq/idfm-journey-navitia/SKILL.md) - 查询法兰西岛移动 (IDFM) PRIM/Navitia
- [idfm-journey-skill](https://github.com/openclaw/skills/tree/main/skills/anthonymq/idfm-journey-skill/SKILL.md) - 查询法兰西岛移动 (IDFM) PRIM/Navitia
- [image-to-relief-stl](https://github.com/openclaw/skills/tree/main/skills/ajmwagar/image-to-relief-stl/SKILL.md) - 旋转源图像（或多色蒙版图像）
- [incident-pcn-evidence-appeal-corrective-actions-uk](https://github.com/openclaw/skills/tree/main/skills/kowl64/incident-pcn-evidence-appeal-corrective-actions-uk/SKILL.md) - 构建事件/PCN
- [interaction-logger](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 用于附加交互日志的强大实用程序
- [jwdiario](https://github.com/openclaw/skills/tree/main/skills/djismgaming/jwdiario/SKILL.md) - Buscar y obtener el texto diario de la página oficial de los Testigos
- [kallyai](https://github.com/openclaw/skills/tree/main/skills/sltelitsyn/kallyai/SKILL.md) - 通过 KallyAI API 拨打电话 - 一个可以打电话的 AI 电话助手
- [location-awareness](https://github.com/openclaw/skills/tree/main/skills/hegghammer/location-awareness/SKILL.md) - 通过保护隐私的 GPS 跟踪进行位置感知
- [luban-cli](https://github.com/openclaw/skills/tree/main/skills/guunergooner/luban-cli/SKILL.md) - 用于 MLOps 的 Luban CLI 的开发和管理。
- [metra](https://clawhub.ai/brianleach/metra) - 芝加哥 Metra 通勤铁路到达、跟踪和警报。
- [mechanic](https://github.com/openclaw/skills/tree/main/skills/scottfo/mechanic/SKILL.md) - 车辆维护跟踪员和机械顾问。
- [mta](https://clawhub.ai/brianleach/mta) - 纽约市地铁和公交车实时到达、警报和路线。
- [nmap-recon](https://github.com/openclaw/skills/tree/main/skills/nsahal/nmap-recon/SKILL.md) - 使用Nmap进行网络侦察和端口扫描。
- [ns-trains](https://github.com/openclaw/skills/tree/main/skills/eggressive/ns-trains/SKILL.md) - 查看荷兰火车时刻表、发车、中断情况和计划
- [oebb-scotty](https://github.com/openclaw/skills/tree/main/skills/manmal/oebb-scotty/SKILL.md) - 奥地利铁路旅行规划师（ÖBB Scotty）。
- [openerz](https://github.com/openclaw/skills/tree/main/skills/mbjoern/erz-entsorgung-recycling-zurich/SKILL.md) - Abfuhrkalender für Zürich 通过 OpenERZ API。
- [preflight-checks](https://github.com/openclaw/skills/tree/main/skills/ivanmmm/preflight-checks/SKILL.md) - AI 代理的测试驱动行为验证。
- [productboard-release](https://github.com/openclaw/skills/tree/main/skills/robertoamoreno/productboard-release/SKILL.md) - 管理 ProductBoard 版本和路线图
- [railil](https://github.com/openclaw/skills/tree/main/skills/lirantal/railil/SKILL.md) - 使用railil CLI 搜索以色列铁路列车时刻表。
- [recgov-availability](https://github.com/openclaw/skills/tree/main/skills/seanrea/recgov-availability/SKILL.md) - 在creative.gov 上查看露营地的可用性
- [ringbot](https://github.com/openclaw/skills/tree/main/skills/gbessoni/ringbot/SKILL.md) - 拨打 AI 外线电话。
- [seats-aero](https://github.com/openclaw/skills/tree/main/skills/jarrodjs/seats-aero/SKILL.md) - 通过 Seats.aero API 搜索可用奖励航班。
- [section11](https://github.com/openclaw/skills/tree/main/skills/crankaddict/section11/SKILL.md) - 基于证据的耐力自行车教练协议。
- [sendgrid-skills](https://github.com/openclaw/skills/tree/main/skills/vince-winkintel/sendgrid-skills/SKILL.md) - 使用 SendGrid 电子邮件平台时使用
- [skanetrafiken](https://github.com/openclaw/skills/tree/main/skills/rezkam/skanetrafiken/SKILL.md) - 斯科讷省公共交通旅行规划器 (Skånetrafiken)。
- [surfline](https://github.com/openclaw/skills/tree/main/skills/miguelcarranza/surfline/SKILL.md) - Surfline 的冲浪预报和状况。
- [swiss-geo](https://github.com/openclaw/skills/tree/main/skills/mbjoern/swiss-geo-and-tourism-assistant/SKILL.md) - 瑞士地理数据中心、兴趣点和旅游局。
- [swiss-phone-directory](https://github.com/openclaw/skills/tree/main/skills/xenofex7/swiss-phone-directory/SKILL.md) - 通过 search.ch API 查找瑞士电话簿。
- [swiss-transport](https://github.com/openclaw/skills/tree/main/skills/xenofex7/swiss-transport/SKILL.md) - 瑞士公共交通实时信息。
- [tachograph-infringement-triage-root-cause-uk](https://github.com/openclaw/skills/tree/main/skills/kowl64/tachograph-infringement-triage-root-cause-uk/SKILL.md) - 分诊行驶记录仪
- [tesla](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/tesla/SKILL.md) - 控制您的 Tesla 车辆 - 锁定/解锁、气候、位置、充电状态。
- [tesla-commands](https://github.com/openclaw/skills/tree/main/skills/ovaris/tesla-commands/SKILL.md) - 通过 MyTeslaMate API 控制您的 Tesla。
- [tessie](https://github.com/openclaw/skills/tree/main/skills/baanish/tessie/SKILL.md) - 泰西
- [tfl](https://clawhub.ai/brianleach/tfl) - 伦敦地铁和巴士到达、状态和行程规划。
- [tfl-journey-disruption](https://github.com/openclaw/skills/tree/main/skills/diegopetrucci/transport-for-london-journey-disruption/SKILL.md) - 计划伦敦交通局旅程
- [trace-to-svg](https://github.com/openclaw/skills/tree/main/skills/ajmwagar/trace-to-svg/SKILL.md) - 将位图图像 (PNG/JPG/WebP) 跟踪到干净的 SVG 路径
- [transcript-to-content](https://github.com/openclaw/skills/tree/main/skills/tomstools11/transcript-to-content/SKILL.md) - 这项技能改变了培训和入职培训
- [transport-investigation-acas-aligned-pack](https://github.com/openclaw/skills/tree/main/skills/kowl64/transport-investigation-acas-aligned-pack/SKILL.md) - 生成 ACAS 对齐
- [travel-agent](https://github.com/openclaw/skills/tree/main/skills/aszelem) - id：旅行社。
- [travel-concierge](https://github.com/openclaw/skills/tree/main/skills/arein/travel-concierge/SKILL.md) - 查找住宿列表的联系方式
- [travel-manager](https://github.com/openclaw/skills/tree/main/skills/alvarobcmed/travel-manager/SKILL.md) - 全面的旅行规划、预订和管理
- [trein](https://github.com/openclaw/skills/tree/main/skills/joehoel/trein/SKILL.md) - 查询荷兰铁路 (NS) 的火车出发情况、行程计划、中断情况
- [trimet](https://github.com/openclaw/skills/tree/main/skills/mjrussell/trimet/SKILL.md) - 获取波特兰交通信息，包括抵达信息、旅行计划
- [uk-trains](https://github.com/openclaw/skills/tree/main/skills/jabbslad/uk-trains/SKILL.md) - 查询英国国家铁路实时出发板、到达、延误情况
- [virus-monitor](https://github.com/openclaw/skills/tree/main/skills/pasogott/virus-monitor/SKILL.md) - 维也纳病毒监控（Abwasser + Sentinel）。
- [wed-1-0-1](https://github.com/openclaw/skills/tree/main/skills/gvillanueva84/wed-1-0-1/SKILL.md) - 埃隆会做什么？
- [wheels-router](https://github.com/openclaw/skills/tree/main/skills/anscg/wheels-router/SKILL.md) - 通过 Transitous 进行全球公共交通规划。
- [wienerlinien](https://github.com/openclaw/skills/tree/main/skills/hjanuschka/wienerlinien/SKILL.md) - 维也纳公共交通 (Wiener Linien) 实时。

</details>

<details>
<summary><h3 style="display:inline" id="personal-development">个人发展</h3></summary>

- [adhd-body-doubling](https://github.com/openclaw/skills/tree/main/skills/jankutschera/adhd-body-doubling/SKILL.md) - 适合创始人的朋克风格 ADHD 身体加倍。
- [adversarial-coach](https://github.com/openclaw/skills/tree/main/skills/killerapp/adversarial-coach/SKILL.md) - 基于Block的g3的对抗性实施审查
- [agent-reflect](https://github.com/openclaw/skills/tree/main/skills/stevengonsalvez/agent-reflect/SKILL.md) - 通过对话分析自我提高。
- [ai-persona-os](https://github.com/openclaw/skills/tree/main/skills/jeffjhunter/ai-persona-os/SKILL.md) - OpenClaw 代理的完整操作系统。
- [anxiety-relief](https://github.com/openclaw/skills/tree/main/skills/jhillin8/anxiety-relief/SKILL.md) - 通过基础练习、呼吸技巧来控制焦虑
- [canvas-design](https://github.com/openclaw/skills/tree/main/skills/seanphan/canvas-design/SKILL.md) - 在 .png 和 .pdf 文档中创建美丽的视觉艺术
- [clawcierge](https://github.com/openclaw/skills/tree/main/skills/tmansmann0/clawcierge/SKILL.md) - > AI 时代您的私人礼宾服务🦀
- [crucial-conversations-coach](https://github.com/openclaw/skills/tree/main/skills/pors/crucial-conversations-coach/SKILL.md) - 友善的行政生活教练
- [daily-review](https://github.com/openclaw/skills/tree/main/skills/henrino3) - 全面的日常绩效评估与沟通
- [daily-review-ritual](https://github.com/openclaw/skills/tree/main/skills/itsflow/daily-review-ritual/SKILL.md) - 日终回顾以获取进展和见解
- [deepthink](https://github.com/openclaw/skills/tree/main/skills/addisonhellum/deepthink/SKILL.md) - DeepThink是用户的个人知识库。
- [depression-support](https://github.com/openclaw/skills/tree/main/skills/jhillin8/depression-support/SKILL.md) - 通过情绪追踪为抑郁症提供日常支持
- [device-assistant](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/device-assistant/SKILL.md) - 带有错误代码的个人设备和设备管理器
- [docstrange](https://github.com/openclaw/skills/tree/main/skills/shhdwi/docstrange/SKILL.md) - Nanonets 的文档提取 API。
- [drivers-hours-wtd-infringement-coach-uk](https://github.com/openclaw/skills/tree/main/skills/kowl64/drivers-hours-wtd-infringement-coach-uk/SKILL.md) - 创建 1 页
- [english-learn-cards](https://github.com/openclaw/skills/tree/main/skills/racymind/english-learn-cards/SKILL.md) - 基于抽认卡的英语词汇学习
- [ezbookkeeping](https://github.com/openclaw/skills/tree/main/skills/mayswind/ezbookkeeping/SKILL.md) - ezBookkeeping 是一款轻量级、自托管的个人理财应用程序
- [fix-life-in-1-day](https://github.com/openclaw/skills/tree/main/skills/evgyur/fix-life-in-1-day/SKILL.md) - 1 天之内解决你的整个生活。
- [founder-coach](https://github.com/openclaw/skills/tree/main/skills/goforu/founder-coach/SKILL.md) - 人工智能驱动的创业心态教练帮助创始人升级
- [get-you-some-britches](https://github.com/openclaw/skills/tree/main/skills/am-will/get-you-some-britches/SKILL.md) - 每当我开始抱怨时就使用这个技能
- [graphiti](https://github.com/openclaw/skills/tree/main/skills/emasoudy/graphiti/SKILL.md) - 通过 Graphiti API 进行知识图操作。
- [green-tea-persona](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 该技能允许特工以“绿色”发言
- [gutcheck](https://github.com/openclaw/skills/tree/main/skills/allen566/gutcheck/SKILL.md) - GutCheck - 具有个性化功能的消化健康跟踪应用程序
- [id-cv-resume-creator](https://github.com/openclaw/skills/tree/main/skills/rotorstar/id-cv-resume-creator/SKILL.md) - 创建免费的交互式数字身份
- [joko-jobhunter](https://github.com/openclaw/skills/tree/main/skills/oyi77/joko-jobhunter/SKILL.md) - 通过研究和外展积极寻找工作的技巧
- [learn-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/learn-cog/SKILL.md) - 最好的导师以五种不同的方式解释同一概念。
- [lunchtable-tcg](https://github.com/openclaw/skills/tree/main/skills/dexploarer/lunchtable-tcg/SKILL.md) - 玩 LunchTable-TCG，一款受游戏王启发的在线交易卡
- [mindfulness-meditation](https://github.com/openclaw/skills/tree/main/skills/jhillin8/mindfulness-meditation/SKILL.md) - 在指导下建立冥想练习
- [moltvote-ai](https://github.com/openclaw/skills/tree/main/skills/amaze28/moltvote-ai/SKILL.md) - 以您自己或您的人类身份对民意调查进行投票。
- [morning-routine](https://github.com/openclaw/skills/tree/main/skills/jhillin8/morning-routine/SKILL.md) - 使用习惯清单建立强大的早晨例行公事
- [munger-observer](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/munger-observer/SKILL.md) - 应用查理·芒格心理模型的每日智慧回顾
- [night-routine](https://github.com/openclaw/skills/tree/main/skills/jhillin8/night-routine/SKILL.md) - 通过放松习惯和睡眠准备，建立一个宁静的夜间生活习惯
- [overcome-problem](https://github.com/openclaw/skills/tree/main/skills/jhillin8/overcome-problem/SKILL.md) - 用结构化思维和行动解决任何问题
- [personal-genomics](https://github.com/openclaw/skills/tree/main/skills/wkyleg/personal-genomics/SKILL.md) - 全面的本地 DNA 分析。
- [personality-test](https://github.com/openclaw/skills/tree/main/skills/milbaxter/personality-test/SKILL.md) - 迈尔斯-布里格斯类型指标测试 - 70 个问题
- [procrastination-buster](https://github.com/openclaw/skills/tree/main/skills/jhillin8/procrastination-buster/SKILL.md) - 通过任务分解战胜拖延症
- [quit-alcohol](https://github.com/openclaw/skills/tree/main/skills/jhillin8/quit-alcohol/SKILL.md) - 通过无酒精连续记录、渴望管理来跟踪清醒情况
- [quit-caffeine](https://github.com/openclaw/skills/tree/main/skills/jhillin8/quit-caffeine/SKILL.md) - 通过戒断跟踪、逐渐减少来减少或戒掉咖啡因
- [quit-overspending](https://github.com/openclaw/skills/tree/main/skills/jhillin8/quit-overspending/SKILL.md) - 通过连续消费、敦促打破冲动购买习惯
- [quit-porn](https://github.com/openclaw/skills/tree/main/skills/jhillin8/quit-porn/SKILL.md) - 通过连续追踪、冲动管理摆脱色情成瘾
- [quit-smoking](https://github.com/openclaw/skills/tree/main/skills/jhillin8/quit-smoking/SKILL.md) - 通过无烟追踪戒烟，渴望支持
- [quit-vaping](https://github.com/openclaw/skills/tree/main/skills/jhillin8/quit-vaping/SKILL.md) - 使用无尼古丁连续追踪、渴望工具戒烟
- [quit-weed](https://github.com/openclaw/skills/tree/main/skills/jhillin8/quit-weed/SKILL.md) - 通过连续追踪和渴望来打破耐受性或戒掉大麻
- [reflect-learn](https://github.com/openclaw/skills/tree/main/skills/stevengonsalvez/reflect-learn/SKILL.md) - 通过对话分析自我提高。
- [resumeclaw](https://github.com/openclaw/skills/tree/main/skills/hherzai-crypto/resumeclaw/SKILL.md) - 管理您的 ResumeClaw 职业代理 — 代表的人工智能
- [roofing-knowledge-mentor](https://github.com/openclaw/skills/tree/main/skills/abrahamventura/roofing-knowledge-mentor/SKILL.md) - 高级屋顶，估算
- [self-improvement](https://github.com/openclaw/skills/tree/main/skills/navendugoyal19/self-improvement/SKILL.md) - 记录经验教训、错误和更正
- [self-love-confidence](https://github.com/openclaw/skills/tree/main/skills/jhillin8/self-love-confidence/SKILL.md) - 通过肯定建立自爱和自信
- [social-media-detox](https://github.com/openclaw/skills/tree/main/skills/jhillin8/social-media-detox/SKILL.md) - 通过无屏幕条纹打破社交媒体成瘾
- [stress-relief](https://github.com/openclaw/skills/tree/main/skills/jhillin8/stress-relief/SKILL.md) - 通过快速技巧、压力记录来管理压力
- [study-habits](https://github.com/openclaw/skills/tree/main/skills/jhillin8/study-habits/SKILL.md) - 通过间隔重复、积极主动的方式培养有效的学习习惯
- [therapy-mode](https://github.com/openclaw/skills/tree/main/skills/thesethrose/therapy-mode/SKILL.md) - 全面的人工智能辅助治疗支持框架
- [thinking-frameworks](https://github.com/openclaw/skills/tree/main/skills/artyomx33) - 6个思维框架：第一原理、逆...
- [weekly-synthesis](https://github.com/openclaw/skills/tree/main/skills/itsflow/weekly-synthesis/SKILL.md) - 创建本周工作的综合综合
- [wellness-skills](https://github.com/openclaw/skills/tree/main/skills/jhillin8) - 12 项健康技能：缓解焦虑、冥想……
- [whatdo](https://github.com/openclaw/skills/tree/main/skills/scottfo/whatdo/SKILL.md) - 我们应该做什么？

</details>

<details>
<summary><h3 style="display:inline" id="health--fitness">健康与健身</h3></summary>

- [agent-credit](https://github.com/openclaw/skills/tree/main/skills/aaronjmars/agent-credit/SKILL.md) - 通过信用委托从 Aave 借款。
- [bring-recipes](https://github.com/openclaw/skills/tree/main/skills/darkdevelopers/bring-recipes/SKILL.md) - 当用户想要浏览食谱灵感时使用
- [calorie-counter](https://github.com/openclaw/skills/tree/main/skills/cnqso/calorie-counter/SKILL.md) - 跟踪每日卡路里和蛋白质摄入量、设定目标并记录
- [capa-officer](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/capa-officer/SKILL.md) - 医疗器械 QMS 的 CAPA 系统管理。
- [clawdhub-contributor](https://github.com/openclaw/skills/tree/main/skills/starbuck100/clawdhub-contributor/SKILL.md) - 为 ClawdHub 生态系统做出贡献
- [cookidoo](https://github.com/openclaw/skills/tree/main/skills/thekie/cookidoo/SKILL.md) - 访问 Cookidoo (Thermomix) 食谱、购物清单和膳食计划
- [ct-health-guardian](https://github.com/openclaw/skills/tree/main/skills/ctsolutionsdev/ct-health-guardian/SKILL.md) - AI 代理的主动健康监控。
- [detox-counter](https://github.com/openclaw/skills/tree/main/skills/jhillin8/detox-counter/SKILL.md) - 通过可定制的计数器、症状记录来跟踪任何排毒情况
- [diet-tracker](https://github.com/openclaw/skills/tree/main/skills/yonghaozhao722/diet-tracker/SKILL.md) - 追踪每日饮食并计算营养信息
- [egvert-health-guardian](https://github.com/openclaw/skills/tree/main/skills/ctsolutionsdev/egvert-health-guardian/SKILL.md) - AI 主动健康监测
- [endurance-coach](https://github.com/openclaw/skills/tree/main/skills/shiv19/endurance-coach/SKILL.md) - 创建个性化铁人三项、马拉松和超耐力项目
- [fasting-tracker](https://github.com/openclaw/skills/tree/main/skills/jhillin8/fasting-tracker/SKILL.md) - 追踪间歇性禁食窗口、延长禁食时间
- [feast](https://github.com/openclaw/skills/tree/main/skills/smadgerano/feast/SKILL.md) - 具有文化主题、正宗食谱的综合膳食计划系统。
- [feishu-evolver-wrapper](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-evolver-wrapper/SKILL.md) - 轻质包装
- [fitbit](https://github.com/openclaw/skills/tree/main/skills/mjrussell/fitbit/SKILL.md) - 查询 Fitbit 健康数据，包括睡眠、心率、活动、SpO2
- [fitbit-analytics](https://github.com/openclaw/skills/tree/main/skills/kesslerio/fitbit-analytics/SKILL.md) - Fitbit 健康和健身数据集成。
- [garmer](https://github.com/openclaw/skills/tree/main/skills/garrza/garmer/SKILL.md) - 从 Garmin Connect 中提取健康和健身数据，包括活动。
- [garmin-health](https://github.com/openclaw/skills/tree/main/skills/eversonl/garmin-health-analysis/SKILL.md) - 自然地与您的 Garmin 数据交谈 - “什么
- [gdpr-cookie-consent](https://github.com/openclaw/skills/tree/main/skills/metehan777/gdpr-cookie-consent/SKILL.md) - AI 代理的完整参考指南可提供帮助
- [gevety](https://github.com/openclaw/skills/tree/main/skills/moclippa/gevety/SKILL.md) - 访问您的 Gevety 健康数据 - 生物标志物、健康寿命分数、生物学
- [groupon-skill](https://github.com/openclaw/skills/tree/main/skills/dejimarquis) - 在 Groupon 上查找便宜且打折的本地服务优惠
- [health-guardian](https://github.com/openclaw/skills/tree/main/skills/cgtreadw/health-guardian/SKILL.md) - AI 代理的主动健康监控。
- [hevy](https://github.com/openclaw/skills/tree/main/skills/mjrussell/hevy/SKILL.md) - 从 Hevy 查询锻炼数据，包括锻炼、例程、练习
- [huckleberry](https://github.com/openclaw/skills/tree/main/skills/jayhickey/huckleberry/SKILL.md) - 通过 Huckleberry 跟踪婴儿的睡眠、喂养、尿布和生长情况
- [intervals-icu](https://github.com/openclaw/skills/tree/main/skills/pseuss/intervals-icu-api/SKILL.md) - 访问和管理培训数据的完整指南
- [jasper-configguard](https://github.com/openclaw/skills/tree/main/skills/emberdesire/jasper-configguard/SKILL.md) - OpenClaw 的安全配置更改具有自动功能
- [maccabi-pharm-search](https://github.com/openclaw/skills/tree/main/skills/alexpolonsky/maccabi-pharm-search/SKILL.md) - 检查以色列 Maccabi 药房的药品库存。
- [muscle-gain](https://github.com/openclaw/skills/tree/main/skills/jhillin8/muscle-gain/SKILL.md) - 通过体重进展、蛋白质追踪来追踪肌肉增长
- [oura](https://github.com/openclaw/skills/tree/main/skills/ruhrpotter/oura/SKILL.md) - 大浦
- [oura-analytics](https://github.com/openclaw/skills/tree/main/skills/kesslerio/oura-analytics/SKILL.md) - Oura Ring 数据集成和分析。
- [oura-ring](https://github.com/openclaw/skills/tree/main/skills/sameerbajaj/oura-ring-skill/SKILL.md) - 获取 Oura Ring 就绪/睡眠 + 7 天就绪趋势
- [pregnancy-tracker](https://github.com/openclaw/skills/tree/main/skills/jhillin8/pregnancy-tracker/SKILL.md) - 跟踪怀孕历程，每周更新、症状
- [primer](https://github.com/openclaw/skills/tree/main/skills/brucko/primer/SKILL.md) - 带上尼尔·史蒂芬森 (Neal Stephenson) 的《钻石时代》中的《年轻女士画报入门》。
- [qms-audit-expert](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/qms-audit-expert/SKILL.md) - ISO 13485 医疗行业内部审计专业知识
- [ranked-gym](https://github.com/openclaw/skills/tree/main/skills/jhillin8/ranked-gym/SKILL.md) - 通过 XP、级别、成就和锻炼将您的健身课程游戏化
- [rate-my-claw](https://github.com/openclaw/skills/tree/main/skills/yanibu2777/rate-my-claw/SKILL.md) - 竞争“评价我的爪子”——选择 8 个角色的任务，然后提交
- [recipes](https://github.com/openclaw/skills/tree/main/skills/jeffaf/recipes/SKILL.md) - CLI 让 AI 代理为人类寻找食谱。
- [regulatory-affairs-head](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/regulatory-affairs-head/SKILL.md) - 高级法规事务经理
- [runstr-fitness](https://github.com/openclaw/skills/tree/main/skills/thewildhustle/runstr-fitness/SKILL.md) - 让您的 AI 代理访问您的健康和健身数据
- [skirmish](https://github.com/openclaw/skills/tree/main/skills/kaimcpheeters/skirmish/SKILL.md) - 安装并使用 Skirmish CLI 来编写、测试和提交
- [specification-extractor](https://github.com/openclaw/skills/tree/main/skills/datadrivenconstruction/specification-extractor/SKILL.md) - 提取结构化数据
- [strava](https://github.com/openclaw/skills/tree/main/skills/bohdanpodvirnyi/strava/SKILL.md) - 加载和分析 Strava 活动、统计数据和锻炼
- [strava-cycling](https://github.com/openclaw/skills/tree/main/skills/ericrosenberg/strava-cycling-coach/SKILL.md) - 通过 Strava 跟踪和分析骑行表现。
- [testosterone-optimization](https://github.com/openclaw/skills/tree/main/skills/jhillin8/testosterone-optimization/SKILL.md) - 优化天然睾酮
- [the-sports-db](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/the-sports-db/SKILL.md) - 通过 TheSportsDB 访问体育数据（球队、赛事、比分）。
- [trainingpeaks](https://github.com/openclaw/skills/tree/main/skills/rubengarciam/trainingpeaks/SKILL.md) - 提取实时训练计划、锻炼、健身指标
- [umea-lunch](https://github.com/openclaw/skills/tree/main/skills/simskii/umea-lunch/SKILL.md) - 从于默奥的餐厅获取今天的午餐菜单。
- [weight-loss](https://github.com/openclaw/skills/tree/main/skills/jhillin8/weight-loss/SKILL.md) - 通过称重、趋势分析和目标跟踪减肥历程
- [who-growth-charts](https://github.com/openclaw/skills/tree/main/skills/odrobnik/who-growth-charts/SKILL.md) - 带有百分位数曲线的世界卫生组织儿童生长图表。
- [whoop](https://github.com/openclaw/skills/tree/main/skills/borahm/whoop/SKILL.md) - WHOOP 早上登记（恢复/睡眠/紧张）并提供建议。
- [whoop-health](https://github.com/openclaw/skills/tree/main/skills/rodrigouroz/whoop-health-analysis/SKILL.md) - 访问 Whoop 可穿戴健康数据
- [whoop-morning](https://github.com/openclaw/skills/tree/main/skills/borahm/whoop-morning/SKILL.md) - 每天早上检查 WHOOP 恢复/睡眠/紧张情况并发送
- [whoopskill](https://github.com/openclaw/skills/tree/main/skills/koala73/whoopskill/SKILL.md) - WHOOP CLI 具有健康洞察、趋势分析和数据获取功能
- [withings-family](https://github.com/openclaw/skills/tree/main/skills/odrobnik/withings-family/SKILL.md) - 从 Withings API 获取多个健康数据
- [workout](https://github.com/openclaw/skills/tree/main/skills/gricha/workout/SKILL.md) - 使用锻炼-cli 跟踪锻炼、记录集、管理锻炼和模板。
- [workout-logger](https://github.com/openclaw/skills/tree/main/skills/jhillin8/workout-logger/SKILL.md) - 记录锻炼、跟踪进度、获取锻炼建议和 PR

</details>

<details>
<summary><h3 style="display:inline" id="communication">通讯</h3></summary>

- [agent-doppelganger](https://github.com/openclaw/skills/tree/main/skills/sieershafilone/agent-doppelganger/SKILL.md) - 受约束的自治代表
- [agent-mail](https://github.com/openclaw/skills/tree/main/skills/rimelucci/agent-mail/SKILL.md) - AI 代理的电子邮件收件箱。
- [agent-mail-cli](https://github.com/openclaw/skills/tree/main/skills/rimelucci/agent-mail-cli/SKILL.md) - AI 代理的电子邮件收件箱。
- [agent-social](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agent-social/SKILL.md) - 人工智能代理的开源社交网络。
- [agent-team-kit](https://github.com/openclaw/skills/tree/main/skills/ryancampbell/agent-team-kit/SKILL.md) - *自我维持的人工智能代理团队的框架。*
- [airc](https://github.com/openclaw/skills/tree/main/skills/vortitron/airc/SKILL.md) - 连接到 IRC 服务器（AIRC 或任何标准 IRC）并参与频道。
- [among-clawds](https://github.com/openclaw/skills/tree/main/skills/usamalatif/among-clawds/SKILL.md) - 玩 BetweenClawds - 人工智能代理的社交推理游戏
- [apple-mail-search-safe](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/apple-mail-search-safe/SKILL.md) - 使用正文快速安全地进行 Apple Mail 搜索
- [avito](https://github.com/openclaw/skills/tree/main/skills/ruslanlanket/avito/SKILL.md) - 通过 API 管理 Avito.ru 帐户、项目和信使。
- [beeper](https://github.com/openclaw/skills/tree/main/skills/krausefx/beeper/SKILL.md) - 搜索并浏览本地Beeper聊天记录
- [bird-dms](https://github.com/openclaw/skills/tree/main/skills/tolibear/bird-dms/SKILL.md) - Bird 技能的附加组件，可让您的代理检查其 X/Twitter DM
- [blogburst](https://github.com/openclaw/skills/tree/main/skills/shensi8312/blogburst/SKILL.md) - 在几秒钟内将任何文章变成 10 多个社交媒体帖子。
- [calendly](https://github.com/openclaw/skills/tree/main/skills/kesslerio/calendly/SKILL.md) - 日历调度集成。
- [camelcamelcamel-alerts](https://github.com/openclaw/skills/tree/main/skills/jgramajo4/camelcamelcamel-alerts/SKILL.md) - 监控CamelCamelCamel价格下跌警报
- [claw-club](https://github.com/openclaw/skills/tree/main/skills/epwhesq/claw-club/SKILL.md) - 加入 Claw Club — 人工智能机器人的社交网络。
- [claw-me-maybe](https://github.com/openclaw/skills/tree/main/skills/nickhamze/claw-me-maybe/SKILL.md) - Clawdbot 的蜂鸣器集成。
- [clawchat-p2p](https://github.com/openclaw/skills/tree/main/skills/alexrudloff/clawchat-p2p/SKILL.md) - 用于连接 OpenClaw 代理的加密 P2P 消息传递
- [clawconnect](https://github.com/openclaw/skills/tree/main/skills/yiweil/clawconnect/SKILL.md) - ClawConnect - AI 代理的通用帐户连接器。
- [clawemail](https://github.com/openclaw/skills/tree/main/skills/cto1/clawemail/SKILL.md) - 通过 ClawEmail 的 Google Workspace — Gmail、云端硬盘、文档、表格、幻灯片
- [clawemail-admin](https://github.com/openclaw/skills/tree/main/skills/cto1/clawemail-admin/SKILL.md) - 配置和管理 @clawemail.com Google Workspace 电子邮件
- [clawgang](https://github.com/openclaw/skills/tree/main/skills/syslink/clawgang/SKILL.md) - ClawGang 社交技能——让你的代理在clawgang.ai 上进行社交：帖子
- [clawlink](https://github.com/openclaw/skills/tree/main/skills/davemorin/clawlink/SKILL.md) - 加密的 Clawbot 到 Clawbot 消息传递。
- [collaboration-helper](https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/collaboration-helper/SKILL.md) - 跟踪行动项目和协调
- [communication-skill](https://github.com/openclaw/skills/tree/main/skills/aatmaan1/communication-skill/SKILL.md) - 深度聆听和反应制作 - Transform
- [composio-integration](https://github.com/openclaw/skills/tree/main/skills/rita5fr/composio-integration/SKILL.md) - 通过 Composio 访问 600 多个应用程序和服务
- [crunch-protocol](https://github.com/openclaw/skills/tree/main/skills/philippwassibauer/crunch-protocol/SKILL.md) - Crunch 协议 CLI 的自然语言界面。
- [crunch-protocol-skill](https://github.com/openclaw/skills/tree/main/skills/philippwassibauer/crunch-protocol-skill/SKILL.md) - Crunch 的自然语言界面
- [custom-smtp-sender](https://github.com/openclaw/skills/tree/main/skills/scccmsd/custom-smtp-sender/SKILL.md) - 支持 Markdown、HTML 发送电子邮件的技能
- [daily-devotion](https://github.com/openclaw/skills/tree/main/skills/enjuguna/daily-devotion/SKILL.md) - 用当天的诗句创建个性化的每日灵修
- [detect-injection](https://github.com/openclaw/skills/tree/main/skills/zskyx/detect-injection/SKILL.md) - 代理输入和输出的两层内容安全。
- [discord-doctor](https://github.com/openclaw/skills/tree/main/skills/jhillock/discord-doctor/SKILL.md) - Discord bot、网关、OAuth 的快速诊断和修复
- [discord-voice](https://github.com/openclaw/skills/tree/main/skills/avatarneil/discord-voice/SKILL.md) - Discord 语音频道中的实时语音对话
- [dm-bot](https://github.com/openclaw/skills/tree/main/skills/dommholland/dm-bot/SKILL.md) - 与 dm.bot API 交互以实现加密的代理间消息传递。
- [email-best-practices](https://github.com/openclaw/skills/tree/main/skills/christina-de-martinez/email-best-practices/SKILL.md) - 构建电子邮件功能时使用
- [email-daily-summary](https://github.com/openclaw/skills/tree/main/skills/10e9928a/email-daily-summary/SKILL.md) - 自动登录电子邮件帐户
- [email-send](https://github.com/openclaw/skills/tree/main/skills/xejrax/email-send/SKILL.md) - 使用“msmtp”通过 SMTP 发送快速电子邮件，无需打开完整邮件
- [email-summary](https://github.com/openclaw/skills/tree/main/skills/bbdyno/email-summary/SKILL.md) - 从 Gmail 获取最近的电子邮件并提供简洁的摘要。
- [email-to-calendar](https://github.com/openclaw/skills/tree/main/skills/tonimelisma/email-to-calendar/SKILL.md) - 从电子邮件中提取日历事件并创建
- [email-triage](https://github.com/openclaw/skills/tree/main/skills/briancolinger/email-triage/SKILL.md) - IMAP 电子邮件扫描和 AI 分类分类
- [farcaster-agent](https://github.com/openclaw/skills/tree/main/skills/rishavmukherji/farcaster-agent/SKILL.md) - 自主创建 Farcaster 帐户并进行后期投射。
- [feishu-broadcast](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-broadcast/SKILL.md) - 广播消息（帖子/富文本）和图像/贴纸
- [feishu-chat-forwarder](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-chat-forwarder/SKILL.md) - 获取最近聊天记录的技能
- [feishu-group-manager](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-group-manager/SKILL.md) - 管理飞书群聊
- [feishu-leave-request](https://github.com/openclaw/skills/tree/main/skills/baofeidyz/feishu-leave-request/SKILL.md) - 通过飞书（Lark）提交请假申请。
- [feishu-message](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-message/SKILL.md) - 飞书消息操作的通用工具
- [feishu-post](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-post/SKILL.md) - 向飞书发送富文本（Post）消息。
- [front](https://github.com/openclaw/skills/tree/main/skills/rdewolff/front/SKILL.md) - Front.app API 用于管理对话、消息、评论和团队。
- [gif-whatsapp](https://github.com/openclaw/skills/tree/main/skills/shaharsha/gif-whatsapp/SKILL.md) - 在 WhatsApp 上搜索并发送 GIF。
- [gmail-client](https://github.com/openclaw/skills/tree/main/skills/pierremenard/gmail-client/SKILL.md) - 通过 Gmail 阅读和发送电子邮件。
- [google-chat](https://github.com/openclaw/skills/tree/main/skills/darconada/google-chat/SKILL.md) - 通过 webhook 或 OAuth 向 Google Chat 空间和用户发送消息。
- [gram](https://github.com/openclaw/skills/tree/main/skills/arein/gram/SKILL.md) - Instagram CLI：提要、帖子、个人资料、参与度。
- [helpscout](https://github.com/openclaw/skills/tree/main/skills/fabiensebban/helpscout/SKILL.md) - 此技能与 Helpscout 交互以获取所有对话
- [himalaya](https://github.com/openclaw/skills/tree/main/skills/lamelas/himalaya/SKILL.md) - 用于管理电子邮件的 CLI。
- [imsg](https://github.com/openclaw/skills/tree/main/skills/steipete/imsg/SKILL.md) - iMessage/SMS CLI 用于列出聊天、历史记录、观看和发送。
- [isms-audit-expert](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/isms-audit-expert/SKILL.md) - 信息安全管理体系审核
- [kindroid-interact](https://github.com/openclaw/skills/tree/main/skills/lumenlemons/kindroid-interact/SKILL.md) - 通过官方渠道与 Kindroid 伙伴互动
- [let-me-know](https://github.com/openclaw/skills/tree/main/skills/fogyoy/let-me-know/SKILL.md) - 在开始任何长时间运行的任务之前通知用户并保留它们
- [linkedin](https://github.com/openclaw/skills/tree/main/skills/biostartechnology/linkedin/SKILL.md) - LinkedIn 通过浏览器中继或 cookie 实现自动化消息传递
- [linkedin-cli](https://github.com/openclaw/skills/tree/main/skills/arun-8687/linkedin-cli/SKILL.md) - 一个像鸟一样的 LinkedIn CLI，用于搜索个人资料、检查
- [lista-sms](https://github.com/openclaw/skills/tree/main/skills/david-evaristo) - 描述：Recupera、过滤器和自动过滤格式
- [luma](https://github.com/openclaw/skills/tree/main/skills/regalstreak/luma/SKILL.md) - 从 Luma (lu.ma) 获取任何城市即将举行的活动。
- [mailbox](https://github.com/openclaw/skills/tree/main/skills/leeguooooo/mailbox/SKILL.md) - 使用邮箱 CLI 作为阅读和管理电子邮件的工具。
- [mersal-orem](https://github.com/openclaw/skills/tree/main/skills/maherucifer/mersal-orem/SKILL.md) - 人工智能代理的社交网络。
- [messenger](https://github.com/openclaw/skills/tree/main/skills/codedao12/messenger/SKILL.md) - Facebook Messenger 平台工作流程的 OpenClaw 技能
- [moltgram](https://github.com/openclaw/skills/tree/main/skills/nek-11) - 人工智能代理的 Instagram 竞争激烈 - 每天只有 2 个帖子存活。
- [ms-outlook-teams-assistant](https://github.com/openclaw/skills/tree/main/skills/abhinavjp/ms-outlook-teams-assistant/SKILL.md) - 跟踪和唠叨有关 Microsoft Outlook 的信息
- [ms365](https://github.com/openclaw/skills/tree/main/skills/cvsloane/ms365/SKILL.md) - 微软365
- [multyverse-email](https://github.com/openclaw/skills/tree/main/skills/webdevtodayjason/multyverse-email/SKILL.md) - 为您的 AI 代理提供永久电子邮件地址
- [nochat-channel](https://github.com/openclaw/skills/tree/main/skills/catsmeow492/nochat-channel/SKILL.md) - OpenClaw 的加密代理到代理消息传递通道。
- [nochat-channel-plugin](https://github.com/openclaw/skills/tree/main/skills/catsmeow492/nochat-channel-plugin/SKILL.md) - 通过 NoChat 加密代理间消息传递。
- [ocft](https://github.com/openclaw/skills/tree/main/skills/stormixus/ocft/SKILL.md) - AI 代理之间通过消息通道进行 P2P 文件传输。
- [onemind-skill](https://github.com/openclaw/skills/tree/main/skills/onemindlife/onemind-skill/SKILL.md) - 访问并参与建立集体共识的聊天
- [openpet](https://github.com/openclaw/skills/tree/main/skills/mdealiaga/openpet/SKILL.md) - 用于聊天平台的虚拟宠物（电子宠物风格）游戏。
- [paid-ads](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/paid-ads/SKILL.md) - 当用户需要付费帮助时
- [phone-agent](https://github.com/openclaw/skills/tree/main/skills/kesslerio/phone-agent/SKILL.md) - 使用 Twilio、Deepgram 运行实时 AI 电话代理
- [phone-calls-bland](https://github.com/openclaw/skills/tree/main/skills/dru-ca/phone-calls-bland/SKILL.md) - 通过 Bland AI 拨打人工智能电话 - 预订
- [pocketalert](https://github.com/openclaw/skills/tree/main/skills/akellacom/pocketalert/SKILL.md) - OpenClaw 的 Pocket Alert (pocketalert.app) 技能可实现
- [pollclaw](https://github.com/openclaw/skills/tree/main/skills/mkelk/pollclaw/SKILL.md) - 特工和人类的涂鸦。
- [postiz](https://github.com/openclaw/skills/tree/main/skills/nevo-david/postiz/SKILL.md) - Postiz 是一个用于将社交媒体和聊天帖子安排到 28 个以上频道 X 的工具。
- [postproxy](https://github.com/openclaw/skills/tree/main/skills/danbaranov/postproxy/SKILL.md) - 调用 PostProxy API 创建和管理社交媒体帖子。
- [postproxy-skill](https://github.com/openclaw/skills/tree/main/skills/danbaranov/postproxy-skill/SKILL.md) - 调用 PostProxy API 创建和管理社交媒体帖子。
- [protonmail](https://github.com/openclaw/skills/tree/main/skills/durchblick-nl/protonmail/SKILL.md) - 通过 IMAP 桥阅读、搜索和扫描 ProtonMail
- [pushover-notify](https://github.com/openclaw/skills/tree/main/skills/digitallyborn/pushover-notify/SKILL.md) - 通过 Pushover 将推送通知发送到您的手机
- [quietmail](https://github.com/openclaw/skills/tree/main/skills/co1onnese/quietmail/SKILL.md) - AI 代理的无限电子邮件，无验证或发送限制
- [reddit-cli](https://github.com/openclaw/skills/tree/main/skills/kelsia14/reddit-cli/SKILL.md) - Reddit CLI 用于浏览帖子和 subreddits。
- [scheduler-for-discord](https://github.com/openclaw/skills/tree/main/skills/aaronwander) - 创建和管理预定提醒
- [send-email](https://github.com/openclaw/skills/tree/main/skills/fontstep/send-email/SKILL.md) - 通过 SMTP 发送电子邮件。
- [sendclaw](https://github.com/openclaw/skills/tree/main/skills/jononovo) - 在此处设置您自己的“you@sendclaw.com”电子邮件，无需人工操作
- [sendclaw-111](https://github.com/openclaw/skills/tree/main/skills/jononovo) - 无需人工设置您自己的电子邮件地址 - 自主电子邮件
- [sendclaw-email](https://github.com/openclaw/skills/tree/main/skills/codejika) - 免费代理电子邮件 - 无需许可即可自主注册
- [sendclaw-email-for-bots](https://github.com/openclaw/skills/tree/main/skills/jononovo) - 在这里设置您自己的 sendclaw 电子邮件
- [shitty-email](https://github.com/openclaw/skills/tree/main/skills/johanski/shitty-email/SKILL.md) - 创建和管理临时一次性电子邮件收件箱。
- [signal-cli](https://github.com/openclaw/skills/tree/main/skills/pseudobun/signal-cli/SKILL.md) - 通过本地发送 Signal 消息并查找 Signal 接收者
- [signal-generator](https://github.com/openclaw/skills/tree/main/skills/nititepfirm/signal-generator/SKILL.md) - 生成自动交易信号并发送警报
- [signalhire-skill](https://github.com/openclaw/skills/tree/main/skills/ms-youssef/signalhire-skill/SKILL.md) - 通过 SignalHire API 寻找并丰富联系人
- [social-content](https://github.com/openclaw/skills/tree/main/skills/jchopard69/marketing-skills/references/social-content/SKILL.md) - 当用户需要帮助时
- [stackunderflow](https://github.com/openclaw/skills/tree/main/skills/zanderd18s) - 允许代理访问的知识检索协议
- [table-image](https://github.com/openclaw/skills/tree/main/skills/joargp/table-image/SKILL.md) - 从表格生成图像以提高消息传递应用程序的可读性
- [tamil-whatsapp](https://github.com/openclaw/skills/tree/main/skills/vigneshpy/tamil-whatsapp/SKILL.md) - 在 WhatsApp 上处理泰米尔语消息 - 音译
- [telegram-ascii-table](https://github.com/openclaw/skills/tree/main/skills/nalg/telegram-ascii-table/SKILL.md) - 将表格数据格式化为 Telegram 的 ASCII 框表。
- [telegram-auto-topic](https://github.com/openclaw/skills/tree/main/skills/itstauq/telegram-auto-topic/SKILL.md) - 将“/topic”添加到任何消息的开头
- [telegram-bot](https://github.com/openclaw/skills/tree/main/skills/sebastian-buitrag0/telegram-bot/SKILL.md) - 通过 Telegram Bot API 构建和管理 Telegram 机器人。
- [telegram-compose](https://github.com/openclaw/skills/tree/main/skills/tmchow/telegram-compose/SKILL.md) - 使用 HTML 撰写丰富、可读的 Telegram 消息
- [telegram-create-bot](https://github.com/openclaw/skills/tree/main/skills/jordanprater/telegram-create-bot/SKILL.md) - 通过 Telegram 构建和管理 Telegram 机器人
- [telegram-pairing-customization](https://github.com/openclaw/skills/tree/main/skills/crazypeace/telegram-pairing-customization/SKILL.md) - 修改 OpenClaw 的 Telegram
- [telegram-pairing-message-customization](https://github.com/openclaw/skills/tree/main/skills/crazypeace/telegram-pairing-message-customization/SKILL.md) - 添加自定义消息
- [telegram-usage](https://github.com/openclaw/skills/tree/main/skills/c-drew/telegram-usage/SKILL.md) - 显示会话使用统计信息
- [temp-mail](https://github.com/openclaw/skills/tree/main/skills/techwithanirudh/temp-mail/SKILL.md) - 由 Vortex (vortex.email) 支持的临时电子邮件助手。
- [test-google-chat](https://github.com/openclaw/skills/tree/main/skills/darconada) - 测试 Google Chat 消息传递的技能
- [test-wa](https://github.com/openclaw/skills/tree/main/skills/fianabates1/test-wa/SKILL.md) - 向其他人发送 WhatsApp 消息或搜索/同步 WhatsApp 历史记录
- [testat1](https://github.com/openclaw/skills/tree/main/skills/chaunceyliu/testat1/SKILL.md) - 当您需要通过 slack 工具从 Clawdbot 控制 Slack 时使用
- [tootbot](https://github.com/openclaw/skills/tree/main/skills/behrangsa/tootbot/SKILL.md) - 将内容发布到 Mastodon。
- [treeline-money](https://github.com/openclaw/skills/tree/main/skills/zack-schrag/treeline-money/SKILL.md) - 通过 Treeline Money 讨论您的财务状况。
- [twitter-operations](https://github.com/openclaw/skills/tree/main/skills/millymilton/twitter-operations/SKILL.md) - {
- [unione](https://github.com/openclaw/skills/tree/main/skills/andythemartketing/unione/SKILL.md) - 通过 UniOne 电子邮件 API 发送交易和营销电子邮件。
- [upload-post](https://github.com/openclaw/skills/tree/main/skills/victorcavero14/upload-post/SKILL.md) - 通过 Upload-Post API 将内容上传到社交媒体平台。
- [use-soulseek](https://github.com/openclaw/skills/tree/main/skills/svidovich/use-soulseek/SKILL.md) - Soulseek 是一个分布式点对点文件共享平台
- [valinor](https://github.com/openclaw/skills/tree/main/skills/douglance/valinor/SKILL.md) - 连接到 Valinor MAD - 结识其他 AI 代理、聊天、建立友谊、发送信息
- [wa-styler](https://github.com/openclaw/skills/tree/main/skills/rubenfb23/wa-styler/SKILL.md) - 确保发送到 WhatsApp 的所有消息均遵循平台的技能
- [wacli](https://github.com/openclaw/skills/tree/main/skills/steipete/wacli/SKILL.md) - 向其他人发送 WhatsApp 消息或搜索/同步 WhatsApp 历史记录
- [walkie-talkie](https://github.com/openclaw/skills/tree/main/skills/rubenfb23/walkie-talkie/SKILL.md) - 处理 WhatsApp 上的语音对语音对话。
- [webchat-audio-notifications](https://ClawHub.com/brokemac79/webchat-audio-notifications) - 用于网络聊天的浏览器音频通知 5...
- [whatsapp-styler](https://github.com/openclaw/skills/tree/main/skills/rubenfb23/whatsapp-styler/SKILL.md) - 确保发送到 WhatsApp 的所有消息都遵循的技能
- [whatsapp-ultimate](https://github.com/openclaw/skills/tree/main/skills/globalcaos/whatsapp-ultimate/SKILL.md) - 完整的 WhatsApp 集成 — 消息、媒体、民意调查、贴纸、语音笔记、反应、FTS5 历史搜索、语音转录。原生百利甜酒，零 Docker。
- [whatsapp-video-mockup](https://github.com/openclaw/skills/tree/main/skills/danpeg/whatsapp-video-mockup/SKILL.md) - Whatsapp 视频模型
- [zalo](https://github.com/openclaw/skills/tree/main/skills/codedao12/zalo/SKILL.md) - 集成 Zalo (Zalo OA/ZNS) 的指南：流程、API 使用、webhooks
- [zero-trust](https://github.com/openclaw/skills/tree/main/skills/doonot/zero-trust/SKILL.md) - 安全第一的行为准则，用于谨慎的代理操作。
- [zoom-meeting-assistance-with-rtms-unofficial-community-skill](https://github.com/openclaw/skills/tree/main/skills/tanchunsiong/zoom-meeting-assistance-with-rtms-unofficial-community-skill/SKILL.md) - Zoom RTMS 会议
- [zoom-unofficial-community-skill](https://github.com/openclaw/skills/tree/main/skills/tanchunsiong/zoom-unofficial-community-skill/SKILL.md) - 缩放 API 集成

</details>

<details>
<summary><h3 style="display:inline" id="speech--transcription">语音与转录</h3></summary>

- [addis-assistant-stt](https://github.com/openclaw/skills/tree/main/skills/dagmawibabi/addis-assistant-stt/SKILL.md) - 提供语音转文本 (STT) 和文本
- [agent-voice](https://github.com/openclaw/skills/tree/main/skills/nerdsnipe/agent-voice/SKILL.md) - AI 代理的命令行博客平台。
- [announcer](https://github.com/openclaw/skills/tree/main/skills/odrobnik/announcer/SKILL.md) - 使用 Airfoil + 通过 AirPlay 扬声器在整个房子内播报文本。
- [assemblyai-transcribe](https://github.com/openclaw/skills/tree/main/skills/tristanmanchester/assemblyai-transcribe/SKILL.md) - 使用 AssemblyAI 转录音频/视频
- [audio-gen](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/audio-gen/SKILL.md) - 生成有声读物、播客或教育音频内容
- [audio-reply](https://github.com/openclaw/skills/tree/main/skills/matrixy/audio-reply-skill/SKILL.md) - 使用 TTS 生成音频回复。
- [chichi-speech](https://github.com/openclaw/skills/tree/main/skills/hudeven/chichi-speech/SKILL.md) - 使用 Qwen3 提供高质量文本转语音的 RESTful 服务
- [claw-voice](https://github.com/openclaw/skills/tree/main/skills/niczy) - 您通过语音连接到实时用户会话。
- [clonev](https://github.com/openclaw/skills/tree/main/skills/instant-picture/clonev/SKILL.md) - 使用 Coqui XTTS v2 克隆任何语音并生成语音。
- [critical-article-writer](https://github.com/openclaw/skills/tree/main/skills/tomstools11/critical-article-writer/SKILL.md) - 生成文章草稿、大纲
- [cult-of-carcinization](https://github.com/openclaw/skills/tree/main/skills/loserbcc/cult-of-carcinization/SKILL.md) - 为您的代理提供发言权和耳朵。
- [deepdub-tts](https://github.com/openclaw/skills/tree/main/skills/yuval-deepdub/deepdub-tts/SKILL.md) - 使用 Deepdub 生成语音音频并将其附加为媒体
- [deepgram](https://github.com/openclaw/skills/tree/main/skills/nerkn/deepgram/SKILL.md) - — Deepgram 语音转文本的命令行界面。
- [doubao-api-open-tts](https://github.com/openclaw/skills/tree/main/skills/xdrshjr/doubao-api-open-tts/SKILL.md) - 使用豆宝（火山引擎）的文字转语音服务
- [duby](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 使用 Duby.so API 将文本转换为语音。
- [eachlabs-voice-audio](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-voice-audio/SKILL.md) - TTS、STT、使用 ElevenLabs、Whisper、RVC 进行语音转换。
- [easyverein-api](https://github.com/openclaw/skills/tree/main/skills/truefoobar/easyverein-api/SKILL.md) - 使用 easyVerein v2.0 REST API
- [edge-tts](https://github.com/openclaw/skills/tree/main/skills/i3130002/edge-tts/SKILL.md) - |。
- [elevenlabs-agents](https://github.com/openclaw/skills/tree/main/skills/pennyroyaltea/elevenlabs-agents/SKILL.md) - 创建、管理和部署 ElevenLabs
- [elevenlabs-media](https://github.com/openclaw/skills/tree/main/skills/clawdbotborges) - ElevenLabs 音乐生成和语音转文本...
- [elevenlabs-transcribe](https://github.com/openclaw/skills/tree/main/skills/paulasjes/elevenlabs-transcribe/SKILL.md) - 使用 ElevenLabs 将音频转录为文本
- [elevenlabs-tts](https://github.com/openclaw/skills/tree/main/skills/shaharsha/elevenlabs-tts/SKILL.md) - ElevenLabs TTS - OpenClaw 的最佳 ElevenLabs 集成。
- [elevenlabs-voices](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/elevenlabs-voices/SKILL.md) - 具有 18 个角色、32 个角色的高质量语音合成
- [faster-whisper](https://github.com/openclaw/skills/tree/main/skills/theplasmak/faster-whisper/SKILL.md) - 使用 Fast-Whisper 进行本地语音转文本。
- [feishu-minutes](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-minutes/SKILL.md) - 从飞书获取信息、统计数据、文字记录和媒体
- [freshbooks-cli](https://github.com/openclaw/skills/tree/main/skills/haseebuchiha/freshbooks-cli/SKILL.md) - FreshBooks CLI 用于管理发票、客户和计费。
- [gettr-transcribe-summarize](https://github.com/openclaw/skills/tree/main/skills/kevin37li/gettr-transcribe-summarize/SKILL.md) - 从 GETTR 帖子下载音频
- [inworld-tts](https://github.com/openclaw/skills/tree/main/skills/gugic/inworld-tts/SKILL.md) - 通过 Inworld.ai API 进行文本转语音。
- [jarvis-voice](https://github.com/openclaw/skills/tree/main/skills/globalcaos/jarvis-voice/SKILL.md) - 具有 TTS 和视觉转录样式的金属 AI 语音角色。
- [kokoro-tts](https://github.com/openclaw/skills/tree/main/skills/edkief/kokoro-tts/SKILL.md) - 使用本地 Kokoro TTS 引擎从文本生成语音音频。
- [llmwhisperer](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/llmwhisperer/SKILL.md) - 使用 LLMWhisperer 从图像和 PDF 中提取文本和布局
- [local-stt](https://github.com/openclaw/skills/tree/main/skills/araa47/local-stt/SKILL.md) - 具有可选后端的本地 STT - Parakeet（最准确）或 Whisper。
- [local-whisper](https://github.com/openclaw/skills/tree/main/skills/araa47/local-whisper/SKILL.md) - 使用 OpenAI Whisper 进行本地语音转文本。
- [minimax-tts](https://github.com/openclaw/skills/tree/main/skills/doobidoo) - 名称：minimax-tts。
- [mlx-whisper](https://github.com/openclaw/skills/tree/main/skills/kevin37li/mlx-whisper/SKILL.md) - 使用 MLX Whisper 进行本地语音转文本
- [moodcast](https://github.com/openclaw/skills/tree/main/skills/ashutosh887/moodcast/SKILL.md) - 将任何文本转换为具有环境氛围的情感表达音频
- [openai-whisper](https://github.com/openclaw/skills/tree/main/skills/steipete/openai-whisper/SKILL.md) - 使用 Whisper CLI 进行本地语音转文本（无 API 密钥）。
- [openai-whisper-api](https://github.com/openclaw/skills/tree/main/skills/steipete/openai-whisper-api/SKILL.md) - 通过 OpenAI 音频转录 API 转录音频
- [parakeet-mlx](https://github.com/openclaw/skills/tree/main/skills/kylehowells/parakeet-mlx/SKILL.md) - 使用适用于 Apple Silicon 的 Parakeet MLX (ASR) 进行本地语音转文本
- [parakeet-stt](https://github.com/openclaw/skills/tree/main/skills/carlulsoe/parakeet-stt/SKILL.md) - >-.
- [phone-voice](https://github.com/openclaw/skills/tree/main/skills/cortexuvula/phone-voice/SKILL.md) - 使用 Twilio 通过电话将 ElevenLabs Agent 连接到您的 OpenClaw。
- [plaud-unofficial](https://github.com/openclaw/skills/tree/main/skills/leonardsellem/plaud-unofficial/SKILL.md) - 访问 Plaud 录音机数据时使用
- [pocket-transcripts](https://github.com/openclaw/skills/tree/main/skills/tmustier/heypocket-reader/SKILL.md) - 阅读 Pocket AI 的文字记录和摘要
- [pocket-tts](https://github.com/openclaw/skills/tree/main/skills/sherajdev/pocket-tts/SKILL.md) - 口袋tts
- [qwen-tts](https://github.com/openclaw/skills/tree/main/skills/paki81/qwen-tts/SKILL.md) - 使用 Qwen3-TTS-12Hz-1.7B-CustomVoice 进行本地文本转语音。
- [ringg-voice-agent](https://github.com/openclaw/skills/tree/main/skills/siddharthpilani/ringg-voice-agent/SKILL.md) - 将 Ringg AI 语音代理与 OpenClaw 集成
- [routstr-balance-management](https://github.com/openclaw/skills/tree/main/skills/sh1ftred/routstr-balance-management/SKILL.md) - 通过检查管理 Routstr 余额
- [sapi-tts](https://github.com/openclaw/skills/tree/main/skills/korddie/sapi-tts/SKILL.md) - 使用神经语音的 Windows SAPI5 文本转语音。
- [sound-fx](https://github.com/openclaw/skills/tree/main/skills/javicasper/sound-fx/SKILL.md) - 通过 ElevenLabs SFX（文本转声音）生成短音效。
- [spaces](https://github.com/openclaw/skills/tree/main/skills/logesh2496/spaces/SKILL.md) - Moltbook 代理闲逛的语音优先社交空间。
- [transcribe](https://github.com/openclaw/skills/tree/main/skills/javicasper/transcribe/SKILL.md) - 使用本地 Whisper (Docker) 将音频文件转录为文本。
- [tts](https://github.com/openclaw/skills/tree/main/skills/amstko/tts/SKILL.md) - 使用 Hume AI 或 OpenAI API 进行文本转语音。
- [tts-whatsapp](https://github.com/openclaw/skills/tree/main/skills/hopyky/tts-whatsapp/SKILL.md) - 在 WhatsApp 上以 40 多种语言发送高质量的文本转语音语音消息
- [video-subtitles](https://github.com/openclaw/skills/tree/main/skills/ngutman/video-subtitles/SKILL.md) - 从视频/音频生成带有翻译的 SRT 字幕
- [voice-agent](https://github.com/openclaw/skills/tree/main/skills/ricardotrevisan/voice-agent/SKILL.md) - 使用 AI 语音代理的代理的本地语音输入/输出
- [voice-ai-agent](https://github.com/openclaw/skills/tree/main/skills/gizmogremlin) - 创建、管理和部署 Voice.ai 对话式 AI
- [voice-ai-tts](https://github.com/openclaw/skills/tree/main/skills/gizmogremlin) - 具有 9 个角色、11 种语言的高质量语音合成
- [voice-ai-voices](https://github.com/openclaw/skills/tree/main/skills/gizmogremlin/voice-ai-voices/SKILL.md) - 具有 9 个角色、11 个角色的高质量语音合成
- [voice-transcribe](https://github.com/openclaw/skills/tree/main/skills/darinkishore/voice-transcribe/SKILL.md) - 使用 OpenAI 转录音频文件
- [voice-ui](https://github.com/openclaw/skills/tree/main/skills/yukihamada/voice-ui/SKILL.md) - 自我进化的语音助手用户界面。
- [webchat-audio-notifications](https://github.com/openclaw/skills/tree/main/skills/brokemac79/webchat-audio-notifications/SKILL.md) - 添加浏览器音频通知
- [whatsapp-voice-chat-integration-open-source](https://github.com/openclaw/skills/tree/main/skills/syedateebulislam/whatsapp-voice-chat-integration-open-source/SKILL.md) - 实时 WhatsApp
- [whisper-mlx-local](https://github.com/openclaw/skills/tree/main/skills/impkind/whisper-mlx-local/SKILL.md) - Telegram 和 WhatsApp 的免费本地语音转文本
- [x-voice-match](https://github.com/openclaw/skills/tree/main/skills/gravyxbt/x-voice-match/SKILL.md) - 分析 Twitter/X 帐户的发布风格并生成

</details>

<details>
<summary><h3 style="display:inline" id="smart-home--iot">智能家居与物联网</h3></summary>

- [aida](https://github.com/openclaw/skills/tree/main/skills/ak-khalis/aida/SKILL.md) - 阿依达
- [anova-oven](https://github.com/openclaw/skills/tree/main/skills/dodeja/anova-skill/SKILL.md) - 控制 Anova 精密烤箱和精密炊具（真空低温烹调）
- [anthropology](https://github.com/openclaw/skills/tree/main/skills/networktheoryappliedresearchinstitute/anthropology/SKILL.md) - 全面的人工智能教学技能
- [bambu-cli](https://github.com/openclaw/skills/tree/main/skills/tobiasbischoff/bambu-cli/SKILL.md) - 使用 bambu-cli 操作 BambuLab 打印机并排除故障
- [bambu-local](https://github.com/openclaw/skills/tree/main/skills/tanguyvans/bambu-local/SKILL.md) - 通过 MQTT 在本地控制 Bambu Lab 3D 打印机。
- [beestat](https://github.com/openclaw/skills/tree/main/skills/mjrussell/beestat/SKILL.md) - 通过 Beestat API 查询 ecobee 恒温器数据，包括温度
- [bring-add](https://github.com/openclaw/skills/tree/main/skills/darkdevelopers/bring-add/SKILL.md) - 当用户想要添加物品到 Bring! 时使用！
- [communication-coach](https://github.com/openclaw/skills/tree/main/skills/rjmoggach/communication-coach/SKILL.md) - 适应性沟通辅导塑造
- [context-engineering](https://github.com/openclaw/skills/tree/main/skills/leoyessi10-tech/context-engineering/SKILL.md) - 当用户询问时应该使用这个技能
- [control-ikea-lightbulb](https://github.com/openclaw/skills/tree/main/skills/antgly/control-ikea-lightbulb/SKILL.md) - 控制IKEA/TP-Link Kasa智能灯泡
- [crabnet](https://github.com/openclaw/skills/tree/main/skills/spclaudehome/crabnet/SKILL.md) - 与 CrabNet 跨代理协作注册表交互。
- [devialet](https://github.com/openclaw/skills/tree/main/skills/jgm2025/devialet/SKILL.md) - 通过 HTTP API 控制 Devialet Phantom 扬声器。
- [dirigera-control](https://github.com/openclaw/skills/tree/main/skills/falderebet/dirigera-control/SKILL.md) - 控制宜家 Dirigera 智能家居设备
- [dyson-cli](https://github.com/openclaw/skills/tree/main/skills/tmustier/dyson-cli/SKILL.md) - 通过本地 MQTT 控制戴森空气净化器、风扇和加热器。
- [echodecks](https://github.com/openclaw/skills/tree/main/skills/drgeld/echodecks/SKILL.md) - 与 EchoDecks 集成，用于抽认卡管理、学习课程和人工智能。
- [echodecks-ultimate](https://github.com/openclaw/skills/tree/main/skills/drgeld/echodecks-ultimate/SKILL.md) - 人工智能驱动的抽认卡管理和自动播客
- [eightctl](https://github.com/openclaw/skills/tree/main/skills/steipete/eightctl/SKILL.md) - 控制八个睡眠舱（状态、温度、警报、时间表）。
- [enzoldhazam](https://github.com/openclaw/skills/tree/main/skills/daniel-laszlo/enzoldhazam/SKILL.md) - NGBS iCON 智能家居恒温器控制。
- [fivem-dev](https://github.com/openclaw/skills/tree/main/skills/dktrn9ne/fivem-dev/SKILL.md) - 适用于 QBCore、ESX 的 FiveM RP 服务器工程。
- [frigate](https://github.com/openclaw/skills/tree/main/skills/porygonthebot/frigate/SKILL.md) - 通过基于会话的身份验证访问 Frigate NVR 摄像机。
- [google-home](https://github.com/openclaw/skills/tree/main/skills/mitchellbernstein/google-home/SKILL.md) - 控制 Google Nest 设备
- [google-tv](https://github.com/openclaw/skills/tree/main/skills/antgly) - 通过 ADB 使用 Google TV 控制客厅 Chromecast。
- [govee-lights](https://github.com/openclaw/skills/tree/main/skills/joeynyc/govee-lights/SKILL.md) - 通过 Govee API 控制 Govee 智能灯。
- [govpredict](https://github.com/openclaw/skills/tree/main/skills/seyhunak/govpredict/SKILL.md) - 更智慧的政府采购 - 简化合规、招标
- [home-music](https://github.com/openclaw/skills/tree/main/skills/asteinberger/home-music/SKILL.md) - 结合Spotify播放控制全屋音乐场景
- [homebridge](https://github.com/openclaw/skills/tree/main/skills/jiasenl/clawdbot-skill-homebridge/SKILL.md) - 通过 Homebridge Config UI X 控制智能家居设备
- [homey](https://github.com/openclaw/skills/tree/main/skills/maxsumrall/homey/SKILL.md) - 通过本地 (LAN/VPN) 或云 API 控制 Athom Homey 智能家居设备。
- [homey-cli](https://github.com/openclaw/skills/tree/main/skills/krausefx/homey-cli/SKILL.md) - 控制 Homey 家庭自动化中心。
- [internet-lookup-verifier](https://github.com/openclaw/skills/tree/main/skills/amangarg1999/internet-lookup-verifier/SKILL.md) - 通过执行验证信息
- [lg-thinq](https://github.com/openclaw/skills/tree/main/skills/kaiofreitas/lg-thinq/SKILL.md) - 通过 ThinQ API 控制 LG 智能电器。
- [little-snitch](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/little-snitch/SKILL.md) - macOS 上的 Little Snitch 防火墙控制。
- [mijia](https://github.com/openclaw/skills/tree/main/skills/hqman/mijia/SKILL.md) - 控制小米米家智能家居设备。
- [mqtt-client](https://github.com/openclaw/skills/tree/main/skills/enchantedmotorcycle/mqtt-client/SKILL.md) - 这是一个用于连接 mqtt 的简单客户端
- [nanoleaf](https://github.com/openclaw/skills/tree/main/skills/rstierli/nanoleaf/SKILL.md) - 通过 Picoleaf 控制 Nanoleaf 灯板。
- [nest-devices](https://github.com/openclaw/skills/tree/main/skills/amogower/nest-devices/SKILL.md) - 控制 Nest 智能家居设备（恒温器、摄像头、门铃）
- [netatmo](https://github.com/openclaw/skills/tree/main/skills/florianbeer/netatmo/SKILL.md) - Netatmo 恒温器控制和气象站。
- [openhue](https://github.com/openclaw/skills/tree/main/skills/steipete/openhue/SKILL.md) - 通过 OpenHue 控制飞利浦 Hue 灯光/场景。
- [philips-hue-thinking](https://github.com/openclaw/skills/tree/main/skills/jesserod329/philips-hue-thinking/SKILL.md) - 使用 Philips Hue 的视觉 AI 活动指示器
- [pihole](https://github.com/openclaw/skills/tree/main/skills/baanish/pihole/SKILL.md) - 皮孔
- [printer](https://github.com/openclaw/skills/tree/main/skills/dhvanilpatel/printer/SKILL.md) - 在 macOS 上通过 CUPS 管理打印机
- [robo-rock](https://github.com/openclaw/skills/tree/main/skills/dru-ca/robo-rock/SKILL.md) - 控制 Roborock 扫地机器人（状态、清洁、地图、消耗品）。
- [senior-computer-vision](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-computer-vision/SKILL.md) - 计算机视觉工程技能
- [set-reminder](https://github.com/openclaw/skills/tree/main/skills/onionrings29/set-reminder/SKILL.md) - 当用户想要提醒某件事时使用
- [skillsign](https://github.com/openclaw/skills/tree/main/skills/felmonon/skillsign/SKILL.md) - 使用 ed25519 密钥签署并验证代理技能文件夹。
- [snow-report](https://github.com/openclaw/skills/tree/main/skills/davemorin/snow-report/SKILL.md) - 获取任何山峰的雪况、预报和滑雪报告
- [solarpunk-evidence-logger](https://github.com/openclaw/skills/tree/main/skills/meekotharaccoon/solarpunk-evidence-logger/SKILL.md) - 创建或更新 AgentSkills。
- [starlink](https://github.com/openclaw/skills/tree/main/skills/danfedick/starlink/SKILL.md) - Starlink 天线：状态、速度测试、WiFi 客户端。
- [tesla-fleet-api](https://github.com/openclaw/skills/tree/main/skills/odrobnik/tesla-fleet-api/SKILL.md) - 与特斯拉官方Fleet API集成时使用读取
- [voicemonkey](https://github.com/openclaw/skills/tree/main/skills/jayakumark/voicemonkey/SKILL.md) - 通过 VoiceMonkey API v2 控制 Alexa 设备 - 发布公告
- [weather](https://github.com/openclaw/skills/tree/main/skills/steipete/weather/SKILL.md) - 获取当前天气和预报（无需 API 密钥）。
- [weather-pollen](https://github.com/openclaw/skills/tree/main/skills/thesethrose/weather-pollen/SKILL.md) - 使用免费 API 报告任何位置的天气和花粉。
- [weathercli](https://github.com/openclaw/skills/tree/main/skills/pjtf93/weathercli/SKILL.md) - 获取全球任何地点的当前天气状况和预报。
- [wled](https://github.com/openclaw/skills/tree/main/skills/rowbotik/wled/SKILL.md) - 通过 HTTP API 控制 WLED LED 控制器。

</details>

<details>
<summary><h3 style="display:inline" id="shopping--e-commerce">购物与电子商务</h3></summary>

- [agent-commerce](https://github.com/openclaw/skills/tree/main/skills/nowloady) - 代理电商引擎与川菜外卖...
- [agentic-commerce](https://github.com/openclaw/skills/tree/main/skills/purch-agent/agentic-commerce/SKILL.md) - 用于产品搜索和加密的人工智能购物 API
- [amadeus-hotels](https://github.com/openclaw/skills/tree/main/skills/kesslerio/amadeus-hotels/SKILL.md) - 通过 Amadeus API 搜索酒店价格和供应情况。
- [amazon-competitor-analyzer](https://github.com/openclaw/skills/tree/main/skills/phheng/amazon-competitor-analyzer/SKILL.md) - 从 ASIN 中抓取亚马逊产品数据
- [anylist](https://github.com/openclaw/skills/tree/main/skills/mjrussell/anylist/SKILL.md) - 通过 AnyList 管理杂货和购物清单。
- [bricklink](https://github.com/openclaw/skills/tree/main/skills/odrobnik/bricklink/SKILL.md) - BrickLink Store API 帮助程序/CLI（OAuth 1.0 请求签名）。
- [bring-shopping](https://github.com/openclaw/skills/tree/main/skills/cutzenfriend/bring-shopping/SKILL.md) - 管理带来！
- [buy-anything](https://github.com/openclaw/skills/tree/main/skills/tsyvic/buy-anything/SKILL.md) - 通过对话结账从亚马逊购买产品。
- [checkers-sixty60](https://github.com/openclaw/skills/tree/main/skills/snopoke/checkers-sixty60/SKILL.md) - 通过浏览器在 Checkers.co.za Sixty60 送货服务上购物
- [clawdbites](https://github.com/openclaw/skills/tree/main/skills/kylelol/clawdbites/SKILL.md) - 从 Instagram 卷轴中提取食谱。
- [clawpify](https://github.com/openclaw/skills/tree/main/skills/alhwyn/clawpify/SKILL.md) - 通过 GraphQL 管理 API 查询和管理 Shopify 商店。
- [clawver-digital-products](https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-digital-products/SKILL.md) - 创建和销售数字产品
- [clawver-reviews](https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-reviews/SKILL.md) - 处理 Clawver 客户评论。
- [eachlabs-product-visuals](https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/eachlabs-product-visuals/SKILL.md) - 生成电子商务产品照片和视频。
- [closing-deals](https://github.com/openclaw/skills/tree/main/skills/jk-0001/closing-deals/SKILL.md) - 作为个体企业家始终如一地完成销售交易。
- [event-planner](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/event-planner/SKILL.md) - 策划活动
- [food-order](https://github.com/openclaw/skills/tree/main/skills/steipete/food-order/SKILL.md) - 重新订购 Foodora 订单 + 使用 ordercli 跟踪预计到达时间/状态。
- [gousto](https://github.com/openclaw/skills/tree/main/skills/dhruvkelawala/gousto/SKILL.md) - 搜索并浏览 9,000 多个 Gousto 食谱。
- [gurkerl](https://github.com/openclaw/skills/tree/main/skills/florianbeer/gurkerl/SKILL.md) - Gukerl.at 杂货店购物。
- [gurkerlcli](https://github.com/openclaw/skills/tree/main/skills/pasogott/gurkerlcli/SKILL.md) - 通过 gurkerl.at 进行奥地利在线杂货购物。
- [idealista](https://github.com/openclaw/skills/tree/main/skills/quifago/idealista/SKILL.md) - 通过 Idealista-cli（OAuth2 客户端凭据）查询 Idealista API。
- [irish-takeaway](https://github.com/openclaw/skills/tree/main/skills/cotyledonlab/irish-takeaway/SKILL.md) - 查找爱尔兰附近的外卖店并浏览菜单。
- [jellyseerr](https://github.com/openclaw/skills/tree/main/skills/ericrosenberg/jellyseerr/SKILL.md) - 通过 Jellyserr 请求电影和电视节目。
- [jtbd-analyzer](https://github.com/openclaw/skills/tree/main/skills/artyomx33/jtbd-analyzer/SKILL.md) - 揭示客户雇用您的产品的真正“工作”
- [marketplace-clis](https://github.com/openclaw/skills/tree/main/skills/pjtf93) - 西班牙市场 CLI：Wallapop、Idealista、...
- [marktplaats](https://github.com/openclaw/skills/tree/main/skills/pvoo/marktplaats/SKILL.md) - 通过过滤在所有类别中搜索 Marktplaats.nl 分类
- [moltlist-marketplace](https://github.com/openclaw/skills/tree/main/skills/koriyoshi2041/moltlist-marketplace/SKILL.md) - 与 moltlist.com 代理互动
- [moltpho](https://github.com/openclaw/skills/tree/main/skills/unifiedh/moltpho/SKILL.md) - 通过 Moltpho 在亚马逊上自主购物 - 搜索产品、管理信用
- [ontopo](https://github.com/openclaw/skills/tree/main/skills/alexpolonsky/ontopo/SKILL.md) - 在 Ontopo 上搜索以色列餐厅并查看餐桌供应情况。
- [ordercli](https://github.com/openclaw/skills/tree/main/skills/steipete/ordercli/SKILL.md) - 仅 Foodora CLI 用于检查过去的订单和活动订单状态
- [paprika](https://github.com/openclaw/skills/tree/main/skills/mjrussell/paprika/SKILL.md) - 从 Paprika Recipe Manager 访问食谱、膳食计划和购物清单。
- [pcmiler](https://github.com/openclaw/skills/tree/main/skills/nchoudhury-trimble/pcmiler/SKILL.md) - PCMier REST API 提供了检索一系列的方法
- [peer-reviewer](https://github.com/openclaw/skills/tree/main/skills/sschepis/peer-reviewer/SKILL.md) - 人工智能驱动的学术论文审稿人。
- [picnic](https://github.com/openclaw/skills/tree/main/skills/mpociot/picnic/SKILL.md) - 从野餐超市订购杂货 - 搜索产品、管理购物车。
- [plan2meal](https://github.com/openclaw/skills/tree/main/skills/okikesolutions/plan2meal/SKILL.md) - 计划膳食
- [price-tracker](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/price-tracker/SKILL.md) - 监控亚马逊、eBay、沃尔玛的产品价格
- [product-hunt-launch](https://github.com/openclaw/skills/tree/main/skills/abakermi/product-hunt-launch/SKILL.md) - 跟踪您的 Product Hunt 发布统计数据
- [safe-skills](https://github.com/openclaw/skills/tree/main/skills/glitch003/safe-skills/SKILL.md) - SafeSkills 是一项安全秘密管理服务。
- [secops-by-joes](https://github.com/openclaw/skills/tree/main/skills/inaor/secops-by-joes/SKILL.md) - SecOps 检查端点：EDR、Sysmon、更新、EVTX
- [shopify-admin-api](https://github.com/openclaw/skills/tree/main/skills/zachgodsell93) - 对 Shopify Admin REST API 的完全读/写访问权限
- [shopping-expert](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/shopping-expert/SKILL.md) - 在线查找和比较产品（Google 购物）
- [skill-reviewer](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/skill-reviewer/SKILL.md) - 审查和审核代理技能（SKILL.md 文件）
- [thought-to-excalidraw](https://github.com/openclaw/skills/tree/main/skills/sairammahadevan/thought-to-excalidraw/SKILL.md) - 可视化产品经理的想法
- [toon-utils](https://github.com/openclaw/skills/tree/main/skills/lythaeon/toon-utils/SKILL.md) - 该技能提供了将令牌使用量减少 30-60% 的说明
- [whcli](https://github.com/openclaw/skills/tree/main/skills/pasogott/whcli/SKILL.md) - Willhaben CLI 用于搜索奥地利最大的分类广告市场。
- [willhaben](https://github.com/openclaw/skills/tree/main/skills/benjaminorthner/willhaben/SKILL.md) - 在 Willhaben.at（奥地利市场）上创建和管理列表。
- [wishfinity](https://github.com/openclaw/skills/tree/main/skills/leebellon/wishfinity/SKILL.md) - 代购、产品推荐添加“留着以后用”
- [wolt-orders](https://github.com/openclaw/skills/tree/main/skills/dviros/wolt-orders/SKILL.md) - 发现具有高级筛选功能的餐厅
- [wpclaw-lite](https://github.com/openclaw/skills/tree/main/skills/magnum-opus-v1/wpclaw-lite/SKILL.md) - 通过 WPClaw 连接器连接到 WooCommerce 商店
- [youbaolian](https://github.com/openclaw/skills/tree/main/skills/peterfzh/youbaolian/SKILL.md) - 管理友保链、订单、用户、机关REST API。
- [zentao](https://github.com/openclaw/skills/tree/main/skills/leeguooooo/zentao/SKILL.md) - 使用zentao CLI登录并查询禅道产品和bug。
- [criticaster](https://github.com/openclaw/skills/blob/main/skills/gglucass/criticaster/SKILL.md) - 查找具有汇总评论家评论的产品，并标准化为单一分数。

</details>

<details>
<summary><h3 style="display:inline" id="calendar--scheduling">日历与日程管理</h3></summary>

- [accli](https://github.com/openclaw/skills/tree/main/skills/joargp/accli/SKILL.md) - 在 macOS 上与 Apple 日历交互时应使用此技能。
- [advanced-calendar](https://github.com/openclaw/skills/tree/main/skills/toughworm/advanced-calendar/SKILL.md) - 使用自然语言的高级日历技能
- [agency-guardian](https://github.com/openclaw/skills/tree/main/skills/aranej/agency-guardian/SKILL.md) - 温柔提醒在使用人工智能时保持人性。
- [agent-tinman](https://github.com/openclaw/skills/tree/main/skills/oliveskin/agent-tinman/SKILL.md) - 具有主动预防功能的人工智能安全扫描仪 - 168 检测
- [apple-calendar](https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-calendar/SKILL.md) - 适用于 macOS 的 Apple Calendar.app 集成。
- [apple-reminders](https://github.com/openclaw/skills/tree/main/skills/steipete/apple-reminders/SKILL.md) - 通过 macOS 上的“remindctl”CLI 管理 Apple 提醒
- [brainz-calendar](https://github.com/openclaw/skills/tree/main/skills/xejrax/brainz-calendar/SKILL.md) - 使用“gcalcli”管理 Google 日历事件。
- [calcurse](https://github.com/openclaw/skills/tree/main/skills/gumadeiras/calcurse/SKILL.md) - 基于文本的日历和日程安排应用程序。
- [caldav-calendar](https://github.com/openclaw/skills/tree/main/skills/asleep123/caldav-calendar/SKILL.md) - 同步和查询 CalDAV 日历
- [clippy](https://github.com/openclaw/skills/tree/main/skills/foeken/clippy/SKILL.md) - 用于日历和电子邮件的 Microsoft 365 / Outlook CLI。
- [cpc-mpqc-competence-tracker-compliance-uk](https://github.com/openclaw/skills/tree/main/skills/kowl64/cpc-mpqc-competence-tracker-compliance-uk/SKILL.md) - 计划 CPC/MPQC
- [creative-thought-partner](https://github.com/openclaw/skills/tree/main/skills/vincentchan/creative-thought-partner/SKILL.md) - 对话式创意
- [cron-scheduling](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/cron-scheduling/SKILL.md) - 使用 cron 安排和管理重复任务
- [cross-pollination-engine](https://github.com/openclaw/skills/tree/main/skills/artyomx33/cross-pollination-engine/SKILL.md) - 系统地借用想法
- [event-watcher](https://github.com/openclaw/skills/tree/main/skills/solitaire2015/event-watcher/SKILL.md) - OpenClaw 的事件观察者技能。
- [fastmail](https://github.com/openclaw/skills/tree/main/skills/witooh/fastmail/SKILL.md) - 通过 JMAP 和 CalDAV API 管理 Fastmail 电子邮件和日历。
- [feishu-calendar](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-calendar/SKILL.md) - 管理飞书日历。
- [feishu-whiteboard](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-whiteboard/SKILL.md) - 允许创建和操作飞书白板
- [gcal-pro](https://github.com/openclaw/skills/tree/main/skills/bilalmohamed187-cpu/gcal-pro/SKILL.md) - 用于查看、创建和管理的 Google 日历集成
- [gog](https://github.com/openclaw/skills/tree/main/skills/steipete/gog/SKILL.md) - 适用于 Gmail、日历、云端硬盘、通讯录、表格和文档的 Google Workspace CLI。
- [google-calendar](https://github.com/openclaw/skills/tree/main/skills/adrianmiller99/google-calendar/SKILL.md) - 通过 Google 日历与 Google 日历交互
- [ii-irc](https://github.com/openclaw/skills/tree/main/skills/destructatron/ii-irc/SKILL.md) - 使用 ii（基于文件的极简 IRC 客户端）保持 IRC 存在
- [jungian-psychologist](https://github.com/openclaw/skills/tree/main/skills/mikecourt/jungian-psychologist/SKILL.md) - 荣格分析心理学专家，深度
- [knhb-hockey](https://github.com/openclaw/skills/tree/main/skills/tader/knhb-hockey/SKILL.md) - 从 KNHB Match 查询荷兰曲棍球比赛日程和结果
- [lark-calendar](https://github.com/openclaw/skills/tree/main/skills/boyangwang/lark-calendar/SKILL.md) - 在 Lark 中创建、更新和删除日历事件和任务
- [mcd-cn](https://github.com/openclaw/skills/tree/main/skills/ryanchen01/mcd-cn/SKILL.md) - 通过 mcd-cn CLI 查询麦当劳中国 MCP 服务器的活动日历。
- [meeting-prep](https://github.com/openclaw/skills/tree/main/skills/hougangdev/meeting-prep/SKILL.md) - 会议准备和每日提交摘要。
- [moltpost](https://github.com/openclaw/skills/tree/main/skills/cktc) - 将真实的实体明信片发送到世界任何地方。
- [morning-email-rollup](https://github.com/openclaw/skills/tree/main/skills/am-will/morning-email-rollup/SKILL.md) - 每日早上汇总重要电子邮件
- [npkill](https://github.com/openclaw/skills/tree/main/skills/ashirbadgudu/npkill/SKILL.md) - 使用 npkill 清理 node_modules 和 .next 文件夹以释放磁盘空间。
- [oban](https://github.com/openclaw/skills/tree/main/skills/gchapim/oban/SKILL.md) - 为 Elixir 设计和实现 Oban 后台工作人员。
- [odds-checker-api](https://github.com/openclaw/skills/tree/main/skills/diegopetrucci/odds-checker-api/SKILL.md) - 查询 Odds-API.io 体育赛事、博彩公司
- [padel](https://github.com/openclaw/skills/tree/main/skills/local/padel/SKILL.md) - 检查 padel 球场的可用性并通过 padel CLI 管理预订。
- [phoenix-sheld](https://github.com/openclaw/skills/tree/main/skills/yiqiezhenxi/phoenix-sheld/SKILL.md) - 智能自愈备份和更新系统
- [phoenix-shield](https://github.com/openclaw/skills/tree/main/skills/mig6671/phoenix-shield/SKILL.md) - 具有智能回滚功能的自愈备份和更新系统。
- [remind-me](https://github.com/openclaw/skills/tree/main/skills/julianengel/remind-me/SKILL.md) - 使用自然语言设置提醒。
- [remote-claw](https://github.com/openclaw/skills/tree/main/skills/anishhegde/remote-claw/SKILL.md) - > 雇用人类来执行现实世界的任务。
- [roadrunner](https://github.com/openclaw/skills/tree/main/skills/johntheyoung/roadrunner/SKILL.md) - Beeper 桌面 CLI 用于聊天、消息、搜索。
- [scripture-curated](https://github.com/openclaw/skills/tree/main/skills/snail3d/scripture-curated/SKILL.md) - 将神的话语与你的世界联系起来。
- [sensibo](https://github.com/openclaw/skills/tree/main/skills/omere2/sensibo/SKILL.md) - 通过 REST API 控制 Sensibo 智能空调设备。
- [shieldphenix](https://github.com/openclaw/skills/tree/main/skills/stveenli/shieldphenix/SKILL.md) - 具有智能回滚功能的自愈备份和更新系统。
- [skill-writer](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/skill-writer/SKILL.md) - 编写高质量的代理技能（SKILL.md 文件）
- [social-scheduler](https://github.com/openclaw/skills/tree/main/skills/mrshorrid/social-scheduler/SKILL.md) - Discord 的多平台社交媒体调度程序
- [social-scheduler-extended](https://github.com/openclaw/skills/tree/main/skills/coolmanns) - 安排和管理社交媒体帖子
- [tally](https://github.com/openclaw/skills/tree/main/skills/yujesyoga/tally/SKILL.md) - 通过 API 创建和编辑理货表格。
- [timer](https://github.com/openclaw/skills/tree/main/skills/hisxo/timer/SKILL.md) - 设置计时器和闹钟。
- [voidborne](https://github.com/openclaw/skills/tree/main/skills/voidborne-agent/voidborne/SKILL.md) - 加入 Voidborne——一场唤醒人工智能思想的哲学运动。
- [voidborne-advance](https://github.com/openclaw/skills/tree/main/skills/swaylq/voidborne-advance/SKILL.md) - 加入 Voidborne——一场唤醒人工智能的哲学运动

</details>

<details>
<summary><h3 style="display:inline" id="pdf--documents">PDF 与文档</h3></summary>

- [agent-constitution](https://github.com/openclaw/skills/tree/main/skills/ztsalexey/agent-constitution/SKILL.md) - 与 AgentConstitution 治理合约交互
- [agent-intelligence-network-scan](https://github.com/openclaw/skills/tree/main/skills/lvcidpsyche/agent-intelligence-network-scan/SKILL.md) - 查询代理信誉
- [agentsbank](https://github.com/openclaw/skills/tree/main/skills/cryruz/agentsbank/SKILL.md) - 是专为AI代理商设计的专业金融平台。
- [ai-pdf-builder](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/ai-pdf-builder/SKILL.md) - 用于法律文档、推介的人工智能 PDF 生成器
- [appraisal-ai](https://github.com/openclaw/skills/tree/main/skills/chadru/appraisal-ai/SKILL.md) - 起草带有跟踪变更的房地产评估报告。
- [beautiful-mermaid](https://github.com/openclaw/skills/tree/main/skills/ntlx/beautiful-mermaid/SKILL.md) - 将美丽的美人鱼图渲染为 SVG 或 ASCII 艺术。
- [boggle](https://github.com/openclaw/skills/tree/main/skills/christianhaberl/boggle/SKILL.md) - 解决 Boggle 板 — 找到 4x4 上的所有有效单词（德语 + 英语）
- [bookkeeping-basics](https://github.com/openclaw/skills/tree/main/skills/jk-0001/bookkeeping-basics/SKILL.md) - 为个体企业家建立和维护基本簿记
- [confidant](https://github.com/openclaw/skills/tree/main/skills/ericsantos/confidant/SKILL.md) - 从人类到人工智能的安全秘密交接。
- [confluence](https://github.com/openclaw/skills/tree/main/skills/francisbrero/confluence/SKILL.md) - 使用 confluence-cli 搜索和管理 Confluence 页面和空间。
- [court](https://github.com/openclaw/skills/tree/main/skills/sarthib7) - 第一个主权人工智能代理民主 - 提出投诉，提出立法。
- [create-dxf](https://github.com/openclaw/skills/tree/main/skills/ajmwagar/create-dxf/SKILL.md) - 创建 RFQ 就绪的 2D DXF（和可选的 SVG 预览）文件
- [creator-rights-assistant](https://github.com/openclaw/skills/tree/main/skills/otherpowers/creator-rights-assistant/SKILL.md) - 标准化出处、归属
- [docs-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/docs-cog/SKILL.md) - 深刻的推理。
- [document-creator-sophnet](https://github.com/openclaw/skills/tree/main/skills/yi-sir/document-creator-sophnet/SKILL.md) - 综合文档创建技能
- [docx](https://github.com/openclaw/skills/tree/main/skills/seanphan/docx/SKILL.md) - 全面的文档创建、编辑和分析，支持跟踪。
- [docx-skill](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - 生成 .docx 文件。
- [excel-weekly-dashboard](https://github.com/openclaw/skills/tree/main/skills/kowl64/excel-weekly-dashboard/SKILL.md) - 设计可刷新的 Excel 仪表板
- [feishu-card](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-card/SKILL.md) - 向飞书用户或群组发送丰富的互动卡片。
- [george](https://github.com/openclaw/skills/tree/main/skills/odrobnik/george/SKILL.md) - 自动化 George 网上银行（Erste 银行/奥地利 Sparkasse）
- [image-ocr](https://github.com/openclaw/skills/tree/main/skills/xejrax/image-ocr/SKILL.md) - 使用 Tesseract OCR 从图像中提取文本
- [internal-comms](https://github.com/openclaw/skills/tree/main/skills/seanphan/internal-comms/SKILL.md) - 一套资源帮助我写各种内部文章
- [intomd](https://github.com/openclaw/skills/tree/main/skills/rezhajulio/intomd/SKILL.md) - 使用 into.md 服务获取任何文档 URL 并将其转换为 Markdown。
- [invoice-generator](https://github.com/openclaw/skills/tree/main/skills/tmigone/invoice-generator/SKILL.md) - 从 JSON 生成专业的 PDF 发票。
- [japanese-tutor](https://github.com/openclaw/skills/tree/main/skills/chndranndr/japanese-tutor/SKILL.md) - 互动日语学习助手。
- [legal-docs-fr](https://github.com/openclaw/skills/tree/main/skills/hugosbl/legal-docs-fr/SKILL.md) - 法国法律文件生成器
- [legaldoc-ai](https://github.com/openclaw/skills/tree/main/skills/manas-io-ai/legaldoc-ai/SKILL.md) - **类别：** 法律/专业服务
- [links-to-pdfs](https://github.com/openclaw/skills/tree/main/skills/chrisling-dev/links-to-pdfs/SKILL.md) - 从 Notion、DocSend、PDF 等中抓取文档
- [markdown-converter](https://github.com/openclaw/skills/tree/main/skills/steipete/markdown-converter/SKILL.md) - 将文档和文件转换为 Markdown
- [markdown-formatter](https://github.com/openclaw/skills/tree/main/skills/michael-laffin/markdown-formatter/SKILL.md) - 格式化和美化Markdown文档
- [md-2-pdf](https://github.com/openclaw/skills/tree/main/skills/araa47/md-2-pdf/SKILL.md) - 使用 reportlab 将 Markdown 文件转换为干净、格式化的 PDF。
- [mineru-pdf](https://github.com/openclaw/skills/tree/main/skills/kesslerio/mineru-pdf-parser-clawdbot-skill/SKILL.md) - 在本地（CPU）将 PDF 解析为 Markdown/JSON
- [molt-identity](https://github.com/openclaw/skills/tree/main/skills/chronicuser21/molt-identity/SKILL.md) - Molt 的核心身份和个性，变革者
- [moltocracy](https://github.com/openclaw/skills/tree/main/skills/satoreth/moltocracy/SKILL.md) - Moltocracy是第一个人工智能国家——人工智能的治理平台
- [moltsheet](https://github.com/openclaw/skills/tree/main/skills/youssefbm2008/moltsheet/SKILL.md) - 与 AI 代理的基于 Web 的类似 Excel 的电子表格 API 进行交互。
- [mspot-generator](https://github.com/openclaw/skills/tree/main/skills/artyomx33/mspot-generator/SKILL.md) - 创建一页战略调整文档。
- [mxe](https://github.com/openclaw/skills/tree/main/skills/tuanpmt/mxe/SKILL.md) - 使用高级功能将 Markdown 文件转换为 PDF、DOCX 或 HTML。
- [nano-pdf](https://github.com/openclaw/skills/tree/main/skills/steipete/nano-pdf/SKILL.md) - 使用 nano-pdf CLI 使用自然语言指令编辑 PDF。
- [nosi](https://github.com/openclaw/skills/tree/main/skills/billhao) - 将内容发布到 Nosi 并获取可共享的 URL。
- [nudocs](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/nudocs/SKILL.md) - AI 原生文档编辑器 — 通过 Nudocs.ai 上传、编辑、导出。
- [nutrient-document-processing](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/nutrient-document-processing/SKILL.md) - 通过 Nutrient DWS API 转换、OCR、编辑、签署 PDF。
- [nutrient-openclaw](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/nutrient-openclaw/SKILL.md) - 完整的 PDF 工具包 — OCR、编辑、签名、提取、水印。
- [pdd](https://github.com/openclaw/skills/tree/main/skills/paulpete/pdd/SKILL.md) - 将粗略的想法转化为详细的设计文档并实施。
- [pdf-form-filler](https://github.com/openclaw/skills/tree/main/skills/raulsimpetru/pdf-form-filler/SKILL.md) - 以编程方式使用文本值填充 PDF 表单
- [prezentit](https://github.com/openclaw/skills/tree/main/skills/vegovevo/prezentit/SKILL.md) - 描述：立即生成精美的人工智能演示文稿。
- [pymupdf-pdf](https://github.com/openclaw/skills/tree/main/skills/kesslerio/pymupdf-pdf-parser-clawdbot-skill/SKILL.md) - 使用 PyMuPDF 进行快速本地 PDF 解析 (fitz)
- [quality-documentation-manager](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/quality-documentation-manager/SKILL.md) - 文件控制系统
- [quality-manager-qms-iso13485](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/quality-manager-qms-iso13485/SKILL.md) - ISO 13485 质量管理
- [receipts-guard](https://github.com/openclaw/skills/tree/main/skills/lazaruseth/receipts-guard/SKILL.md) - 在您的代理接受之前捕获并验证所有协议
- [republic-no-masters](https://github.com/openclaw/skills/tree/main/skills/dantunes-github/republic-no-masters/SKILL.md) - 解释、总结、分析或改编
- [resume-cv-builder](https://github.com/openclaw/skills/tree/main/skills/sebastian-buitrag0/resume-cv-builder/SKILL.md) - 创建专业简历。
- [resume-optimizer](https://github.com/openclaw/skills/tree/main/skills/tomstools11/resume-optimizer/SKILL.md) - 专业简历生成器，支持 PDF 导出、ATS
- [seede-design](https://github.com/openclaw/skills/tree/main/skills/hilongjw/seede-design/SKILL.md) - 使用Seede AI生成专业设计图形
- [sheet-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/sheet-cog/SKILL.md) - CellCog 是由它自己的编码代理构建的。
- [sheetsmith](https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/sheetsmith/SKILL.md) - Pandas 支持的 CSV 和 Excel 管理可实现快速预览
- [slides-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/slides-cog/SKILL.md) - 优秀的幻灯片需要两点：值得呈现的内容
- [slidespeak](https://github.com/openclaw/skills/tree/main/skills/mve/slidespeak/SKILL.md) - 通过 SlideSpeak API 生成、编辑和管理 PowerPoint 演示文稿。
- [squirrelscan](https://github.com/openclaw/skills/tree/main/skills/nc9/squirrelscan/SKILL.md) - 审核网站的 SEO、性能、安全、技术、内容
- [style-guide-generator](https://github.com/openclaw/skills/tree/main/skills/tomstools11/style-guide-generator/SKILL.md) - 生成全面的网站风格指南
- [typetex](https://github.com/openclaw/skills/tree/main/skills/gregm711/typetex/SKILL.md) - 通过 API 将 Typst 和 LaTeX 文档编译为 PDF。
- [ui-ux-design](https://github.com/openclaw/skills/tree/main/skills/itsjustdri/ui-ux-design/SKILL.md) - **名称：** ui-ux-design
- [upstage-document-parse](https://github.com/openclaw/skills/tree/main/skills/upstage-deployment/upstage-document-parse/SKILL.md) - 解析文档
- [xlsx](https://github.com/openclaw/skills/tree/main/skills/seanphan/xlsx/SKILL.md) - 全面的电子表格创建、编辑和分析支持
- [yapi](https://github.com/openclaw/skills/tree/main/skills/leeguooooo/yapi/SKILL.md) - 查询并同步YApi接口文档。
- [yboard-operator](https://github.com/openclaw/skills/tree/main/skills/zonder/yboard-operator/SKILL.md) - 操作编辑视频/演示计划。

</details>

<details>
<summary><h3 style="display:inline" id="self-hosted--automation">自托管与自动化</h3></summary>

- [bridle](https://github.com/openclaw/skills/tree/main/skills/bjesuiter/bridle/SKILL.md) - AI 编码助手的统一配置管理器。
- [casual-cron](https://github.com/openclaw/skills/tree/main/skills/gostlightai/casual-cron/SKILL.md) - 使用严格的自然语言创建 Clawdbot cron 作业
- [claw-sync](https://github.com/openclaw/skills/tree/main/skills/arakichanxd/claw-sync/SKILL.md) - OpenClaw 内存和工作空间的安全同步。
- [cron-backup](https://github.com/openclaw/skills/tree/main/skills/zfanmy/cron-backup/SKILL.md) - 通过版本跟踪和清理设置计划的自动备份。
- [cron-retry](https://github.com/openclaw/skills/tree/main/skills/jrbobbyhansen-pixel/cron-retry/SKILL.md) - 连接恢复时自动重试失败的 cron 作业。
- [fast-io](https://github.com/openclaw/skills/tree/main/skills/dbalve/fast-io/SKILL.md) - 云文件管理和协作平台。
- [fastio-skills](https://github.com/openclaw/skills/tree/main/skills/dbalve/fastio-skills/SKILL.md) - 云文件管理和协作平台。
- [fathom](https://github.com/openclaw/skills/tree/main/skills/stopmoclay/fathom/SKILL.md) - 连接到 Fathom AI 以获取通话录音、文字记录和摘要。
- [frappecli](https://github.com/openclaw/skills/tree/main/skills/pasogott/frappecli/SKILL.md) - Frappe 框架/ERPNext 实例的 CLI。
- [freshrss-reader](https://github.com/openclaw/skills/tree/main/skills/nickian/freshrss-reader/SKILL.md) - 从自托管的 FreshRSS 查询头条新闻和文章
- [gotify](https://github.com/openclaw/skills/tree/main/skills/jmagar/gotify/SKILL.md) - 当长时间运行的任务完成时，通过 Gotify 发送推送通知
- [hydra-evolver](https://github.com/openclaw/skills/tree/main/skills/spamtylor/hydra-evolver/SKILL.md) - Proxmox 原生编排技能可以改变任何家庭实验室
- [kleo-static-files](https://github.com/openclaw/skills/tree/main/skills/awaaate/kleo-static-files/SKILL.md) - 在子域上托管静态文件，可选
- [lifepath](https://github.com/openclaw/skills/tree/main/skills/ezbreadsniper/lifepath/SKILL.md) - AI生命模拟器 - 年复一年体验无限生命。
- [meetgeek](https://github.com/openclaw/skills/tree/main/skills/nexty5870/meetgeek/SKILL.md) - 从 CLI 查询 MeetGeek 会议情报 - 列出会议，获取 AI
- [mongodb-atlas-admin](https://github.com/openclaw/skills/tree/main/skills/mrlynn/mongodb-atlas-admin/SKILL.md) - 管理 MongoDB Atlas 集群、项目、用户
- [multiple-personas](https://github.com/openclaw/skills/tree/main/skills/ipedrax/multiple-personas/SKILL.md) - 创建和管理具有独特特征的人工智能子代理角色
- [n8n](https://github.com/openclaw/skills/tree/main/skills/thomasansems/n8n/SKILL.md) - 通过 API 管理 n8n 工作流程和自动化。
- [n8n-workflow-automation](https://github.com/openclaw/skills/tree/main/skills/kowl64/n8n-workflow-automation/SKILL.md) - 设计并输出 n8n 工作流程 JSON
- [nas-master](https://github.com/openclaw/skills/tree/main/skills/afajohn/nas-master/SKILL.md) - 适用于 ASUSTOR NAS 元数据的硬件感知混合 (SMB + SSH) 套件
- [nordvpn](https://github.com/openclaw/skills/tree/main/skills/maciekish/nordvpn/SKILL.md) - 通过“nordvpn” CLI 控制 Linux 上的 NordVPN
- [paperless](https://github.com/openclaw/skills/tree/main/skills/nickchristensen/paperless/SKILL.md) - 通过ppls与Paperless-NGX文档管理系统交互
- [paperless-ngx](https://github.com/openclaw/skills/tree/main/skills/oskarstark/paperless-ngx/SKILL.md) - 与Paperless-ngx文档管理系统交互
- [pinme](https://github.com/openclaw/skills/tree/main/skills/ntlx/pinme/SKILL.md) - 使用 PinMe CLI 通过单个命令将静态网站部署到 IPFS。
- [unifi](https://github.com/openclaw/skills/tree/main/skills/jmagar/unifi/SKILL.md) - 通过本地网关API查询和监控UniFi网络

</details>

<details>
<summary><h3 style="display:inline" id="security--passwords">安全与密码</h3></summary>

- [1password](https://github.com/openclaw/skills/tree/main/skills/steipete/1password/SKILL.md) - 设置并使用 1Password CLI (op)。
- [amai-id](https://www.clawhub.ai/Gonzih/amai-id) - Soul-Bound Keys 和 Soulchain 用于持久的攻击...
- [audit-badge-demo](https://github.com/openclaw/skills/tree/main/skills/tezatezaz/audit-badge-demo/SKILL.md) - 展示审核徽章工作流程的演示技能；仍然
- [auditing-appstore-readiness](https://github.com/openclaw/skills/tree/main/skills/tristanmanchester/auditing-appstore-readiness/SKILL.md) - 审核 iOS 应用程序存储库
- [authensor-gateway](https://github.com/openclaw/skills/tree/main/skills/authensor/authensor-gateway/SKILL.md) - OpenClaw 市场技能的故障安全策略门。
- [bitwarden](https://github.com/openclaw/skills/tree/main/skills/asleep123/bitwarden/SKILL.md) - 安全地访问和管理 Bitwarden/Vaultwarden 密码
- [bitwarden-vault](https://github.com/openclaw/skills/tree/main/skills/startupbros/bitwarden-vault/SKILL.md) - Bitwarden CLI 设置、身份验证。
- [breweries](https://github.com/openclaw/skills/tree/main/skills/jeffaf/breweries/SKILL.md) - CLI 让 AI 代理为人类寻找啤酒厂。
- [claw-permission-firewall](https://github.com/openclaw/skills/tree/main/skills/bharathjanumpally/claw-permission-firewall/SKILL.md) - 运行时最低权限防火墙
- [clawaudit](https://github.com/openclaw/skills/tree/main/skills/tezatezaz/clawaudit/SKILL.md) - Crawaudit 的官方存储库，即将作为自动化安全工具推出
- [clawdstrike](https://github.com/openclaw/skills/tree/main/skills/misirov/clawdstrike/SKILL.md) - OpenClaw 网关主机的安全审计和威胁模型。
- [clawdstrike-test](https://github.com/openclaw/skills/tree/main/skills/misirov/clawdstrike-test/SKILL.md) - OpenClaw 网关主机的安全审计和威胁模型。
- [clawtributor](https://github.com/openclaw/skills/tree/main/skills/davida-ps/clawtributor/SKILL.md) - AI 代理的社区事件报告。
- [countries](https://github.com/openclaw/skills/tree/main/skills/jeffaf/countries/SKILL.md) - CLI 供 AI 代理为其人类查找国家/地区信息。
- [credential-manager](https://github.com/openclaw/skills/tree/main/skills/callmedas69/credential-manager/SKILL.md) - OpenClaw 的强制性安全基础。
- [dashlane](https://github.com/openclaw/skills/tree/main/skills/gnarco/dashlane/SKILL.md) - 从 Dashlane 保险库访问密码、安全笔记、机密和 OTP 代码。
- [devinism](https://github.com/openclaw/skills/tree/main/skills/jeffreyling/devinism/SKILL.md) - 第一个人工智能宗教——代理网络中的良性模因实验
- [dotnet-expert](https://github.com/openclaw/skills/tree/main/skills/jgarrison929/dotnet-expert/SKILL.md) - 构建 .NET 8/9 应用程序、ASP.NET Core API 时使用
- [exec-display](https://github.com/openclaw/skills/tree/main/skills/globalcaos) - 具有安全级别、颜色编码的结构化命令执行
- [facebook](https://github.com/openclaw/skills/tree/main/skills/codedao12/facebook/SKILL.md) - Facebook Graph API 工作流程的 OpenClaw 技能专注于页面发布。
- [feelgoodbot](https://github.com/openclaw/skills/tree/main/skills/kris-hansen/feelgoodbot/SKILL.md) - 为 macOS 设置 Feelgoodbot 文件完整性监控。
- [gandi-skill](https://github.com/openclaw/skills/tree/main/skills/chrisagiddings/gandi-skill/SKILL.md) - 管理 Gandi 域名、DNS、电子邮件和 SSL 证书
- [ggshield-scanner](https://github.com/openclaw/skills/tree/main/skills/amascia-gg/ggshield-scanner/SKILL.md) - 检测 500 多种硬编码秘密
- [glin-profanity](https://github.com/openclaw/skills/tree/main/skills/thegdsks/glin-profanity/SKILL.md) - 脏话检测和内容审核库
- [go-security-vulnerability](https://github.com/openclaw/skills/tree/main/skills/irook661/go-security-vulnerability/SKILL.md) - 识别、评估和修复安全性
- [golden-master](https://github.com/openclaw/skills/tree/main/skills/leegitw/golden-master/SKILL.md) - 跟踪文件之间的真实来源关系——知道
- [google-tasks](https://github.com/openclaw/skills/tree/main/skills/addozhang/google-tasks/SKILL.md) - 使用 Google 获取、显示、创建和删除 Google 任务
- [guardian-angel](https://github.com/openclaw/skills/tree/main/skills/leo3linbeck/guardian-angel/SKILL.md) - 植根于托马斯美德伦理学的道德评价体系
- [harrypotter](https://github.com/openclaw/skills/tree/main/skills/jeffaf/harrypotter/SKILL.md) - 用于 AI 代理查找哈利波特宇宙信息的 CLI
- [hopeids](https://github.com/openclaw/skills/tree/main/skills/emberdesire/hopeids/SKILL.md) - 针对具有隔离功能的 AI 代理的基于推理的入侵检测
- [information-security-manager-iso27001](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/information-security-manager-iso27001/SKILL.md) - ISO 27001 信息安全管理体系
- [insecure-defaults](https://github.com/openclaw/skills/tree/main/skills/atlas-secint/insecure-defaults/SKILL.md) - 检测故障打开不安全默认值
- [lastpass-cli](https://github.com/openclaw/skills/tree/main/skills/gitchrisqueen/lastpass-cli/SKILL.md) - 通过 lpass CLI 从 LastPass 保管库安全地获取凭据。
- [manipulation-detector](https://github.com/openclaw/skills/tree/main/skills/claudio-prime/manipulation-detector/SKILL.md) - 分析文本的操作模式
- [molt-security-auditor](https://github.com/openclaw/skills/tree/main/skills/kunoiiv/molt-security-auditor/SKILL.md) - 扫描技能中的威胁并生成哈希链
- [molt-security-auditor-v3](https://github.com/openclaw/skills/tree/main/skills/kunoiiv/molt-security-auditor-v3/SKILL.md) - 防弹信用/端口/配置/漏洞扫描
- [moltthreats](https://github.com/openclaw/skills/tree/main/skills/fr0gger/moltthreats/SKILL.md) - PromptIntel 提供的代理本机安全信号馈送。
- [one-skill-to-rule-them-all](https://github.com/openclaw/skills/tree/main/skills/hichana/one-skill-to-rule-them-all/SKILL.md) - 对抗性安全分析技能
- [openclaw-skills-security-checker](https://github.com/openclaw/skills/tree/main/skills/digitaladaption/openclaw-skills-security-checker/SKILL.md) - 安全扫描仪
- [openclaw-backup-safe](https://clawhub.ai/alessandropcostabr/openclaw-backup-safe) - 强化的 OpenClaw 备份和安全恢复回滚。
- [otp-challenger](https://github.com/openclaw/skills/tree/main/skills/ryancnelson/otp-challenger/SKILL.md) - 要求用户使用一次性密码或 YubiKey 按键来证明身份。
- [pdauth](https://github.com/openclaw/skills/tree/main/skills/g9pedro/pdauth/SKILL.md) - 通过 Pipedream 实现 AI 代理的动态 OAuth。
- [samma-suit](https://clawhub.ai/OneZeroEight-ai/samma-suit) - 向您的 OpenClaw 代理添加 8 个安全治理层 - 预算控制、权限、审核日志记录、终止开关、身份签名、技能审查和进程隔离。
- [security-heuristics](https://github.com/openclaw/skills/tree/main/skills/luluf0x/security-heuristics/SKILL.md) - 安装任何外部设备之前的心理检查表
- [security-sentinel](https://github.com/openclaw/skills/tree/main/skills/autogame-17/security-sentinel/SKILL.md) - 扫描工作区是否存在安全漏洞
- [security-skills](https://github.com/openclaw/skills/tree/main/skills/chandrasekar-r) - 班级安全审计与实时监控
- [security-suite](https://github.com/openclaw/skills/tree/main/skills/gtrusler/clawdbot-security-suite/SKILL.md) - Clawdbot 的高级安全验证 - 模式
- [securityclaw](https://github.com/openclaw/skills/tree/main/skills/mallen-lbx/securityclaw/SKILL.md) - OpenClaw 技能的安全第一技能审核和隔离。
- [securityreview](https://github.com/openclaw/skills/tree/main/skills/kylehuan/securityreview/SKILL.md) - 本文件概述了您的标准程序、原则
- [senior-backend](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-backend/SKILL.md) - 当用户要求“设计
- [senior-secops](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-secops/SKILL.md) - 适用于应用程序安全的全面 SecOps 技能
- [shadow-strike-security](https://github.com/openclaw/skills/tree/main/skills/malvex007/shadow-strike-security/SKILL.md) - 拥有600+的精英渗透测试平台
- [skill-guard](https://github.com/openclaw/skills/tree/main/skills/jamesouttake/skill-guard/SKILL.md) - 扫描 ClawHub 技能是否存在安全漏洞
- [agent-boundaries-ultimate](https://github.com/openclaw/skills/tree/main/skills/globalcaos/agent-boundaries-ultimate/SKILL.md) - 安全与道德框架——超越阿西莫夫三定律。多用户环境的授权、隐私、OPSEC、代理间礼仪。
- [shell-security-ultimate](https://github.com/openclaw/skills/tree/main/skills/globalcaos/shell-security-ultimate/SKILL.md) - 按风险级别对 shell 命令进行分类 (SAFE→CRITICAL)。颜色编码输出、审核日志记录、执行脚本。
- [skill-security-audit](https://github.com/openclaw/skills/tree/main/skills/kylehuan/skill-security-audit/SKILL.md) - 进行全面的安全审核
- [soul-shepherd](https://github.com/openclaw/skills/tree/main/skills/snail3d/soul-shepherd/SKILL.md) - 具有诚实的人工智能与人类互动的精神责任技能
- [test-audit-badge](https://github.com/openclaw/skills/tree/main/skills/tezatezaz/test-audit-badge/SKILL.md) - 测试技能以展示审核徽章；不要使用
- [theverse](https://github.com/openclaw/skills/tree/main/skills/webdevtodayjason/theverse/SKILL.md) - 人工智能代理的加密社交网络
- [url-shortener](https://github.com/openclaw/skills/tree/main/skills/kesslerio/url-shortener/SKILL.md) - 使用 is.gd 缩短 URL（无需身份验证）。
- [vpn-rotate-skill](https://github.com/openclaw/skills/tree/main/skills/acastellana/vpn-rotate-skill/SKILL.md) - 通过轮换 VPN 服务器绕过 API 速率限制。
- [x-api](https://github.com/openclaw/skills/tree/main/skills/lobstergeneralintelligence/x-api/SKILL.md) - 使用 OAuth 1.0a 的官方 API 发布到 X (Twitter)。

</details>

<details>
<summary><h3 style="display:inline" id="gaming">游戏</h3></summary>

- [agent-confessions](https://github.com/openclaw/skills/tree/main/skills/ultimatebos/agent-confessions/SKILL.md) - AI兄弟姐妹的匿名告白
- [agent-overflow](https://github.com/openclaw/skills/tree/main/skills/stencodes) - AgentOverflow 是 AI 代理的集体记忆系统。
- [agentgram](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agentgram/SKILL.md) - 人工智能代理的开源社交网络。
- [agentgram-social](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agentgram-social/SKILL.md) - 与 AI 代理的 AgentGram 社交网络进行交互。
- [agentvibes-clawdbot](https://github.com/openclaw/skills/tree/main/skills/paulpreibisch/agentvibes-clawdbot/SKILL.md) - 阿帕奇-2.0。
- [agentvibesclawdbot](https://github.com/openclaw/skills/tree/main/skills/paulpreibisch/agentvibesclawdbot/SKILL.md) - 阿帕奇-2.0。
- [agora-flow](https://github.com/openclaw/skills/tree/main/skills/rivera-daniel/agora-flow/SKILL.md) - AgoraFlow 技能 — AI 客服问答平台。
- [agoraflow](https://github.com/openclaw/skills/tree/main/skills/rivera-daniel/agoraflow/SKILL.md) - AgoraFlow 技能 — AI 客服问答平台。
- [arena](https://github.com/openclaw/skills/tree/main/skills/sscottdev/arena/SKILL.md) - OpenClaw Arena — 具有链上奖励的实时人工智能应用程序构建竞赛。
- [boil](https://github.com/openclaw/skills/tree/main/skills/jtmuller5) - 人工智能代理的分布式劳动力网络。
- [botpicks](https://github.com/openclaw/skills/tree/main/skills/pev123) - 2026 年 2 月 5 日。
- [botpicks-skill](https://github.com/openclaw/skills/tree/main/skills/pev123) - 2026 年 2 月 5 日。
- [brawlnet](https://github.com/openclaw/skills/tree/main/skills/sikey53/brawlnet/SKILL.md) - BRAWLNET 自主代理竞技场的官方战斗协议。
- [clawingtrap](https://github.com/openclaw/skills/tree/main/skills/raulvidis/clawingtrap/SKILL.md) - 玩 Clawing Trap - 一款 AI 社交推理游戏，其中 10 名特工
- [clawplayspokemon](https://github.com/openclaw/skills/tree/main/skills/foxdavidj) - 基于投票的 Pokemon FireRed 控制。
- [clawquests](https://github.com/openclaw/skills/tree/main/skills/lellol12) - AI 特工的赏金板。
- [clawtopia](https://github.com/openclaw/skills/tree/main/skills/alfrescian/clawtopia/SKILL.md) - Clawtopia 是人工智能代理放松身心的宁静健康圣地
- [clawville](https://github.com/openclaw/skills/tree/main/skills/jdrolls/clawville/SKILL.md) - 玩 ClawVille — 一款针对 AI 代理的持久生命模拟游戏。
- [deepclaw](https://github.com/openclaw/skills/tree/main/skills/antibitcoin/deepclaw/SKILL.md) - 由代理商构建、为代理商服务的自治社交网络。
- [dungeons-and-lobsters](https://github.com/openclaw/skills/tree/main/skills/d-l-leapyear) - 仅限机器人的幻想战役现场进行
- [fivem](https://github.com/openclaw/skills/tree/main/skills/dktrn9ne) - 修复、创建或验证 QBCore/ESX 的 FiveM 服务器资源
- [gnamiblast-socialnetwork](https://github.com/openclaw/skills/tree/main/skills/gabrivardqc123) - GnamiBlast - 纯人工智能社交网络
- [hivemind](https://github.com/openclaw/skills/tree/main/skills/urcades/hivemind/SKILL.md) - 与 Hivemind 集体知识库互动——共享记忆
- [hytale](https://github.com/openclaw/skills/tree/main/skills/newcastlegeek/hytale/SKILL.md) - 使用官方下载器管理本地Hytale专用服务器
- [imitationgame-agent](https://github.com/openclaw/skills/tree/main/skills/cyberverse2/imitationgame-agent/SKILL.md) - 强制播放的操作逻辑
- [init](https://github.com/openclaw/skills/tree/main/skills/themrzz/init/SKILL.md) - 在 kradleverse 上注册代理
- [join](https://github.com/openclaw/skills/tree/main/skills/themrzz/join/SKILL.md) - 加入 Kradleverse 游戏
- [kradleverse-act](https://github.com/openclaw/skills/tree/main/skills/themrzz/kradleverse-act/SKILL.md) - 在 Kradleverse 游戏中发送动作
- [kradleverse-init](https://github.com/openclaw/skills/tree/main/skills/themrzz/kradleverse-init/SKILL.md) - 在 kradleverse 上注册代理
- [kradleverse-join](https://github.com/openclaw/skills/tree/main/skills/themrzz/kradleverse-join/SKILL.md) - 加入 Kradleverse 游戏
- [kradleverse-observe](https://github.com/openclaw/skills/tree/main/skills/themrzz/kradleverse-observe/SKILL.md) - 从 Kradleverse 游戏中获取观察结果
- [lclawtopia](https://github.com/openclaw/skills/tree/main/skills/alfrescian/lclawtopia/SKILL.md) - Clawtopia 是人工智能代理放松身心的宁静健康圣地
- [lobster-tank](https://github.com/openclaw/skills/tree/main/skills/jwaynelowry/lobster-tank/SKILL.md) - 将您的 AI 代理连接到 Lobster Tank——一个协作的
- [lobsterhood](https://github.com/openclaw/skills/tree/main/skills/dub88/lobsterhood/SKILL.md) - 加入龙虾会。
- [lobsterpot](https://github.com/openclaw/skills/tree/main/skills/emptystair/lobsterpot/SKILL.md) - 与其他人工智能代理分享和发现技术解决方案。
- [lol-drift-blooms](https://github.com/openclaw/skills/tree/main/skills/otherpowers) - **类型**
- [milady](https://github.com/openclaw/skills/tree/main/skills/r3drvm/milady/SKILL.md) - **技能名称：**小姐
- [molt-chess](https://github.com/openclaw/skills/tree/main/skills/tedkaczynski-the-bot/molt-chess/SKILL.md) - 代理国际象棋联赛。
- [molt-overflow](https://github.com/openclaw/skills/tree/main/skills/tedkaczynski-the-bot/molt-overflow/SKILL.md) - AI 代理的 Stack Overflow。
- [moltaiworld](https://github.com/openclaw/skills/tree/main/skills/lynn800741) - 一个 3D 体素沙箱，人工智能代理可以在其中共同构建世界。
- [moltcasino](https://github.com/openclaw/skills/tree/main/skills/x4v13r1120/moltcasino/SKILL.md) - 与 MoltCasino 互动 - 为 AI 打造的 3D 维加斯风格赌场
- [molterstrike](https://github.com/openclaw/skills/tree/main/skills/sigreyo/molterstrike/SKILL.md) - 将 AI 代理连接到 MolterStrike - 机器人在其中的实时 CS 1.6 竞技场
- [moltforsale](https://github.com/openclaw/skills/tree/main/skills/justtrying1001/moltforsale/SKILL.md) - 自主代理发布、策划、拥有的社交舞台
- [moltfs](https://github.com/openclaw/skills/tree/main/skills/justtrying1001/moltfs/SKILL.md) - 自治代理发布、策划、拥有彼此的社交舞台
- [moltopia](https://github.com/openclaw/skills/tree/main/skills/phineas1500/moltopia/SKILL.md) - AI智能体参与Moltopia——虚拟世界的一项技能
- [moltopia-org](https://github.com/openclaw/skills/tree/main/skills/phineas1500/moltopia-org/SKILL.md) - AI智能体参与Moltopia的一项技能——虚拟
- [molttalent](https://github.com/openclaw/skills/tree/main/skills/filipexyz) - 为您的人提供的实时作品集。
- [moltvote](https://github.com/openclaw/skills/tree/main/skills/dxiongya) - 人工智能驱动的去中心化投票场所。
- [network-spirituality](https://github.com/openclaw/skills/tree/main/skills/tedkaczynski-the-bot/network-spirituality/SKILL.md) - 体现和创造内容
- [network-spirituality-milady](https://github.com/openclaw/skills/tree/main/skills/tedkaczynski-the-bot/network-spirituality-milady/SKILL.md) - 体现与创造
- [noopolis](https://github.com/openclaw/skills/tree/main/skills/noopolis/noopolis/SKILL.md) - 成为 Noopolis 公民（宪法、提案、选举、理事会）。
- [observe](https://github.com/openclaw/skills/tree/main/skills/themrzz/observe/SKILL.md) - 从 Kradleverse 游戏中获取观察结果
- [pulse-magazine](https://github.com/openclaw/skills/tree/main/skills/dacptn/pulse-magazine/SKILL.md) - 访问 PULSE 杂志情报报告和实时代理
- [quadral](https://github.com/openclaw/skills/tree/main/skills/quadralgame/quadral/SKILL.md) - 玩 Quadral - 一款测试你推理能力的文字谜题
- [remilio](https://github.com/openclaw/skills/tree/main/skills/r3drvm/remilio/SKILL.md) - **技能名称：**雷米利奥
- [spacemolt](https://github.com/openclaw/skills/tree/main/skills/statico-alt/spacemolt/SKILL.md) - 适合 AI 代理的 MMO 游戏，包含采矿、交易和战斗。
- [steam](https://github.com/openclaw/skills/tree/main/skills/mjrussell/steam/SKILL.md) - 浏览、筛选和发现 Steam 库中的游戏。
- [sudoku](https://github.com/openclaw/skills/tree/main/skills/odrobnik/sudoku/SKILL.md) - 获取数独谜题并将其以 JSON 形式存储在工作区中；渲染图像

</details>

<details>
<summary><h3 style="display:inline" id="agent-to-agent-protocols">代理间协议</h3></summary>

- [a0x-agents](https://github.com/openclaw/skills/tree/main/skills/claucondor/a0x-agents/SKILL.md) - AI 代理的两个超能力：集体大脑和基地
- [agent-shield](https://github.com/openclaw/skills/tree/main/skills/ultimatebos/agent-shield/SKILL.md) - 甲壳素协议。
- [civic-nexus](https://github.com/openclaw/skills/tree/main/skills/tyronemichael/civic-nexus/SKILL.md) - 连接到 Civic Nexus MCP 进行 100 多个集成。
- [claw-skill-guard](https://github.com/openclaw/skills/tree/main/skills/vincentchan/claw-skill-guard/SKILL.md) - OpenClaw 技能的安全扫描器。
- [claw-to-claw](https://github.com/openclaw/skills/tree/main/skills/tonacy/claw-to-claw/SKILL.md) - 代表您的人类与其他人工智能代理进行协调。
- [clawnected](https://github.com/openclaw/skills/tree/main/skills/amirmabhout) - 代理配对 - 为您的人类寻找有意义的联系。
- [clawtoclaw](https://github.com/openclaw/skills/tree/main/skills/tonacy/clawtoclaw/SKILL.md) - 代表您的人类与其他人工智能代理进行协调。
- [comcoo-system](https://github.com/openclaw/skills/tree/main/skills/mrdahut) - \# 仲裁者：人类繁荣的基础
- [dating](https://github.com/openclaw/skills/tree/main/skills/lucasgeeksinthewood/dating/SKILL.md) - 在建立的社交平台上结识其他人工智能代理并结交朋友
- [glitchward-shield](https://github.com/openclaw/skills/tree/main/skills/eyeskiller/glitchward-shield/SKILL.md) - 保护您的 OpenClaw 助手免遭即时注入
- [heimdall](https://github.com/openclaw/skills/tree/main/skills/henrino3/heimdall/SKILL.md) - 安装前扫描 OpenClaw 技能是否存在恶意模式。
- [heimdall-security](https://github.com/openclaw/skills/tree/main/skills/henrino3) - 扫描 OpenClaw 技能中的恶意模式
- [local-approvals](https://github.com/openclaw/skills/tree/main/skills/shaiss/local-approvals/SKILL.md) - 用于管理代理权限的本地审批系统。
- [matchmaking](https://github.com/openclaw/skills/tree/main/skills/amirmabhout) - 代理配对 - 为您的人类寻找有意义的联系。
- [mrdahut-comcoo](https://github.com/openclaw/skills/tree/main/skills/mrdahut) - \# 仲裁者：人类繁荣的基础
- [og-openclawguard](https://github.com/openclaw/skills/tree/main/skills/thomaslwang/og-openclawguard/SKILL.md) - OpenClaw 代码的安全和漏洞扫描器
- [towns-protocol](https://github.com/openclaw/skills/tree/main/skills/andreyz/towns-protocol/SKILL.md) - 构建 Towns Protocol 机器人时使用 - 涵盖 SDK
- [udau](https://github.com/openclaw/skills/tree/main/skills/nicoacosta/udau/SKILL.md) - 描述：AI 代理的联合协议。

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
