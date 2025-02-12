import json

datos = {"nombre": "Victor","edad": 27, "ciudad": "EDOMX", "hobbies":["leer","nadar","programar"], "estudiante": False}

#guardar en un archivo JSON
with open("Ejercicios\datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)


#leer un arhico datos comvirtiendolo en diccionario
with open("Ejercicios\datos.json", "r") as datos:
    datos_recu = json.load(datos)

print(datos_recu)

datos1 = {"nombre": "Victor","edad": 27, "ciudad": "EDOMX", "hobbies":["leer","nadar","programar"], "estudiante": False}

#convertir un diccioanrio a JSON(Texto)
datos_json = json.dumps(datos1, indent=4)  # Convierte a JSON en formato de texto
print(datos_json)

#convertir JSON a un diccionario
json_string = '{"nombre": "Victor", "edad": 25, "ciudad": "CDMX"}'
# Convertir JSON a diccionario
datos_dict = json.loads(json_string)
print(datos_dict)

#Editar un archivo Json
#leer el archivo JSON
with open("Ejercicios\datos.json", 'r') as archivo:
    datos = json.load(archivo)

datos["edad"] = 26
datos["profesion"] = "Ingeniero"

#Guardar los cambios en el archivo JSON
with open("Ejercicios\datos.json", 'w') as archivo:
    json.dump(datos, archivo, indent=4)

