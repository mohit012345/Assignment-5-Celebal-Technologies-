import sqlite3
import os

src_db = "source.db"
dest_db = "destination.db"

tables_to_copy = {
    "students": ["id", "name"],
    "teachers": ["id", "subject"]
}

if os.path.exists(dest_db):
    os.remove(dest_db)


src_conn = sqlite3.connect(src_db)
dest_conn = sqlite3.connect(dest_db)
src_cursor = src_conn.cursor()
dest_cursor = dest_conn.cursor()

for table, columns in tables_to_copy.items():
    columns_str = ', '.join(columns)
    
    
    src_cursor.execute(f"PRAGMA table_info({table})")
    schema_info = src_cursor.fetchall()

   
    column_defs = []
    for col in schema_info:
        if col[1] in columns:
            column_defs.append(f"{col[1]} {col[2]}")  # name + type
    create_stmt = f"CREATE TABLE {table} ({', '.join(column_defs)});"
    dest_cursor.execute(create_stmt)

    
    src_cursor.execute(f"SELECT {columns_str} FROM {table}")
    rows = src_cursor.fetchall()

    if rows:
        placeholders = ', '.join(['?'] * len(columns))
        dest_cursor.executemany(
            f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})",
            rows
        )

dest_conn.commit()
src_conn.close()
dest_conn.close()

print("Selected tables and columns copied to destination database.")
