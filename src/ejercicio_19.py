def gestion_calificaciones():
    estudiantes = {}

    while True:
        print("\n--- Gestión de Calificaciones ---")
        print("1. Agregar estudiante")
        print("2. Agregar calificación")
        print("3. Mostrar promedios")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            estudiantes[nombre] = []
        elif opcion == "2":
            nombre = input("Nombre del estudiante: ")
            if nombre in estudiantes:
                nota = float(input("Nota: "))
                estudiantes[nombre].append(nota)
            else:
                print("Estudiante no encontrado.")
        elif opcion == "3":
            for nombre, notas in estudiantes.items():
                if notas:
                    promedio = sum(notas) / len(notas)
                    print(f"{nombre}: Promedio = {promedio:.2f}")
                else:
                    print(f"{nombre}: Sin calificaciones.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

gestion_calificaciones()
