sqlite3 songs.db
.headers on
.mode table
SELECT name FROM songs; -- Makes one column with all the song names
SELECT name FROM songs ORDER BY tempo DESC; -- List all song names ordered in descending tempo
SELECT name FROM songs ORDER BY duration_ms DESC LIMIT 5; -- Find names of the 5 longest songs
SELECT name FROM songs WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75; -- Find songs where all three factors are above 0.75
SELECT AVG(energy) as 'Average Energy' FROM songs; -- Find average song energy
SELECT songs.name FROM songs JOIN artists ON artist_id = artists.id WHERE artists.name = 'Post Malone'; -- Find all songs by Post Malone
SELECT AVG(energy) FROM songs JOIN artists ON artist_id = artists.id WHERE artists.name = 'Drake'; --Find average energy of Drake songs
SELECT name FROM songs WHERE name LIKE '%feat%'; -- Find all songs with features

CREATE TABLE songs (
    id INTEGER,
    name TEXT,
    artist_id INTEGER,
    danceability REAL,
    energy REAL,
    key INTEGER,
    loudness REAL,
    speechiness REAL,
    valence REAL,
    tempo REAL,
    duration_ms INTEGER
);
CREATE TABLE artists (
    id INTEGER,
    name TEXT
);