import sqlite3
conn = sqlite3.connect("Example.db")
c = conn.cursor()
'''
c.execute(""" CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARY KEY,NAME TEXT,SALARY REAL) """)
c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES (101,'Kadir','100000')")
c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES (102,'rik','120000')")
c.execute("INSERT INTO EMP(ID,NAME,SALARY) VALUES (103,'Saifan','200000')")
conn.execute("Commit")'''

c.execute(""" SELECT * FROM EMP """)

for i in c:
	print(i)
c.execute(""" UPDATE EMP SET NAME = 'SHAAYN' WHERE ID = 103 """)
conn.execute("COMMIT")
print(next(c))
