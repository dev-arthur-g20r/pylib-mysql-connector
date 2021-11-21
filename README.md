
# MySQL Connector Guide
This is a documentation explaining the basics of MySQL Connector created by Arthur Tristan M. Ramos to be presented in the 2021 Mini Workshop Series: Into Coding: Introduction to Python Libraries.

## MySQL Connector
MySQL Connector is a driver in Python for us to enable our Python program to connect to a MySQL database.

## Import MySQL Connector
We need to use import *mysql.connector* to use the codes involved in it.
```
import mysql.connector
```

## Tuples
Tuples are an ordered and immutable indexed collection of items of any data type enclosed in a **()**. We mostly use this class data type to represent the data we fetch, insert, update and delete.

```
# 1 item (required to have comma (,) after the item)
# ("Pizza",)

# Multiple Items
# ("Pizza", "Cake", "Pancakes")
```

## Connect to a MySQL Database
To connect to a MySQL database, we need to provide these 4 key arguments:

 - *host* - Domain
 - *user* - Username of the database
 - *password*
 - *database* - Set of tables that store data

```
databaseObject = mysql.connector.connect(  
	host="localhost",  
	user="root",  
	password="",  
	database="db_todolist"  
)
```

## Cursor
The cursor is a reusable object responsible for executing SQL queries and fetching data from the MySQL database.

```
dataCursor = databaseObject.cursor()
```

## Execute SQL Statement
We execute the SQL statement which is a *string* using the cursor.

## Query Fetching Data from the Table
We use **SELECT FROM** clause to fetch data from the table in the database.

```
# Fetch all lessons
dataCursor.execute("SELECT * FROM tbl_todolist")
```

## Fetch All Data

 - It displays all data in an *array of tuples* .
  - It displays *None* when there are no data.

```
dataResult = dataCursor.fetchall()
print(dataResult)

# OUTPUT (Display fld_id and fld_tasks)
# [(16, 'Eat'), (19, 'Sleep'), (20, 'Pray')]
```
In this example, it has displayed an array containing the ID of the task which is index 0 of each tuple and the task which is index 1 of each tuple.

## Fetch One Data
It displays a *tuple* of the first data (index 0) of the array of fetched data. It will display *None* when there is no data in it.

```
dataResult = dataCursor.fetchone()
print(dataResult)

# OUTPUT
# (16, 'Eat')
```

## Insert 1 Row
- We use **INSERT INTO** clause to insert data to the table in the database.
- The *execute()* method also has a 2nd parameter wherein you store the *tuple* containing the data.
- The *%s* is a placeholder to escape string referring to each item in a tuple.
- We need to call the *database* object's (databaseObject in the example)  *commit()* for the data to actually be updated in the table.

```
sqlStatement = "INSERT INTO tbl_tasks(fld_task) VALUES (%s)";
data = ("Sleep",)

dataCursor.execute(sqlStatement, data)

databaseObject.commit()

print(f"{dataCursor.rowcount} data inserted.")

# OUTPUT
# 1 data inserted.

dataCursor.execute("SELECT * FROM tbl_todolist")
dataResult = dataCursor.fetchall()
print(dataResult)

# OUTPUT
# [(16, 'Eat'), (20, 'Pray'), (24, 'Sleep')]
```
In this example, **rowcount** from the cursor is a property that displays *number of rows inserted*.

## Delete 1 Row
We use **DELETE FROM** clause to delete data from the table in the database.

```
sqlStatement = "DELETE FROM tbl_tasks WHERE fld_task = %s";
data = ("Sleep",)
dataResult.execute(sqlStatement, data)

databaseObject.commit()

print(f"{dataCursor.rowcount} data removed.")

dataCursor.execute("SELECT * FROM tbl_todolist")
dataResult = dataCursor.fetchall()
print(dataResult)

# OUTPUT
# [(16, 'Eat'), (20, 'Pray')]
```

## Insert More than 1 Data
- We use *executemany()* wherein we pass *array of tuples* containing the data as the 2nd parameter. It loops to all tuples in the array.

```
sqlStatement = "INSERT INTO tbl_tasks(fld_task) VALUES (%s)";
data = [
	("Code",),
	("Play",)
]

dataCursor.executemany(sqlStatement, data)

databaseObject.commit()

print(f"{dataCursor.rowcount} data inserted.")

# OUTPUT
# 2 data inserted.

dataCursor.execute("SELECT * FROM tbl_todolist")
dataResult = dataCursor.fetchall()
print(dataResult)

# OUTPUT
# [(16, 'Eat'), (20, 'Pray'), (24, 'Sleep'), (25, 'Code'), (26, 'Play')]
```

## Update Data
- We use the **UPDATE SET** clause to update specific columns in a specific row in a table.
- If we have multiple *%s* placeholders, the escaping is *in order* with the order of the tuple.
- **executemany()** loops to every tuple executing technically the *execute()* per tuple in the looped array.

```
sqlStatement = "UPDATE tbl_tasks SET fld_task = %s WHERE fld_task = %s";
data = [
	("Go to Sleep","Sleep"),
	("Pray to God", "Pray")
]

dataCursor.executemany(sqlStatement, data)

databaseObject.commit()

print(f"{dataCursor.rowcount} data updated.")

# OUTPUT
# 2 data updated.

dataCursor.execute("SELECT * FROM tbl_todolist")
dataResult = dataCursor.fetchall()
print(dataResult)

# OUTPUT
# [(16, 'Eat'), (20, 'Pray to God'), (24, 'Go to Sleep'), (25, 'Code'), (26, 'Play')]
```

## Todo List
![Todo List for the Activity](https://photos.app.goo.gl/MxD4jxpCXMhsUbwSA)


> Written with [StackEdit](https://stackedit.io/).
