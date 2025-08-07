def sistema_temperaturas():
    temperaturas = {
        "Madrid": {"Lunes": 30, "Martes": 31, "Miércoles": 29},
        "Barcelona": {"Lunes": 28, "Martes": 30, "Miércoles": 27},
        "Valencia": {"Lunes": 32, "Martes": 33, "Miércoles": 31}
    }

    print("\n--- Temperaturas por ciudad ---")
    for ciudad, dias in temperaturas.items():
        print(f"\nCiudad: {ciudad}")
        total = 0
        for dia, temp in dias.items():
            print(f"{dia}: {temp}°C")
            total += temp
        promedio = total / len(dias)
        print(f"Promedio semanal: {promedio:.2f}°C")

    print("\n--- Promedio por día ---")
    dias_semana = ["Lunes", "Martes", "Miércoles"]
    for dia in dias_semana:
        suma = sum(temperaturas[ciudad][dia] for ciudad in temperaturas)
        promedio_dia = suma / len(temperaturas)
        print(f"{dia}: {promedio_dia:.2f}°C")

sistema_temperaturas()
