from dao.edificacionDao import EdificacionDao
from dominio.edificacion import Edificacion

class EdificacionNegocio:

    def __init__(self):
        self.dao = EdificacionDao()

    def close(self):
        self.dao.close_cursor()

    def listar(self, num):
        return self.dao.listar(num)
    
    def modificar(self, edificacion: Edificacion):
        return self.dao.modificar(edificacion)
    
    def buscarXnombre(self, nombre):
        return self.dao.buscarXnombre(nombre)


    def agregar(self,nombre, descripcion, efecto, industria, riqueza, riqXturno):
        return self.dao.agregar(nombre, descripcion, efecto, industria, riqueza, riqXturno)
    
    def eliminar(self, nombre):
        return self.dao.eliminar(nombre)