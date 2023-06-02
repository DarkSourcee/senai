import mysql.connector
 
# Conexão com o banco de dados MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="teste"
)
