# Modificar para que en cada iteracion inserte una nueva linea en un archivo.
import time
import keyboard
archivo=open("archivoReto.txt","w")
linea=0
while True:
    print("😈 ***\n")
    archivo.write(f"{linea} ===> ********\n")
    linea +=1
    if keyboard.is_pressed("esc"):
        print("\nTecla ESC detectada. Bucle detenido.")
        
        break
    # Lógica de tu programa
    print("Procesando...", end="\r")
    time.sleep(0.1)
archivo.close()