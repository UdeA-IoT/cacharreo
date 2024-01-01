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

```sql
ALTER TABLE celebs 
ADD COLUMN twitter_handle TEXT; 

SELECT * FROM celebs; 
```

## 8 - Update

```sql
UPDATE celebs 
SET twitter_handle = '@taylorswift13' 
WHERE id = 4; 

SELECT * FROM celebs;
```

## 9 - Delete

```sql
DELETE FROM celebs 
WHERE twitter_handle IS NULL;

SELECT * FROM celebs; 
```

## 10 - Constraints


```sql
CREATE TABLE celebs (
   id INTEGER PRIMARY KEY, 
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);
```


```sql
CREATE TABLE celebs (
   id INTEGER PRIMARY KEY, 
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);
```

## 11 - Review

We’ve learned six commands commonly used to manage data stored in a relational database and how to set constraints on such data. What can we generalize so far?

SQL is a programming language designed to manipulate and manage data stored in relational databases.
* A *relational database* is a database that organizes information into one or more tables.
* A *table* is a collection of data organized into rows and columns.

A statement is a string of characters that the database recognizes as a valid command.
* ```CREATE TABLE``` creates a new table.
* ```INSERT INTO``` adds a new row to a table.
* ```SELECT``` queries data from a table.
* ```ALTER TABLE``` changes an existing table.
* ```UPDATE``` edits a row in a table.
* ```DELETE FROM``` deletes rows from a table.

Constraints add information about how a column can be used.

## Create a Table

In this project, you will create your own friends table and add/delete data from it!

The instructions provided are a general guideline. Feel free to add more columns, insert more data, and create more tables.

After completing the instructions for each Task below, click the “Save” button to check your progress. If nothing populates in the “Query Results” tab to the right, double-check your work for syntax errors.

If you get stuck during this project or would like to see an experienced developer work through it, click Get Unstuck to see a walkthrough video.

### Tasks

1. Create a table named ```friends``` with three columns:
   * ```id``` that stores ```INTEGER```
   * ```name``` that stores ```TEXT```
   * ```birthday``` that stores ```DATE```

2. Beneath your current code, add Ororo Munroe to ```friends```.

   Her birthday is May 30th, 1940.

3. Let’s make sure that Ororo has been added to the database:
   
   ```sql
   SELECT * 
   FROM friends;
   ```

   Check for two things:
   * Is friends table created?
   * Is Ororo Munroe added to it?

4. Let’s move on!

   Add two of your friends to the table.

   Insert an ```id```, ```name```, and ```birthday``` for each of them.

5. Ororo Munroe just realized that she can control the weather and decided to change her name. Her new name is “Storm”.

   Update her record in ```friends```.

6. Add a new column named email.

7. Update the email address for everyone in your table.

   Storm’s email is ```storm@codecademy.com```.

8. Wait, Storm is fictional...

   Remove her from ```friends```.

9. Great job! Let’s take a look at the result one last time:

   ```sql
   SELECT * 
   FROM friends;
   ```

**Solucion**: [link](https://gist.github.com/codecademydev/282f6c7d7cd7be4fadabe4415a2e0df6)

```sql
-- 1
CREATE TABLE friends (
   id INTEGER, 
   name TEXT,
   birthday DATE
);

-- 2
INSERT INTO friends (id, name, birthday) 
VALUES (1, 'Ororo Munroe', '1940-05-30');

-- 3
SELECT * 
FROM friends;

-- 4
INSERT INTO friends (id, name, birthday) 
VALUES (2, 'James Logan', '1930-03-04');
INSERT INTO friends (id, name, birthday) 
VALUES (3, 'Charles Xavier', '1920-12-12');

-- 5
UPDATE friends
SET name = 'Storm'
WHERE id = 1;

-- 6
ALTER TABLE friends
ADD email TEXT;

-- 7
UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'logan@codecademy.com'
WHERE id = 2;

UPDATE friends
SET email = 'xavier@codecademy.com'
WHERE id = 3;

-- 8
DELETE FROM friends
WHERE id = 1;

-- 9
SELECT * 
FROM friends;
```



**Cheatsheet**: [Working With Your First Database](https://www.codecademy.com/learn/paths/cscj-22-databases/tracks/cscj-22-database-basics/modules/wdcp-22-working-with-a-database-bed4c6cd-c2f2-40c1-a505-150eea4f15e9/cheatsheet)

## Referencias

1. https://www.codecademy.com/article/what-is-rdbms-sql
2. https://www.codecademy.com/resources/docs/general/database?page_ref=catalog
3. https://www.codecademy.com/resources/docs/sql/about-sql
4. https://www.codecademy.com/article/sql-commands
5. https://www.codecademy.com/resources/docs/general/relational-database?page_ref=catalog
6. https://www.codecademy.com/resources/docs/sql/data-types?page_ref=catalog
7. https://www.codecademy.com/learn/paths/cscj-22-databases/tracks/cscj-22-database-basics/modules/wdcp-22-working-with-a-database-bed4c6cd-c2f2-40c1-a505-150eea4f15e9/cheatsheet
8. https://www.codecademy.com/resources/docs/sql/constraints?page_ref=catalog

