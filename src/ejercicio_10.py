def suma_tuplas(tupla1, tupla2):
    if len(tupla1) != len(tupla2):
        return "Error: Las tuplas deben tener la misma longitud."
    
    resultado = tuple(tupla1[i] + tupla2[i] for i in range(len(tupla1)))
    return resultado

print("Suma:", suma_tuplas((1, 2, 3), (4, 5, 6)))  
