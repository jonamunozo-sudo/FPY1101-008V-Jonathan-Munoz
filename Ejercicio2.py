from random import randint
num1 = int(input("Ingrese limite inferior: "))
num2 = int(input("Ingrese limite superior: "))
numero = randint(num1, num2)

if numero % 2 != 0:
    if numero + 1 <= num2:
        numero_final = numero + 1
    else:
        numero_final = numero - 1
else:
    numero_final = numero

correcto = numero_final
intento = 1
adivino = False
intento1 = 0
intento2 = 0

while intento <= 3 and adivino == False:
    if intento == 1:
        usuario = int(input("Intente adivinar: "))
        intento1 = usuario 
    elif intento == 2:
        usuario = int(input("Intente de nuevo: "))
        intento2 = usuario 
    else:
        usuario = int(input("Intente la ultima vez: "))
    if usuario == correcto:
        adivino = True
        if intento == 1:
            print("Felicitaciones, adivino en el primer intento.")
        elif intento == 2:
            print("Felicitaciones, adivino en su segundo intento.")
        else:
            print("Felicitaciones, pudiste adivinar.")
            
    else:
        if intento < 3:
            if correcto > usuario:
                print("El numero es mayor.")
            else:
                print("El numero es menor.")
        
        if intento == 2:
            distancia1 = abs(correcto - intento1)
            distancia2 = abs(correcto - intento2)
            
            print("te dare una pista:")
            if distancia2 < distancia1:
                print("El numero que buscas está más cerca de", intento2, "que de", intento1)
            else:
                print("El numero que buscas está más cerca de", intento1, "que de", intento2)
                
        if intento == 3:
            print("Perdiste.")
            print("El numero era:", correcto)
            
    intento = intento + 1