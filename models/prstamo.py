from models.libro import Libro

class Prestamo: 
    
    # Constructor de la clase Prestamo
    def __init__(self, id_prestamo, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False # Por defecto, el prestamo no está devuelto

    def devolver(self): # Método para devolver el libro
        self.devuelto = True
        self.libro.devolver() #Marcar el libro como disponible nuevamente
    
    def mostrar_info(self):
        return f"prestamo ID: {self.id_prestamo}, Usuario: {self.usuario.nombre}, Libro: {self.libro.titulo}, Fech de prestamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}, Devuelto: {'Si' if self.devuelto else 'No'}"