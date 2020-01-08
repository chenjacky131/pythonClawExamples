from MysqlClient import MysqlClient
mysql = MysqlClient()
conn = mysql.conn
sql = 'SELECT * FROM proxy_pool WHERE status = "1" order by update_date ASC'
cursor = conn.cursor()
cursor.execute(sql)
res = cursor.fetchall()
cursor.close()
conn.commit()

for item in list(res):
    print(item[1] + '://' + item[2] + ':' + item[3])
