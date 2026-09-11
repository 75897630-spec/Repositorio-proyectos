nombre=input("Ingresa un nombre de animal en plural")
archivo=open("mi_archivo.txt","a")
archivo.write(f"Tres tristes {nombre} \n")
archivo.close()
