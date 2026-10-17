import mysql.connector as c

con = c.connect(
    host='localhost',
    user='root',
    password='root123'
)

if con.is_connected():
    print('Done')
else:
    print('Not Done')