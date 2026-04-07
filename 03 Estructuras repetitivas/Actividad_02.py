# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.

#CREDENCIALES
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

#LOGIN (MAX 3 INTENTOS)
while intentos < 3:

    print(f"Intento {intentos + 1}/3")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.\n")
        intentos += 1

#BLOQUEO DE CUENTA
if not acceso:
    print("Cuenta bloqueada.")

#MENU SI ACCEDIO
while acceso:

    print("\n1) Estado de inscripción")
    print("2) Cambiar clave")
    print("3) Mensaje motivacional")
    print("4) Salir")

    opcion = input("Opción: ")

    #VALIDAR QUE SEA NUMERO
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion = int(opcion)

    #VALIDAR RANGO
    if opcion < 1 or opcion > 4:
        print("Error: opción fuera de rango.")
        continue

    #OPCIONES DEL MENU
    if opcion == 1:
        print("Estado: Inscripto")

    elif opcion == 2:

        nueva_clave = input("Nueva clave: ")

        if len(nueva_clave) < 6:
            print("Error: mínimo 6 caracteres.")
            continue

        confirmar = input("Confirmar clave: ")

        if nueva_clave != confirmar:
            print("Error: las claves no coinciden.")
        else:
            clave_correcta = nueva_clave
            print("Clave cambiada correctamente.")

    elif opcion == 3:
        print("¡ La práctica hace al maestro !")

    elif opcion == 4:
        print("Saliendo del sistema...")
        break