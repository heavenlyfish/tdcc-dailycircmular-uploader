import requests
import json
import pandas as pd
from datetime import datetime, timedelta

# 日期處理
today = datetime.today()
fetch_date_str = today.strftime("%Y/%m/%d")
offset = (today.weekday() - 4) % 7
last_friday = today - timedelta(days=offset)
friday_str = last_friday.strftime("%Y%m%d")

# 擷取資料
url = "https://openapi.tdcc.com.tw/v1/opendata/2-26"
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.content.decode('utf-8'))
    records = data if isinstance(data, list) else data.get("data", [])

    if records:
        df = pd.DataFrame(records)
        df.columns = [col.strip('\ufeff') for col in df.columns]
        df = df[["股票代號", "股票名稱", "發行比率", "上週餘額", "本週餘額", "增減數額", "增減比率"]]
        df["FetchedDate"] = fetch_date_str
        df.set_index("股票代號", inplace=True)

        filename = f"tdcc_2-26_{friday_str}.csv"
        df.to_csv(filename, encoding="utf-8-sig")

        # 儲存檔名供下一支程式使用
        with open("latest_file.txt", "w") as f:
            f.write(filename)
    else:
        raise Exception("⚠️ 沒有資料")
else:
    raise Exception(f"❌ 擷取失敗，狀態碼 {response.status_code}")
