def eliminar_duplicados(lista):
    conjunto = set()
    for num in lista:
        conjunto.add(num)

    cantidad_original = len(lista)
    cantidad_unicos = len(conjunto)
    duplicados = cantidad_original - cantidad_unicos

    print("Lista original:", lista)
    print("Conjunto sin duplicados:", conjunto)
    print(f"Números duplicados eliminados: {duplicados}")

eliminar_duplicados([1, 2, 2, 3, 4, 4, 4, 5])
