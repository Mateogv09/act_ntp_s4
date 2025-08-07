def palabras_unicas():
    palabras = set()
    repetidas = set()

    while True:
        palabra = input("Ingresa una palabra (o 'salir' para terminar): ").lower()
        if palabra == 'salir':
            break
        if palabra in palabras:
            repetidas.add(palabra)
        else:
            palabras.add(palabra)

    print(f"\nPalabras únicas: {palabras}")
    print(f"Cantidad únicas: {len(palabras)}")
    print(f"Repetidas: {repetidas}")


palabras_unicas()
