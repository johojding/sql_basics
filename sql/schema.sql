CREATE TABLE participants (
    person_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    sex TEXT NOT NULL,
    study_group TEXT NOT NULL
);

CREATE TABLE visits (
    visit_id INTEGER PRIMARY KEY,
    person_id INTEGER NOT NULL,
    visit_date  TEXT NOT NULL,
    visit_length REAL NOT NULL,
    FOREIGN KEY (person_id)
        REFERENCES participants(person_id)
);

CREATE TABLE measurements (
    measurement_id INTEGER PRIMARY KEY,
    visit_id INTEGER NOT NULL,
    weight REAL,
    height REAL,
    waist REAL,
    FOREIGN KEY (visit_id)
        REFERENCES visits(visit_id)
);

