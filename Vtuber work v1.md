---
aliases:
---
你好！身為初學者唔使驚，我會用最簡單嘅廣東話，一步步教你點樣整起呢個 Open LLM VTuber。

簡單嚟講，呢個程式係將幾個部分砌埋一齊：
1. **ASR (聽覺)**：聽你講嘢。
2. **LLM (大腦)**：諗點樣覆你（用 Ollama）。
3. **TTS (說話)**：將文字變做聲。
4. **Live2D (外表)**：你嘅虛擬形象。

我哋依家開始！

---

### 第一步：準備工具 (裝嘢)

你要喺電腦裝幾樣基本工具。如果你係 Windows 用家，請撳 **Win + R** 掣，打 `cmd` 撳 Enter，然後逐行 Copy 呢啲指令入去行：

1.  **裝 Git** (用嚟攞個程式返嚟)：
    ```bash
    winget install Git.Git
    ```
2.  **裝 FFmpeg** (處理音效，一定要裝)：
    ```bash
    winget install ffmpeg
    ```
3.  **裝 uv** (用嚟管理 Python 環境，好方便嘅工具)：
    ```bash
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
    *裝完 uv 之後，請熄咗個 cmd 視窗再開返一個新嘅，等佢生效。*

---

### 第二步：攞個程式返嚟

1.  去呢個 [GitHub Release 網頁](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/releases)。
2.  搵最新版本，下載嗰個 `Open-LLM-VTuber-v1.x.x.zip`。
3.  **重要：** 搵個地方解壓佢（例如 `D:\vtuber`）。**路徑唔好有中文**，唔好擺喺「桌面」或「下載」資料夾（因為路徑可能含中文名）。

---

### 第三步：裝「大腦」(Ollama)

我哋用 Ollama 做 AI 大腦，因為佢喺本地行，唔使錢又快。

1.  去 [Ollama 官網](https://ollama.com/) 下載同安裝。
2.  裝完之後，開 cmd 視窗，打呢句嚟下載個 AI 模型（推薦 Qwen 2.5，廣東話/中文好好）：
    ```bash
    ollama run qwen2.5:latest
    ```
3.  見到佢可以對話就代表成功，可以熄咗個 cmd。

---

### 第四步：設定程式

1.  入去你啱啱解壓個 `Open-LLM-VTuber` 資料夾。
2.  搵一個叫 `config_templates` 嘅資料夾，入面有個 `conf.ZH.default.yaml`。
3.  將呢個檔案 **Copy 份去項目嘅根目錄**（即係最出嗰層），然後改名做 `conf.yaml`。
4.  用記事本打開 `conf.yaml`，確保入面呢幾行係咁樣：
    ```yaml
    llm_provider: ollama_llm
    ollama_llm:
      base_url: http://localhost:11434
      model: qwen2.5:latest  # 確保同你頭先 download 嘅名一樣
    ```

---

### 第五步：換入你嘅 Live2D 模型

既然你有自己嘅 Live2D 模型，跟我咁做：

1.  喺項目資料夾入面，搵一個叫 `live2d` 或者 `public/live2d` 嘅資料夾（視乎版本，通常喺 `src/open_llm_vtuber/resources/live2d` 或者直接喺根目錄）。
2.  將你成個 Live2D 模型資料夾（入面要有 `.model3.json` 嗰堆嘢）抄入去。
3.  **點樣套用？** 
    *   你可以喺 `conf.yaml` 入面搵 `live2d_model` 嗰行，改做你個資料夾名。
    *   **更簡單嘅方法：** 陣間開咗網頁介面之後，直接喺介面上揀返你個模型。

---

### 第六步：開波！

1.  喺項目資料夾個位開 cmd，行呢句裝依賴（第一次行要等一陣）：
    ```bash
    uv sync
    ```
2.  然後行呢句啟動後端：
    ```bash
    uv run run_server.py
    ```
3.  當你見到佢寫住 `Running on http://localhost:12393`，就用 **Chrome 瀏覽器** 打開呢個網址。
4.  喺網頁右邊或者設定位，你應該可以見到你個 Live2D 模型名，揀佢就得喇！

---

### 初學者小貼士：

*   **點解唔識郁？** 記得喺 Chrome 網頁撳吓個「Start」或者「Mic」掣，佢先會開始聽你講嘢。
*   **點改 AI 性格？** 喺 `conf.yaml` 入面搵 `system_prompt`，你可以寫「你係一個可愛嘅女仔，用廣東話同我傾偈」。
*   **遇到 Error？** 大部分原因係 FFmpeg 冇裝好，或者 Ollama 未開。

如果你行到邊一步卡住咗，話我知個 Error 係咩，我再幫你！

---
# part 2
要將呢個 VTuber 程式連接到 **Ollama AI**，其實原理好簡單：Ollama 喺你電腦入面開咗一間「大腦辦公室」，而 VTuber 程式就係透過一個「內部電話號碼」打過去問嘢。

以下係詳細嘅連接步驟同埋原理：

### 1. 連接嘅原理（最簡單解釋）
*   **Ollama** 係一個服務器（Server），佢行嗰陣會佔用你電腦嘅 **11434** 呢個埠（Port）。
*   **Open-LLM-VTuber** 係一個客戶端（Client），佢會發送你講嘅嘢去 `http://localhost:11434`。
*   只要呢個地址啱，佢哋就會連通。

---

### 2. 點樣設定連接？（步步教你）

你主要需要改個 `conf.yaml` 檔案：

**第一步：話俾程式聽你要用 Ollama**
喺 `conf.yaml` 入面搵到 `llm_provider` 呢一行，改做：
```yaml
llm_provider: "ollama_llm"
```

**第二步：話俾程式聽 Ollama 喺邊度同埋用邊個模型**
喺同一個檔案入面，搵到 `ollama_llm:` 嗰一忽，跟住下面咁填：
```yaml
ollama_llm:
  base_url: "http://localhost:11434"  # 呢個係 Ollama 預設嘅「內部電話」
  model: "qwen2.5:latest"            # 呢個名一定要同你喺 Ollama pull 嘅名一樣
  temperature: 0.7                   # 數值越高，AI 講嘢越活潑（0 到 1 之間）
```

---

### 3. 點樣檢查連唔連到？

如果你唔肯定 Ollama 有冇開好，你可以做呢個測試：

1.  **檢查 Ollama 有冇行緊：**
    打開瀏覽器（Chrome），喺網址欄打：`http://localhost:11434`
    *   如果你見到一句 **"Ollama is running"**，代表個門口已經開咗，VTuber 程式可以入去。
    *   如果顯示「無法連上網站」，代表你仲未開 Ollama 程式。

2.  **檢查模型名啱唔啱：**
    開 Cmd (終端機)，打：
    ```bash
    ollama list
    ```
    你會見到一張清單。你要將 `NAME` 下面嗰串字（例如 `qwen2.5:latest`）完整咁 Copy 落 `conf.yaml` 嘅 `model` 位。

---

### 4. 常見問題 (Troubleshooting)

*   **點解我改咗 `conf.yaml` 都冇反應？**
    *   記得改完要 **Save 檔案**。
    *   你要**重新啟動** `uv run run_server.py`（即係喺 Cmd 按 Ctrl+C 熄咗佢再開過），啲新設定先會生效。
*   **連到但 AI 唔識講嘢？**
    *   睇吓行緊個個 Cmd 視窗，如果有紅色字寫住 `404 Not Found`，通常係因為你個 `model` 名打錯咗。
*   **防火牆問題：**
    *   如果你有開 VPN 或者好勁嘅防毒軟件，有時會塞住咗 `localhost` 呢條路。試吓暫時熄咗 VPN 再試。

**總結：** 只要 Ollama 喺後台行緊（見到 "Ollama is running"），而且 `conf.yaml` 入面個 `base_url` 同 `model` 名啱，佢哋就會自動連埋一齊㗎喇！