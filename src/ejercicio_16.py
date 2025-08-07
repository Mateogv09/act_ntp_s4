def inventario_productos():
    inventario = {}

    while True:
        opcion = input(
            "\n1.Agregar  2.Actualizar  3.Eliminar  4.Mostrar  5.Salir\nElige opción: ")

        if opcion == "1":
            p = input("Producto: ")
            c = int(input("Cantidad: "))
            inventario[p] = c

        elif opcion == "2":
            p = input("Producto a actualizar: ")
            if p in inventario:
                inventario[p] = int(input("Nueva cantidad: "))
            else:
                print("No existe.")

        elif opcion == "3":
            p = input("Producto a eliminar: ")
            inventario.pop(p, None)

        elif opcion == "4":
            print("Inventario:", inventario)

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

inventario_productos()