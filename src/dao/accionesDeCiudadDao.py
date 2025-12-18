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