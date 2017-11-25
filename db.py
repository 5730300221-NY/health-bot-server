
from urllib import parse
import psycopg2

parse.uses_netloc.append("postgres")
url = parse.urlparse('postgres://fjofpvoarswjmb:63555fbe9041f5e38680e1a3557882a83569382a9a7416572824bcebd377fcb8@ec2-174-129-195-73.compute-1.amazonaws.com:5432/d1rvsa42culqja')

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
def doQuery(  ) :

    cur.execute( "SELECT id,menu,cal From calorie" )

    for id,menu,cal in cur.fetchall() :
        return (id,menu,cal)

# doInsert(conn)
def doInsert():
    food = ({"id":"000055","menu":"ข้าวหมูแดง","cal":"541"})
    cur.execute("""INSERT INTO calorie (id,menu, cal)VALUES (%(id)s,%(menu)s,%(cal)s);""",food)
    conn.commit()
    return ("Insert Done!!!")