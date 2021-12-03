import sqlite3
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
conn = sqlite3.connect("mydb.db")

print("成功連線資料庫")

cursor = conn.cursor()
print("成功建立游標物件")

sqlstr = '''
    CREATE TABLE IF NOT EXISTS "employee" (
    	"id"	INTEGER,
    	"name"	TEXT NOT NULL,
    	"salary"	REAL NOT NULL,
    	PRIMARY KEY("id" AUTOINCREMENT)
    );
'''
cursor.execute(sqlstr)
print("成功建立資料表")


''' 
# //第一次新增完畢後，先註解掉
sqlstr = '
    INSERT INTO employee("name","salary")
    VALUES ("Sharon",70000), ("Crystal",25000),
           ("Travis",30000), ("Jason",50000);
'
cursor.execute(sqlstr)
print("成功新增四筆資料")
'''

# 查詢出來 pandas顯示
sqlstr = "SELECT * FROM employee"
cursor.execute(sqlstr)
datas=[]
indexs=[]
columns=[]
# 抓取 columns
with open("employee.csv",encoding="utf-8") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        columns.append(row[1])
        break
print(columns)

# 抓取 indexs
for item in cursor.fetchall():
    indexs.append(item[1])
    datas.append((int)(item[2]))
print(indexs)
print(datas)
conn.commit()
conn.close()
print()
df = pd.DataFrame(datas,columns=columns,index=indexs)
print(df)

xticks = np.arange(1,len(indexs)+1)
plt.figure(figsize=(20,12))
plt.bar(xticks,datas,width=0.8)
plt.xticks(xticks, indexs)
plt.title("Employee",fontsize=40)
plt.xlabel("Name",fontsize=30)
plt.ylabel("Salary (Per Month)",fontsize=30)
plt.xticks(fontsize=20)
plt.yticks(fontsize=25)
plt.show()
