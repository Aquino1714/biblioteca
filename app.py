import flet as ft

from dao.libro_dao import LibroDAO
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

import flet as ft
from ui.main_window import main_window

def ver_libros():
    try:
        libro_dao = LibroDAO()
        
        libros = libro_dao.obtener_todos()
        
        print("=== Libros en la biblioteca ===")
        if len(libros) == 0:
            print("No hay libros disponibles.")
        else:
            for libro in libros:
                print(f"ID: {libro.id}, Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Disponible: {'Si' if libro.disponible else 'No'}")
        
        print("\n conexion exitosa a la base de datos")
    
    except Exception as e:
        print("Error:")
        print(e)

def insertar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = int(input("Ingrese el id del autor: "))
    isbn = input("Ingrese el ISBN del libro: ")
    disponible = True

    try:
        libro_dao= LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        libro =Libro(id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Libro insertado exitosamente.")
    except Exception as e:
        print("Error al insertar el libro:")
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles: ")
        ver_libros()
        id = int(input("Escribe el id del libro a eliminal: "))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eliminado con éxito")
    
    except Exception as e:
        print(f"Error al eliminar el libro {id}")
        print(e)
        
def ver_usuarios():
    try:
        usuario_dao = UsuarioDAO()

        usuarios = usuario_dao.obtener_todos()

        print("=== Usuarios registrados ===")
        if len(usuarios) == 0:
            print("No hay usuarios registrados.")
        else:
            for usuario in usuarios:
                print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Matrícula: {usuario.matricula}, Carrera: {usuario.carrera}, Correo: {usuario.correo}")

        print("\nConexión exitosa a la base de datos")

    except Exception as e:
        print("Error:")
        print(e)


def insertar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    matricula = input("Ingrese la matrícula: ")
    carrera = input("Ingrese la carrera: ")
    correo = input("Ingrese el correo: ")

    try:
        usuario_dao = UsuarioDAO()
        id = usuario_dao.obtener_ultimo_id() + 1

        usuario = Usuario(id, nombre, matricula, carrera, correo)

        usuario_dao.insertar(usuario)

        print("Usuario insertado exitosamente.")

    except Exception as e:
        print("Error al insertar el usuario:")
        print(e)


def eliminar_usuario():
    try:
        usuario_dao = UsuarioDAO()

        print("Lista de usuarios:")
        ver_usuarios()

        id = int(input("Escriba el ID del usuario a eliminar: "))

        usuario_dao.eliminar(id)

        print(f"El usuario {id} ha sido eliminado con éxito.")

    except Exception as e:
        print(f"Error al eliminar el usuario {id}")
        print(e)


def actualizar_usuario():
    print("Seleccione el usuario a actualizar")

    try:
        usuario_dao = UsuarioDAO()

        ver_usuarios()

        id = int(input("Ingrese el ID del usuario a actualizar: "))
        nombre = input("Ingrese el nuevo nombre: ")
        matricula = input("Ingrese la nueva matrícula: ")
        carrera = input("Ingrese la nueva carrera: ")
        correo = input("Ingrese el nuevo correo: ")

        usuario = Usuario(id, nombre, matricula, carrera, correo)

        usuario_dao.actualizar(usuario)

        print(f"Usuario con ID {id} actualizado exitosamente.")

    except Exception as e:
        print("Error al actualizar el usuario")
        print(e)

    
    
    
def menu_libro():
    print("1. Ver libros")
    print("2. Agregar libro")
    print("3. Actualizar libro")
    print("4. Eliminar libro")
    
    opcion = input("Seleccione una opción (1-4): ")
    match opcion:
        case "1":
            ver_libros()
        case "2":
            insertar_libro()
        case "3":
            actualizar_libro()
        case "4":
            eliminar_libro()
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

# def menu_usuario():
#     print("1. Ver usuarios")
#     print("2. Agregar usuario")
#     print("3. Actualizar usuario")
#     print("4. Eliminar usuario")
    
#     opcion = input("Seleccione una opción (1-4): ")
#     match opcion:
#         case "1":
#             ver_usuarios()
#         case "2":
#             insertar_usuario()
#         case "3":
#             actualizar_usuario()
#         case "4":
#             eliminar_usuario()
#         case _:
#             print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

#def main():
#    print("==================Biblioteca universitaria==========================")
#    print("Menu de opciones")
#    print("1. Libros")
#    print("2. Usuarios")
    
    # opcion = input("Seleccione una opción (1-2): ")
    # match opcion:
    #     case "1":
    #         menu_libro()
    #     case "2":
    #         menu_usuario()
    #     case _:
    #         print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")

def actualizar_libro():
    print("Selecciona el libro a actializar")
    try:
        libro_dao = LibroDAO()
        ver_libros()
        id = int(input("Ingrese el id del libro a actualizar: "))
        titulo = input("Ingrese el nuevo título del libro: ")
        autor = input("Ingrese el nuevo autor disponible: ")
        isbn = input("Ingrese el nuevo ISBN del libro: ")
        disponible = bool(input("Ingrese True para disponible, False para no disponible: "))
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print(f"Libro con ID {id} actualizado exitosamente.")

    except Exception as e:
        print("Error al actualizar el libro")
        print(e)

ft.app(target = main_window)