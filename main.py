import mysql.connector
from mysql.connector import Error

connection = None

try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Karol2208',
        database='mi_db_1'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        print("Conexion exitosa con mi_db_1")

        while True:
            print("\n--- MENU DE OPERACIONES ---")
            print("1. Consultar empleados")
            print("2. Insertar empleado")
            print("3. Actualizar salario")
            print("4. Eliminar empleado")
            print("5. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                cursor.execute(
                    "SELECT * FROM empleados LIMIT 10"
                )
                for empleado in cursor.fetchall():
                    print(empleado)

            elif opcion == "2":
                datos = (
                    input("ID del empleado: "),
                    input("Nombre completo: "),
                    input("Cargo: "),
                    input("Departamento: "),
                    input("Unidad de negocio: "),
                    input("Genero: "),
                    input("Etnia: "),
                    int(input("Edad: ")),
                    float(input("Salario anual: ")),
                    float(input("Bonificacion: "))
                )

                sql = """
                INSERT INTO empleados (
                    Employee_ID, Full_Name, Job_Title,
                    Department, Business_Unit, Gender,
                    Ethnicity, Age, Annual_Salary, Bonus
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                cursor.execute(sql, datos)
                connection.commit()
                print("Empleado agregado correctamente.")

            elif opcion == "3":
                empleado_id = input("ID del empleado: ")
                salario = float(input("Nuevo salario anual: "))

                cursor.execute(
                    "UPDATE empleados SET Annual_Salary = %s WHERE Employee_ID = %s",
                    (salario, empleado_id)
                )
                connection.commit()
                print("Empleados actualizados:", cursor.rowcount)

            elif opcion == "4":
                empleado_id = input("ID del empleado que desea eliminar: ")
                confirmacion = input("¿Esta seguro? Escriba SI para confirmar: ")

                if confirmacion == "SI":
                    cursor.execute(
                        "DELETE FROM empleados WHERE Employee_ID = %s",
                        (empleado_id,)
                    )
                    connection.commit()
                    print("Empleados eliminados:", cursor.rowcount)
                else:
                    print("Operacion cancelada.")

            elif opcion == "5":
                print("Finalizando programa.")
                break

            else:
                print("Opcion no valida.")

except Error as ex:
    print("Error en la conexion o consulta:", ex)

finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexion cerrada.")
