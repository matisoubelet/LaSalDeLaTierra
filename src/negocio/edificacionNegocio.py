from dao.edificacionDao import EdificacionDao
from models.edificacion import Edificacion

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


    # def listarIndustria(self):
    #     return self.dao.listarIndustria()
    
    # def listarRiqueza(self):
    #     return self.dao.listarRiqueza()