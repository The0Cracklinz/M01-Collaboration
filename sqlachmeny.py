import sqlite3

conn = sqlite3.connect('books.db')


c = conn.cursor()

#c.execute("""CREATE TABLE books(
#          title text,
#          author text,
#          year text
#) """)

#manyBooks = [
#                    ('The Weirdstone of Brisingamen','Alan Garner','1960'),
#                    ('Perdido Street Station','China Miéville','2000'),
#                    ('Thud!','Terry Pratchett','2005'),
#                    ('The Spellman Files','Lisa Lutz','2007'),
#                    ('Small Gods','Terry Pratchett','1992'),
#                              ]
#c.executemany("INSERT INTO books VALUES (?,?,?)", manyBooks)
query = "SELECT title FROM books ORDER BY title ASC"

results = conn.execute(query).fetchall()


for row in results:
        print(row[0])

print("gud run!")


conn.commit()
conn.close()





