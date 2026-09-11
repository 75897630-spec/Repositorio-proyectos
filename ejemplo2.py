nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

# Calcular el año de nacimiento
anio_actual = datetime.datetime.now().year
anio_nacimiento = anio_actual - edad

# Mostrar el resultado
print(f"¡Hola, {nombre}! Naciste aproximadamente en el año {anio_nacimiento}.")