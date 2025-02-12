usuario = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Barcelona"
}

usuario["edad"] = 35
usuario["profesion"] = "Ingeniero"
usuario["ciudad"] = "Madrid"

print(usuario)

estudiante = {
    "nombre": "Ana",
    "cursos": ["Matemáticas", "Historia", "Física"]
}

estudiante["cursos"].append("Quimica")
estudiante["cursos"][1] = "Leteratura"
estudiante["cursos"].pop(2)
print(estudiante)

biblioteca = {
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

biblioteca["Maria"] = {
    "Contrasena": "123",
        "Libros": [
        ]
}

biblioteca["Victor"]["Libros"].append({
    "titulo": "1984",
    "Autor": "George Orwell",
    "Genero": "Ciencia ficción",
    "leido": True
    }) 

biblioteca["Victor"]["Libros"][0]["leido"] = True

biblioteca["Maria"]["Libros"].append({
    "titulo": "Lo se",
    "Autor": "Juan",
    "Genero": "Psicologico",
    "leido": True
    }) 
print(biblioteca)

empresa = {
    "nombre": "TechCorp",
    "empleados": [
        {"nombre": "Juan", "edad": 28, "departamento": "Ventas"},
        {"nombre": "Laura", "edad": 34, "departamento": "IT"},
        {"nombre": "Pedro", "edad": 45, "departamento": "Finanzas"}
    ]
}

empresa["empleados"][0]["departamento"] = "Marketing"
empleado4 = {"nombre": "Sofia", "edad": 29, "departamento": "RH"}
empresa["empleados"].append(empleado4)
empresa["empleados"].pop(2)
print(empresa)
