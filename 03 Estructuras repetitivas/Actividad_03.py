# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

#OPERADOR
operador = input("Nombre del operador: ").strip()

while operador == "" or not operador.isalpha():
    operador = input("Error. Ingrese solo letras: ").strip()


#AGENDA (VACIA)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

#MENU PRINCIPAL
while True:

    print("\n1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: opción inválida.")
        continue


#RESERVAR
    if opcion == 1:

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1,2]:
            dia = input("Error. Día (1=Lunes, 2=Martes): ")

        dia = int(dia)

        nombre = input("Nombre del paciente: ").strip()

        while nombre == "" or not nombre.isalpha():
            nombre = input("Error. Solo letras: ").strip()


        if dia == 1:

            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Ese paciente ya tiene turno el lunes.")

            elif lunes1 == "":
                lunes1 = nombre

            elif lunes2 == "":
                lunes2 = nombre

            elif lunes3 == "":
                lunes3 = nombre

            elif lunes4 == "":
                lunes4 = nombre

            else:
                print("No hay turnos disponibles el lunes.")


        if dia == 2:

            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Ese paciente ya tiene turno el martes.")

            elif martes1 == "":
                martes1 = nombre

            elif martes2 == "":
                martes2 = nombre

            elif martes3 == "":
                martes3 = nombre

            else:
                print("No hay turnos disponibles el martes.")


#CANCELAR
    elif opcion == 2:

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1,2]:
            dia = input("Error. Día (1=Lunes, 2=Martes): ")

        dia = int(dia)

        nombre = input("Nombre del paciente: ").strip()

        while nombre == "" or not nombre.isalpha():
            nombre = input("Error. Solo letras: ").strip()


        if dia == 1:

            if lunes1 == nombre:
                lunes1 = ""
            elif lunes2 == nombre:
                lunes2 = ""
            elif lunes3 == nombre:
                lunes3 = ""
            elif lunes4 == nombre:
                lunes4 = ""
            else:
                print("Paciente no encontrado.")


        if dia == 2:

            if martes1 == nombre:
                martes1 = ""
            elif martes2 == nombre:
                martes2 = ""
            elif martes3 == nombre:
                martes3 = ""
            else:
                print("Paciente no encontrado.")


#VER AGENDA
    elif opcion == 3:

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1,2]:
            dia = input("Error. Día (1=Lunes, 2=Martes): ")

        dia = int(dia)

        if dia == 1:

            print("\nAgenda Lunes")

            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")


        if dia == 2:

            print("\nAgenda Martes")

            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")


#RESUMEN
    elif opcion == 4:

        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1


        libres_lunes = 4 - ocupados_lunes
        libres_martes = 3 - ocupados_martes


        print("\nResumen")

        print("Lunes - Ocupados:", ocupados_lunes, "Libres:", libres_lunes)
        print("Martes - Ocupados:", ocupados_martes, "Libres:", libres_martes)


        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")

        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")

        else:
            print("Empate de turnos entre ambos días.")


#SALIR
    elif opcion == 5:
        print("Sistema cerrado.")
        break