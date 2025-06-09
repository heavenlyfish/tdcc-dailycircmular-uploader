from mega import Mega
import os
import requests

# 讀取上一步生成的檔名
with open("latest_file.txt", "r") as f:
    filename = f.read().strip()

# 上傳至 MEGA
mega = Mega()
m = mega.login(os.getenv("MEGA_EMAIL"), os.getenv("MEGA_PASSWORD"))

# Step 2: Traverse or create folder path: "CB_Database/Weekly_Circulate"
def get_or_create_folder(path):
    parts = path.strip("/").split("/")
    nodes = m.get_files()
    parent = None

    for part in parts:
        folder_node = None

        for node in nodes.values():
            if node["t"] == 1 and node["a"]["n"] == part:
                if parent is None and node["p"] == m.root_id:
                    folder_node = node
                    break
                elif parent is not None and "h" in parent and node["p"] == parent["h"]:
                    folder_node = node
                    break

        if folder_node is None:
            folder_node = m.create_folder(part, parent["h"] if parent else None)

        parent = folder_node

    return parent

# Use this path
dest_folder = get_or_create_folder("CB_Database/Weekly_Circulate")

# Step 3: Upload the file into the target folder
file = m.upload(filename, dest=dest_folder["h"])
link = m.get_upload_link(file)

# 寫入 input.txt 做追蹤
with open("input.txt", "a", encoding="utf-8") as f:
    f.write(f"{filename}\n{link}\n")

# 傳送 Telegram 通知
bot_token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")
message = f"📊 TDCC 資料已上傳至 MEGA！\n📁 檔名：`{filename}`\n🔗 [點此下載]({link})"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {
    "chat_id": chat_id,
    "text": message,
    "parse_mode": "Markdown"
}

res = requests.post(url, json=payload)
if res.ok:
    print("📲 Telegram 通知已發送。")
else:
    print("❌ 傳送 Telegram 失敗：", res.text)
