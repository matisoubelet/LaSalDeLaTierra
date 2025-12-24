from dao.animalDao import AnimalDao
from dominio.animal import Animal

class AnimalNegocio:

    def __init__(self):
        self.dao = AnimalDao()
    

    def close(self):
        return self.dao.close_cursor()


    def listar(self):
        return self.dao.listar()
    

    def buscarXnombre(self, nombre):
        return self.dao.buscarXnombre(nombre)
    

    def eliminar(self, nombre):
        return self.dao.eliminar(nombre)
    

    def agregar(self, nombre, domestico, grupo):
        return self.dao.agregar(nombre, domestico, grupo)
    
    
    def modificar(self, animal: Animal):
        return self.dao.modificar(animal)