import json
from datetime import datetime

#clase Libro
class Libro:
    def __init__(self, titulo, autor, genero, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.leido = False

    def marcar_como_leido(self):
        self.leido = True

    def editar_libro(self, titulo,autor, genero, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion

 #clase usuario
class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def eliminar_libro(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo != titulo]

    def obtener_libros(self):
        return self.libros

#clase sisteme de gestion de libros
class SistemaGestionLibros:
    def __init__(self, archivos_datos = "Ejercicios\chivos_datos.json"):
        self.usuarios = {}
        self.archivos_datos = archivos_datos
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open(self.archivos_datos, "r") as archivo:
                datos = json.load(archivo)
                for nombre_usuario, info in datos.items():
                    usuario = Usuario(nombre_usuario, info["contrasena"])
                    for libro_info in info["libros"]:
                        libro = Libro(libro_info["titulo"], libro_info["autor"], libro_info["genero"], libro_info["anio_publicacion"])
                        libro.leido = libro_info["leido"]
                        usuario.agregar_libro(libro)
                    self.usuarios[nombre_usuario] = usuario
        except FileNotFoundError:
            print("El archivo no fue encontrado")

    def guardar_datos(self):
        datos = {}
        for nombre_usuario, usuario in self.usuarios.items():
            datos[nombre_usuario] = {"contrasena": usuario.contrasena, "libros": [{"titulo": libro.titulo, "autor": libro.autor, "genero": libro.genero, "anio_publicacion": libro.anio_publicacion, "leido": libro.leido} for libro in usuario.libros]}

        with open(self.archivos_datos, "w") as archivo:
            json.dump(datos, archivo)

    def registrar_usuario(self, nombre_usuario, contrasena):
        if nombre_usuario in self.usuarios:
            print("El usuario ya existe")
            return False
        else:
            self.usuarios[nombre_usuario] = Usuario(nombre_usuario, contrasena)
            self.guardar_datos()
            print("Registro de usuario realizado")
            return True
        
    def iniciar_sesion(self, nombre_usuario, contrasena):
        usuario = self.usuarios.get(nombre_usuario)
        if usuario and usuario.contrasena == contrasena:
            print("Inicio de sesion")
            return usuario
        else:
            print("Sesion incorrecta")
            return None

    def menu_usuario(self, usuario):
        while True:
            print("\n1. Agregar Libro")
            print("2. Ver Libros")
            print("3. Editar Libro")
            print("4 Completar Libros")
            print("5. Elimnar Libro")
            print("6. cerrar sesion")

            opcion = input("Escribe el numero de la accion a realizar: ")
            if opcion == "1":
                titulo = input("titulo del libro: ")
                autor = input("autor del libro: ")
                genero = input("genero del libro: ")
                anio_publicacion = input("anio dde publicacion del libro: ")
                libro = Libro(titulo, autor, genero, anio_publicacion)
                usuario.agregar_libro(libro)
                self.guardar_datos()
            elif opcion == "2":
                libros = usuario.obtener_libros()
                if not libros:
                    print("No tiene libros")
                for indice, libro in enumerate(libros, start=1):
                    leido = "leido" if libro.leido else "pendiente"
                    print(f"{indice}. {libro.titulo} - {leido}")
            elif opcion == "3":
                titulo_libro = input("Titulo del libro a editar: ")
                libro = next((titu for titu in usuario.libros if titu.titulo == titulo_libro), None)
                if libro:
                    nuevo_titulo = input("Nevo titulo: ")
                    nuevo_autor = input("Nuevo autor: ")
                    nuevo_genero = input("Nuevo genero: ")
                    nuevo_anio_publicacion= input("Nuevo anio de publicacion: ")
                    libro.editar_libro(nuevo_titulo, nuevo_autor, nuevo_genero, nuevo_anio_publicacion)
                    self.guardar_datos()
                    print("Libro actualizado ")
                else:
                    print("Libro no encontrado")
            elif opcion == "4":
                titulo_libro = input("Dime el nombre del libro completado")
                libro = next((titu for titu in usuario.libros if titu.titulo == titulo_libro), None)
                if libro:
                    libro.marcar_como_leido()
                    self.guardar_datos()
                    print("Libro marcado como completado")
                else:
                    print("Libro no encontrado en tu lista")
            elif opcion == "5":
                titulo_libro = input("Dime el nombre del libro completado")
                usuario.eliminar_libro(titulo_libro)
                self.guardar_datos()
                print("Libro eliminado de tu lista")
            elif opcion == "6":
                print("Sesion cerrada")
                break
            else:
                print("Opcion no valida intenta de nuevo")
            
#Efucucion del programa
if __name__ == "__main__":
    sistema = SistemaGestionLibros()
    while True:
        print("\n ----- Sistema de Gestion de Lirnos -------")
        print("1. Registrar usuario")
        print("2. Iniciar sesion")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre_usuario = input("Escribe el nombre de usuario")
            contrasena = input("Escribe la contrasena")
            sistema.registrar_usuario(nombre_usuario, contrasena)
        elif opcion == "2":
            nombre_usuario = input("Escribe el nombre de usuario")
            contrasena = input("Escribe la contrasena")
            usuario = sistema.iniciar_sesion(nombre_usuario, contrasena)
            if usuario:
                sistema.menu_usuario(usuario)
        elif opcion == 3:
            print("Saliendo del menu")
            break
        else:
            print("Opcion invalida intente de nnuevo")