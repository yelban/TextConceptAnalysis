# Article Generator Skill 實現計畫

> **狀態**: 已完成 (2026-01-07)
> **位置**: `~/.claude/skills/article-generator/`

## 概述
建立一個全域 Claude Code skill，將 URL、PDF、純文字轉換為精緻的雜誌風格文章，並自動生成 AI 配圖。

## 目錄結構

```
~/.claude/skills/article-generator/
├── SKILL.md                      # Skill 定義 (Claude Code 入口)
├── scripts/
│   ├── pyproject.toml            # uv 專案配置
│   ├── .env.example              # 環境變數範本
│   ├── main.py                   # 主流程控制
│   ├── extract_content.py        # 內容提取 (URL/PDF/文字)
│   ├── generate_illustrations.py # Nano Banana Pro 圖像生成
│   ├── analyze_for_images.py     # 分析文章段落，生成配圖提示詞
│   └── utils/
│       ├── __init__.py
│       ├── pdf_handler.py        # PDF 解析與圖表提取
│       └── web_handler.py        # 網頁抓取與截圖
├── prompts/
│   ├── magazine_style.md         # 雜誌風格文章提示詞
│   ├── reflection_polish.md      # 反思潤色提示詞
│   └── image_concept_extract.md  # 從段落提取配圖概念提示詞
└── styles/                       # 配圖風格模板
    ├── vintage.md                # 復古插畫風格 (預設)
    ├── minimalist.md             # 極簡現代風格
    ├── cartoon.md                # 卡通信息圖風格
    ├── watercolor.md             # 水彩藝術風格
    └── technical.md              # 技術圖解風格
```

## 工作流程

```
輸入 (URL/PDF/文字)
    ↓
[extract_content.py] 內容提取
    ↓
[Claude] 第一遍：生成文章草稿 (magazine_style.md)
    ↓
[Claude] 第二遍：反思潤色 (reflection_polish.md)
    ↓
┌─────────────────────────────────────────────┐
│ 配圖策略判斷                                  │
├─────────────────────────────────────────────┤
│ 有圖片來源 (PDF/URL):                        │
│   → [pdf_handler.py] 提取 PDF 圖表           │
│   → [web_handler.py] 網頁截圖                │
│   → 補充 AI 生成配圖                          │
├─────────────────────────────────────────────┤
│ 純文字 / 無圖片:                             │
│   → [Claude] 分析文章段落，提取核心觀點        │
│   → 為每個觀點生成配圖提示詞                   │
│   → [generate_illustrations.py] 全部 AI 生成  │
└─────────────────────────────────────────────┘
    ↓
輸出: output/article-{timestamp}.md + output/images/
```

## 使用方式

```bash
# 從 URL
/article-generator https://arxiv.org/abs/2401.12345

# 從 PDF
/article-generator ~/papers/paper.pdf

# 從純文字
/article-generator "text:文章內容..."

# 從剪貼簿 (macOS: pbpaste, Linux: xclip)
/article-generator --clipboard

# 指定輸出目錄
/article-generator https://example.com --output ./my-output

# 選擇配圖風格
/article-generator https://example.com --style cartoon
/article-generator --clipboard --style minimalist

# 列出可用風格
/article-generator --list-styles
```

## 配圖風格選項

| 風格 | 參數 | 說明 |
|------|------|------|
| 復古插畫 | `vintage` | **預設**。水彩手繪、大地色系、1950s-70s 雜誌風格 |
| 極簡現代 | `minimalist` | 簡潔線條、大量留白、單色或雙色調 |
| 卡通信息圖 | `cartoon` | 可愛卡通元素、明亮色彩、適合科普內容 |
| 水彩藝術 | `watercolor` | 柔和水彩渲染、夢幻氛圍、藝術感強 |
| 技術圖解 | `technical` | 清晰的圖表風格、流程圖、適合技術文章 |

## 關鍵文件清單

| 文件 | 用途 |
|------|------|
| `SKILL.md` | Skill 定義與入口 |
| `scripts/main.py` | 主流程控制 |
| `scripts/extract_content.py` | 內容提取路由 |
| `scripts/generate_illustrations.py` | Gemini 圖像生成 |
| `scripts/analyze_for_images.py` | 分析段落、生成配圖提示詞 |
| `scripts/utils/pdf_handler.py` | PDF 處理 |
| `scripts/utils/web_handler.py` | 網頁處理 |
| `prompts/magazine_style.md` | 文章生成提示詞 |
| `prompts/reflection_polish.md` | 反思潤色提示詞 |
| `prompts/image_concept_extract.md` | 段落配圖概念提取提示詞 |
| `styles/vintage.md` | 復古插畫風格 (預設) |
| `styles/minimalist.md` | 極簡現代風格 |
| `styles/cartoon.md` | 卡通信息圖風格 |
| `styles/watercolor.md` | 水彩藝術風格 |
| `styles/technical.md` | 技術圖解風格 |

## 技術規格

- **Python**: 使用 uv 管理依賴
- **圖像生成**: Gemini API `gemini-3-pro-image-preview` (Nano Banana Pro)
- **PDF 處理**: PyMuPDF (fitz)
- **網頁截圖**: Playwright
- **環境變數**: GEMINI_API_KEY 存放在 .env
