def carrito_compras():
    carrito = []
    precios = {}

    while True:
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar carrito")
        print("4. Calcular total")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            producto = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            carrito.append(producto)
            precios[producto] = precio
        elif opcion == "2":
            producto = input("Producto a eliminar: ")
            if producto in carrito:
                carrito.remove(producto)
                precios.pop(producto, None)
                print(f"{producto} eliminado.")
            else:
                print("Producto no encontrado.")
        elif opcion == "3":
            if carrito:
                print("Productos en el carrito:")
                for producto in carrito:
                    print(f"- {producto}: ${precios[producto]:.2f}")
            else:
                print("El carrito está vacío.")
        elif opcion == "4":
            total = sum(precios[producto] for producto in carrito)
            print(f"Total: ${total:.2f}")
        elif opcion == "5":
            print("Saliendo del carrito...")
            break
        else:
            print("Opción inválida.")

carrito_compras()
