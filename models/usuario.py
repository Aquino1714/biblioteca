import email


class Usuario: 
    
    # Constructor de la clase Usuario
    def __init__(self, id_usuario, nombre, email, carrera):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.carrera = carrera
        self.actuvo = True #Por defecto, el usario esta activo

    def activar(self):
        self.activo = True
    
    def desactivar(self):
        self.activo = False
    
    def mostrar_info(self): return f"Ususario Id: {self.id_usuario}, Nombre: {self.nombre}, Email:{self.email}, Carrera: {self.carrera}, Activo: {'Si' if self.activo else 'No'}"