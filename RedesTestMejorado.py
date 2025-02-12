red_social = {
    "nombre": "SocialNet",
    "usuarios": [],  # Lista de usuarios
    "indice_usuarios": {}  # Diccionario para acceder a usuarios por nombre
}

def agregar_usuario():
    try:
        nombre = input("Cual es tu nombre: ").lower()
        
        # Verificar si el usuario ya existe
        if nombre in red_social["indice_usuarios"]:
            print(f"El usuario '{nombre}' ya existe.")
            return

        Noamigos = int(input("Cuantos amigos quieres agregar: "))
        amigo = []
        if Noamigos < 1:
            print("No se agregaron amigos.")
        else:
            for l in range(Noamigos):
                amigo.append(input(f"Nombre del amigo {l+1}: ").lower())

        Nopublicaciones = int(input("Cuantas publicaciones quieres agregar: "))
        publicaciones = []
        if Nopublicaciones < 1:
            print("No se agregaron publicaciones.")
        else:
            for l in range(Nopublicaciones):
                publicaciones.append({
                    "contenido": input(f"Que postearas {l+1}: "),
                    "likes": int(input(f"likes de {l+1}: "))
                })

        usuario = {
            "nombre": nombre,
            "amigos": amigo,
            "publicaciones": publicaciones
        }

        # Agregar el usuario a la lista y al diccionario
        red_social["usuarios"].append(usuario)
        red_social["indice_usuarios"][nombre] = len(red_social["usuarios"]) - 1  # Guardar el índice
        print(f"Usuario '{nombre}' agregado correctamente.")
    except ValueError:
        print("Error: Ingresa un número válido.")

def agregar_publicacion():
    nombre = input("Cual es tu nombre: ").lower()
    
    # Buscar el usuario en el diccionario
    if nombre in red_social["indice_usuarios"]:
        indice = red_social["indice_usuarios"][nombre]  # Obtener el índice
        usuario = red_social["usuarios"][indice]  # Acceder al usuario
        
        usuario["publicaciones"].append({
            "contenido": input("Que postearas: "),
            "likes": int(input("likes: "))
        })
        print("Publicación agregada correctamente.")
    else:
        print(f"Usuario '{nombre}' no encontrado.")

def agregar_amigos():
    nombre = input("Cual es tu nombre: ").lower()
    amigo = input("Cual es el nombre de tu amigo: ").lower()
    
    # Buscar el usuario en el diccionario
    if nombre in red_social["indice_usuarios"]:
        indice = red_social["indice_usuarios"][nombre]  # Obtener el índice
        usuario = red_social["usuarios"][indice]  # Acceder al usuario
        
        if amigo not in usuario["amigos"]:
            usuario["amigos"].append(amigo)
            print(f"Amigo '{amigo}' agregado a '{nombre}'.")
        else:
            print(f"'{amigo}' ya es amigo de '{nombre}'.")
    else:
        print(f"Usuario '{nombre}' no encontrado.")

def mostrar_usuario():
    for usuario in red_social["usuarios"]:
        print(f"Nombre: {usuario['nombre']}")
        print("Amigos:", ", ".join(usuario["amigos"]))
        print("Publicaciones:")
        for publicacion in usuario["publicaciones"]:
            print(f"  - Contenido: {publicacion['contenido']}, Likes: {publicacion['likes']}")
        print()

def Menu():
    while True:
        print("\n--- Menú de SocialNet ---")
        print("1. Agregar un nuevo usuario")
        print("2. Agregar una publicación")
        print("3. Agregar Amigo")
        print("4. Mostrar todos los usuarios")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            agregar_publicacion()
        elif opcion == "3":
            agregar_amigos()
        elif opcion == "4":
            mostrar_usuario()
        elif opcion == "5":
            print("Saliendo de SocialNet. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

Menu()