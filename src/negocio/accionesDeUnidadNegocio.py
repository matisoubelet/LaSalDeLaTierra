from dao.accionesDeUnidadDao import AccionesDeUnidadDao
from dominio.accionesDeUnidad import AccionesDeUnidad

class AccionesDeUnidadNegocio:

    def __init__(self):
        self.dao = AccionesDeUnidadDao()


    def listar(self):
        return self.dao.listar()
    

    def modificar(self, accion: AccionesDeUnidad):
        return self.dao.modificar(accion)
    

    def buscarXnombre(self, nombre, tipo):
        return self.dao.buscarXnombre(nombre, tipo)
    

    def agregar(self, nombre, tipo, descripcion, industria, riqueza):
        return self.dao.agregar(nombre, tipo, descripcion, industria, riqueza)
    

    def eliminar(self, nombre, tipo):
        return self.dao.eliminar(nombre, tipo)