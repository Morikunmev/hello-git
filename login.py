print("¡Bienvenido al sistema de autenticación!")

usuario = input("Por favor, ingrese su nombre de usuario: ")

if usuario == "admin":
    contrasena = input("Ingrese su contraseña: ")
    if contrasena == "password":
        print("¡Acceso concedido! Bienvenido, Administrador.")
    else:
        print("Error: Contraseña incorrecta. Inténtelo de nuevo.")
elif usuario == "usuario":
    contrasena = input("Ingrese su contraseña: ")
    if contrasena == "userpass":
        print("¡Acceso concedido! Bienvenido, Usuario.")
    else:
        print("Error: Contraseña incorrecta. Inténtelo de nuevo.")
else:
    print("Error: Usuario no encontrado. Verifique su nombre de usuario.")
