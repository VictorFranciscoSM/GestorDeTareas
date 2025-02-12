with open("Ejercicios\lumnos.txt", "w") as file:
    file.write("[{'alumno': 'victor', 'edad': 25},{'alumno': 'diego', 'edad': 23},{'alumno': 'oman', 'edad': 19}]")



#with open("Ejercicios\palabras.txt", "a") as file:
#    file.write("\nEsto es una  tercera prueba de escritura")


with open("Ejercicios\lumnos.txt", "r") as file:
    contenido = file.readlines()
    print(contenido)