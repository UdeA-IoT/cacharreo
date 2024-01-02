# AGGREGATE FUNCTIONS

**Cheatsheet**: Aggregate Functions [[link](https://www.codecademy.com/learn/paths/cscj-22-databases/tracks/cscj-22-working-with-databases/modules/wdcp-22-aggregate-functions-737d40d0-3fcf-46fe-945e-d8cb26bcc7eb/cheatsheet)]

## 1 - Introduction

Calculations performed on multiple rows of a table are called **aggregates**.

Here is a quick preview of some important aggregates:
* ```COUNT()```: count the number of rows
* ```SUM()```: the sum of the values in a column
* ```MAX()/MIN()```: the largest/smallest value
* ```AVG()```: the average of the values in a column
* ```ROUND()```: round the values in the column

**Tabla**:

![1](1-aggregado.png)

**Esquema**:

![2](2-aggregado.png)

## 2 - Count


The fastest way to calculate how many rows are in a table is to use the ```COUNT()``` function.

```COUNT()``` is a function that takes the name of a column as an argument and counts the number of non-empty values in that column.

```sql
SELECT COUNT(*)
FROM table_name;
```

```sql
-- 1 
SELECT COUNT(*) 
FROM fake_apps;
-- 2 (Aplicaciones gratuitas)
SELECT COUNT(*) 
FROM fake_apps
WHERE price = 0;
```

## 3 - Sum

SQL makes it easy to add all values in a particular column using ```SUM()```.

```SUM()``` is a function that takes the name of a column as an argument and returns the sum of all the values in that column.

```sql
-- 1
SELECT SUM(downloads)
FROM fake_apps;
```

## 4 - Max / Min

```sql
SELECT MAX(downloads)
FROM fake_apps;
```

```sql
-- 1
SELECT MIN(downloads)
FROM fake_apps;
-- 2
SELECT MAX(price)
FROM fake_apps;
```

## 5 - Average

SQL uses the ```AVG()``` function to quickly calculate the average value of a particular column.

```sql
SELECT AVG(downloads)
FROM fake_apps;
```

```sql
-- 1
SELECT AVG(downloads)
FROM fake_apps;
-- 2
SELECT AVG(price)
FROM fake_apps;
```

## 6 - Round

By default, SQL tries to be as precise as possible without rounding. We can make the result table easier to read using the ```ROUND()``` function.

```ROUND()``` function takes two arguments inside the parenthesis:
* a column name
* an integer

```sql
SELECT ROUND(price, 0)
FROM fake_apps;
```

```sql
-- 1
SELECT ROUND(price, 0)
FROM fake_apps;
-- 2
SELECT ROUND(AVG(price),2)
FROM fake_apps;
```

## 7 - Group By I

```sql
SELECT AVG(imdb_rating)
FROM movies
WHERE year = 1999;

SELECT AVG(imdb_rating)
FROM movies
WHERE year = 2000;

SELECT AVG(imdb_rating)
FROM movies
WHERE year = 2001;
```

We can use ```GROUP BY``` to do this in a single step:

```sql
SELECT year,
   AVG(imdb_rating)
FROM movies
GROUP BY year
ORDER BY year;
```

```GROUP BY``` is a clause in SQL that is used with aggregate functions. It is used in collaboration with the ```SELECT``` statement to arrange identical data into *groups*.

```sql
-- 1
SELECT price, COUNT(*) 
FROM fake_apps
GROUP BY price;
-- 2: count the total number of apps that have been downloaded more than 20,000 times, at each price.
SELECT price, COUNT(*) 
FROM fake_apps
WHERE downloads > 20000
GROUP BY price;
-- 3
SELECT category, SUM(downloads)
FROM fake_apps
GROUP BY category;
```

## 8 - Group By II

Sometimes, we want to ```GROUP BY``` a calculation done on a column.

For instance, we might want to know how many movies have IMDb ratings that round to 1, 2, 3, 4, 5. We could do this using the following syntax:

```sql
SELECT ROUND(imdb_rating),
   COUNT(name)
FROM movies
GROUP BY ROUND(imdb_rating)
ORDER BY ROUND(imdb_rating);
```