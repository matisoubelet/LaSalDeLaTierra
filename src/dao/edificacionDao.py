import mysql.connector
from typing import Dict, Any, cast, List, Optional, Tuple
from dao.database import Database
from dominio.edificacion import Edificacion

class EdificacionDao:

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor()


    def close_cursor(self):
        self.cursor.close()


    def listar(self, num) -> List[Edificacion]:
        listaEdificaciones = []

        # Llamamos al stored procedure segun el numero ingresado
        if num == 0:
            self.cursor.callproc('EDIFICACIONES_CON_COSTO')
        elif num == 1:
            self.cursor.callproc('EDIFICACIONES_INDUSTRIA')
        elif num == 2:
            self.cursor.callproc('EDIFICACIONES_RIQUEZA')
        else:
            self.close_cursor()
            self.cursor = self.db.cursor()
            return listaEdificaciones
        

        for resultado in self.cursor.stored_results():
            rows = resultado.fetchall()

        for row in rows:
            row = cast(Dict[str, Any], row)

            edificacion = Edificacion(
                id=row["ID"],
                nombre=row["NOMBRE"],
                descripcion=row["DESCRIPCION"],
                efecto=row["EFECTO"],
                industria=row["INDUSTRIA"],
                riqueza=row["RIQUEZA"],
                riqXturno=row["RIQ_X_TURNO"]
            )

            listaEdificaciones.append(edificacion)

        self.close_cursor()
        self.cursor = self.db.cursor()

        return listaEdificaciones
    

    def modificar(self, edificacion: Edificacion):

        self.cursor.callproc('MODIFICAR_EDIFICACION',
            (
            edificacion.getID(),
            edificacion.getNombre(),
            edificacion.getDescripcion(),
            edificacion.getEfecto(),
            edificacion.getIndustria(),
            edificacion.getRiqueza(),
            edificacion.getRiqXturno()
            )
        )

        self.db.commit() #Esto se debe poner tras ejecutar el prodecidimiento, siempre que se trate de un ALTER, DELETE o INSERT.
        self.close_cursor()
        self.cursor = self.db.cursor()
    

    def buscarXnombre(self, nombre: str) -> Optional[Edificacion]: 
    #Existe una forma de crear un menu de seleccion donde puedan marcar especifcamene que quieren modificar, revisar mas adelante.

        self.cursor.callproc("EDIFICACION_X_NOMBRE", (nombre,))

        for result in self.cursor.stored_results():

            raw_row = result.fetchone()

            if raw_row is None:
                continue

            row = cast(Dict[str, Any], raw_row)

            edificacion = Edificacion(
                id=row["ID"],
                nombre=row["NOMBRE"],
                descripcion=row["DESCRIPCION"],
                efecto=row["EFECTO"],
                industria=row["INDUSTRIA"],
                riqueza=row["RIQUEZA"],
                riqXturno=row["RIQ_X_TURNO"],
            )

            self.close_cursor()
            self.cursor = self.db.cursor()

            return edificacion

        self.close_cursor()
        self.cursor = self.db.cursor()
        return None
    

    def agregar(self, nombre, descripcion, efecto, industria, riqueza, riqXturno) -> int:
        self.cursor.execute(
            "CALL AGREGAR_EDIFICACION(%s,%s,%s,%s,%s,%s)",
            (nombre, descripcion, efecto, industria, riqueza, riqXturno)
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


    def eliminar(self, nombre):

        self.cursor.callproc("ELIMINAR_EDIFICACION", (nombre,))

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

        


        