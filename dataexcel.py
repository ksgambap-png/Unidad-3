import pandas as pd
from mysql.connector import Error
import mysql.connector
df = pd.read_excel('data1.xlsx',sheet_name='Data')
df = df.drop(columns=['Country', 'City'])
filas = []
for index, row in df.iterrows():
	filas.append(tuple(row.tolist()))

#print(filas[3])
connection = None
try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Karol2208',
        db='mi_db_1'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO empleados(
        	Employee_ID,
        	Full_Name, 
        	Job_Title,
         	Department, 
         	Business_Unit, 
         	Gender, 
         	Ethnicity,
         	Age,
         	Annual_Salary,
         	Bonus
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", filas)
        if (len(filas) == cursor.rowcount):
            connection.commit()
            print("{} Filas insertadas.".format(len(filas)))
        else:
            connection.rollback()
except Error as ex:
    print("Error en la conexion: {}".format(ex))
finally:
    if connection is not None and connection.is_connected():
        connection.close()
        print("Conexion cerrada.")


