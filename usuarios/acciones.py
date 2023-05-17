import usuarios.usuario as modelo

class Acciones:
    
    def registro(self):
        print("Ok. Vamos a registrarte en el sistema...")
        
        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Ingresa tu email: ")
        password = input("Ingresa una contraseña: ")
        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente.")
        
    def login(self):
        print("Ok. Identificate en el sistema...")
        email = input("Ingresa tu email: ")
        password = input("Ingresa una contraseña: ")