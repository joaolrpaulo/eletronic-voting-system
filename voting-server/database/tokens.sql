CREATE TABLE IF NOT EXISTS tokens(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    voter_id INTEGER NOT NULL,
    token VARCHAR(255) NOT NULL,
    expiration_ts INTEGER NOT NULL
);