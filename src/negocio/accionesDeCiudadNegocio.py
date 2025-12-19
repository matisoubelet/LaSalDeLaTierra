from dao.accionesDeCiudadDao import AccionesDeCiudadDao
from dominio.accionesDeCiudad import AccionesDeCiudad

class AccionesDeCiudadNegocio:

    def __init__(self):
        self.dao = AccionesDeCiudadDao()


    def listar(self):
        return self.dao.listar()
    

    def modificar(self, accion: AccionesDeCiudad):
        return self.dao.modificar(accion)
    

    def buscarXnombre(self, nombre):
        return self.dao.buscarXnombre(nombre)
    

    def agregar(self, nombre, requisito, descripcion, efecto, industria, poblacion, riqueza):
        return self.dao.agregar(nombre, requisito, descripcion, efecto, industria, poblacion, riqueza)