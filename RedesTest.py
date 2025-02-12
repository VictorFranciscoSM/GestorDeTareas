import json

red_social = {
    "nombre": "SocialNet",
    "usuarios": []
}

def agregar_usuario():
    try:
        nombre = input("Cual es tu nombre: ").lower()
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
                publicaciones.append({"contenido" : input(f"Que postearas {l+1}: "), "likes" : int(input(f"likes de {l+1}: "))})

        usuario= {
            "nombre": nombre,
            "amigos": amigo,
            "publicaciones": publicaciones
        }

        # Agregar el usuario a la red social
        red_social["usuarios"].append(usuario)
    except ValueError:
        print("Error: Ingresa un número válido.")



def agregar_publicacion():
    nombre = input("Cual es tu nombre: ").lower()
    for usuario in red_social["usuarios"]:
        if nombre == usuario["nombre"]:
            usuario["publicaciones"].append({"contenido" : input(f"Que postearas: "), "likes" : int(input(f"likes: "))})

def agregar_amigos():
    nombre = input("Cual es tu nombre: ").lower()
    amigo = input("Cual es el nombre de tu amigo: ").lower()
    for usuario in red_social["usuarios"]:
        if nombre == usuario["nombre"] and amigo not in usuario["amigos"]:
            usuario["amigos"].append(amigo)
        else:
            print("El amigos ya existe")

def mostrar_usuario():
    for usuario in red_social["usuarios"]:
        print(f"Nombre: {usuario['nombre']}")
        for amigos in usuario["amigos"]:
            print(f"Amigos: {amigos}")
        for publicaciones in usuario["publicaciones"]:
            print(f"Contenido: {publicaciones['contenido']} y Likes: {publicaciones['likes']}")
        print()

def guardar_usuarios():
    try: 
        with open("usuarios.json", "w") as archivo:
            json.dump(red_social, archivo, indent=4)
            print("Datos guardados")
    except Exception as e:
        print(f"Erroal guardar el archivo: {e}")

def cargar_usuarios():
    try: 
        with open("usuarios.json", "r") as archivo:
            datos = json.load(archivo)
            red_social.update(datos)
            print("Datos cargados")
    except FileNotFoundError:
        print(f"Archivo no encontrado")
    except Exception as e:
        print(f"Error al cargar los datos {e}")


def Menu():
    while True:
        print("\n--- Menú de SocialNet ---")
        print("1. Agregar un nuevo usuario")
        print("2. Agregar una publicación")
        print("3. Agregar Amigo")
        print("4. Mostrar todos los usuarios")
        print("5. Guardar todos los usuarios")
        print("6. Obtener ususarios anteriores")
        print("7. Salir")
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
            guardar_usuarios()
        elif opcion == "6":
            cargar_usuarios()
        elif opcion == "7":
            guardar_usuarios()
            break
        else:
            print("Opcion no encontrada")

Menu()