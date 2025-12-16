import mysql.connector
from typing import Dict, Any, cast, List, Optional
from dao.database import Database
from models.edificacion import Edificacion

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


    def agregar(self,nombre, descripcion, efecto, industria, riqueza, riqXturno):

        resultado = 0
        
        resultado_sp = self.cursor.callproc('AGREGAR_EDIFICACION',
            (
            nombre,
            descripcion,
            efecto,
            industria,
            riqueza,
            riqXturno,
            resultado #Aca se guarda despues el valor del return del SP
            )
        )

        if resultado_sp is None:
            self.close_cursor()
            self.cursor = self.db.cursor()
            return -1

        resultadoTupla = tuple(resultado_sp) #Transformamos a una tupla para que Pylance no se queje
        out = resultadoTupla[-1] #Guardamos el valor OUT del SP, que siempre es el ultimo (por eso el -1)

        resultado: int = 1 if out == 1 else 0 #Como sabemos que el valor OUT SIEMPRE es o 1 o 0, lo ponemos de esta forma para que Pylance no se queje

        self.db.commit() #Esto se debe poner tras ejecutar el prodecidimiento, siempre que se trate de un ALTER, DELETE o INSERT.
        self.close_cursor()
        self.cursor = self.db.cursor()
        return resultado