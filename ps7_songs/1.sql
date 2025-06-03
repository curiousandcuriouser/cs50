sqlite3 songs.db
.headers on
.mode table
SELECT name FROM songs; -- Makes one column with all the song names
SELECT name FROM songs ORDER BY tempo DESC; -- List all song names ordered in descending tempo
