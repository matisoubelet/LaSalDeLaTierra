from dao.bosqueDao import BosqueDao
from dominio.bosque import Bosque

class BosqueNegocio:

    def __init__(self):
        self.dao = BosqueDao()
    

    def close(self):
        return self.dao.close_cursor()


    def listar(self):
        return self.dao.listar()
    

    def buscarXnombre(self, nombre):
        return self.dao.buscarXnombre(nombre)
    

    def eliminar(self, nombre):
        return self.dao.eliminar(nombre)
    

    def agregar(self, nombre, grupo):
        return self.dao.agregar(nombre, grupo)
    
    
    def modificar(self, bosque: Bosque):
        return self.dao.modificar(bosque)