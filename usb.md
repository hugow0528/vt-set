要在朋友部完全「乾淨」嘅電腦重新整過，而且想儘量做到「便攜（Portable）」，我哋可以將大部分嘢擺喺個資料夾或者 USB 入面。

不過要注意：**Ollama**（AI 大腦）通常需要安裝喺系統入面，其他嘢都可以跟住資料夾走。

以下係喺新電腦重新整起嘅**最強「便攜式」攻略**：

---

### 1. 準備工作 (準備好你個 USB)
喺你出發去朋友部機之前，或者喺朋友部機下載定呢幾樣嘢放入 USB：

1.  **FFmpeg 執行檔**：
    *   下載 [ffmpeg-release-full.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z)。
    *   入去 `bin` 資料夾，攞走 `ffmpeg.exe` 同 `ffprobe.exe`。
2.  **Open-LLM-VTuber 程式碼**：
    *   去 [GitHub Release](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/releases) 下載 `Source code (zip)`。
3.  **Live2D 模型**：
    *   帶埋你個「新女兒0.1」資料夾。

---

### 2. 喺朋友部機嘅正式步驟 (Step-by-Step)

#### 第一步：安裝「大腦」(Ollama)
因為 Ollama 係系統服務，一定要裝一次：
1.  去 [Ollama 官網](https://ollama.com/) 下載並安裝。
2.  開 PowerShell，下載 AI 模型（呢步要等一陣，視乎網速）：
    ```powershell
    ollama run qwen2.5:latest
    ```
3.  見到可以傾偈就代表 Ollama 搞掂，可以熄咗佢。

#### 第二步：擺放程式同 FFmpeg (便攜化核心)
1.  將 `Open-LLM-VTuber.zip` 解壓到一個路徑**冇中文**嘅地方（例如 `D:\AI_VTuber`）。
2.  **關鍵一步：** 將 USB 入面嗰兩個 `ffmpeg.exe` 同 `ffprobe.exe` 直接 Copy 貼入 `D:\AI_VTuber\Open-LLM-VTuber\` 入面。
    *   *咁樣就唔使喺朋友部機搞環境變數。*

#### 第三步：安裝 `uv` (管理 Python 環境)
雖然朋友部機乜都冇，但用 `uv` 係最快最乾淨嘅方法：
1.  開 PowerShell，打呢句裝 `uv`：
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
2.  **重啟 PowerShell**。

#### 第四步：安裝專案依賴
1.  喺 PowerShell 入去你個資料夾：
    ```powershell
    cd D:\AI_VTuber\Open-LLM-VTuber
    ```
2.  行呢句（佢會自動幫你裝 Python 同所有 library）：
    ```powershell
    uv sync
    ```

---

### 3. 設定你嘅 Live2D 同 Config (解決之前嘅問題)

由於你之前遇到中文檔名同資料夾名唔夾嘅問題，重新嚟過嗰陣要咁做：

1.  **放模型**：將「新女兒0.1」資料夾放入 `live2d-models` 入面。
2.  **改 `model_dict.json`**：喺主目錄搵到呢個檔案，改做：
    ```json
    {
      "mao_pro": "mao_pro/mao_pro.model3.json",
      "新女兒": "新女兒0.1/新女兒.model3.json"
    }
    ```
3.  **準備 `conf.yaml`**：
    *   去 `config_templates` Copy `conf.ZH.default.yaml` 出去主目錄，改名做 `conf.yaml`。
    *   打開 `conf.yaml` 改呢幾行：
        *   `llm_provider: 'ollama_llm'`
        *   `live2d_model_name: '新女兒'`
        *   `ollama_llm` 下面嘅 `model: 'qwen2.5:latest'`
        *   `voice: zh-HK-HiuGaaiNeural` (如果你想聽廣東話)

---

### 4. 啟動玩得！
喺 PowerShell 行：
```powershell
uv run run_server.py
```
然後打開 Chrome 入 `http://localhost:12393`。

---

### 總結：點樣先算「Portable」？
如果你想將成舊嘢帶走，下次去另一部機：
1.  **帶走成個 `Open-LLM-VTuber` 資料夾**。入面已經有晒 `ffmpeg`、你改好嘅 `conf.yaml` 同埋 `.venv`（Python 環境）。
2.  喺新機**唯一要做**嘅係：
    *   安裝 **Ollama** 並下載模型。
    *   安裝 **uv**。
    *   然後直接喺嗰個資料夾行 `uv run run_server.py`。

**咁樣做，你就唔使重新改過啲 Config 內容，只需要喺新電腦準備好 AI 大腦（Ollama）同工具（uv）就得！** 如果你喺朋友部機搞嗰陣卡住咗，隨時問我！
