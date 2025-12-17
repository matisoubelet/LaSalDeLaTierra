from dao.terrenoDao import TerrenoDao

class TerrenoNegocio:

    def __init__(self):
        self.dao = TerrenoDao()
    

    def close(self):
        return self.dao.close_cursor()


    def listar(self):
        return self.dao.listar()
    

    def buscarXnombre(self, nombre):
        return self.dao.buscarXnombre(nombre)
    

    def eliminar(self, nombre):
        return self.dao.eliminar(nombre)
    
    