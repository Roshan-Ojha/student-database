import sqlite3
conn=sqlite3.connect('Add.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS addstudent(
            name text,
            gender text,
            class integer,
            sec text,
            roll integer,
            address text,
            contact integer,
            father_name text,
            mother_name text
            )""")
conn.commit()
conn.close()