# Session Handoff

**日期**: 2026-01-07 01:45
**分支**: master
**結束原因**: completed

## 會話摘要

### 目標
為「查理與巧克力工廠」英語舞台劇排練手冊 (index.html) 加入台詞語音播放功能，讓小學生演員可以點擊按鈕聽取每句台詞的舞台劇風格朗讀示範。

### 完成項目
- [x] 規劃實作方案（AI TTS vs Web Speech API vs 真人錄製）
- [x] 建立 `generate_audio.py` 腳本，使用 OpenAI TTS API 生成語音
- [x] 為 Archie (echo) 和 Mera (nova) 配置不同聲音
- [x] 修改 index.html 加入播放按鈕 CSS 樣式
- [x] 為 11 句台詞加入播放按鈕
- [x] 實作 JavaScript 播放邏輯（含播放動畫）
- [x] 調整語音效果：語速 0.9 倍、誇張舞台劇語調
- [x] 修正台詞錯誤："we are proudly present" → "we proudly present"
- [x] 使用 ffmpeg 放大音量 2 倍
- [x] 優化播放按鈕 UI（金色圓形 + 白色三角形）

### 修改的檔案
| 檔案 | 變更類型 | 說明 |
|------|----------|------|
| `generate_audio.py` | 新增 | OpenAI TTS 批次生成腳本 |
| `audio/*.mp3` | 新增 | 11 個語音檔案（已放大音量） |
| `audio_backup/*.mp3` | 新增 | 原始音檔備份 |
| `index.html` | 修改 | CSS 樣式 + 播放按鈕 + JavaScript |
| `pyproject.toml` | 新增 | Python 專案設定 (uv) |
| `.venv/` | 新增 | Python 虛擬環境 |

## 問題與阻礙

無重大問題。過程中微調了：
- OpenAI TTS 聲音選擇（onyx → echo，因小學生聲音不應太低沉）
- 播放按鈕位置（從台詞後移到角色名後）
- 語音文字加入大寫強調和停頓以增加戲劇效果

## 下一步建議

### 優先事項
1. 根據實際使用回饋調整語音效果
2. 考慮加入「全部播放」功能
3. 部署到 GitHub Pages

### 關鍵檔案參考
- `index.html:199-243` - 播放按鈕 CSS 樣式
- `index.html:377-400` - JavaScript 播放邏輯
- `generate_audio.py:17-52` - 台詞列表和聲音配置
- `generate_audio.py:76-82` - TTS API 呼叫（含 speed 參數）

### 建議命令
```bash
# 重新生成語音（如需調整）
set -a && source .env && set +a && uv run python generate_audio.py

# 放大音量（如需調整倍數）
for f in audio/*.mp3; do ffmpeg -y -i "$f" -filter:a "volume=2.0" "${f%.mp3}_loud.mp3" && mv "${f%.mp3}_loud.mp3" "$f"; done

# 本地測試
python3 -m http.server 8000
```

## 上下文提示

- 這個專案使用 **uv** 管理 Python 依賴，不要用 pip
- OpenAI API Key 存放在 `.env` 檔案中
- 語音配置：Archie=echo（年輕男聲）, Mera=nova（女聲）, 合唱=alloy（中性）
- 語速設為 0.9 倍（稍慢，適合舞台劇）
- 台詞文字使用大寫強調和省略號來引導 TTS 語調
- 音檔已用 ffmpeg 放大 2 倍音量，原始備份在 `audio_backup/`
