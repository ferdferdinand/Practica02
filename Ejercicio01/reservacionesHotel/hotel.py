#from funciones import fechas_disponibles as fechas

class Hotel:
    
    def __init__(self,habitaciones:list):
        """
        Método constructor de la clase

        Params:
            habitaciones(list): Lista con objetos Habitacion
        """
        self.__habitaciones = habitaciones


    #reservar habitacion por tipo y fecha, reservación de un día
    def reservar(self,cap:int,fecha,usuario):
        """
        Método para reservar una habitación
        Params:
            cap(int): Capacidad de la habitación a reservar
            fecha(date): Fecha de la reservación (limitada a un día)
            usuario(objet): Objeto del usuario
        Returns:
            None
        """
            
        for habitacion in self.__habitaciones:
            if habitacion.get_tipo().get_cap() == cap:
                if habitacion.get_status(fecha):
                    habitacion.set_status(fecha)
                    print("Resumen reservación: ",habitacion,sep = "\n",end = "\n\n")
                    usuario.reservarHab(habitacion,fecha)
                    break
            elif habitacion == self.__habitaciones[-1]:
                print(f"No hay habitaciones disponibles en la fecha {fecha}\n")
                for habitacion in self.__habitaciones:
                    if habitacion.get_tipo().get_cap() == cap:
                        print(f"Las fechas disponibles para {habitacion.get_tipo().get_nombre()} personas son:")
                        for fechas in habitacion.fechas_disponibles():
                            print(fechas)
                        break

    def capacidad(self,tipo:int):
        """
        Método para obtener la capacidad de la habitación, a partir de la opción elegida
        por el usuario en el menú, así podemos usar el método reservar.
        
        Params:
            tipo(int): tipo de habitación (nombre) (índice de la lista del método tipo_habitaciones_dis())
        Returns:
            capacidad(int): Capacidad de la habitación
        """
        hab = self.tipo_habitaciones_dis()
        
        if tipo > 0 and tipo <= len(hab):
            tipo = hab[tipo - 1]
            
        for habitacion in self.__habitaciones:
            if habitacion.get_tipo().get_nombre() == tipo:
                return habitacion.get_tipo().get_cap()
                

    def tipo_habitaciones_dis(self):
        """
        Método para mostrar los tipos de habitaciones en el hotel
        
        Params:
            None.
        Returns:
            disp(list): Lista con los nombres de los tipos de habitaciones disponibles en el hotel
        """
        disp = []
        for habitacion in self.__habitaciones:
            aux = habitacion.get_tipo().get_nombre()
            if aux not in disp:
                disp.append(aux)
        return disp
    

    def precios(self):
        """
        Método para obtener los precios de las habitaciones

        Params:
            None.
        Returns:
            disp(list): Lista con los precios de las habitaciones disponibles en el hotel (como el método anterior)
        """
        disp = []
        for habitacion in self.__habitaciones:
            aux = habitacion.get_tipo().get_precio()
            if aux not in disp:
                disp.append(aux)
        return disp
    
    #Se cancelan todas las habitaciones
    def cancelar(self,usuario):
        """
        Método para cancelar las reservaciones del usuario

        Params:
            usuario(Objet): Un usuario
        Returns:
            None.
        """
        habitaciones = usuario.get_habitaciones()
        copia = habitaciones.copy() #Copia porque se modifica la lista de habitaciones entonces ya no sirve el for
        fecha = usuario.get_fecha()
        for hab in copia:
            for habitacion in self.__habitaciones:
                if habitacion == hab:
                    habitacion.set_status(fecha)
                    print(f"{habitacion.get_tipo().get_nombre()} cancelada\n")
            usuario.cancelar(hab)      

    def resumen(self,usuario):
        """
        Método para el resumen de la reservación

        Params:
            Usuario(Objet): Un usuario
        Return:
            None
        """
        if usuario.get_habitaciones() == []:
            print("No hay reservaciones\n\n")
        else:
            print(f"Resumen de reservación: \n\n{usuario}")


    
