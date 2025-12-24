class Animal:
    def __init__(self, id, nombre, domestico, grupo):
        self.id = id
        self.nombre = nombre
        self.domestico = domestico
        self.grupo = grupo


    def setNombre(self, nombre):
        self.nombre = nombre

    def setDomestico(self, domestico):
        self.domestico = domestico

    def setGrupo(self, grupo):
        self.grupo = grupo
    

    def getID(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getDomestico(self):
        return self.domestico
    
    def getGrupo(self):
        return self.grupo