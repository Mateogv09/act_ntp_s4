def buscar_palabras_con_letra(lista_palabras, letra):
    resultado = []
    for palabra in lista_palabras:
        if letra.lower() in palabra.lower():
            resultado.append(palabra)
    return resultado


palabras = ["gato", "perro", "elefante", "jirafa", "león"]
letra = input("Ingresa una letra para buscar: ")
print("Palabras que contienen la letra:", buscar_palabras_con_letra(palabras, letra))
