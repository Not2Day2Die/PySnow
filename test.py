import requests
import time
import datetime
from datetime import timedelta, date
import os
from io import StringIO
import pandas as pd
import numpy as np

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2012, 1, 1)
end_date = date(2015, 1, 1)
for single_date in daterange(start_date, end_date):
    try:
        datestr = single_date.strftime('%Y%m%d')
        # 下載股價
        r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
        # 整理資料，變成表格
        df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
            for i in r.text.split('\n') 
                if len(i.split('",')) == 17 and i[0] != '='])), header=0)
        print(df)
        json = df.to_json(orient='records')
        filename = "json/"+datestr+".json"
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(filename, 'w')as f:
            f.write(json)
        time.sleep(3)
    except:
        print("An exception occurred"+single_date.strftime('%Y%m%d'))
        time.sleep(3)

    



