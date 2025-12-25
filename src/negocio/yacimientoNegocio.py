from dao.yacimientoDao import YacimientoDao
from dominio.yacimiento import Yacimiento

class YacimientoNegocio:

    def __init__(self):
        self.dao = YacimientoDao()
    

    def close(self):
        return self.dao.close_cursor()


    def listar(self):
        return self.dao.listar()
    

    def buscarXnombre(self, nombre):
        return self.dao.buscarXnombre(nombre)
    

    def eliminar(self, nombre):
        return self.dao.eliminar(nombre)
    

    def agregar(self, nombre, tipo):
        return self.dao.agregar(nombre, tipo)
    
    
    def modificar(self, yacimiento: Yacimiento):
        return self.dao.modificar(yacimiento)