import json

class Publicacion:
    def __init__(self, contenido, likes):
        self.contenido = contenido
        self.likes = likes

    def __str__(self):
        return f"Publicación: {self.contenido} (Likes: {self.likes})"
    
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
        self.publicaciones = []

    def agregar_amigo(self, amigo):
        if amigo not in self.amigos:
            self.amigos.append(amigo)
            print(f"Amigo '{amigo}' agregado a '{self.nombre}'.")
        else:
            print(f"'{amigo}' ya es amigo de '{self.nombre}'.")

    def agregar_publicacion(self, contenido, likes):
        publicacion = Publicacion(contenido, likes)
        self.publicaciones.append(publicacion)
        print("Publicación agregada correctamente.")

    def __str__(self):
        amigos_str = ", ".join(self.amigos) if self.amigos else "Ninguno"
        publicaciones_str = "\n  ".join(str(p) for p in self.publicaciones) if self.publicaciones else "Ninguna"
        return (
            f"Nombre: {self.nombre}\n"
            f"Amigos: {amigos_str}\n"
            f"Publicaciones:\n  {publicaciones_str}"
        )

class RedSocial:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []
        self.indice_usuarios = {}

    def agregar_usuario(self, nombre):
        if nombre in self.indice_usuarios:
            print(f"El usuario '{nombre}' ya existe.")
            return None

        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        self.indice_usuarios[nombre] = len(self.usuarios) - 1
        print(f"Usuario '{nombre}' agregado correctamente.")
        return usuario

    def buscar_usuario(self, nombre):
        if nombre in self.indice_usuarios:
            return self.usuarios[self.indice_usuarios[nombre]]
        else:
            print(f"Usuario '{nombre}' no encontrado.")
            return None

    def guardar_json(self, archivo="red_social.json"):
        try:
            datos = {
                "nombre": self.nombre,
                "usuarios": [
                    {
                        "nombre": usuario.nombre,
                        "amigos": usuario.amigos,
                        "publicaciones": [
                            {"contenido": p.contenido, "likes": p.likes}
                            for p in usuario.publicaciones
                        ]
                    }
                    for usuario in self.usuarios
                ]
            }
            with open(archivo, "w") as f:
                json.dump(datos, f, indent=4)
            print(f"Datos guardados correctamente en '{archivo}'.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_json(self, archivo="red_social.json"):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.nombre = datos["nombre"]
                self.usuarios = []
                self.indice_usuarios = {}
                for i, usuario_data in enumerate(datos["usuarios"]):
                    usuario = Usuario(usuario_data["nombre"])
                    usuario.amigos = usuario_data["amigos"]
                    usuario.publicaciones = [
                        Publicacion(p["contenido"], p["likes"])
                        for p in usuario_data["publicaciones"]
                    ]
                    self.usuarios.append(usuario)
                    self.indice_usuarios[usuario.nombre] = i
            print(f"Datos cargados correctamente desde '{archivo}'.")
        except FileNotFoundError:
            print(f"No se encontró el archivo '{archivo}'. Se creará uno nuevo al guardar.")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")

def Menu():
    red_social = RedSocial("SocialNet")
    red_social.cargar_json()  # Cargar datos al iniciar

    while True:
        print("\n--- Menú de SocialNet ---")
        print("1. Agregar un nuevo usuario")
        print("2. Agregar una publicación")
        print("3. Agregar Amigo")
        print("4. Mostrar todos los usuarios")
        print("5. Guardar red social")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Cual es tu nombre: ").lower()
            red_social.agregar_usuario(nombre)

        elif opcion == "2":
            nombre = input("Cual es tu nombre: ").lower()
            usuario = red_social.buscar_usuario(nombre)
            if usuario:
                contenido = input("Que postearas: ")
                likes = int(input("Likes: "))
                usuario.agregar_publicacion(contenido, likes)

        elif opcion == "3":
            nombre = input("Cual es tu nombre: ").lower()
            usuario = red_social.buscar_usuario(nombre)
            if usuario:
                amigo = input("Cual es el nombre de tu amigo: ").lower()
                usuario.agregar_amigo(amigo)

        elif opcion == "4":
            for usuario in red_social.usuarios:
                print(usuario)
                print()

        elif opcion == "5":
            red_social.guardar_json()

        elif opcion == "6":
            red_social.guardar_json()  # Guardar antes de salir
            print("Saliendo de SocialNet. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

Menu()