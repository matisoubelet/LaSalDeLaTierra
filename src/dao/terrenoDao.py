import mysql.connector
from typing import Dict, Any, cast
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


    def listarID(self, id):
        try:
            
            id = int(id)

            query = "SELECT * FROM TERRENOS WHERE ID = %s"
            self.cursor.execute(query, (id,)) #La coma va porque el execute necesita un minimo de 2 parametros. Si tuviera "id, nombre" no hace falta la coma al final
            row = cast(Dict[str, Any], self.cursor.fetchone())

            # Si no existe ese ID
            if row is None:

                self.close_cursor()
                self.cursor = self.db.cursor()

                return None

            # Pasa todo a minusculas
            row = {k.lower(): v for k, v in row.items()}

            self.close_cursor()
            self.cursor = self.db.cursor()

            return Terreno(**row)

        except ValueError: # Cuando id no puede convertirse a int
            print("ERROR: El ID debe ser un número.")

            self.close_cursor()
            self.cursor = self.db.cursor()

            return None

        except mysql.connector.Error as e: # Errores que tengan que ver con la base de datos
            print(f"ERROR en la base de datos: {e}")
            
            self.close_cursor()
            self.cursor = self.db.cursor()
            
            return None

        except Exception as e: #Cualquier otro error que no sean los anteriores
            print(f"ERROR inesperado: {e}")
            
            self.close_cursor()
            self.cursor = self.db.cursor()
            
            return None
    
    