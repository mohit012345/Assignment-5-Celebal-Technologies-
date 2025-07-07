import sqlite3
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from fastavro import writer, parse_schema

conn = sqlite3.connect("mydata.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER,
        name TEXT,
        department TEXT,
        salary REAL
    )
""")

cursor.execute("DELETE FROM employees")  
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", [
    (1, "Alice", "HR", 50000),
    (2, "Bob", "Engineering", 75000),
    (3, "Charlie", "Marketing", 60000)
])
conn.commit()

df = pd.read_sql_query("SELECT * FROM employees", conn)

df.to_csv("employees.csv", index=False)
print("✔ Data exported to CSV: employees.csv")


df.to_parquet("employees.parquet", index=False)
print("✔ Data exported to Parquet: employees.parquet")


schema = {
    "type": "record",
    "name": "Employee",
    "fields": [{"name": col, "type": "string"} for col in df.columns]
}


records = df.astype(str).to_dict(orient='records')

with open("employees.avro", "wb") as out:
    writer(out, parse_schema(schema), records)

print("✔ Data exported to Avro: employees.avro")


conn.close()
