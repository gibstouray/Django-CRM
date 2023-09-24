import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	port = 3306,
	user = 'gibril',
	passwd = 'My@SirehDucsft42'


	)

# prepare a cursor object

cursorObject = dataBase.cursor()


# create a database

cursorObject.execute("CREATE DATABASE softcom")

print("All Done!!")

