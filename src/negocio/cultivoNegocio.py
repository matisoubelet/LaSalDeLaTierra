from dao.cultivoDao import CultivoDao
from dominio.cultivo import Cultivo

class CultivoNegocio:

    def __init__(self):
        self.dao = CultivoDao()
    

    def close(self):
        return self.dao.close_cursor()


    def listar(self):
        return self.dao.listar()
    

    def buscarXnombre(self, nombre):
        return self.dao.buscarXnombre(nombre)
    

    def eliminar(self, nombre):
        return self.dao.eliminar(nombre)
    

    def agregar(self, nombre, estacion):
        return self.dao.agregar(nombre, estacion)
    
    
    def modificar(self, cultivo: Cultivo):
        return self.dao.modificar(cultivo)