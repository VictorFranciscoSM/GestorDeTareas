with open("Ejercicios\palabras.txt", "w") as file:
    file.write("Esto es una prueba de escritura")
    file.write("\nEsto es segunda prueba escritura")



with open("Ejercicios\palabras.txt", "a") as file:
    file.write("\nEsto es una  tercera prueba de escritura")


with open("Ejercicios\palabras.txt", "r") as file:
    contenido = file.readline()     #al leer la primera liena el puntero se queda en sigueinte liena 
    print(contenido)
    contenido = file.readline()
    print(contenido)
    contenido = file.readline()
    print(contenido)
    #contenido = file.read()
    #print(contenido)