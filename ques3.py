import sqlite3
import shutil
import os


src_db = 'source.db'
dest_db = 'destination.db'

if os.path.exists(dest_db):
    os.remove(dest_db)

src_conn = sqlite3.connect(src_db)
dest_conn = sqlite3.connect(dest_db)

src_cursor = src_conn.cursor()
dest_cursor = dest_conn.cursor()

src_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = src_cursor.fetchall()

for table_name in tables:
    table = table_name[0]
    print(f"Copying table: {table}")
    
   
    src_cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table}';")
    create_stmt = src_cursor.fetchone()[0]
    
    dest_cursor.execute(create_stmt)
    
   
    src_cursor.execute(f"SELECT * FROM {table}")
    rows = src_cursor.fetchall()
    
    if rows:
        placeholders = ','.join(['?'] * len(rows[0]))
        dest_cursor.executemany(f"INSERT INTO {table} VALUES ({placeholders})", rows)


dest_conn.commit()
src_conn.close()
dest_conn.close()

print("All tables copied from source.db to destination.db successfully.")
