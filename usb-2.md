可以！絕對可以！我哋依家就將個 USB 變做一個「VTuber 隨身啟動盤」。

你可以先喺自己部機（或者任何有網嘅電腦）將所有「材料」準備好入落 USB，去到朋友部機就唔使再慢慢搵、慢慢 Download 咁辛苦。

以下係你個 **USB 懶人包** 嘅準備流程：

---

### 第一階段：喺你自己機準備 USB (唔使理 Ollama 先)

請確保你個 USB 空間夠大（建議 16GB 以上，因為 AI 模型好大舊）。

#### 1. 放入程式碼 (利用你嘅 GitHub CLI)
打開你 USB 嘅視窗，喺裡面開 PowerShell：
```powershell
# 用你 USB 入面嘅 gh cli clone 專案
gh repo clone Open-LLM-VTuber/Open-LLM-VTuber
```

#### 2. 放入「工人」 (FFmpeg)
1. 將你之前搵到嘅 `ffmpeg.exe` 同 `ffprobe.exe` 直接 Copy。
2. 貼入 USB 嘅 `Open-LLM-VTuber` 資料夾入面（即係同 `run_server.py` 擺埋一齊）。

#### 3. 放入「外表」 (Live2D 模型)
1. 將你個「**新女兒0.1**」資料夾，放入 USB 嘅 `Open-LLM-VTuber\live2d-models\` 入面。

#### 4. 預設「地圖」 (Config)
呢步好緊要，因為你要預先指路：
1. **修改 `model_dict.json`**：
   直接喺 USB 打開佢，改成你之前嗰段：
   ```json
   {
     "mao_pro": "mao_pro/mao_pro.model3.json",
     "新女兒": "新女兒0.1/新女兒.model3.json"
   }
   ```
2. **準備 `conf.yaml`**：
   將樣板 Copy 出嚟，改定入面嘅 `live2d_model_name: '新女兒'`。

#### 5. 準備「大腦安裝包」 (Ollama)
去 [Ollama 官網](https://ollama.com/download/OllamaSetup.exe) 下載個安裝程式，直接擺喺 USB 根目錄。**先唔好裝住**，純粹帶住佢走。

---

### 第二階段：去到朋友部機 (正式開工)

當你插條 USB 入朋友部機，跟住呢個順序行：

#### 1. 裝工具 (uv) - 呢個一定要行
雖然你想 Portable，但 `uv` 幫你搞 Python 環境係最快嘅。
1. 喺朋友部機開 PowerShell，打嗰句 `irm https://astral.sh/uv/install.ps1 | iex`。
2. 重啟 PowerShell。

#### 2. 建立 Python 環境 (uv sync)
1. 喺 PowerShell 入去 USB 嗰個 `Open-LLM-VTuber` 資料夾。
2. 行 `uv sync`。
   * *解釋：呢步會喺 USB 入面建立一個 `.venv` 資料夾。雖然啲庫喺 USB，但佢會根據朋友部機嘅硬體做少少調整。*

#### 3. 處理大腦 (Ollama) - 呢度有個 Portable 技巧！
如果你想將 AI 模型都擺喺 USB，唔想佔用朋友部機嘅 C Drive：
1. 行 USB 入面個 `OllamaSetup.exe` 裝咗佢。
2. **重點：** 裝完先**唔好**開 Ollama。
3. 喺 PowerShell 打呢句（假設你 USB 係 `E:`）：
   ```powershell
   $env:OLLAMA_MODELS = "E:\OllamaModels"
   ```
   *(咁樣 Ollama 就會將幾 GB 咁大嘅 AI 模型 Download 入你 USB，而唔係朋友部機。)*
4. 行 `ollama run qwen2.5:latest`。

#### 4. 啟動 VTuber
最後，返返去專案資料夾行：
```powershell
uv run run_server.py
```

---

### 點解咁樣做最 Portable？

*   **FFmpeg 同 Live2D**：已經喺 USB 資料夾入面，程式一開就見到。
*   **Config**：你已經喺 USB 改好晒，唔使去到新機再慢慢用記事本執。
*   **Python 環境**：`uv` 幫你喺 USB 搞掂，唔會整亂朋友部機。
*   **模型 (Models)**：透過設定 `OLLAMA_MODELS` 變數，你可以將最重嘅 AI 模型帶住走。

### 給你的小貼士：
如果你想更方便，可以喺 USB 寫一個 `start.bat` (批次檔)，入面寫：
```batch
@echo off
set OLLAMA_MODELS=%~dp0OllamaModels
start ollama serve
timeout /t 5
uv run run_server.py
pause
```
下次去到新機，一 Double Click 呢個檔就全自動開晒所有嘢！

**你而家可以開始搬啲嘢入 USB 先。如果有邊個檔案你唔肯定擺邊，再問我！**
