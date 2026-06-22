class Libro: 
    
    # Constructor de la clase Libro
    def __init__(self, id, titulo, autor, isbn, disponible):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible # Por defecto, el libro está disponible

    def prestar(self): # Método para prestar el libro
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self): # Método para devolver el libro
        return True
    
    def mostar_info(self):
        return f"Libro ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {'Si' if self.disponible else 'No'}"