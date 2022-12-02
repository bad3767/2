import pymysql

db=pymysql.connect ("localhost","root","aaaa","collage")
c=db.cursor()

sql="delete from emp where name = 'ganesh'"
c.execute(sql)
db.commit()
db.close()
print("data inserted")
