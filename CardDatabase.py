import sqlite3
from CardLogic import mainDictionary

# Connect to the database, named 'card.db'
conn = sqlite3.connect('flashcard_database.db')

c = conn.cursor()

c.execute("CREATE TABLE cards (firstSide text, secondSide text, category text, image text)")

for i in mainDictionary:
    c.execute("INSERT INTO cards VALUES ('" + i + "','" + mainDictionary[i] + "','" + "default" + "','" + "image" + "')")

conn.commit()

print(c.fetchall())
conn.close()
