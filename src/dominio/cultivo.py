class Cultivo:
    def __init__(self, id, nombre, estacion):
        self.id = id
        self.nombre = nombre
        self.estacion = estacion


    def setNombre(self, nombre):
        self.nombre = nombre

    def setEstacion(self, estacion):
        self.estacion = estacion
    

    def getID(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getEstacion(self):
        return self.estacion