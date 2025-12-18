class AccionesDeCiudad:
    def __init__(self, id, nombre, requisito, descripcion, efecto, industria, poblacion, riqueza):
        self.id = id
        self.nombre = nombre
        self.requisito = requisito
        self.descripcion = descripcion
        self.efecto = efecto
        self.industria = industria
        self.poblacion = poblacion
        self.riqueza = riqueza

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setRequisito(self, requisito):
        self.requisito = requisito

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setEfecto(self, efecto):
        self.efecto = efecto

    def setIndustria(self, industria):
        self.industria = industria
    
    def setPoblacion(self, poblacion):
        self.poblacion = poblacion
    
    def setRiqueza(self, riqueza):
        self.riqueza = riqueza


    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getRequisito(self):
        return self.requisito
    
    def getDescripcion(self):
        return self.descripcion
    
    def getEfecto(self):
        return self.efecto
    
    def getIndustria(self):
        return self.industria
    
    def getPoblacion(self):
        return self.poblacion
    
    def getRiqueza(self):
        return self.riqueza
    