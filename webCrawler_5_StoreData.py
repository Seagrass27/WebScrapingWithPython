import pymysql

conn = pymysql.connect(host = '127.0.0.1', user='root',passwd='123',
                       database = 'mysql',charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=2")

print(cur.fetchone())

cur.close()
conn.close()
