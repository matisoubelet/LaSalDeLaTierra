class Yacimiento:
    def __init__(self, id, nombre, tipo):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo


    def setNombre(self, nombre):
        self.nombre = nombre

    def setTipo(self, tipo):
        self.tipo = tipo
    

    def getID(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getTipo(self):
        return self.tipo