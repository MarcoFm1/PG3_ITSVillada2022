#Ejercicio 6
from msilib.schema import Error
import mysql.connector
def MySqlEj6():
    try:
        mydb = mysql.connector.connect(
            host = str(input("Host: ")),
            user = str(input("User:")),
            passw = str(input("Password: ")),
        )

        mydb.database = str(input("Database's name: "))

        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE " + str(input('(table name)')) + " (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)") 
        print("Query OK, 0 rows affected (0.03 sec)")
        while True:
            if(input("DELATE TABLE Y/N") == "N"):
                print("Query OK, 0 rows affected (0.01 sec)")
                break
            else:
                mycursor.execute("DROP TABLE " + str(input('use: (table name)')))
                print("Query OK, 0 rows affected (0.01 sec)")
        mydb.close()

    except ValueError:
        print("Syntaxis ValueError: " + str(ValueError))
    
    except mysql.connector.Error:
        print("Error...No found Database " + str(Error))
            
MySqlEj6()