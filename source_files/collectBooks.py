import sqlite3

import igraslov
import labirint

sqlite_connection = sqlite3.connect('../books.db')
cursor = sqlite_connection.cursor()
books_igraslov = igraslov.parse()
# for i in books_igraslov['title']:
#     cursor.execute(f"""INSERT INTO books
#                           (id,name)
#                           VALUES
#                           ('{str(uuid.uuid4())}','{i}');""")

# sqlite_connection.commit()

for i in books_igraslov['title']:
    a = labirint.parse(i)
    print(111)
