import mysql.connector
from typing import Dict, Any, cast, List, Optional, Tuple
from dao.database import Database
from dominio.accionesDeUnidad import AccionesDeUnidad

class AccionesDeUnidadDao:

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor()


    def close_cursor(self):
        self.cursor.close()

    
    def listar(self) -> List[AccionesDeUnidad]:
        listaAccionesDeUnidad = []
        
        self.cursor.callproc('ACCIONES_DE_UNIDAD_CON_COSTO')
        
        for resultado in self.cursor.stored_results():
            rows = resultado.fetchall()

        for row in rows:
            row = cast(Dict[str, Any], row)

            acciones = AccionesDeUnidad(
                id=row["ID"],
                nombre=row["NOMBRE"],
                tipo=row["TIPO"],
                descripcion=row["DESCRIPCION"],
                industria=row["INDUSTRIA"],
                riqueza=row["RIQUEZA"]
            )

            listaAccionesDeUnidad.append(acciones)

        self.close_cursor()
        self.cursor = self.db.cursor()

        return listaAccionesDeUnidad
    

    def modificar(self, accion: AccionesDeUnidad):

        self.cursor.callproc('MODIFICAR_ACCION_DE_UNIDAD',
            (
            accion.getId(),
            accion.getNombre(),
            accion.getTipo(),
            accion.getDescripcion(),
            accion.getIndustria(),
            accion.getRiqueza()
            )
        )

        self.db.commit() #Esto se debe poner tras ejecutar el prodecidimiento, siempre que se trate de un ALTER, DELETE o INSERT.
        self.close_cursor()
        self.cursor = self.db.cursor()


    def buscarXnombre(self, nombre: str, tipo: int) -> Optional[AccionesDeUnidad]: 
    #Existe una forma de crear un menu de seleccion donde puedan marcar especifcamene que quieren modificar, revisar mas adelante.

        self.cursor.callproc("ACCION_DE_UNIDAD_X_NOMBRE", (nombre, tipo))

        for result in self.cursor.stored_results():

            raw_row = result.fetchone()

            if raw_row is None:
                continue

            row = cast(Dict[str, Any], raw_row)

            accion = AccionesDeUnidad(
                id=row["ID"],
                nombre=row["NOMBRE"],
                tipo=row["TIPO"],
                descripcion=row["DESCRIPCION"],
                industria=row["INDUSTRIA"],
                riqueza=row["RIQUEZA"]
            )

            self.close_cursor()
            self.cursor = self.db.cursor()

            return accion

        self.close_cursor()
        self.cursor = self.db.cursor()
        return None
    

    def agregar(self, nombre, tipo, descripcion, industria, riqueza) -> int:
        self.cursor.execute(
            "CALL AGREGAR_ACCION_DE_UNIDAD(%s,%s,%s,%s,%s)",
            (nombre, tipo, descripcion, industria, riqueza)
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
    

    def eliminar(self, nombre, tipo):

        self.cursor.callproc("ELIMINAR_ACCION_DE_UNIDAD", (nombre, tipo))

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