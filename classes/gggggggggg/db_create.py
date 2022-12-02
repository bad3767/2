import pymysql

db = pymysql.connect("localhost","root","aaaa","school")
c = db.cursor()

sql = "create table student (id int(3),name char(30),phno int (10),location char(30))"

c.execute(sql)
db.close()
print("table created")
