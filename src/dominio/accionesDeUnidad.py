class AccionesDeUnidad:
    def __init__(self, id, nombre, tipo, descripcion, industria, riqueza):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.descripcion = descripcion
        self.industria = industria
        self.riqueza = riqueza

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setTipo(self, tipo):
        self.tipo = tipo

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setIndustria(self, industria):
        self.industria = industria
    
    def setRiqueza(self, riqueza):
        self.riqueza = riqueza


    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getTipo(self):
        return self.tipo
    
    def getDescripcion(self):
        return self.descripcion
    
    def getIndustria(self):
        return self.industria
    
    def getRiqueza(self):
        return self.riqueza
    