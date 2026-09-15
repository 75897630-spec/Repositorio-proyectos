import csv

# Abrimos el archivo CSV
with open('archivoexportar.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo, delimiter=';')
    
    # Recorremos cada fila buscando el nombre 'mirella'
    encontrado = False
    for fila in lector:
        # Usamos strip() y lower() para ignorar espacios o mayúsculas
        if fila['nombre'].strip().lower() == 'mirella':
            print(f"La edad de Mirella es: {fila['edad'].strip()} años")
            encontrado = True
            break
            
    if not encontrado:
        print("No se encontró a Mirella en el archivo.")