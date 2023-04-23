
#El archivo funciones se encuentra dentro de otra carpeta, se importa desde esa carpeta
from reservacionesHotel.funciones import *

class Asiento:

    def __init__(self, tipo:object ,num: str):
        """
        Método constructor
        Params:
            tipo(object): Objeto de la clase TipoAsiento, nos indica el tipo de asiento
            num(str): Es el número de asiento
        Return:
            None.
        """
        self.__tipo = tipo
        self.__num = num
        self.__reservaciones = reservaciones(10)
        
    def get_tipo(self):
        """
        Método get para el tipo de asiento
        Params:
            None.
        Returns:
            self.__tipo(object): Nos regresa el objeto tipo de asiento
        """
        return self.__tipo

    def get_num(self):
        """
        Método get para el número de asiento
        Params:
            None.
        Returns:
            self.__num(str): El número de asiento
        """
        return self.__num

    def get_status(self,fechas,date):
        """
        Método get para el status del asiento en una fecha específica
        Params:
            fechas(list): Lista de fechas disponibles
            date(object): Fecha en que buscamos la disponibilidad del asiento
        Returns:
            status(bool): True si está disponible, False en caso contrario.
        """
        indice = encontrar(fechas,date)
        status = self.__reservaciones[indice]
        return status
        
    def set_status(self,fechas,date):
        """
        Método set para el status del asiento en una fecha específica (cuando se reserva o se cancela)
        Params:
            fechas(list): Lista de fechas disponibles
            date(object): Fecha en que buscamos la disponibilidad del asiento
        Returns:
            None.
        """
        indice = encontrar(fechas,date)
        status = self.__reservaciones[indice]
        self.__reservaciones[indice] = not status

    def __str__(self):
        """
        Método str de la clase.
        Params:
            None.
        Returns:
            str: Los datos del asiento para el resumen del mismo
        """
        return f'Asiento {self.__tipo.get_asiento()} con número {self.__num}'
