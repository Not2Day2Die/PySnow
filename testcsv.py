import csv
class stk:
    number = 0
    name = ''
    tradeStockCount = 0
    tradeCount = 0
    p_op = 0
    p_h = 0
    p_l = 0
    p_cl = 0 
    updown = 0
    pe = 0

    def __init__(self, var1, var2, var3, var4, var5, var6,var7, var8, var9, var10)
        self.number = var1
        self.name = var2
        self.tradeStockCount = var3
        self.tradeCount = var4
        self.p_op = var5
        self.p_h = var6
        self.p_l = var7
        self.p_cl = var8
        self.updown = var9
        self.pe = var10



my_list = []

with open('20190124.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        my_list.append(stk(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],row[10]))

print(my_list)