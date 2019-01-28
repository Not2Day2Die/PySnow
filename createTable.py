import pymssql

conn = pymssql.connect(host='60.251.238.43',
                       user='sa',
                       password='8179311!QAZ',
                       database='db8780',
                       charset='utf8',
                       port=8433)

#查看连接是否成功
cursor = conn.cursor()
'CREATE TABLE Customer(First_Name char(50),Last_Name char(50),Address char(50),City char(50),Country char(25),Birth_Date datetime);'
sql = ''
cursor.execute(sql)
#用一个rs变量获取数据
rs = cursor.fetchall()

print(rs)