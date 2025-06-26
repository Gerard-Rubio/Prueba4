#Ejercicio
datos={}

while True:
     print("\n******MENÚ DE INGRESO DE USUARIOS******")
     print("1)Ingresar usuario")
     print("2)Usuarios registrados")
     print("3)Eliminar usuario")
     print("4)Salir")
     opción=input(("Ingrese una opción (1-4): "))

     if opción=="1":
        usuario=input("Ingrese su usuario: ")
        if usuario in datos:
          print("Favor de ingresar datos de usuario no existente")
        else:
           nombre=input(("Ingrese su nombre y apellido: "))
           sexo=input(("Ingrese sexo del usuario (F o M): "))
           permitidos="f,m"
        if sexo in permitidos:
          contraseña=input(("Ingrese una contraseña: "))
          if len (contraseña)>8:
             print("La contraseña debe tener como máximo y mínimo 8 caracteres")
          datos[usuario]={"Usuario": nombre, "Sexo": sexo, "Contraseña": contraseña}
          print("Datos registrados")
        else:
           print("Ingrese un sexo valido")
     elif opción=="2":
        print("\nLista de usuarios registrados")
        if not datos:
           print("No hay usuarios registrados aún")
        else: 
         for usuario, dato in datos.items():
            print(f"Usuario: {usuario}")
            print(f"    Nombre: {dato['nombre']}")
            print(f"    Sexo: {dato['sexo']}")
            print(f"    Contraseña: {dato['contraseña']}")
     elif opción=="3":
        usuario=input(("Ingrese el usuario al cual quiere eliminar: "))
        if usuario in datos:
           del datos[usuario]
           print("Usuario Eliminado....")
        else:
           print("Usuario no existe")
     elif opción=="4":
        print("Programa terminado....")
        break
     else:
        print("Ingrese una opción valida")