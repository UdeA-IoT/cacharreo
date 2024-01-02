# ¿Que puedo hacer con las bases de datos?


**Cheatsheet**: What Can I Do With A Database? [[link](https://www.codecademy.com/learn/paths/cscj-22-databases/tracks/cscj-22-working-with-databases/modules/wdcp-22-what-can-i-do-with-a-database-77f195cc-06a4-457a-9db4-6f697f303f0e/cheatsheet)]



## 1 - Queries

```sql
SELECT * FROM movies;
```

## 2 - Queries - Select

```sql
SELECT column1, column2 
FROM table_name;
```

```sql
-- 1
SELECT name, genre 
FROM movies;
-- 
SELECT name, genre, year 
FROM movies;
```

## 3 - Queries - As

```sql
-- 1
SELECT name AS 'Titles'
FROM movies;
-- 2
SELECT imdb_rating AS 'IMDb'
FROM movies;
```

## 4 - Queries - Distinct

```sql
SELECT tools 
FROM inventory;
```

Sale:

```
tools
Hammer
Nails
Nails
Nails
```

```sql
SELECT tools 
FROM inventory;
```

Sale:

```
tools
Hammer
Nails
```

Asi tenemos:

```sql
-- 1
SELECT DISTINCT genre 
FROM movies;
-- 2 
SELECT DISTINCT year
FROM movies;
```

## 5 - Queries - Where

```sql
SELECT *
FROM movies
WHERE imdb_rating > 8;
```

```sql
-- 1
SELECT * 
FROM movies 
WHERE imdb_rating < 5;
-- 2
SELECT * 
FROM movies 
WHERE year > 2014;
```

## 6 - Queries - Like I

```LIKE``` can be a useful operator when you want to compare similar values. The movies table contains two films with similar titles, 'Se7en' and 'Seven'.

```sql
-- 1
SELECT * 
FROM movies
WHERE name LIKE 'Se_en';
```

## 7 - Queries - Like II

The percentage sign ```%``` is another wildcard character that can be used with ```LIKE```.

This statement below filters the result set to only include movies with names that begin with the letter ```'A'```:

```sql
SELECT * 
FROM movies
WHERE name LIKE 'A%';
```

```LIKE``` is not case sensitive

```sql
-- 1
SELECT * 
FROM movies 
WHERE name LIKE '%man%';
-- 2
SELECT * 
FROM movies
WHERE name LIKE 'The %';
```

## 8 - Queries - Is Null

```sql
SELECT name
FROM movies 
WHERE imdb_rating IS NOT NULL;
```


```sql
-- 1
SELECT name
FROM movies 
WHERE imdb_rating IS NULL;
```

## 9 - Queries - Between

```sql
SELECT *
FROM movies
WHERE year BETWEEN 1990 AND 1999;
```

```sql
SELECT *
FROM movies
WHERE name BETWEEN 'A' AND 'J';
```


```sql
-- 1 (D, E y F)
SELECT *
FROM movies
WHERE name BETWEEN 'D' AND 'G';
-- 2 (movies that were released in the 1970’s.)
SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979;
```

* ```BETWEEN``` two numbers is inclusive of the second number.
* The numeric values (INTEGER or REAL data types) don’t need to be wrapped with single quotes, whereas TEXT values do.

## 10 - Queries - And


```sql
SELECT * 
FROM movies
WHERE year BETWEEN 1990 AND 1999
   AND genre = 'romance';
```


```sql
-- 1
SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979
  AND imdb_rating > 8;
-- 2
SELECT *
FROM movies
WHERE year < 1985
  AND genre = 'horror';
```

## 11 - Queries - Or

```sql
-- 1
SELECT *
FROM movies
WHERE year > 2014
   OR genre = 'action';
-- 2
SELECT *
FROM movies
WHERE genre = 'romance'
   OR genre = 'comedy';
```

## 12 - Queries - Order By

We can sort the results using ```ORDER BY```, either alphabetically or numerically. Sorting the results often makes the data more useful and easier to analyze.

```sql
SELECT *
FROM movies
ORDER BY name;
```

```sql
SELECT *
FROM movies
WHERE imdb_rating > 8
ORDER BY year DESC;
```

The column that we ```ORDER BY``` doesn’t even have to be one of the columns that we’re displaying.

Note: ```ORDER BY``` always goes after ```WHERE``` (if ```WHERE``` is present).

```sql
-- 1
SELECT name, year
FROM movies
ORDER BY name;
-- 2
SELECT name, year, imdb_rating
FROM movies
ORDER BY imdb_rating DESC;
```

## 13 - Queries - Limit

```LIMIT``` is a clause that lets you specify the maximum number of rows the result set will have. This saves space on our screen and makes our queries run faster.

```sql
SELECT *
FROM movies
LIMIT 10;
```

```sql
-- 1 - Top 3 movies
SELECT *
FROM movies
ORDER BY imdb_rating DESC
LIMIT 3;
```

## 14 - Queries - Case

A ```CASE``` statement allows us to create different outputs (usually in the ```SELECT``` statement). It is SQL’s way of handling if-then logic.

```sql
SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END
FROM movies;
```

In the result, you have to scroll right because the column name is very long. To shorten it, we can rename the column to 'Review' using ```AS```:

```sql
SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END AS 'Review'
FROM movies;
```

Let’s try one on your own.

Select the ```name``` column and use a ```CASE``` statement to create the second column that is:
* 'Chill' if ```genre = 'romance'```
* 'Chill' if ```genre = 'comedy'```
* 'Intense' in all other cases

Optional: Rename the whole ```CASE``` statement to ```'Mood'``` using AS.

```sql
SELECT name,
 CASE
  WHEN genre = 'romance' or genre = 'comedy' THEN 'Chill'
  ELSE 'Intense'
 END AS 'Mood'
FROM movies;
```

## 15 - Review


We just learned how to query data from a database using SQL. We also learned how to filter queries to make the information more specific and useful.

Let’s summarize:
* ```SELECT``` is the clause we use every time we want to query information from a database.
* ```AS``` renames a column or table.
* ```DISTINCT``` return unique values.
* ```WHERE``` is a popular command that lets you filter the results of the query based on conditions that you specify.
* ```LIKE``` and ```BETWEEN``` are special operators.
* ```AND``` and ```OR``` combines multiple conditions.
* ```ORDER BY``` sorts the result.
* ```LIMIT``` specifies the maximum number of rows that the query will return.
* ```CASE``` creates different outputs.

**Cheatsheet**: What Can I Do With A Database? [[link](https://www.codecademy.com/learn/paths/cscj-22-databases/tracks/cscj-22-working-with-databases/modules/wdcp-22-what-can-i-do-with-a-database-77f195cc-06a4-457a-9db4-6f697f303f0e/cheatsheet)]

