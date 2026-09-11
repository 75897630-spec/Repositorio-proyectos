#MODIFICAR PARA LEER 2 NUMEROS POR TECLADO.
#Y OPERAR: 1=> suma, 2=>resta, 3=> multiplicacion}
print ("CALCULADORA \n Ingresa 2 números")
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
print ("Selecciona operación: 1=> suma, 2=>resta, 3=> multiplicacion")
opcion= int(input("selecciona operación: "))
match opcion:
    case 1:
        print (f"SUMA")
        print(f"Resultado: {numero1+numero2}")
    case 2:
        print(f"RESTA")
        print(f"Resultado: {numero1-numero2}")
    case 3:
        print (f"MULTIPLICACION")
        print(f"Resultado: {numero1*numero2}")
    case 5:
        print(f"opcion5 {opcion}")
    case _:
        print(f"Ninguna opción {opcion}")
