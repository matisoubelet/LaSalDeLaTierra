class Bosque:
    def __init__(self, id, nombre, grupo):
        self.id = id
        self.nombre = nombre
        self.grupo = grupo


    def setNombre(self, nombre):
        self.nombre = nombre

    def setGrupo(self, grupo):
        self.grupo = grupo
    

    def getID(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getGrupo(self):
        return self.grupo