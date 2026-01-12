#!/usr/bin/env python3
"""
專業雜誌風格 PDF 生成器
整合封面與配圖，以美術編輯角度優化排版
"""

import fitz  # PyMuPDF
from pathlib import Path
import re

# 配置
OUTPUT_DIR = Path("/Users/orz99/zoo/TextConceptAnalysis/ShareGuru/output")
IMAGES_DIR = OUTPUT_DIR / "images"

# 圖片檔案
COVER_IMAGE = list(IMAGES_DIR.glob("cover_bloomberg_*.jpg"))[0]
ILLUSTRATION_1 = list(IMAGES_DIR.glob("illustration_*_015049.jpg"))[0]  # 資料主權堡壘
ILLUSTRATION_2 = list(IMAGES_DIR.glob("illustration_*_015137.jpg"))[0]  # GraphRAG
ILLUSTRATION_3 = list(IMAGES_DIR.glob("illustration_*_015229.jpg"))[0]  # 四大應用

# 色彩配置（專業雜誌風格）
COLORS = {
    "primary": (0.12, 0.16, 0.22),      # 深藍灰 - 標題
    "secondary": (0.25, 0.32, 0.42),    # 中灰藍 - 副標題
    "accent": (0.85, 0.55, 0.15),       # 暖金色 - 強調
    "text": (0.2, 0.2, 0.2),            # 深灰 - 內文
    "light": (0.95, 0.95, 0.97),        # 淺灰 - 背景
    "white": (1, 1, 1),
    "highlight": (0.15, 0.45, 0.65),    # 科技藍 - 連結/重點
}

# 頁面尺寸 (A4)
PAGE_WIDTH = 595
PAGE_HEIGHT = 842
MARGIN = 50
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN


def create_cover_page(doc):
    """建立封面頁"""
    page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)

    # 全版封面圖
    img_rect = fitz.Rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT * 0.6)
    page.insert_image(img_rect, filename=str(COVER_IMAGE))

    # 半透明漸層遮罩效果（從上到下漸深）
    gradient_rect = fitz.Rect(0, PAGE_HEIGHT * 0.45, PAGE_WIDTH, PAGE_HEIGHT)
    page.draw_rect(gradient_rect, color=None, fill=COLORS["primary"], fill_opacity=0.92)

    # 標題區域
    title_y = PAGE_HEIGHT * 0.52

    # 主標題
    page.insert_text(
        (MARGIN, title_y),
        "思銳科技",
        fontsize=42,
        fontname="china-s",
        color=COLORS["white"]
    )
    page.insert_text(
        (MARGIN, title_y + 55),
        "本地推理環境",
        fontsize=42,
        fontname="china-s",
        color=COLORS["white"]
    )

    # 副標題
    page.insert_text(
        (MARGIN, title_y + 120),
        "策略評估與應用路線圖",
        fontsize=24,
        fontname="china-s",
        color=COLORS["accent"]
    )

    # 分隔線
    line_y = title_y + 150
    page.draw_line(
        fitz.Point(MARGIN, line_y),
        fitz.Point(MARGIN + 120, line_y),
        color=COLORS["accent"],
        width=3
    )

    # 核心價值標籤
    tags = ["資料主權", "場域專用", "極致安全"]
    tag_x = MARGIN
    tag_y = title_y + 180
    for tag in tags:
        # 標籤背景
        tag_width = len(tag) * 16 + 20
        tag_rect = fitz.Rect(tag_x, tag_y - 5, tag_x + tag_width, tag_y + 22)
        page.draw_rect(tag_rect, color=None, fill=COLORS["accent"], fill_opacity=0.2)
        page.insert_text(
            (tag_x + 10, tag_y + 14),
            tag,
            fontsize=12,
            fontname="china-s",
            color=COLORS["accent"]
        )
        tag_x += tag_width + 15

    # 報告對象
    page.insert_text(
        (MARGIN, PAGE_HEIGHT - 80),
        "報告對象：決策管理層 / 技術主管",
        fontsize=11,
        fontname="china-s",
        color=(0.7, 0.7, 0.7)
    )

    # 頁碼區域留白
    return page


def create_section_page(doc, section_num, title, content_lines, illustration=None, illustration_caption=None):
    """建立章節頁面"""
    page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)

    current_y = MARGIN

    # 章節編號（大型裝飾數字）
    page.insert_text(
        (MARGIN, current_y + 60),
        f"{section_num:02d}",
        fontsize=72,
        fontname="helv",
        color=(*COLORS["accent"], 0.15)  # 半透明
    )

    # 章節標題
    page.insert_text(
        (MARGIN + 80, current_y + 45),
        title,
        fontsize=28,
        fontname="china-s",
        color=COLORS["primary"]
    )

    # 標題下方裝飾線
    current_y += 70
    page.draw_line(
        fitz.Point(MARGIN, current_y),
        fitz.Point(MARGIN + 60, current_y),
        color=COLORS["accent"],
        width=2
    )

    current_y += 30

    # 如果有配圖，放在章節開頭
    if illustration:
        img_height = 220
        img_rect = fitz.Rect(
            MARGIN,
            current_y,
            PAGE_WIDTH - MARGIN,
            current_y + img_height
        )
        page.insert_image(img_rect, filename=str(illustration))

        # 圖片邊框
        page.draw_rect(img_rect, color=COLORS["secondary"], width=0.5)

        current_y += img_height + 10

        # 圖說
        if illustration_caption:
            page.insert_text(
                (MARGIN, current_y + 12),
                illustration_caption,
                fontsize=9,
                fontname="china-s",
                color=COLORS["secondary"]
            )
            current_y += 25

    current_y += 15

    # 內文
    line_height = 18
    for line in content_lines:
        if current_y > PAGE_HEIGHT - MARGIN - 30:
            # 需要換頁
            page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
            current_y = MARGIN + 30

        # 處理不同類型的內容
        if line.startswith("##"):
            # 子標題
            text = line.replace("##", "").strip()
            current_y += 15
            page.insert_text(
                (MARGIN, current_y + 16),
                text,
                fontsize=16,
                fontname="china-s",
                color=COLORS["highlight"]
            )
            current_y += 30
        elif line.startswith("•") or line.startswith("-"):
            # 項目符號
            page.insert_text(
                (MARGIN + 15, current_y + 12),
                line,
                fontsize=11,
                fontname="china-s",
                color=COLORS["text"]
            )
            current_y += line_height
        elif line.startswith("**") and line.endswith("**"):
            # 粗體強調
            text = line.replace("**", "")
            page.insert_text(
                (MARGIN, current_y + 12),
                text,
                fontsize=12,
                fontname="china-s",
                color=COLORS["primary"]
            )
            current_y += line_height + 5
        elif line.strip() == "":
            current_y += 10
        else:
            # 一般段落
            page.insert_text(
                (MARGIN, current_y + 12),
                line[:70],  # 限制每行長度
                fontsize=11,
                fontname="china-s",
                color=COLORS["text"]
            )
            current_y += line_height
            # 如果有更多文字，換行繼續
            remaining = line[70:]
            while remaining:
                if current_y > PAGE_HEIGHT - MARGIN - 30:
                    page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)
                    current_y = MARGIN + 30
                page.insert_text(
                    (MARGIN, current_y + 12),
                    remaining[:70],
                    fontsize=11,
                    fontname="china-s",
                    color=COLORS["text"]
                )
                current_y += line_height
                remaining = remaining[70:]

    return page


def create_toc_page(doc):
    """建立目錄頁"""
    page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)

    # 目錄標題
    page.insert_text(
        (MARGIN, MARGIN + 50),
        "目錄",
        fontsize=32,
        fontname="china-s",
        color=COLORS["primary"]
    )

    # 裝飾線
    page.draw_line(
        fitz.Point(MARGIN, MARGIN + 70),
        fitz.Point(MARGIN + 40, MARGIN + 70),
        color=COLORS["accent"],
        width=2
    )

    # 目錄項目
    toc_items = [
        ("01", "執行摘要", "核心發現與策略定位"),
        ("02", "現況技術評估", "測試環境、效能表現、SWOT分析"),
        ("03", "雲端vs本地模型差距分析", "能力比較與本質原因"),
        ("04", "本地推理真正價值定位", "資料主權、批次處理、垂直專用"),
        ("05", "四大高價值應用場景", "GraphRAG、ASR、智慧解析、批次標註"),
        ("06", "技術架構建議", "分層架構、Embedding、硬體配置"),
        ("07", "展示腳本設計", "向決策者展示的劇本設計"),
        ("08", "結論與建議", "核心價值主張與行動項目"),
    ]

    current_y = MARGIN + 120
    for num, title, desc in toc_items:
        # 章節編號
        page.insert_text(
            (MARGIN, current_y + 15),
            num,
            fontsize=24,
            fontname="helv",
            color=COLORS["accent"]
        )
        # 章節標題
        page.insert_text(
            (MARGIN + 50, current_y + 15),
            title,
            fontsize=14,
            fontname="china-s",
            color=COLORS["primary"]
        )
        # 章節描述
        page.insert_text(
            (MARGIN + 50, current_y + 35),
            desc,
            fontsize=10,
            fontname="china-s",
            color=COLORS["secondary"]
        )
        # 分隔線
        page.draw_line(
            fitz.Point(MARGIN, current_y + 55),
            fitz.Point(PAGE_WIDTH - MARGIN, current_y + 55),
            color=(*COLORS["light"][:3],),
            width=0.5
        )
        current_y += 70

    return page


def create_highlight_box(page, x, y, width, height, title, content_lines):
    """建立重點提示框"""
    # 背景
    rect = fitz.Rect(x, y, x + width, y + height)
    page.draw_rect(rect, color=None, fill=COLORS["highlight"], fill_opacity=0.08)

    # 左側強調線
    page.draw_line(
        fitz.Point(x, y),
        fitz.Point(x, y + height),
        color=COLORS["highlight"],
        width=3
    )

    # 標題
    page.insert_text(
        (x + 15, y + 20),
        title,
        fontsize=12,
        fontname="china-s",
        color=COLORS["highlight"]
    )

    # 內容
    current_y = y + 40
    for line in content_lines:
        page.insert_text(
            (x + 15, current_y + 12),
            line,
            fontsize=10,
            fontname="china-s",
            color=COLORS["text"]
        )
        current_y += 16


def main():
    """主程式"""
    print("開始建立專業排版 PDF...")

    # 建立新文件
    doc = fitz.open()

    # 1. 封面頁
    print("  → 建立封面頁...")
    create_cover_page(doc)

    # 2. 目錄頁
    print("  → 建立目錄頁...")
    create_toc_page(doc)

    # 3. 執行摘要（含資料主權堡壘配圖）
    print("  → 建立第一章：執行摘要...")
    section1_content = [
        "本報告基於 gpt-oss-120b 模型於思銳本地推理環境的實測結果，",
        "從企業 AI 導入顧問視角提出策略建議。",
        "",
        "## 核心發現",
        "",
        "測試顯示該模型具備優異的「文檔理解與結構化提取」能力，",
        "但在「多輪對話記憶」與「深度邏輯推理」上與雲端頂級模型存在差距。",
        "",
        "## 策略定位",
        "",
        "不追求「全能聊天機器人」，而是定位為：",
        "",
        "**「鈣鈦礦研發的專屬機密資料處理器」**",
        "",
        "透過 GraphRAG（圖譜檢索）、本地 Embedding、本地 ASR（語音轉錄）等技術，",
        "規避模型推理與記憶短板，最大化機密資料處理價值。",
    ]
    create_section_page(doc, 1, "執行摘要", section1_content,
                       ILLUSTRATION_1, "▲ 資料主權堡壘：本地推理環境的核心價值在於機密資料永不離開內網")

    # 4. 現況技術評估
    print("  → 建立第二章：現況技術評估...")
    section2_content = [
        "## 測試環境",
        "",
        "• 模型：gpt-oss-120b (ChatGPT 開源版本)",
        "• 測試 GPU：RTX 5090 (測試) / RTX Pro 6000 (目標)",
        "• 支援格式：PDF、Excel (xls)、CSV",
        "",
        "## 效能表現",
        "",
        "• 首字生成延遲：5-8 秒（存在冷啟動延遲，需硬體升級）",
        "• 後續生成速度：流暢（一旦啟動輸出速度佳）",
        "• 資料提取能力：優異（能精準從 PDF 抓取特定數據並製表）",
        "• 深度推理能力：有限（不如 GPT-4o）",
        "• 多輪對話記憶：缺失（每次提問視為獨立請求）",
        "",
        "## SWOT 分析",
        "",
        "**優勢 (S)**：資料提取精準、生成流暢、全本地運行絕對安全",
        "**劣勢 (W)**：缺乏上下文記憶、推理偏弱、格式敏感",
        "**機會 (O)**：RTX 6000 Ada 升級、GraphRAG 補強推理",
        "**威脅 (T)**：使用者對記憶功能的期待落差",
    ]
    create_section_page(doc, 2, "現況技術評估", section2_content)

    # 5. 雲端vs本地差距分析
    print("  → 建立第三章：雲端vs本地差距分析...")
    section3_content = [
        "理解差距才能正確定位。以下比較 GPT-5.2 與本地 gpt-oss-120b 的能力差異：",
        "",
        "## 能力比較重點",
        "",
        "• 數學推理：GPT-5.2 滿分，本地估計 40-50%（顯著落後）",
        "• 科學問答：GPT-5.2 92%，本地估計 60-70%（明顯落後）",
        "• 程式碼生成：GPT-5.2 55.6%，本地估計 30-40%",
        "• 文檔提取與整理：雙方均優秀（接近持平）",
        "• 長文本摘要：GPT-5.2 優秀，本地良好（可接受）",
        "",
        "## 差距的本質原因",
        "",
        "**訓練資源差距**",
        "GPT-5.2 使用 NVIDIA H100/H200/GB200 叢集訓練，",
        "訓練算力估計為本地模型的 100-1000 倍。",
        "",
        "**推理時算力差距**",
        "GPT-5.2 Thinking/Pro 模式可使用「延長思考」機制，",
        "單次推理可消耗數分鐘雲端算力。本地 RTX Pro 6000 無法支援。",
        "",
        "## 結論",
        "",
        "在「文檔處理」和「結構化提取」等特定任務上，",
        "差距可控且可透過 RAG 補強。",
    ]
    create_section_page(doc, 3, "雲端vs本地差距分析", section3_content)

    # 6. 本地推理真正價值定位
    print("  → 建立第四章：本地推理價值定位...")
    section4_content = [
        "在雲端大模型推理能力明顯領先的情況下，本地推理環境的價值必須重新聚焦：",
        "",
        "## 4.1 資料主權與合規",
        "",
        "實驗配方、製程參數、良率數據等機密資訊絕不離開內網。",
        "符合 ISO 27001、半導體業客戶稽核要求。",
        "",
        "## 4.2 低延遲批次處理",
        "",
        "本地 GPU 處理大量文件無需排隊等待雲端 API，",
        "適合批次報告生成、資料預處理任務。",
        "",
        "## 4.3 垂直領域專用化",
        "",
        "透過 RAG/GraphRAG 注入領域知識，",
        "讓通用模型成為「鈣鈦礦專家」，而非追求通用推理能力。",
        "",
        "## 4.4 成本可控",
        "",
        "高頻使用場景下，本地部署的總持有成本 (TCO)",
        "優於按次計費的雲端 API。",
    ]
    create_section_page(doc, 4, "本地推理價值定位", section4_content)

    # 7. 四大應用場景（含四大場景配圖）
    print("  → 建立第五章：四大高價值應用場景...")
    section5_content = [
        "以下場景設計原則：利用「資料提取強」優勢，規避「推理弱、記憶差」劣勢。",
        "",
        "## 場景一：本地 GraphRAG 知識圖譜檢索",
        "",
        "**痛點**：傳統 RAG 只能關鍵字匹配，無法回答跨文件複雜問題",
        "",
        "**技術方案**：",
        "• 本地 Embedding：bge-m3 / text2vec-chinese",
        "• 向量資料庫：Milvus / Qdrant（本地部署）",
        "• 知識圖譜：Neo4j / NebulaGraph（本地）",
        "• 檢索策略：向量相似度 + 圖譜遍歷混合查詢",
        "",
        "## 場景二：機密會議本地 ASR 轉錄與摘要",
        "",
        "**痛點**：研發會議含機密，絕不能使用雲端轉錄服務",
        "",
        "**技術方案**：",
        "• 語音轉文字：Whisper Large-v3（本地）",
        "• 說話者辨識：pyannote-audio（本地）",
        "• 會議摘要：gpt-oss-120b 長文本摘要",
        "",
        "## 場景三：一鍵式實驗報告結構化",
        "",
        "建立預處理層，統一轉換各種格式為 Markdown/JSON，確保輸出一致性。",
        "",
        "## 場景四：批次資料標註與分類",
        "",
        "利用本地 LLM 進行批次分類任務，每份文件獨立處理，不需記憶上下文。",
    ]
    create_section_page(doc, 5, "四大高價值應用場景", section5_content,
                       ILLUSTRATION_3, "▲ 四大應用場景：語音轉錄、智慧解析、知識圖譜、批次標註")

    # 8. 加入 GraphRAG 配圖頁
    print("  → 建立 GraphRAG 專題頁...")
    graphrag_content = [
        "## GraphRAG：讓 AI「顯得變聰明」",
        "",
        "實際上是檢索能力變強，完全不出內網。",
        "",
        "工程師問「統整封裝失敗趨勢」，系統先透過知識圖譜找出關聯，",
        "再將整理好的素材餵給 LLM 潤飾摘要。",
        "",
        "## 技術組件",
        "",
        "• 本地 Embedding：bge-m3（568M 參數，MTEB 排名前列）",
        "• 向量資料庫：Milvus / Qdrant（本地部署）",
        "• 知識圖譜：Neo4j / NebulaGraph（建立實體關係）",
        "• 混合檢索：向量相似度 + 圖譜遍歷",
        "",
        "## 價值主張",
        "",
        "**「AI 就像一個剛看完這五份報告的資深助理，**",
        "**但他不會累，也不會把數據洩漏給競爭對手。」**",
    ]
    create_section_page(doc, 5, "GraphRAG 知識圖譜", graphrag_content,
                       ILLUSTRATION_2, "▲ 知識圖譜檢索：文件透過 AI 建立關聯，揭示隱藏的知識連結")

    # 9. 技術架構建議
    print("  → 建立第六章：技術架構建議...")
    section6_content = [
        "建議採用分層架構，將本地推理環境定位為「資料處理引擎」而非「對話介面」：",
        "",
        "## 整體架構",
        "",
        "• 資料輸入層：Pre-processor (Python) — 格式統一化、ETL",
        "• 知識儲存層：Vector DB + Graph DB — 向量索引、知識圖譜",
        "• 檢索層：Hybrid Retrieval Engine — 向量相似度 + 圖譜遍歷",
        "• 推理層：gpt-oss-120b (RTX Pro 6000) — 文本生成、摘要",
        "• 應用層：Task-oriented UI — 單次任務介面，非聊天式",
        "",
        "## 本地 Embedding 部署建議",
        "",
        "• bge-m3（568M）：多語言、長文本，MTEB 排名前列，推薦",
        "• bge-large-zh（326M）：中文專用，中文效果最佳",
        "• text2vec-base-chinese（102M）：輕量部署",
        "",
        "## 硬體配置建議",
        "",
        "• GPU：RTX 5090 → RTX Pro 6000 Ada（降低首字延遲至 <3 秒）",
        "• VRAM：48GB+（支援更長上下文）",
        "• 儲存：NVMe SSD RAID（加速向量檢索）",
    ]
    create_section_page(doc, 6, "技術架構建議", section6_content)

    # 10. 結論與建議
    print("  → 建立第八章：結論與建議...")
    section8_content = [
        "## 總結",
        "",
        "gpt-oss-120b 是優秀的「閱讀者」與「整理者」，但不是好的「思考者」。",
        "產品策略應鎖定 RAG（檢索）與 ETL（資料清洗）應用，而非 Chatbot。",
        "",
        "## 核心價值主張",
        "",
        "**「在通用推理上，雲端超大模型確實有優勢。**",
        "**但在垂直領域，我們透過 RAG 技術讓本地模型專注於解讀內部文件。**",
        "**在工廠裡，我們不需要 AI 會寫詩，**",
        "**我們需要它讀得懂實驗報表——這點 RTX Pro 6000 配合 120B 模型已經綽綽有餘。」**",
        "",
        "## 立即行動項目",
        "",
        "**P0（最高優先）**",
        "• 硬體遷移至 RTX Pro 6000 — 解決 5-8 秒延遲的體驗問題",
        "• 建立格式預處理 Pipeline — 確保輸出一致性",
        "",
        "**P1（高優先）**",
        "• 部署本地 Embedding 模型 — 為 GraphRAG 奠定基礎",
        "• 啟動 50 份 PDF 向量索引 POC — 驗證檢索準確度提升",
        "",
        "**P2（中優先）**",
        "• 本地 Whisper ASR 部署 — 會議機密轉錄需求",
        "",
        "這套方案將把「思銳本地推理環境」從「測試工具」",
        "轉變為「製造業不可或缺的資安生產力工具」。",
    ]
    create_section_page(doc, 8, "結論與建議", section8_content)

    # 儲存
    output_path = OUTPUT_DIR / "shareguru_magazine.pdf"
    doc.save(str(output_path))
    doc.close()

    print(f"\n✓ 專業排版 PDF 已儲存至：{output_path}")
    print(f"  檔案大小：{output_path.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
