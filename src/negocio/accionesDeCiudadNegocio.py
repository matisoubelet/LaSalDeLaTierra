from dao.accionesDeCiudadDao import AccionesDeCiudadDao
from dominio.accionesDeCiudad import AccionesDeCiudad

class AccionesDeCiudadNegocio:

    def __init__(self):
        self.dao = AccionesDeCiudadDao()

    def listar(self):
        return self.dao.listar()