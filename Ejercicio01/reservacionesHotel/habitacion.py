from funciones import * #Importamos las funciones auxiliares para fechas

class Habitacion:

    def __init__(self, tipo: object, numHab: str):
        """
        Método constructor de la clase

        Params:
            tipo(objet): Objeto TipoHab
            numHab(str): Número de la habitación
        """
        self.__tipoHab = tipo
        self.__numHab = numHab
        self.__piso = str
        self.__fecha = fechas_disponibles()
        self.__reservaciones = reservaciones(31)#Pequeño cambio para poder usar la misma función con vuelo
        
        self.set_piso() #Actualizamos el piso

    def get_status(self,date):
        """
        Método get para el status de la habitación por fecha

        Params:
            date(date): Objeto date (fecha que queremos revisar)
        Returns:
            status(bool): Si la habitación está disponible en dicha fecha
        """
        indice = encontrar(self.__fecha,date)
        status = self.__reservaciones[indice]
        return status
        
    def set_status(self,date):
        """
        Método set para el status de la habitación por fecha

        Params:
            date(date): Objeto date (fecha que queremos revisar)
        Returns:
            None.
        """
        indice = encontrar(self.__fecha,date)
        status = self.__reservaciones[indice]
        self.__reservaciones[indice] = not status

    def get_numHab(self):
        """
        Método get para el número de habitación

        Params:
            None.
        Returns:
            self.__numHab(str): Número de la habitación
        """
        return self.__numHab

    def set_piso(self):
        """
        Método set para el piso de habitación

        Params:
            None.
        Returns:
            None.
        """
        if self.__numHab[0] == "0":
            self.__piso = "Planta baja"
        elif self.__numHab[0] == "1":
            self.__piso = "Primer piso"
        elif self.__numHab[0] == "2":
            self.__piso = "Segundo piso"
        elif self.__numHab[0] == "3":
            self.__piso = "Tercer piso"
        elif self.__numHab[0] == "4":
            self.__piso = "Cuarto piso"
        elif self.__numHab[0] == "5":
            self.__piso = "Quinto piso"
        elif self.__numHab[0] == "3":
            self.__piso = "Sexto piso"

    def get_piso(self):
        """
        Método get para el piso de habitación

        Params:
            None.
        Returns:
            self.__piso(str): Piso en que se encuentra la habitación
        """
        return self.__piso

    def get_tipo(self):
        """
        Método get para el tipo de habitación

        Params:
            None.
        Returns:
            self.__tipoHab(objet): Tipo de habitación
        """
        return self.__tipoHab

    def fechas_disponibles(self):
        """
        Método para obtejer las fechas que tienen disponibilidad de reserva

        Params:
            None.
        Returns:
            disp(list): Fechas disponibles
        """
        disp = encontrar2(self.__fecha,self.__reservaciones)
        return disp


    def __str__(self):
        """
        Método str de la clase.

        Params:
            None.
        Return
            str: Los datos de la habitación para el resumen de la misma
        """
        return f"Habitación {self.get_numHab()}" + "\n" + \
               "Piso: " + self.get_piso() + "\n" +\
               "Tipo: " + self.get_tipo().get_nombre() + "\n" +\
               "Precio: $" + str(self.get_tipo().get_precio())
