#!/usr/bin/env python3
"""Generate README_zh.md from README.md.

Translates framework text (headings, paragraphs, table headers, categories)
and skill descriptions to Chinese. Skill names and links stay in English.

Uses Google Translate free API with local caching to avoid re-translating
unchanged descriptions on subsequent runs.

Usage:
    python3 scripts/generate-zh-readme.py                    # generate README_zh.md
    python3 scripts/generate-zh-readme.py --patch-readme      # add language switcher to README.md
    python3 scripts/generate-zh-readme.py --no-translate-desc  # skip description translation
"""

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
ZH_README_PATH = REPO_ROOT / "README_zh.md"
CACHE_PATH = REPO_ROOT / "scripts" / ".zh-desc-cache.json"

LANG_SWITCHER = "[English](README.md) | [中文](README_zh.md)\n"

# ── Google Translate (free API, no dependencies) ──────────────────────────────

TRANSLATE_URL = "https://translate.googleapis.com/translate_a/single"
MAX_CHARS_PER_BATCH = 4000  # stay under Google's ~5000 char limit
BATCH_DELAY = 1.5  # seconds between batches to avoid rate-limiting


def _google_translate(text: str, src: str = "en", tgt: str = "zh-CN") -> str:
    """Translate text via Google Translate free API."""
    params = urllib.parse.urlencode(
        {"client": "gtx", "sl": src, "tl": tgt, "dt": "t", "q": text}
    )
    url = f"{TRANSLATE_URL}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return "".join(seg[0] for seg in data[0])


def _load_cache() -> dict[str, str]:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


def _save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def translate_descriptions(descriptions: list[str]) -> dict[str, str]:
    """Batch-translate skill descriptions with caching.

    Returns a dict mapping English description → Chinese translation.
    """
    cache = _load_cache()
    new_descs = [d for d in descriptions if d not in cache]

    if not new_descs:
        return cache

    # Group into batches by character count
    batches: list[list[str]] = []
    batch: list[str] = []
    batch_len = 0
    for desc in new_descs:
        added_len = len(desc) + 1  # +1 for newline separator
        if batch_len + added_len > MAX_CHARS_PER_BATCH and batch:
            batches.append(batch)
            batch = []
            batch_len = 0
        batch.append(desc)
        batch_len += added_len
    if batch:
        batches.append(batch)

    total = len(new_descs)
    print(f"Translating {total} skill descriptions in {len(batches)} batches...")

    translated_count = 0
    for i, b in enumerate(batches, 1):
        combined = "\n".join(b)
        try:
            result = _google_translate(combined)
            parts = result.split("\n")
            if len(parts) == len(b):
                for en, zh in zip(b, parts):
                    cache[en] = zh.strip()
                translated_count += len(b)
            else:
                # Newline count mismatch — fall back to one-by-one
                print(f"  Batch {i}/{len(batches)}: line count mismatch, retrying individually...")
                for desc in b:
                    try:
                        cache[desc] = _google_translate(desc).strip()
                        translated_count += 1
                        time.sleep(0.3)
                    except Exception:
                        cache[desc] = desc  # keep English on failure
        except Exception as e:
            print(f"  Batch {i}/{len(batches)} failed: {e}")
            for desc in b:
                cache[desc] = desc  # keep English on failure

        print(f"  [{translated_count}/{total}]", end="\r")

        if i < len(batches):
            time.sleep(BATCH_DELAY)

    print(f"  [{translated_count}/{total}] done.            ")

    _save_cache(cache)
    return cache


# ── Skill line regex ──────────────────────────────────────────────────────────

SKILL_RE = re.compile(r"^(- \[.+?\]\(.+?\)) - (.+)$")

# ── Section heading translations ──────────────────────────────────────────────

HEADING_MAP = {
    "# Awesome OpenClaw Skills": "# Awesome OpenClaw 技能合集",
    "## Installation": "## 安装",
    "## Why This List Exists?": "## 为什么有这个列表？",
    "## Table of Contents": "## 目录",
    "## 🤝 Contributing": "## 🤝 贡献",
    "## License": "## 许可证",
    "### ClawHub CLI": "### ClawHub CLI",
    "### Manual Installation": "### 手动安装",
    "### Alternative": "### 其他方式",
}

# ── Category name translations ────────────────────────────────────────────────

CATEGORY_MAP = {
    "Coding Agents & IDEs": "编码代理与 IDE",
    "Git & GitHub": "Git 与 GitHub",
    "Moltbook": "Moltbook",
    "Web & Frontend Development": "Web 与前端开发",
    "DevOps & Cloud": "DevOps 与云服务",
    "Browser & Automation": "浏览器与自动化",
    "Image & Video Generation": "图像与视频生成",
    "Apple Apps & Services": "Apple 应用与服务",
    "Search & Research": "搜索与研究",
    "Clawdbot Tools": "Clawdbot 工具",
    "CLI Utilities": "CLI 工具",
    "Marketing & Sales": "市场营销与销售",
    "Productivity & Tasks": "生产力与任务管理",
    "AI & LLMs": "AI 与大语言模型",
    "Data & Analytics": "数据与分析",
    "Finance": "金融",
    "Media & Streaming": "媒体与流媒体",
    "Notes & PKM": "笔记与个人知识管理",
    "iOS & macOS Development": "iOS 与 macOS 开发",
    "Transportation": "交通出行",
    "Personal Development": "个人发展",
    "Health & Fitness": "健康与健身",
    "Communication": "通讯",
    "Speech & Transcription": "语音与转录",
    "Smart Home & IoT": "智能家居与物联网",
    "Shopping & E-commerce": "购物与电子商务",
    "Calendar & Scheduling": "日历与日程管理",
    "PDF & Documents": "PDF 与文档",
    "Self-Hosted & Automation": "自托管与自动化",
    "Security & Passwords": "安全与密码",
    "Gaming": "游戏",
    "Agent-to-Agent Protocols": "代理间协议",
}

# ── Paragraph / block translations ────────────────────────────────────────────
# Each tuple: (compiled regex matching the full line, replacement template)

PARAGRAPH_PATTERNS = [
    # "Discover N community-built OpenClaw skills …"
    (
        re.compile(
            r"(\s*<strong>)Discover (\d[\d,]*) community-built OpenClaw skills, organized by category\."
        ),
        r"\g<1>发现 \2 个社区构建的 OpenClaw 技能，按分类整理。",
    ),
    # Main intro paragraph
    (
        re.compile(
            r"^OpenClaw \(previously known as Moltbot, originally Clawdbot\.\.\. identity crisis included, no extra charge\) is a locally-running AI assistant that operates directly on your machine\. Skills extend its capabilities, allowing it to interact with external services, automate workflows, and perform specialized tasks\. This collection helps you discover and install the right skills for your needs\.$"
        ),
        "OpenClaw（曾用名 Moltbot，最初叫 Clawdbot……改名危机不另收费）是一个在本地运行的 AI 助手，直接在你的机器上工作。技能扩展了它的能力，让它能与外部服务交互、自动化工作流并执行专业任务。本合集帮助你发现并安装合适的技能。",
    ),
    # "Skills in this list are sourced from ClawHub …"
    (
        re.compile(
            r"^Skills in this list are sourced from \[ClawHub\]\(https://www\.clawhub\.ai/\) \(OpenClaw's public skills registry\) and categorized for easier discovery\.$"
        ),
        "本列表中的技能来源于 [ClawHub](https://www.clawhub.ai/)（OpenClaw 的公共技能注册中心），并按分类整理以方便发现。",
    ),
    # "These skills follow the Agent Skill convention …"
    (
        re.compile(
            r"^These skills follow the Agent Skill convention develop by Anthropic, an open standard for AI coding assistants\.$"
        ),
        "这些技能遵循 Anthropic 开发的 Agent Skill 规范，这是一个面向 AI 编程助手的开放标准。",
    ),
    # Want to add a skill blockquote
    (
        re.compile(
            r'^> \*\*Want to add a skill\?\*\* This list only includes skills that are \*\*already published\*\* in the "github\.com/openclaw/skills"\. We do not accept links to personal repos, gists, or any other external source\. If your skill isn\'t in the OpenClaw skills repo yet, publish it there first\. See \[CONTRIBUTING\.md\]\(CONTRIBUTING\.md\) for details\.$'
        ),
        '> **想添加技能？** 本列表仅收录**已发布**在 "github.com/openclaw/skills" 中的技能。我们不接受个人仓库、gist 或其他外部来源的链接。如果你的技能尚未发布到 OpenClaw 技能仓库，请先在那里发布。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。',
    ),
    # ClawHub CLI note
    (
        re.compile(
            r"^> \*\*Note:\*\* As you probably know, they keep renaming things\. This reflects the current official docs\. We'll update this when they rename it again\.$"
        ),
        "> **注意：** 你可能知道，他们一直在改名。这里反映的是当前的官方文档，下次改名时我们会再更新。",
    ),
    # "Copy the skill folder to one of these locations:"
    (
        re.compile(r"^Copy the skill folder to one of these locations:$"),
        "将技能文件夹复制到以下位置之一：",
    ),
    # Manual install table headers
    (
        re.compile(r"^\| Location \| Path \|$"),
        "| 位置 | 路径 |",
    ),
    # "Priority: Workspace > Local > Bundled"
    (
        re.compile(r"^Priority: Workspace > Local > Bundled$"),
        "优先级：工作区 > 本地 > 内置",
    ),
    # Alternative paragraph
    (
        re.compile(
            r"^You can also paste the skill's GitHub repository link directly into your assistant's chat and ask it to use it\. The assistant will handle the setup automatically in the background\.$"
        ),
        "你也可以将技能的 GitHub 仓库链接直接粘贴到助手的聊天中，让它使用该技能。助手会在后台自动完成设置。",
    ),
    # "Why This List Exists" intro with dynamic numbers
    (
        re.compile(
            r"^OpenClaw's public registry \(ClawHub\) hosts \*\*(\d[\d,]*) community-built skills\*\* as of .+\. This awesome list has \*\*(\d[\d,]*) skills\*\*\. Here's what we filtered out:$"
        ),
        r"OpenClaw 的公共注册中心（ClawHub）拥有 **\1 个社区构建的技能**。本列表收录了 **\2 个技能**。以下是我们筛除的内容：",
    ),
    # Filter table header
    (
        re.compile(r"^\| Filter \| Excluded \|$"),
        "| 筛选条件 | 排除数量 |",
    ),
    # Filter table rows
    (
        re.compile(
            r"^\| Possibly spam — bulk accounts, bot accounts, test/junk \| ([\d,]+) \|$"
        ),
        r"| 疑似垃圾信息 — 批量账号、机器人账号、测试/垃圾内容 | \1 |",
    ),
    (
        re.compile(
            r"^\| Crypto / Blockchain / Finance / Trade \| ([\d,]+) \|$"
        ),
        r"| 加密货币 / 区块链 / 金融 / 交易 | \1 |",
    ),
    (
        re.compile(r"^\| Duplicate / Similar name \| ([\d,]+) \|$"),
        r"| 重复 / 相似名称 | \1 |",
    ),
    (
        re.compile(
            r"^\| Malicious — identified by security audits published by researchers \(excluding VirusTotal\) \| ([\d,]+) \|$"
        ),
        r"| 恶意内容 — 由研究人员发布的安全审计识别（不含 VirusTotal） | \1 |",
    ),
    (
        re.compile(
            r"^\| Non-English — descriptions not in English \| ([\d,]+) \|$"
        ),
        r"| 非英语 — 描述不是英文 | \1 |",
    ),
    (
        re.compile(
            r"^\| \*\*Total not taken from OpenClaw's official skill registry\*\* \| \*\*([\d,]+)\*\* \|$"
        ),
        r"| **未从 OpenClaw 官方技能注册中心收录的总数** | **\1** |",
    ),
    # Disclaimer blockquote
    (
        re.compile(
            r"^> \*\*Disclaimer:\*\* Inclusion in this list does \*\*not\*\* guarantee a skill is safe or trustworthy\. OpenClaw now has a VirusTotal partnership that provides security scanning for skills\. Before installing a skill, visit its page on ClawHub and check the VirusTotal report to see if it's flagged as risky\. We also recommend reviewing a skill's source code before installing and using tools like Claude Code or Codex to inspect it for potentially harmful behavior\.$"
        ),
        "> **免责声明：** 收录在本列表中**不代表**该技能是安全或可信的。OpenClaw 现已与 VirusTotal 合作，为技能提供安全扫描。安装技能前，请访问其 ClawHub 页面并查看 VirusTotal 报告，确认是否被标记为有风险。我们还建议在安装前审查技能的源代码，并使用 Claude Code 或 Codex 等工具检查是否存在潜在有害行为。",
    ),
    # "If you think a skill was incorrectly excluded …"
    (
        re.compile(
            r"^If you think a skill was incorrectly excluded or miscategorized, feel free to open an issue or PR\. We may have made mistakes\.$"
        ),
        "如果你认为某个技能被错误排除或分类有误，请随时提交 issue 或 PR。我们可能犯了错误。",
    ),
    # Contributing section
    (
        re.compile(
            r"^We welcome contributions! See \[CONTRIBUTING\.md\]\(CONTRIBUTING\.md\) for detailed guidelines\.$"
        ),
        "欢迎贡献！详细指南请参见 [CONTRIBUTING.md](CONTRIBUTING.md)。",
    ),
    (
        re.compile(r"^- Submit new skills via PR$"),
        "- 通过 PR 提交新技能",
    ),
    (
        re.compile(r"^- Improve existing definitions$"),
        "- 改进现有定义",
    ),
    # Contributing note
    (
        re.compile(
            r"^> \*\*Note:\*\* Please don't submit skills you created 3 hours ago\. We're now focusing on community-adopted skills, especially those published by development teams and proven in real-world usage\. Quality over quantity\.$"
        ),
        "> **注意：** 请不要提交你 3 小时前刚创建的技能。我们现在专注于社区采用的技能，特别是由开发团队发布并在实际使用中经过验证的技能。质量优于数量。",
    ),
    # License section
    (
        re.compile(r"^MIT License - see \[LICENSE\]\(LICENSE\)$"),
        "MIT 许可证 - 见 [LICENSE](LICENSE)",
    ),
    (
        re.compile(
            r"^Skills in this list are sourced from the OpenClaw official skills repo and categorized for easier discovery\. Skills listed here are created and maintained by their respective authors, not by us\. We do not audit, endorse, or guarantee the security or correctness of listed projects\. They are not security-audited and should be reviewed before production use\.$"
        ),
        "本列表中的技能来源于 OpenClaw 官方技能仓库，按分类整理以方便发现。列出的技能由各自的作者创建和维护，并非我们所有。我们不审核、不背书、也不保证所列项目的安全性或正确性。它们未经安全审计，生产环境使用前请自行审查。",
    ),
    (
        re.compile(
            r"^If you find an issue with a listed skill or want your skill removed, please open an issue and we'll take care of it promptly\.$"
        ),
        "如果你发现列出的技能有问题，或者想要移除你的技能，请提交 issue，我们会及时处理。",
    ),
]


# ── Table of Contents line translation ────────────────────────────────────────

def translate_toc_cell(cell: str) -> str:
    """Translate a single TOC cell like '[Coding Agents & IDEs](#anchor) (133)'."""
    m = re.match(r"\[(.+?)\]\((#.+?)\)\s*\((\d+)\)", cell.strip())
    if not m:
        return cell
    name, anchor, count = m.group(1), m.group(2), m.group(3)
    zh_name = CATEGORY_MAP.get(name, name)
    return f"[{zh_name}]({anchor}) ({count})"


def translate_toc_line(line: str) -> str:
    """Translate a TOC table row."""
    if not line.startswith("|") or "---" in line:
        return line
    cells = line.split("|")
    translated = [translate_toc_cell(c) if c.strip() else c for c in cells]
    return "|".join(translated)


# ── Category <summary> translation ────────────────────────────────────────────

SUMMARY_RE = re.compile(
    r'^(<summary><h3 style="display:inline">)(.+?)(</h3></summary>)$'
)


def translate_summary(line: str) -> str:
    m = SUMMARY_RE.match(line)
    if not m:
        return line
    prefix, name, suffix = m.group(1), m.group(2), m.group(3)
    zh_name = CATEGORY_MAP.get(name, name)
    anchor = name.lower().replace(" & ", "--").replace(" ", "-")
    return f'<summary><h3 style="display:inline" id="{anchor}">{zh_name}</h3></summary>'


# ── Main translation logic ────────────────────────────────────────────────────

def translate_readme(lines: list[str], desc_translations: dict[str, str]) -> list[str]:
    out: list[str] = []
    in_code_block = False
    in_toc = False

    for line in lines:
        stripped = line.rstrip("\n")

        # Track code blocks — never translate inside them
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            out.append(line)
            continue
        if in_code_block:
            out.append(line)
            continue

        # Skip the language switcher line if it already exists (from --patch-readme)
        if stripped == LANG_SWITCHER.strip():
            continue

        # Skill entry lines — translate description part
        if stripped.startswith("- ["):
            m = SKILL_RE.match(stripped)
            if m and m.group(2) in desc_translations:
                out.append(f"{m.group(1)} - {desc_translations[m.group(2)]}\n")
            else:
                out.append(line)
            continue

        # Headings
        matched_heading = False
        for en, zh in HEADING_MAP.items():
            if stripped == en:
                out.append(zh + "\n")
                matched_heading = True
                break
        if matched_heading:
            if stripped == "## Table of Contents":
                in_toc = True
            elif stripped.startswith("## ") and stripped != "## Table of Contents":
                in_toc = False
            continue

        # TOC table rows
        if in_toc and stripped.startswith("|"):
            out.append(translate_toc_line(stripped) + "\n")
            continue

        # Exit TOC when we hit a non-table, non-empty line after TOC started
        if in_toc and stripped and not stripped.startswith("|") and not stripped.startswith("<"):
            in_toc = False

        # Category summary headers
        if SUMMARY_RE.match(stripped):
            out.append(translate_summary(stripped) + "\n")
            continue

        # Paragraph / block patterns
        matched_para = False
        for pattern, replacement in PARAGRAPH_PATTERNS:
            m = pattern.match(stripped)
            if m:
                out.append(m.expand(replacement) + "\n")
                matched_para = True
                break
        if matched_para:
            continue

        # Default: keep line as-is (graceful degradation)
        out.append(line)

    return out


# ── --patch-readme: add language switcher to README.md ────────────────────────

def patch_readme():
    content = README_PATH.read_text(encoding="utf-8")
    if LANG_SWITCHER.strip() in content:
        print("README.md already has language switcher — skipping.")
        return
    content = LANG_SWITCHER + "\n" + content
    README_PATH.write_text(content, encoding="utf-8")
    print("Added language switcher to README.md.")


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    if "--patch-readme" in sys.argv:
        patch_readme()
        return

    skip_desc = "--no-translate-desc" in sys.argv

    lines = README_PATH.read_text(encoding="utf-8").splitlines(keepends=True)

    # Collect all skill descriptions
    desc_translations: dict[str, str] = {}
    if not skip_desc:
        all_descs: list[str] = []
        seen: set[str] = set()
        for line in lines:
            m = SKILL_RE.match(line.rstrip("\n"))
            if m:
                desc = m.group(2)
                if desc not in seen:
                    all_descs.append(desc)
                    seen.add(desc)
        desc_translations = translate_descriptions(all_descs)

    translated = translate_readme(lines, desc_translations)

    header = LANG_SWITCHER + "\n"
    ZH_README_PATH.write_text(header + "".join(translated), encoding="utf-8")
    print(f"Generated {ZH_README_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
