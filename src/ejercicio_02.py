def sistema_calificaciones():
    calificaciones = []
    while True:
        entrada = input("Ingresa una calificación o escribe 'fin' para terminar: ")
        if entrada.lower() == 'fin':
            break
        try:
            calificacion = float(entrada)
            calificaciones.append(calificacion)
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número o 'fin'.")
    
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print("Promedio:", promedio)
        print("Nota más alta:", max(calificaciones))
        print("Nota más baja:", min(calificaciones))
    else:
        print("No se ingresaron calificaciones.")

print (sistema_calificaciones())
