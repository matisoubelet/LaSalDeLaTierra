from dao.terrenoDao import TerrenoDao

class TerrenoNegocio:

    def __init__(self):
        self.terrenoNegocio = TerrenoDao()
    

    def close(self):
        return self.terrenoNegocio.close()


    def listar(self):
        return self.terrenoNegocio.listar()
    

    def listarID(self, id):
        return self.terrenoNegocio.listarID(id)