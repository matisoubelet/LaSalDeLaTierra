import mysql.connector
from typing import Dict, Any, cast, Optional
from dao.database import Database
from dominio.animal import Animal
from typing import List

class AnimalDao:

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor()


    def close_cursor(self):
        self.cursor.close()


    
    def listar(self) -> List[Animal]:

            listaAnimales = []
            self.cursor.execute("SELECT * FROM ANIMALES ORDER BY GRUPO, NOMBRE")

            for row in self.cursor.fetchall():

                row = cast(Dict[str, Any], row) #Le estamos diciendo a Pylance que "row" es de tipo diccionario
                animal = Animal(
                id=row["ID"],
                nombre=row["NOMBRE"],
                domestico=row["DOMESTICO"],
                grupo=row["GRUPO"]
                )
                listaAnimales.append(animal)

            self.close_cursor()
            self.cursor = self.db.cursor()
            
            return listaAnimales


    def buscarXnombre(self, nombre: str) -> Optional[Animal]:

        self.cursor.execute("SELECT ID, NOMBRE, DOMESTICO, GRUPO FROM ANIMALES WHERE NOMBRE = %s", (nombre,))

        row = self.cursor.fetchone()
        self.cursor.close()

        if row is None:
            return None

        row = cast(Dict[str, Any], row)
        
        return Animal(
                id=row["ID"],
                nombre=row["NOMBRE"],
                domestico=row["DOMESTICO"],
                grupo=row["GRUPO"]
                )


    def eliminar(self, nombre):

        self.cursor.callproc("ELIMINAR_ANIMAL", (nombre,))

        resultado = None

        for result in self.cursor.stored_results():
            fila = result.fetchone()
            if fila is not None:
                fila = tuple(fila) 
                resultado = fila[0]

        self.db.commit()
        self.close_cursor()
        self.cursor = self.db.cursor()

        if resultado is None:
            return -1 
        elif resultado:
            return 1
        else:
            return 0


    def agregar(self, nombre, domestico, grupo) -> int:

        self.cursor.execute(
            "CALL AGREGAR_ANIMAL(%s,%s,%s)",
            (nombre, domestico, grupo)
        )

        resultado = 0

        while True:
            raw = self.cursor.fetchone()
            if raw is not None:
                fila = cast(Dict[str, Any], raw)
                resultado = int(fila["RESULTADO"])

            if not self.cursor.nextset():
                break

        self.db.commit()
        self.close_cursor() 
        self.cursor = self.db.cursor()

        return resultado
    
    
    def modificar(self, animal: Animal):

        self.cursor.callproc('MODIFICAR_ANIMAL',
            (
            animal.getID(),
            animal.getNombre(),
            animal.getDomestico(),
            animal.getGrupo()
            )
        )

        self.db.commit() #Esto se debe poner tras ejecutar el prodecidimiento, siempre que se trate de un ALTER, DELETE o INSERT.
        self.close_cursor()
        self.cursor = self.db.cursor()