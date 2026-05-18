# Valores

Valor_Medicamento = 60000
Valor_Despacho = 8000

continuar = True
while continuar:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad > 0:  
            continuar = False
        else:
            print("Debe ingresar una edad valida.")
    except ValueError:
        print("Debe ingresar un numero entero.")

continuar = True
while continuar:
    tramo_cliente = input("Ingrese su tramo (A, B, C o D): ").upper()
    if tramo_cliente in ["A", "B", "C", "D"]:
        continuar = False
    else:
        print("Debe ingresar una opcion valida (A, B, C o D).")

if edad <= 30:
    if tramo_cliente in ["A", "B"]:
        Porcentaje_Med = 18
    else:
        Porcentaje_Med = 12
elif 31 <= edad <= 60:
    if tramo_cliente in ["A", "B"]:
        Porcentaje_Med = 12
    else:
        Porcentaje_Med = 8
else: 
    Porcentaje_Med = 0

Porcentaje_Despacho = 0
if tramo_cliente in ["A", "B"]:
    Porcentaje_Despacho += 10  
    if edad >= 55:
        Porcentaje_Despacho += 5  

Descuento_Med = Valor_Medicamento * (Porcentaje_Med / 100)
medicamento_final = Valor_Medicamento - Descuento_Med

Descuento_Despacho = Valor_Despacho * (Porcentaje_Despacho / 100)
Despacho_final = Valor_Despacho - Descuento_Despacho    

print(f"El valor de medicamentos es: {int(medicamento_final)}")
print(f"El valor del despacho es: {int(Despacho_final)}")