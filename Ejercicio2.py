stock_disponible = 120
capaxidad_maxima = 120
prestamos_activos = 0

print("¡Bienvenido al sistema de gestion de prestamos de la Biblioteca Central!")
while True:
    print("\n===MENU PRINCIPAL===")
    print("1. Libros disponibles")
    print("2. Realizar prestamo")
    print("3. Devolver prestamo")
    print("4. Historial de prestamos")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            break 
        except:
            print("¡Opcion invalida! Por favor, ingrese un numero entero.")
        
    if opcion == 1:
        print(f"\n[info] Cantidad actual de libros disponibles: {stock_disponible}")
        
    elif opcion == 2:
        print(f"\n--- Realizar prestamo (Disponibles: {stock_disponible}) ---")
        if stock_disponible == 0:
            print("Lo sentimos, no hay libros disponibles en este momento para prestar.")
            continue
            
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de libros a prestar: "))
                if cantidad <= 0:
                    print("¡Error! La cantidad a prestar debe ser mayor a 0.")
                elif cantidad > stock_disponible:
                    print(f"¡Error! No hay suficiente stock. Solo quedan {stock_disponible} libros.")
                else:
                    stock_disponible -= cantidad
                    prestamos_activos += cantidad
                    print(f"¡Prestamo exitoso! Se han prestado {cantidad} libro(s).")
                    break
            except:
                print("¡Error de entrada! Debe ingresar un número entero positivo.")
            
    elif opcion == 3:
        print(f"\n--- Devolver prestamo (En prestamo actual: {prestamos_activos}) ---")
        
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de libros a devolver: "))
                if cantidad <= 0:
                    print("¡Error! La cantidad a devolver debe ser mayor a 0.")
                elif stock_disponible + cantidad > capaxidad_maxima:
                    print(f"¡Error! No se pueden devolver más libros de la capacidad máxima ({capaxidad_maxima} libros).")
                    print(f"Actualmente la biblioteca tiene {stock_disponible} en estantería. Solo puede devolver un máximo de {capaxidad_maxima - stock_disponible} libros.")
                else:
                    stock_disponible += cantidad
                    prestamos_activos -= cantidad
                    print(f"¡Devolución exitosa! Se han devuelto {cantidad} libro(s).")
                    break
            except:
                print("¡Error de entrada! Debe ingresar un número entero positivo.")
            
    elif opcion == 4:
        print("\n--- HISTORIAL DE PRESTAMOS ---")
        print(f"Total de prestamos activos en esta sesion: {prestamos_activos} libro(s).")
        
    elif opcion == 5:
        print("\nGracias por utilizar nuestro software, hasta la próxima.")
        break 
        
    else:
        print("¡Opcion no valida! Seleccione un numero del 1 al 5.")
