import json
import sqlite3
conn = sqlite3.connect("mydb.db")
print("連上資料庫 mydb")
cursor = conn.cursor()
print("建立游標物件")

with open("employee.json",encoding="utf-8")as file:
    data = json.load(file)
    for i in range(len(data)):
        name = data[i]["name"]
        salary = data[i]["salary"]
        sqlstr = '''
            INSERT INTO employee(name,salary) VALUES('{}',{})
        '''.format(name,salary)
        print("新增第 "+(str)(i+1)+" 筆資料")
        cursor.execute(sqlstr)
conn.commit()
conn.close()
