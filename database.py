import os
from urllib import parse
import psycopg2

parse.uses_netloc.append("postgres")
url = parse.urlparse('postgres://jdkmwbvojlabyy:a94ff5eb01d2a2804163b2c7c3d5230f754b7c9d64ba57a3ec8534d0c4f3bfc9@ec2-23-21-101-174.compute-1.amazonaws.com:5432/d7kdh01tu0nvas')

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

# insert
# def doInsert( conn ) :
#     cur = conn.cursor()
#     cur.execute('''INSERT into calorie (id, menu,cal)
#                   values (%s, %s,%s)''',
#                   ("000055", "ไข่ต้ม","50"))
#     conn.commit()

# query
cur = conn.cursor()
def docreate() :

    cur.execute("""CREATE TABLE user_detail (
                    user_id VARCHAR(100) PRIMARY KEY,
                    age int NOT NULL,
                    height float ,
                    weight float ,
                    bmi float)
                """)

    conn.commit()
    print ("create done!!")

# doInsert(conn)
def insertUser(user_detail):
    cur.execute("""INSERT INTO user_detail (user_id,age)VALUES (%(id)s,%(age)s)""",user_detail)
    conn.commit()
    return ("Insert Done!!!")
