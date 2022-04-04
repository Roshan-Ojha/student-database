import  sqlite3
conn=sqlite3.connect('Marks.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS mark(
            name text,
            class integer,
            sec text,
            roll integer,
            english_theory real,
            english_practical real,
            nepali_theory real,
            nepali_practical real,
            mathematics real,
            science_theory real,
            science_practical real,
            social_theory real,
            social_practical real,
            eph_theory real,
            eph_practical real,
            opt_i real,
            opt_ii_theory real,
            opt_ii_practical real
            
            )
        
        """)
conn.commit()
conn.close()
