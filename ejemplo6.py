import time
import keyboard

porcentaje=0
while porcentaje < 100:
    porcentaje += 25 #Incrementar en 25 a la variable
    print(f"Cargando... {porcentaje}%")
print ("Descarga completa!")

#Implementar un bucle que se detenga 
#cuando la tecla pulsada es "ESCape"


print("Ejecutando bucle. Presiona ESC para salir...")

while True:
    if keyboard.is_pressed("esc"):
        print("\nTecla ESC detectada. Bucle detenido.")
        break

    # Lógica de tu programa
    print("Procesando...", end="\r")
    time.sleep(0.1)