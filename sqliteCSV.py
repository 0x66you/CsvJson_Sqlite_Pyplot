import csv
import sqlite3
conn = sqlite3.connect("mydb.db")
print("連上資料庫 mydb")
cursor = conn.cursor()
print("建立游標物件")

with open("employee.csv",encoding="utf-8")as file:
    readcsv = csv.reader(file)
    count = 0
    for item in readcsv:
        if(count==0):
            count+=1
            continue
        name = item[0]
        salary = (int)(item[1])
        sqlstr = '''
            INSERT INTO employee(name,salary)
            VALUES ('{0}',{1})
        '''
        sqlstr = sqlstr.format(name,salary)
        cursor.execute(sqlstr)
        print("新增第 " + (str)(count)+ " 筆資料")
        count+=1
conn.commit()
conn.close()
