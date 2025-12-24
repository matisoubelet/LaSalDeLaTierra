import mysql.connector
from typing import Dict, Any, cast, Optional
from dao.database import Database
from dominio.bosque import Bosque
from typing import List

class BosqueDao:

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor()


    def close_cursor(self):
        self.cursor.close()


    
    def listar(self) -> List[Bosque]:

            listaAnimales = []
            self.cursor.execute("SELECT * FROM BOSQUES ORDER BY GRUPO, NOMBRE")

            for row in self.cursor.fetchall():

                row = cast(Dict[str, Any], row) #Le estamos diciendo a Pylance que "row" es de tipo diccionario
                bosque = Bosque(
                id=row["ID"],
                nombre=row["NOMBRE"],
                grupo=row["GRUPO"]
                )
                listaAnimales.append(bosque)

            self.close_cursor()
            self.cursor = self.db.cursor()
            
            return listaAnimales


    def buscarXnombre(self, nombre: str) -> Optional[Bosque]:

        self.cursor.execute("SELECT ID, NOMBRE, GRUPO FROM BOSQUES WHERE NOMBRE = %s", (nombre,))

        row = self.cursor.fetchone()
        self.cursor.close()

        if row is None:
            return None

        row = cast(Dict[str, Any], row)
        
        return Bosque(
                id=row["ID"],
                nombre=row["NOMBRE"],
                grupo=row["GRUPO"]
                )


    def eliminar(self, nombre):

        self.cursor.callproc("ELIMINAR_BOSQUE", (nombre,))

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


    def agregar(self, nombre, grupo) -> int:

        self.cursor.execute(
            "CALL AGREGAR_BOSQUE(%s,%s)",
            (nombre, grupo)
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
    
    
    def modificar(self, bosque: Bosque):

        self.cursor.callproc('MODIFICAR_BOSQUE',
            (
            bosque.getID(),
            bosque.getNombre(),
            bosque.getGrupo()
            )
        )

        self.db.commit() #Esto se debe poner tras ejecutar el prodecidimiento, siempre que se trate de un ALTER, DELETE o INSERT.
        self.close_cursor()
        self.cursor = self.db.cursor()