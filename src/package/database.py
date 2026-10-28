import sqlite3
from pathlib import Path
from src.package.table_data import participants

def create_schema(connection: sqlite3.Connection) -> None:
    file_path = Path("sql/schema.sql")
    sql_text = file_path.read_text(encoding="utf-8")
    connection.executescript(sql_text)

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
create_schema(connection)

connection.executemany(
    "INSERT INTO participants (name, age, sex, study_group)"
    "VALUES (?, ?, ?, ?)",
    participants
)

cursor = connection.execute("SELECT * FROM participants;")
print(cursor.fetchall())