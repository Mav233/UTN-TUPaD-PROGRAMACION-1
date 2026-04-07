# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"


print("--- BIENVENIDO A LA ARENA ---")

# NOMBRE DEL JUGADOR
nombre = input("Nombre del Gladiador: ").strip()

while nombre == "" or not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").strip()


# ESTADISTICAS INICIALES
vida_jugador = 100
vida_enemigo = 100
pociones = 3

danio_ataque_pesado = 15
danio_enemigo = 12

turno_jugador = True

print("\n=== INICIO DEL COMBATE ===")


# CICLO DE COMBATE
while vida_jugador > 0 and vida_enemigo > 0:

    print("\n=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    if turno_jugador:

        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        # VALIDACION DEL MENU
        while not opcion.isdigit() or int(opcion) not in [1,2,3]:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        # ATAQUE PESADO
        if opcion == 1:

            danio_final = danio_ataque_pesado

            if vida_enemigo < 20:
                danio_final = danio_ataque_pesado * 1.5
                print("¡Golpe Crítico!")

            vida_enemigo -= int(danio_final)

            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")


        # RAFAGA VELOZ
        elif opcion == 2:

            print(">> ¡Inicias una ráfaga de golpes!")

            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")


        # CURAR
        elif opcion == 3:

            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print(">> Usaste una poción y recuperaste 30 de vida")
            else:
                print("¡No quedan pociones!")


        turno_jugador = False


    # TURNO DEL ENEMIGO
    else:

        if vida_enemigo > 0:
            vida_jugador -= danio_enemigo
            print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

        turno_jugador = True


# FIN DEL JUEGO
print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")