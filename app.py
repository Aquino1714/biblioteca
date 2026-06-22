from dao.libro_dao import LibroDAO
from models.libro import Libro

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



def main():
    print("==================Biblioteca universitaria==========================")
    print("Menu de opciones")
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


if __name__ =="__main__":
    main()