# Explorando sobre bases de datos

[output.txt](output.txt)

```
1|Justin Bieber|29
2|Beyonce Knowles|42
3|Jeremy Lin|35
4|Taylor Swift|33
```

## 1 - Introduction to SQL

```sql
SELECT * FROM celebs;
```

## 2 - Relational Databases

```sql
SELECT * FROM celebs;
```

## 3 - Statements

```sql
CREATE TABLE table_name (
   column_1 data_type, 
   column_2 data_type, 
   column_3 data_type
);
```

## 4 - Create


```sql
--1. Select all
SELECT * FROM celebs;

--2. Create celebs table
CREATE TABLE celebs (
   id INTEGER, 
   name TEXT, 
   age INTEGER
); 
```

## 4 - Insert

```sql
-- 1. Add row to the table
INSERT INTO celebs (id, name, age) 
VALUES (1, 'Justin Bieber', 29);

-- 2. Add three more celebrities to the table
INSERT INTO celebs (id, name, age) 
VALUES (2, 'Beyonce Knowles', 42); 

INSERT INTO celebs (id, name, age) 
VALUES (3, 'Jeremy Lin', 35); 

INSERT INTO celebs (id, name, age) 
VALUES (4, 'Taylor Swift', 33); 
```

## 6 - Select

```sql
SELECT name FROM celebs;
```


```sql
SELECT * FROM celebs;
```

```sql
-- 1. select column name 
SELECT name FROM celebs;
-- 2. select all columns
SELECT * FROM celebs; 
```

## 7 - Alter



**Cheatsheet**: [Working With Your First Database](https://www.codecademy.com/learn/paths/cscj-22-databases/tracks/cscj-22-database-basics/modules/wdcp-22-working-with-a-database-bed4c6cd-c2f2-40c1-a505-150eea4f15e9/cheatsheet)

## Referencias

1. https://www.codecademy.com/article/what-is-rdbms-sql
2. https://www.codecademy.com/resources/docs/general/database?page_ref=catalog
3. https://www.codecademy.com/resources/docs/sql/about-sql
4. https://www.codecademy.com/article/sql-commands
5. https://www.codecademy.com/resources/docs/general/relational-database?page_ref=catalog
6. https://www.codecademy.com/resources/docs/sql/data-types?page_ref=catalog
7. https://www.codecademy.com/learn/paths/cscj-22-databases/tracks/cscj-22-database-basics/modules/wdcp-22-working-with-a-database-bed4c6cd-c2f2-40c1-a505-150eea4f15e9/cheatsheet

