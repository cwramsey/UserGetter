from dbUtils import *
import pymysql.cursors

con = dbConnect()
print con

try:
	with con.cursor() as cursor:
		sql = "SELECT * FROM users;"
		cursor.execute(sql)
		result = cursor.fetchone()
		print result
finally:
	con.close()
