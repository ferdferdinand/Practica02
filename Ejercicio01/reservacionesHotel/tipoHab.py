class TipoHab:

    def __init__(self,capacidad = 1, precio = 400):
        """
        Método constructor de la clase TipoHab

        Params:
            capacidad(int): Capacidad del tipo de habitación
            precio(int): Precio de la habitación
        Returns:
            None.
        """
        self.__nombre = str
        self.__capacidad = capacidad
        self.__precio = precio

        self.set_nombre() #Actualizamo el nombre de la habitación 

    def set_nombre(self):
        """
        Método set para el nombre la habitación

        Params:
            None.
        Returns:
            None.
        """
        
        if self.__capacidad == 1:
            self.__nombre = "Habitación individual"
        elif self.__capacidad == 2:
            self.__nombre = "Habitación para dos personas"
        elif self.__capacidad == 3:
            self.__nombre = "Habitación para tres personas"
        else:
            self.__nombre = "Habitación para 4 personas"

    def get_nombre(self):
        """
        Método get para el nombre la habitación

        Params:
            None.
        Returns:
            self.__nombre(str): Nombre de la habitación
        """
        return self.__nombre


    def get_cap(self):
        """
        Método get para la capacidad la habitación

        Params:
            None.
        Returns:
            self.__capacidad(int): Capacidad de la habitación
        """
        return self.__capacidad
    

    def get_precio(self):
        """
        Método get para el precio la habitación

        Params:
            None.
        Returns:
            self.__precio(int): Precio de la habitación
        """
        return self.__precio
