# SQL NOTES
## high level concept
- filed
  - A field is a column in a table that is designed to maintain specific information about every record in the table.
- table
  - A database most often contains one or more tables. Each table is identified by a name (e.g. "Customers" or "Orders"). Tables contain records (rows) with data.
   
## basic command
- SELECT: extracts data from a database
  ```sql
  SELECT * FROM Customers;
  SELECT column1, column2 FROM Customers;
  SELECT COUNT(DISTINCT Country) FROM Customers;
  ```
  - * means all columns
  - data returned is stored in a result table, called the result-set.
  - SELECT DISTINCT: extracts only distinct entries
  - SELECT COUNT(DISTINCT XXX) FROM XXX;
  
- WHERE: used to filter by conditions
  ```sql
  SELECT column1, column2
  FROM Customers
  WHERE Country='Mexico';
  ```
  - operators
    - "=" eaquals "=="
    - between
    - like
    - in
    - AND, OR, NOT
    
- ORDER
  ```sql
  SELECT column1, column2, ...
  FROM table_name
  ORDER BY column1 ASC, column2, ... DESC;
  ```
- INSERT INTO
  - create a new row containing the inserted. missing values are NULL
  ```sql
  INSERT INTO table_name (column1, column2, column3, ...)
  VALUES (value1, value2, value3, ...);
  ```
- UPDATE & SET
  - 
  ```sql
  UPDATE Customers
  SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
  WHERE CustomerID = 1;
  ```
- ALTER
- DELETE FROM
- INSERT: insert new data into a database

- CREATE TABLE
- ALTER TABLE
- DROP TABLE
- CREATE INDEX
- DROP INDEX

## more highlevel commands
- use SELECT AS to create ALIAS
- EXPLICIT JOIN
  - combine rows in two or more tables
  ```sql
  SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
  FROM Orders
  INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;
  ```

