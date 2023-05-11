from usuarios import acciones

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