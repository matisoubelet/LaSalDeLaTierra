import mysql.connector
from typing import Dict, Any, cast, Optional
from dao.database import Database
from models.terreno import Terreno
from typing import List

class TerrenoDao:

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor()


    def close_cursor(self):
        self.cursor.close()


    
    def listar(self) -> List[Terreno]:

            listaTerrenos = []
            self.cursor.execute("SELECT * FROM TERRENOS ORDER BY NOMBRE ASC")

            for row in self.cursor.fetchall():

                row = cast(Dict[str, Any], row) #Le estamos diciendo a Pylance que "row" es de tipo diccionario
                terreno = Terreno(
                id=row["ID"],
                nombre=row["NOMBRE"],
                descripcion=row["DESCRIPCION"]
                )
                listaTerrenos.append(terreno)

            self.close_cursor()
            self.cursor = self.db.cursor()
            
            return listaTerrenos


    def buscarXnombre(self, nombre: str) -> Optional[Terreno]:

        self.cursor.execute("SELECT ID, NOMBRE, DESCRIPCION FROM TERRENOS WHERE NOMBRE = %s", (nombre,))

        row = self.cursor.fetchone()
        self.cursor.close()

        if row is None:
            return None

        row = cast(Dict[str, Any], row)
        
        return Terreno(
            id=row["ID"],
            nombre=row["NOMBRE"],
            descripcion=row["DESCRIPCION"]
        )


    def eliminar(self, nombre):

        self.cursor.callproc("ELIMINAR_TERRENO", (nombre,))

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


    
    
    