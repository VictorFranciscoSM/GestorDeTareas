# Diccionario inicial de la red social
red_social = {
    "nombre": "SocialNet",
    "usuarios": []
}

# Función para agregar un nuevo usuario
def agregar_usuario():
    nombre = input("Ingresa el nombre del nuevo usuario: ")
    amigos = input("Ingresa los nombres de los amigos (separados por comas): ").split(",")
    publicaciones = []

    # Crear el diccionario del usuario
    usuario = {
        "nombre": nombre,
        "amigos": [amigo.strip() for amigo in amigos],  # Eliminar espacios en blanco
        "publicaciones": publicaciones
    }

    # Agregar el usuario a la red social
    red_social["usuarios"].append(usuario)
    print(f"Usuario '{nombre}' agregado correctamente.")

# Función para agregar una publicación a un usuario
def agregar_publicacion():
    nombre_usuario = input("Ingresa el nombre del usuario: ")
    contenido = input("Ingresa el contenido de la publicación: ")
    likes = int(input("Ingresa la cantidad de likes: "))

    # Buscar al usuario en la red social
    for usuario in red_social["usuarios"]:
        if usuario["nombre"] == nombre_usuario:
            # Agregar la publicación
            usuario["publicaciones"].append({"contenido": contenido, "likes": likes})
            print(f"Publicación agregada a '{nombre_usuario}'.")
            return

    print(f"Usuario '{nombre_usuario}' no encontrado.")

# Función para mostrar todos los usuarios y sus datos
def mostrar_usuarios():
    print("\n--- Usuarios en la red social ---")
    for usuario in red_social["usuarios"]:
        print(f"Nombre: {usuario['nombre']}")
        print(f"Amigos: {', '.join(usuario['amigos'])}")
        print("Publicaciones:")
        for publicacion in usuario["publicaciones"]:
            print(f"  - {publicacion['contenido']} (Likes: {publicacion['likes']})")
        print()

# Menú principal
def menu():
    while True:
        print("\n--- Menú de SocialNet ---")
        print("1. Agregar un nuevo usuario")
        print("2. Agregar una publicación")
        print("3. Mostrar todos los usuarios")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            agregar_publicacion()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            print("Saliendo de SocialNet. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
menu()