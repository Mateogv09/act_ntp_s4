def generar_conjuntos():
    pares = set()
    multiplos3 = set()

    for i in range(2, 21):
        if i % 2 == 0:
            pares.add(i)
    for i in range(3, 31):
        if i % 3 == 0:
            multiplos3.add(i)

    print("Pares:", pares)
    print("Múltiplos de 3:", multiplos3)
    print("Unión:", pares | multiplos3)
    print("Intersección:", pares & multiplos3)
    print("Diferencia (pares - múltiplos3):", pares - multiplos3)
    print("Diferencia Simétrica:", pares ^ multiplos3)

generar_conjuntos()
