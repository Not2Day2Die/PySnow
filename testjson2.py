import json
import os
import pymssql

conn = pymssql.connect(host='60.251.238.43',
                       user='sa',
                       password='8179311!QAZ',
                       database='db8780',
                       charset='utf8',
                       port=8433)

with open('json/20170612.json') as json_data:
    d = json.load(json_data)
    for obj in d : 
        cursor = conn.cursor()
        sql = 'DROP TABLE s'+obj["證券代號"]+';'
        #cursor.execute(sql)
        filename = "txt/dtable.txt"
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(filename, 'a')as f:
            f.write(sql)