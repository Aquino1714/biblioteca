class Usuario: 
    
    # Constructor de la clase Usuario
    def __init__(self, id, nombre, matricula, carrera, correo):
        self.id = id
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.correo = correo
        self.actuvo = True #Por defecto, el usario esta activo

    def activar(self):
        self.activo = True
    
    def desactivar(self):
        self.activo = False
    
    def mostrar_info(self): return f"Usuario Id: {self.id}, Nombre: {self.nombre}, Email:{self.correo}, Carrera: {self.carrera}, Activo: {'Si' if self.activo else 'No'}"
