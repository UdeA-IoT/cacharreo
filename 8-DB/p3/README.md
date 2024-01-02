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

Lo anterior es equivalente a:

```sql
SELECT ROUND(imdb_rating),
   COUNT(name)
FROM movies
GROUP BY 1
ORDER BY 1;
```

```sql
-- 1
SELECT category, 
   price,
   AVG(downloads)
FROM fake_apps
GROUP BY category, price;
```

Lo anterior es equivalente a:

```sql
SELECT category, 
   price,
   AVG(downloads)
FROM fake_apps
GROUP BY 1, 2;
```

## 9 - Having

For instance, imagine that we want to see how many movies of different genres were produced each year, but we only care about years and genres with at least 10 movies.

```HAVING``` is very similar to ```WHERE```. In fact, all types of ```WHERE``` clauses you learned about thus far can be used with ```HAVING```.

We can use the following for the problem:

```sql
SELECT year,
   genre,
   COUNT(name)
FROM movies
GROUP BY 1, 2
HAVING COUNT(name) > 10;
```

* When we want to limit the results of a query based on values of the individual rows, use ```WHERE```.
* When we want to limit the results of a query based on an aggregate property, use ```HAVING```

```HAVING``` statement always comes after ```GROUP BY```, but before ```ORDER BY``` and ```LIMIT```.

```sql
-- 1
SELECT price, 
   ROUND(AVG(downloads)),
   COUNT(*)
FROM fake_apps
GROUP BY price
HAVING COUNT(price) > 10;
```

## 10 - Review

You just learned how to use aggregate functions to perform calculations on your data. What can we generalize so far?

* ```COUNT()```: count the number of rows
* ```SUM()```: the sum of the values in a column
* ```MAX()/MIN()```: the largest/smallest value
* ```AVG()```: the average of the values in a column
* ```ROUND()```: round the values in the column

Aggregate functions combine multiple rows together to form a single value of more meaningful information.

* ```GROUP BY``` is a clause used with aggregate functions to combine data from one or more columns.
* ```HAVING``` limit the results of a query based on an aggregate property.

## Trends in Startups

Howdy! It’s your first day as a [TechCrunch](https://techcrunch.com/) reporter. Your first task is to write an article on the rising trends in the startup world.

To get you started with your research, your boss emailed you a project.sqlite file that contains a table called ```startups```. It is a portfolio of some of the biggest names in the industry.

Write queries with aggregate functions to retrieve some interesting insights about these companies.

What are you waiting for? Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click "Get Unstuck" to see a project walkthrough video.

### Tasks - Write the following queries:

1. Getting started, take a look at the startups table:

   ```sql
   SELECT *
   FROM startups;
   ```
   
   How many columns are there?

2. Calculate the total number of companies in the table.

3. We want to know the total value of all companies in this table.
   
   Calculate this by getting the ```SUM()``` of the ```valuation``` column.

4. What is the highest amount raised by a startup?
   
   Return the maximum amount of money ```raised```.

5. Edit the query so that it returns the maximum amount of money ```raised```, during 'Seed' stage.
   
6. In what year was the oldest company on the list founded?

### Let's find out the valuations among different sectors:


7. Return the average ```valuation```.

8. Return the average ```valuation```, in each ```category```.

9. Return the average ```valuation```, in each ```category```.

   Round the averages to two decimal places.

10. Return the average ```valuation```, in each ```category```.

    Round the averages to two decimal places.

    Lastly, order the list from highest averages to lowest.

### What are the most competitive markets?

11. First, return the name of each ```category``` with the total number of companies that belong to it.

12. Next, filter the result to only include categories that have more than three companies in them.

    What are the most competitive markets?

### Let's see if there's a difference in startups sizes among different locations:

13. What is the average size of a startup in each ```location```?

14. What is the average size of a startup in each ```location```, with average sizes above 500?