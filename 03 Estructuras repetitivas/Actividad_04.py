# Ejercicio 4 — “Escape Room: La Bóveda”
# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados. Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.



# VARIABLES INICIALES
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0

# NOMBRE DEL AGENTE
agente = input("Nombre del agente: ").strip()

while agente == "" or not agente.isalpha():
    agente = input("Error. Ingrese solo letras: ").strip()


# BUCLE PRINCIPAL DEL JUEGO
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print("\n🚨 El sistema se bloqueó por la alarma.")
        break

    print("\n------ ESTADO ------")
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", "ACTIVA" if alarma else "OFF")
    print("Código parcial:", codigo_parcial)

    print("\n1) Forzar cerradura (-20 energía, -2 tiempo)")
    print("2) Hackear panel (-10 energía, -3 tiempo)")
    print("3) Descansar (+15 energía, -1 tiempo)")

    opcion = input("Acción: ")

    while not opcion.isdigit() or int(opcion) not in [1,2,3]:
        opcion = input("Error. Ingrese 1, 2 o 3: ")

    opcion = int(opcion)


# OPCION 1: FORZAR 
    if opcion == 1:

        energia -= 20
        tiempo -= 2

        forzar_seguidas += 1

        # regla anti-spam
        if forzar_seguidas == 3:
            alarma = True
            print("⚠️ Forzaste demasiadas veces. La cerradura se trabó.")
            continue

        if energia < 40:
            print("⚠️ Riesgo de alarma.")
            riesgo = input("Elige número 1-3: ")

            while not riesgo.isdigit() or int(riesgo) not in [1,2,3]:
                riesgo = input("Error. Elige 1-3: ")

            if int(riesgo) == 3:
                alarma = True
                print("🚨 Se activó la alarma.")

        if not alarma:
            cerraduras_abiertas += 1
            print("🔓 Cerradura abierta.")


# OPCION 2: HACKEAR
    elif opcion == 2:

        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        print("Hackeando panel...")

        for paso in range(4):
            print("Progreso:", paso + 1, "/4")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("🔓 El hackeo desbloqueó una cerradura.")


# OPCION 3: DESCANSAR
    elif opcion == 3:

        tiempo -= 1
        forzar_seguidas = 0

        energia += 15
        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10
            print("⚠️ La alarma te estresa. Pierdes energía extra.")

        print("Descansaste y recuperaste energía.")


# RESULTADO FINAL
print("\n------ RESULTADO ------")

if cerraduras_abiertas == 3:
    print("🏆 VICTORIA. La bóveda se abrió.")

elif energia <= 0 or tiempo <= 0:
    print("💀 DERROTA. Te quedaste sin energía o tiempo.")

elif alarma and tiempo <= 3:
    print("🚨 DERROTA. El sistema bloqueó la bóveda.")