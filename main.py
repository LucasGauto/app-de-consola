from usuarios import acciones
import pyodbc
direccion_servidor = 'LAPTOP-TCBDQ8PH\SQLEXPRESS'
nombre_bd = 'app_consola'
nombre_usuario ='login1'
password = '123'
try:
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=' +
                            direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("OK! conexión exitosa")
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)

print("""
Acciones disponibles:
    - registro
    - login
""")
hazEl = acciones.Acciones()
accion = input("Que desea hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()