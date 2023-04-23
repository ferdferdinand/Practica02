from reservacionesHotel.funciones import *
from random import *

class Vuelo_destino:

    def __init__(self, destino:str, costo:int, asientos:list):
        """
        Método constructor de la clase.
        Params:
            destino(str): Nombre del destino 
            costo(int): Costo base del destino
            asientos(list): Asientos por destino
        """
        self.__detino = destino
        self.__costo = costo
        self.__asientos = asientos
        self.__fechas = sample(fechas_disponibles(),10) #10 elementos aleatorios de una lista
        self.__precioAT = int
        self.__precioAV = int

        self.set_precios()

    def get_destino(self):
        """
        Método get para el nombre del destino
        Params:
            None.
        Returns:
            self.__detino(str): Nombre del destino
        """
        return self.__detino

    def get_asientos(self):
        """
        Método get para los asientos del destino
        Params:
            None.
        Returns:
            self.__asientos(list): Lista de objetos asiento del destino
        """
        return self.__asientos

    def get_fechas(self):
        """
        Método get para las fechas disponibles del destino
        Params:
            None.
        Returns:
            self.__fechas(list): Lista de objetos date del destino
        """
        return self.__fechas

    def set_precios(self):
        """
        Método set para calcular el precio de los asientos tradicional y VIP del destino
        Params:
            None.
        Returns:
            None.
        """
        aux = []
        for asiento in self.__asientos:
            if asiento.get_tipo() not in aux:
                aux.append(asiento.get_tipo())
        self.__precioAT = round(self.__costo * (1 + aux[0].get_porcentaje())) #int
        self.__precioAV = round(self.__costo * (1 + aux[1].get_porcentaje())) #int

    def get_precioAT(self):
        """
        Método get para obtener el precio del asiento tradicional del destino
        Params:
            None.
        Returns:
            self.__precioAT(int): Precio del asiento tradicional para este destino
        """
        return self.__precioAT
    
    def get_precioAV(self):
        """
        Método get para obtener el precio del asiento VIP del destino
        Params:
            None.
        Returns:
            self.__precioAV(int): Precio del asiento VIP para este destino
        """
        return self.__precioAV

    def __str__(self):
        """
        Método str de la clase destino.
        Params:
            None.
        Return:
            cadena(str): Información del destino: fechas y precios
        """
        cadena = ""
        cadena += self.__detino + '\n\nFechas Disponibles:\n'
        
        for fecha in self.__fechas:
            cadena += str(fecha) + '\n'
            
        cadena += '\nAsientos:\nTradicional: $' + format(self.__precioAT,",d") + \
                  '\nVIP: $' + format(self.__precioAV,",d") + '\n\n'

        return cadena

        

    
        
        

    


