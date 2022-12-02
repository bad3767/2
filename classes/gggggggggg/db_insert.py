import pymysql

db = pymysql.connect("localhost","root","aaaa","school")
c = db.cursor()

sql = "insert into student(id,name,phno,location) values(111,'aaa',23524543,'chennai')"

c.execute(sql)
db.commit()
db.close()
print("data inserted")
