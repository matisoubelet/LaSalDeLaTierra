import mysql.connector
from typing import Dict, Any, cast, Optional
from dao.database import Database
from dominio.yacimiento import Yacimiento
from typing import List

class YacimientoDao:

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor()


    def close_cursor(self):
        self.cursor.close()


    
    def listar(self) -> List[Yacimiento]:

            listaYacimientos = []
            self.cursor.execute("SELECT * FROM YACIMIENTOS ORDER BY TIPO, NOMBRE ASC")

            for row in self.cursor.fetchall():

                row = cast(Dict[str, Any], row) #Le estamos diciendo a Pylance que "row" es de tipo diccionario
                yacimiento = Yacimiento(
                id=row["ID"],
                nombre=row["NOMBRE"],
                tipo=row["TIPO"]
                )
                listaYacimientos.append(yacimiento)

            self.close_cursor()
            self.cursor = self.db.cursor()
            
            return listaYacimientos


    def buscarXnombre(self, nombre: str) -> Optional[Yacimiento]:

        self.cursor.execute("SELECT ID, NOMBRE, TIPO FROM YACIMIENTOS WHERE NOMBRE = %s", (nombre,))

        row = self.cursor.fetchone()
        self.cursor.close()

        if row is None:
            return None

        row = cast(Dict[str, Any], row)
        
        return Yacimiento(
            id=row["ID"],
            nombre=row["NOMBRE"],
            tipo=row["TIPO"]
        )


    def eliminar(self, nombre):

        self.cursor.callproc("ELIMINAR_YACIMIENTO", (nombre,))

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


    def agregar(self, nombre, tipo) -> int:

        self.cursor.execute(
            "CALL AGREGAR_YACIMIENTO(%s,%s)",
            (nombre, tipo)
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
    
    
    def modificar(self, yacimiento: Yacimiento):

        self.cursor.callproc('MODIFICAR_YACIMIENTO',
            (
            yacimiento.getID(),
            yacimiento.getNombre(),
            yacimiento.getTipo()
            )
        )

        self.db.commit() #Esto se debe poner tras ejecutar el prodecidimiento, siempre que se trate de un ALTER, DELETE o INSERT.
        self.close_cursor()
        self.cursor = self.db.cursor()