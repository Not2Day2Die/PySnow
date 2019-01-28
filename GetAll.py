import requests
import time
import json

input_file = open ('stockCode.json')
json_array = json.load(input_file)

for item  in json_array:
    start_time = time.time()
    resp = requests.get("http://60.251.238.43:8780/Crawler/GetStockHistoryPrice?stockNumber="+item["code"])
    print("--- %s seconds ---" % (time.time() - start_time))
    print(item["code"])
    time.sleep(5)