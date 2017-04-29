CREATE TABLE IF NOT EXISTS voters(
    voter_id INTEGER PRIMARY KEY NOT NULL,
    hash TEXT NOT NULL,
    salt TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL
);
