import sqlite3
from CardLogic import mainDictionary

# Connect to the database, named 'card.db'
conn = sqlite3.connect('card.db')

c = conn.cursor()


#c.execute("""CREATE TABLE cards (
 #          firstSide text,
  #          secondSide text
    #         )""")

# TODO Move this to CardLogic.py? Why does it NEED to be here?
#for i in mainDictionary:
#    c.execute("INSERT INTO cards VALUES ('" + i + "','" + mainDictionary[i] + "')")


c.execute("SELECT * FROM cards WHERE secondSide='Russia'")
print(c.fetchall())


conn.commit()
conn.close()
