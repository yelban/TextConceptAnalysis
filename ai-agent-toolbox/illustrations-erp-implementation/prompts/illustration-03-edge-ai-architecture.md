# Edge AI Hybrid Architecture - Technical Framework

Layout: Three-tier architecture diagram

TOP TIER - User Touchpoints:
- Header: "使用者接觸點"
- Icons in row: LINE Bot | 語音助手 | Web Chat | 手機 App | 傳統 ERP
- All converge to single arrow pointing down

MIDDLE TIER - Cloud/Edge Split:

LEFT BOX - Cloud Agent Gateway:
- Header: "Agent Gateway (雲端)"
- Location: "總部機房"
- Items:
  - "複雜決策"
  - "跨廠協調"
  - "經營分析"
- Skills: production-advisor, executive-dashboard

RIGHT BOXES - Edge AI (two parallel):
- Box 1: "Edge AI (台北廠)"
- Box 2: "Edge AI (嘉義廠)"
- Each contains:
  - "本地推理伺服器"
  - "OCR 辨識"
  - "即時品檢"
  - "設備異常偵測"
  - "語音指令處理"

CENTER ARROWS:
- Bidirectional arrows between Cloud and Edge
- Labels: "複雜任務上雲" / "即時任務本地"

BOTTOM TIER - Integration:
- Box: "ERP Integration Layer"
- Sub-box: "鼎新 Workflow ERP"
- Connection lines from both Edge AI boxes

ANNOTATIONS:
- Latency markers: "< 100ms 本地" vs "1-2s 雲端"
- Data flow arrows with labels

VISUAL ELEMENTS:
- Blueprint-style boxes with headers
- Layered architecture (top to bottom)
- 90-degree connection lines
- Grid background
- Dimension markers

COLORS:
- Background: Blueprint Off-White (#FAF8F5)
- Cloud tier: Engineering Blue (#2563EB)
- Edge tier: Cyan (#06B6D4)
- ERP tier: Navy Blue (#1E3A5F)
- Arrows: Deep Slate (#334155)
- Highlights: Amber (#F59E0B)

STYLE: Blueprint technical architecture diagram. Precise layered layout, grid alignment. Engineering drawing quality. System architecture documentation feel. Clear hierarchy and data flow.

ASPECT: 16:9
