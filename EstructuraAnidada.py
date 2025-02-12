diccionario = {
    "Victor": {
        "Contrasena": "123",
        "Libros": [
            {
                "titulo": "No pienses",
                "Autor": "Leo",
                "Genero": "Suspenso",
                "leido": False
            }
        ]
    }
}

for llave, valor in diccionario.items():
    valor["Contrasena"] = "456"
#print(diccionario)

diccionario["Victor"]["contrasena"] = "123"
#print(diccionario)

print(diccionario["Victor"]["Libros"])
for libro in diccionario["Victor"]["Libros"]:
    libro["leido"] = True
    libro["Autor"] = "Sin nombre"
    libro["Genero"] = "Mayor"

print(diccionario)

diccionario["Victor"]["Libros"][0]["leido"] = True
print(diccionario)

diccionario["Victor"]["Libros"].append( {
                "titulo": "No pienses",
                "Autor": "Leo",
                "Genero": "Suspenso",
                "leido": False
            })

diccionario["David"] = {
        "Contrasena": "123",
        "Libros": [
            {
                "titulo": "No pienses",
                "Autor": "Leo",
                "Genero": "Suspenso",
                "leido": False
            }
        ]
    }
print(diccionario)

