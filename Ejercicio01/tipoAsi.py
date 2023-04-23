class TipoAsiento:

    def __init__(self, asiento = "Tradicional", porcentaje = 0.10):
        """
        Método constructor de la clase
        Params:
            asiento(str)opcional: Nombre del tipo de asiento
            porcentaje(float)opcional: Porcentaje del tipo de asiento
        """
        self.__asiento = asiento
        self.__porcentaje = porcentaje

    def get_asiento(self):
        """
        Método get para el nombre del tipo de asiento
        Params:
            None.
        Return:
            self.__asiento(str): Nombre del tipo de la clase
        """
        return self.__asiento

    def get_porcentaje(self):
        """
        Método get para el porcentaje del tipo de asiento
        Params:
            None.
        Return:
            self.__porcentaje(float): Porcentaje del tipo de la clase
        """
        return self.__porcentaje

