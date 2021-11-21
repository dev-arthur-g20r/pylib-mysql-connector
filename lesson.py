import mysql.connector

# GROUP: Set up parameters to pass for database connection
databaseHost = "localhost"
databaseUser = "root"
databasePassword = ""
database = "db_todolist"

databaseObject = mysql.connector.connect(
	host = databaseHost,
	user = databaseUser,
	password = databasePassword,
	database = database
)

dataCursor = databaseObject.cursor()

# GROUP: Fetch data from a table in the database
sqlStatement = "SELECT * FROM tbl_tasks"
dataCursor.execute(sqlStatement)
dataResult = dataCursor.fetchall()
print(dataResult)

# GROUP: Set up insert query to reuse
sqlStatement = "INSERT INTO tbl_tasks(fld_task) VALUES(%s)"

# GROUP: Insert 1 row to table. Pass the tuple then use `execute`.
data = ("Attend Google Meet Webinar",)
dataCursor.execute(sqlStatement,data)
databaseObject.commit()
print(f"{dataCursor.rowcount} data inserted.")

# GROUP: Insert multiple rows of data. Pass an array of tuples then use `executemany`.
data = [
	("Listen to BTS",),
	("Watch Arcane",)
]
dataCursor.executemany(sqlStatement, data)
databaseObject.commit()
print(f"{dataCursor.rowcount} data inserted.")

# GROUP: Delete row from a table
sqlStatement = "DELETE FROM tbl_tasks WHERE fld_task = %s"
data = ("Play Chess",)
dataCursor.execute(sqlStatement, data)
databaseObject.commit()
print(f"{dataCursor.rowcount} data deleted.")

# GROUP: Update multiple rows from a table
sqlStatement = "UPDATE tbl_tasks SET fld_task = %s WHERE fld_task = %s"
data = [
	("Pray", "Pray to God"),
	("Wild Rift", "Play Wild Rift")
]
dataCursor.executemany(sqlStatement, data)
databaseObject.commit()
print(f"{dataCursor.rowcount} data updated.")

