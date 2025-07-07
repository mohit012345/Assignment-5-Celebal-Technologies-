# Assignment-5-Celebal-Technologies-
Database Automation & Transformation
# 📦 Database Automation & Transformation – Assignment Set

This project contains four complete solutions focused on data movement, transformation, and automation using Python and relational databases. These solutions are essential for backup, migration, real-time processing, and format conversion use cases in modern data engineering tasks.

##  1: Copy Data from Database to CSV, Parquet, and Avro File Formats

### 🎯 Objective
Extract data from a relational database and export it into three common file formats:
- **CSV** – For universal readability and reporting
- **Parquet** – For efficient columnar storage used in analytics
- **Avro** – For schema evolution and compact serialization, often used in big data pipelines

### 🛠️ Technologies Used
- Python
- SQLite (as relational DB)
- Libraries: `pandas`, `pyarrow`, `fastavro`

### 📌 Steps
1. Connect to a SQLite database
2. Read data into a DataFrame using SQL
3. Export to:
   - `employees.csv`
   - `employees.parquet`
   - `employees.avro`

### ▶️ Run Command

pip install pandas pyarrow fastavro
python extract_export.py




## 2: Configure Schedule Trigger and Event Triggers to Automate the Pipeline Process
🎯 Objective
Automate the execution of a data pipeline using:

Schedule-based triggers – Run the pipeline periodically (e.g., every day at 2 AM)

Event-based triggers – Run the pipeline immediately after an action (e.g., file added)

🛠️ Tools Used
Python

cron (Linux/macOS) or Windows Task Scheduler

watchdog library for event-based automation

⚙️ Examples
⏰ Schedule Trigger (Linux/macOS)
Add to crontab:

0 2 * * * /usr/bin/python3 /full/path/to/extract_export.py
⚡ Event Trigger (File watcher)
pip install watchdog
python event_trigger.py
Triggers the pipeline when a new file is added to input_files/ folder.




## 3: Copy All Tables from One Database to Another
🎯 Objective
Perform full database replication by dynamically:

Detecting all tables

Copying schema (structure)

Copying all table data

This is useful for backup, cloning, or staging-to-production syncs.

🛠️ Technologies Used
Python

sqlite3 (lightweight relational DB)

📌 Output
All tables from source.db are copied to destination.db with their full data and structure.

▶️ Run Command
python copy_all_tables.py




 ## 4: Copy Selective Tables with Selective Columns from One Database to Another
🎯 Objective
Copy only specific tables and columns from a source database to a destination database. Useful for:

Selective migration

Data minimization for compliance

Migrating only business-relevant data

🛠️ Technologies Used
Python

SQLite for demo

MySQL version available using pymysql + pandas

📌 Example Mapping
tables_to_copy = {
    "students": ["id", "name"],
    "teachers": ["id", "subject"]
}
▶️ Run (SQLite)
python copy_selective_columns.py
▶️ Run (MySQL Version)
pip install pymysql pandas
python copy_selective_mysql.py
Update the database credentials and connection config in the script.

🧠 Summary
Assignment	Description
1	Export DB data into CSV, Parquet, and Avro formats
2	Automate pipeline using scheduled and event-based triggers
3	Copy all tables and data from one DB to another
4	Copy only selected tables and columns from source to destination DB
📬 Contact
For help, improvements, or contributions, feel free to connect.
