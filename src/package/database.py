import sqlite3
from pathlib import Path
from .table_data import participants, visits, measurements

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

connection.executemany(
    "INSERT INTO visits (person_id, visit_date, visit_length)"
    "VALUES (?, ?, ?)",
    visits
)

connection.executemany(
    "INSERT INTO measurements (visit_id, weight, height, waist)"
    "VALUES (?, ?, ?, ?)",
    measurements
)

cursor = connection.execute("SELECT * FROM measurements;")
print(cursor.fetchall())