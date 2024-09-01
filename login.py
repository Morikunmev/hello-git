print("Esto es un login")

usuario = input("Ingrese su nombre de usuario: ")

if usuario == "admin":
    contrasena = input("Ingrese su contraseña: ")
    if contrasena == "password":
        print("Bienvenido administrador")
    else:
        print("Contraseña incorrecta")
        