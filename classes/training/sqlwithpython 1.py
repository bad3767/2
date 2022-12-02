import pymysql
db = pymysql.connect("localhost",'root','aaaa','biodata')
c =db.cursor()

sql="insert into biodata(name,father_name,gender,age) values('bala','chandran','male',45)"
c.execute(sql)
db.commit()
db.close()
print ("data inserted")
