import sqlite3
import uuid

import igraslov

sqlite_connection = sqlite3.connect('../books.db')
cursor = sqlite_connection.cursor()
books_igraslov = igraslov.parse()
for i in books_igraslov['title']:
    cursor.execute(f"""INSERT INTO books
                          (id,name)
                          VALUES
                          ('{str(uuid.uuid4())}','{i}');""")

sqlite_connection.commit()
