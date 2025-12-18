class Edificacion:
    def __init__(self, id, nombre, descripcion, efecto, industria, riqueza, riqXturno):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.efecto = efecto
        self.industria = industria
        self.riqueza = riqueza
        self.riqXturno = riqXturno

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def setEfecto(self, efecto):
        self.efecto = efecto

    def setIndustria(self, industria):
        self.industria = industria

    def setRiqueza(self, riqueza):
        self.riqueza = riqueza    

    def setRiqXturno(self, riqXturno):
            self.riqXturno = riqXturno   


    def getID(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion
    
    def getEfecto(self):
        return self.efecto
    
    def getIndustria(self):
        return self.industria
    
    def getRiqueza(self):
        return self.riqueza
    
    def getRiqXturno(self):
        return self.riqXturno
    

    def __repr__(self):
        return f"Terreno(id={self.id}, nombre='{self.nombre}', descripcion='{self.descripcion}', efecto='{self.efecto}')"