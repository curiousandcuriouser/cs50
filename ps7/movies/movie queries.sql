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
SELECT title FROM movies
  JOIN stars ON movies.id = stars.movie_id
  JOIN people ON stars.person_id = people.id
  WHERE name = 'Bradley Cooper'

INTERSECT

SELECT title FROM movies
  JOIN stars ON movies.id = stars.movie_id
  JOIN people ON stars.person_id = people.id
  WHERE name = 'Jennifer Lawrence'; -- 12: Find all movies with Bradley Cooper and Jennifer Lawrence

SELECT DISTINCT(name)  
FROM people  
WHERE name IS NOT 'Kevin Bacon' AND id IN(
    SELECT person_id FROM stars WHERE movie_id IN(
        SELECT movie_id FROM stars WHERE person_id IN(
            SELECT id FROM people WHERE name IS 'Kevin Bacon'and birth = 1958)))  
ORDER BY name; -- 13: List the names of all people who starred in a movie in which Kevin Bacon (b.1958) also starred.




In 13.sql, write a SQL query to 
Your query should output a table with a single column for the name of each person.
There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
Kevin Bacon himself should not be included in the resulting list.




Movies
stars
people

1. Select name 

SELECT DISTINCT name FROM people JOIN stars ON stars.person_id = people.id 
WHERE stars.movie_id IN (
SELECT stars.movie_id 
FROM stars
WHERE people.name = 'Kevin Bacon' AND people.birth = 1958)
AND people.name != 'Kevin Bacon' ;

For stars
In the same movie
As Kevin Bacon
Born in 1958
And don't include Kevin Bacon