import mysql.connector
from typing import Dict, Any, cast, List, Optional, Tuple
from dao.database import Database
from dominio.accionesDeCiudad import AccionesDeCiudad

class AccionesDeCiudadDao:

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor()


    def close_cursor(self):
        self.cursor.close()

    
    def listar(self) -> List[AccionesDeCiudad]:
        listaAccionesDeCiudad = []
        
        self.cursor.callproc('ACCIONES_DE_CIUDAD_CON_COSTO')
        
        for resultado in self.cursor.stored_results():
            rows = resultado.fetchall()

        for row in rows:
            row = cast(Dict[str, Any], row)

            acciones = AccionesDeCiudad(
                id=row["ID"],
                nombre=row["NOMBRE"],
                requisito=row["REQUISITO"],
                descripcion=row["DESCRIPCION"],
                efecto=row["EFECTO"],
                industria=row["INDUSTRIA"],
                poblacion=row["POBLACION"],
                riqueza=row["RIQUEZA"]
            )

            listaAccionesDeCiudad.append(acciones)

        self.close_cursor()
        self.cursor = self.db.cursor()

        return listaAccionesDeCiudad
    

    def modificar(self, accion: AccionesDeCiudad):

        self.cursor.callproc('MODIFICAR_ACCION_DE_CIUDAD',
            (
            accion.getId(),
            accion.getNombre(),
            accion.getRequisito(),
            accion.getDescripcion(),
            accion.getEfecto(),
            accion.getIndustria(),
            accion.getPoblacion(),
            accion.getRiqueza()
            )
        )

        self.db.commit() #Esto se debe poner tras ejecutar el prodecidimiento, siempre que se trate de un ALTER, DELETE o INSERT.
        self.close_cursor()
        self.cursor = self.db.cursor()


    def buscarXnombre(self, nombre: str) -> Optional[AccionesDeCiudad]: 
    #Existe una forma de crear un menu de seleccion donde puedan marcar especifcamene que quieren modificar, revisar mas adelante.

        self.cursor.callproc("ACCION_DE_CIUDAD_X_NOMBRE", (nombre,))

        for result in self.cursor.stored_results():

            raw_row = result.fetchone()

            if raw_row is None:
                continue

            row = cast(Dict[str, Any], raw_row)

            accion = AccionesDeCiudad(
                id=row["ID"],
                nombre=row["NOMBRE"],
                requisito=row["REQUISITO"],
                descripcion=row["DESCRIPCION"],
                efecto=row["EFECTO"],
                industria=row["INDUSTRIA"],
                poblacion=row["POBLACION"],
                riqueza=row["RIQUEZA"]
            )

            self.close_cursor()
            self.cursor = self.db.cursor()

            return accion

        self.close_cursor()
        self.cursor = self.db.cursor()
        return None
    

    def agregar(self, nombre, requisito, descripcion, efecto, industria, poblacion, riqueza) -> int:
        self.cursor.execute(
            "CALL AGREGAR_ACCION_DE_CIUDAD(%s,%s,%s,%s,%s,%s,%s)",
            (nombre, requisito, descripcion, efecto, industria, poblacion, riqueza)
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