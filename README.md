# tdcc-dailycircmular-uploader

自動每週抓取 TDCC（櫃買中心）公佈的 **流通餘額證券標的資料**，並上傳到 MEGA 雲端，同時透過 Telegram 通知使用者。

---

## 📊 TDCC Weekly Circular Uploader

This GitHub Actions workflow automatically:

1. ✅ **Fetches the latest TDCC data file** weekly
2. ☁️ **Uploads the file to your MEGA cloud folder**
3. 📲 **Notifies you via Telegram with the filename and MEGA download link**

---

## 🔧 Features

- 🕙 **Automated Every Friday** at 10:00 PM (Taipei time)
- 🐍 Uses **Python 3.10** runtime
- 🔗 Integrates with:
  - ✅ [MEGA.io](https://mega.io/) for file storage
  - ✅ Telegram bot for instant alerts

---

## 📂 Folder Structure on MEGA

Uploaded files will be saved in:
CB_Database/
└── Weekly_Circulate/
---

## 📦 Requirements

Install the following Python packages:

```txt
pandas
requests
mega.py==1.0.8
tenacity==5.1.5  # Required by mega.py


## 🔐 GitHub Secrets 設定

請至你的 GitHub Repository → `Settings` → `Secrets and variables` → `Actions` → `New repository secret`，新增以下項目：

| Secret Name        | 說明                          |
|--------------------|-------------------------------|
| `MEGA_EMAIL`       | 你的 MEGA 登入信箱             |
| `MEGA_PASSWORD`    | 你的 MEGA 密碼                 |
| `TELEGRAM_TOKEN`   | 你的 Telegram 機器人 Token     |
| `TELEGRAM_CHAT_ID` | 你的 Telegram 使用者 ID（用 `/getUpdates` 可得） |


## 📁 專案結構

tdcc-dailycircmular-uploader/
├── tdcc_fetch_and_save.py            # 抓取 TDCC 最新檔案並儲存檔名
├── upload_to_mega_and_notify.py      # 上傳到 MEGA 並發送 Telegram 通知
├── requirements.txt                  # 所需 Python 套件
├── .github/
│   └── workflows/
│       └── tdcc_mega.yml             # GitHub Actions 排程設定
└── README.md                         # 本說明文件
