def registrar_medicos():
    print(".... SISTEMA DE REGISTRO - HOSPITAL CENTRAL METROPOLITANO ....\n")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de medicos que desea registrar: "))
            if cantidad > 0:
                break
            else:
                print("Registro medico invalido. Ingresa un entero positivo para continuar.")
        except: 
            print("Registro medico invalido. Ingresa un entero positivo para continuar.")
    especialistas_senior = 0
    residentes_junior = 0
    for i in range(1, cantidad + 1):
        print(f"\n--- Registro del Médico #{i} ---")
        while True:
            nombre = input("Nombre Profesional (minimo 6 caracteres, sin espacios): ").strip()
            if len(nombre) >= 6 and " " not in nombre:
                break
            else:
                print("Nombre invalido. Debe tener al menos 6 caracteres y no contener espacios.")
        while True:
            try:
                experiencia = int(input(f"Años de experiencia clinica de {nombre}: "))
                if experiencia >= 0:
                    break
                else:
                    print("¡Error clinico!.Ingresa un numero entero positivo para la experiencia.")
            except:  # Captura cualquier error de entrada
                print("¡Error clinico!. Ingresa un numero entero positivo para la experiencia.")
        if experiencia > 5:
            print(f"-> Clasificación: Especialista Senior")
            especialistas_senior += 1
        else:
            print(f"-> Clasificación: Residente Junior")
            residentes_junior += 1
    print("\n.....................................................")
    print("..................RESUMEN DE REGISTRO..................")
    print(".......................................................")
    print(f"El hospital cuenta con {especialistas_senior} Especialistas Senior y {residentes_junior} ¡Residentes Junior! ¡Sistema listo para operar!")
    print("=======================================================")

if __name__ == "__main__":
    registrar_medicos()  