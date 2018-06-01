import MySQLdb
db = MySQLdb.connect(user='root',passwd='admin',db='roja')
c = db.cursor()
s = c.execute("select * from roja_info")
s.commit()
data = c.fetchall(s)
db.close()
