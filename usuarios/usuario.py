import pyodbc
import datetime
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

cursor = conexion.cursor()
#aca irian las consultas

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        #sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s);"
        #usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)
        #cursor.execute(sql % usuario)
        cursor.execute("""
            INSERT INTO users
            VALUES  (?, ?, ?, ?, ?)
        """, self.nombre, self.apellidos, self.email, self.password, fecha)

        conexion.commit()
        return [cursor.rowcount, self]

    def identificar(self):
        return self.nombre