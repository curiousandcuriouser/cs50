sqlite3
.header on
.mode table
SELECT title FROM movies WHERE year = 2008; -- 1: Find all movies made in 2008
SELECT birth FROM people WHERE name = 'Emma Stone'; -- 2: Find Emma Stone's YOB
SELECT title FROM movies WHERE year >= 2018 ORDER BY title ASC; -- 3: Find all movies made on or after 2018 ordered alphabetically
SELECT COUNT(rating) FROM ratings WHERE rating = 10.0; -- 4: Count all movies with rating 10
SELECT title, year FROM movies WHERE title LIKE 'Harry Potter%' ORDER BY year ASC; -- 5: List all Harry Potter Movies chronologically
SELECT AVG(rating) FROM ratings JOIN movies ON ratings.movie_id = movies.id WHERE year = 2012; -- Find average rating for all movies released in 2012 
SELECT title, rating FROM movies JOIN ratings ON ratings.movie_id = movies.id WHERE year = 2010 ORDER BY rating DESC, title ASC; -- 7: Sort all 2010 movies by rating alphabetically
SELECT name FROM people
  JOIN stars ON stars.person_id = people.id
  JOIN movies ON movies.id = stars.movie_id
  WHERE stars.movie_id = (SELECT id FROM movies WHERE movies.title = 'Toy Story'); -- 8: List the names of all people who starred in Toy Story.
SELECT name, birth FROM people
  JOIN stars ON stars.person_id = people.id
  JOIN movies ON movies.id = stars.movie_id
  WHERE movies.year = 2004
  ORDER BY people.birth; --9: List names of people in a 2004 movie by birth year.
SELECT name FROM people
  JOIN directors ON directors.person_id = people.id
  JOIN movies ON movies.id = directors.movie_id
  JOIN ratings ON ratings.movie_id = movies.id
  WHERE rating >= 9.0; -- List names of directors with a 9.0 movie rating
SELECT title FROM movies
  JOIN ratings ON ratings.movie_id = movies.id
  JOIN stars ON stars.movie_id = movies.id
  JOIN people ON people.id = stars.person_id
  WHERE stars.person_id = (SELECT id FROM people WHERE name = 'Chadwick Boseman')
  ORDER BY rating DESC
  LIMIT 5; -- 11: List 5 best-rated films with Chadwick Boseman

In 12.sql, write a SQL query to list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred.
Your query should output a table with a single column for the title of each movie.
You may assume that there is only one person in the database with the name Bradley Cooper.
You may assume that there is only one person in the database with the name Jennifer Lawrence.
In 13.sql, write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
Your query should output a table with a single column for the name of each person.
There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
Kevin Bacon himself should not be included in the resulting list.