from dao.libro_dao import LibroDAO
from models.libro import Libro

def main():
    libro_dao = LibroDAO()
    
    libros = libro_dao.obtener_todos()
    
    print("=== Libros en la biblioteca ===")
    if len(libros) == 0:
        print("No hay libros disponibles.")
    else:
        for libro in libros:
            print(f"ID: {libro.id}, Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Disponible: {'Si' if libro.disponible else 'No'}")