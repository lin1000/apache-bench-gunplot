# url=jdbc:postgresql://172.31.72.130:3433/postgres
# #url=jdbc:postgresql://rm-3ns40d8hp7xi206z48o.pg.rds.aliyuncs.com:3432/postgres
# username1=lin1000
# password=98sc@SAenv
import psycopg2

conn = psycopg2.connect(database="postgres", user="lin1000", password="98sc@SAenv", host="rm-3ns40d8hp7xi206z48o.pg.rds.aliyuncs.com", port="3432")
print("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print("Table created successfully")

conn.commit()
conn.close()