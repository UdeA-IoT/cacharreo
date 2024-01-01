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

## 4 - Queries - Where

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

## 5 - Queries - Like I

```LIKE``` can be a useful operator when you want to compare similar values. The movies table contains two films with similar titles, 'Se7en' and 'Seven'.

```sql
-- 1
SELECT * 
FROM movies
WHERE name LIKE 'Se_en';
```

## 6 - Queries - Like II

The percentage sign ```%``` is another wildcard character that can be used with ```LIKE```.

This statement below filters the result set to only include movies with names that begin with the letter ```'A'```:

```sql
SELECT * 
FROM movies
WHERE name LIKE 'A%';
```

```sql
-- 1
SELECT * 
FROM movies 
WHERE name LIKE '%man%';
```


```sql

```


```sql

```

```sql

```

```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```