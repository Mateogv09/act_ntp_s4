def contador_palabras(frase):
    frase = frase.lower()
    palabras = frase.split()
    contador = {}

    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1

    ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    print("Frecuencia de palabras:")
    for palabra, frecuencia in ordenadas:
        print(f"{palabra}: {frecuencia}")


contador_palabras("Hola mundo mateo código mateo mateo código")
