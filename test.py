from millify import millify
import pandas as pd
import requests
import json
import util.constants.urls as urls

save_dict = {"platform": [], "volume": []}
web_data = requests.get(url=urls.url_sales_volume_cmp, headers={})
for item in json.loads(web_data.text):
  save_dict["platform"].append(item["PLATFORM_NAME"])
  save_dict["volume"].append(item["TRANSACTION_VOLUMES"])
df = pd.DataFrame(data=save_dict, columns=['platform', 'volume'])
print(df)