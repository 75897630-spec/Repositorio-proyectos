temperatura = 18

def detectarTemperatura(lectura):
    # Paso 1: Evalúa si lectura (18) es exactamente igual a 17
    if lectura == 17:
        print("es verdad, estoy dentro de la estructura de control IF")
        lectura = lectura + 3
        print(f"temperatura: {lectura}")
    else:
        # Paso 2: Como 18 NO es igual a 17, entra a este bloque ELSE
        print("tambien estoy dentro de la estructura")
        lectura = lectura - 1         # 18 - 1 = 17
        print(f"temperatura: {lectura}") # Imprime: temperatura: 17

    # Paso 3: Sale de la estructura IF/ELSE pero sigue dentro de la función
    print("estoy fuera de la estructura IF")

    # Paso 4: Multiplica la temperatura actual por 10
    lectura = lectura * 10            # 17 * 10 = 170
    print(f"temperatura: {lectura}") # Imprime: temperatura: 170

# Paso 5: Llamada a la función pasándole la variable inicial
detectarTemperatura(temperatura)