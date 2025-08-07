def operaciones_conjuntos(lista1, lista2):
    conjunto1 = set()
    conjunto2 = set()

    for elem in lista1:
        conjunto1.add(elem)
    for elem in lista2:
        conjunto2.add(elem)

    print("Conjunto 1:", conjunto1)
    print("Conjunto 2:", conjunto2)
    print("Unión:", conjunto1 | conjunto2)
    print("Intersección:", conjunto1 & conjunto2)
    print("Diferencia (1 - 2):", conjunto1 - conjunto2)
    print("Diferencia Simétrica:", conjunto1 ^ conjunto2)

operaciones_conjuntos([1, 2, 3, 4], [3, 4, 5, 6])
