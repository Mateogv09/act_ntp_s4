def agenda_telefonica():
    agenda = {}

    while True:
        print("\n--- Agenda Telefónica ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            agenda[nombre] = telefono
        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            if nombre in agenda:
                print(f"{nombre}: {agenda[nombre]}")
            else:
                print("Contacto no encontrado.")
        elif opcion == "3":
            print("Contactos en la agenda:")
            for nombre, telefono in agenda.items():
                print(f"- {nombre}: {telefono}")
        elif opcion == "4":
            nombre = input("Nombre a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")
        elif opcion == "5":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción inválida.")

agenda_telefonica()
