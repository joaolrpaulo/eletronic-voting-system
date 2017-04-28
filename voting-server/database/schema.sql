CREATE TABLE IF NOT EXISTS voters(
    national_id INTEGER PRIMARY KEY NOT NULL,
    username TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL
);
