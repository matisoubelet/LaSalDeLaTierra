import mysql.connector
from typing import Dict, Any, cast, Optional
from dao.database import Database
from dominio.cultivo import Cultivo
from typing import List

class CultivoDao:

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor()


    def close_cursor(self):
        self.cursor.close()


    
    def listar(self) -> List[Cultivo]:

            listaCultivos = []
            self.cursor.execute("SELECT * FROM CULTIVOS ORDER BY ESTACION, NOMBRE ASC")

            for row in self.cursor.fetchall():

                row = cast(Dict[str, Any], row) #Le estamos diciendo a Pylance que "row" es de tipo diccionario
                terreno = Cultivo(
                id=row["ID"],
                nombre=row["NOMBRE"],
                estacion=row["ESTACION"]
                )
                listaCultivos.append(terreno)

            self.close_cursor()
            self.cursor = self.db.cursor()
            
            return listaCultivos


    def buscarXnombre(self, nombre: str) -> Optional[Cultivo]:

        self.cursor.execute("SELECT ID, NOMBRE, ESTACION FROM CULTIVOS WHERE NOMBRE = %s", (nombre,))

        row = self.cursor.fetchone()
        self.cursor.close()

        if row is None:
            return None

        row = cast(Dict[str, Any], row)
        
        return Cultivo(
            id=row["ID"],
            nombre=row["NOMBRE"],
            estacion=row["ESTACION"]
        )


    def eliminar(self, nombre):

        self.cursor.callproc("ELIMINAR_CULTIVO", (nombre,))

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


    def agregar(self, nombre, estacion) -> int:

        self.cursor.execute(
            "CALL AGREGAR_CULTIVO(%s,%s)",
            (nombre, estacion)
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
    
    
    def modificar(self, cultivo: Cultivo):

        self.cursor.callproc('MODIFICAR_CULTIVO',
            (
            cultivo.getID(),
            cultivo.getNombre(),
            cultivo.getEstacion()
            )
        )

        self.db.commit() #Esto se debe poner tras ejecutar el prodecidimiento, siempre que se trate de un ALTER, DELETE o INSERT.
        self.close_cursor()
        self.cursor = self.db.cursor()