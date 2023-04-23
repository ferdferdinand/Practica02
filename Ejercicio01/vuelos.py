

class Reservar_vuelos:
    
    def __init__(self, destinos:list):
        """
        Método constructor para la clase Vuelo.
        Params:
            Destinos(list) = Lista de Objetos de la clase Destinos
        Return:
            None.
        """
        self.__destinos = destinos
    
    def mostrar_destinos(self):
        """
        Método que muestra los destinos disponibles.
        Params:
            None.
        Return:
            u(str): Información de todos los destinos
        """
        u = ''
        x = 1
        for destino in self.__destinos:
            u += str(x)+ '. ' + str(destino) #Se está usando el método str de la clase destino
            x += 1
        return u 
        
    def fecha_disponible(self,destino:int, fecha:object):
        """
        Método que muestra las fechas disponibles por cada destino
        Params:
            destino(str): destino deseado
            fecha(object): fecha objeto date
        Return:
            bool: Si la fecha está disponible en el destino
        """
        destino = self.__destinos[destino - 1]
        return fecha in destino.get_fechas()
    
        
    def reservar(self, usuario:object, destino:int, fecha:object, tipo:str, cantidad:int):
        """
        Método para reservar los asientos de un vuelo
        Params:
            usuario(object): un usuario
            destino(int): destino deseado
            fecha(object): fecha que se reserva
            tipo(str): tipo de asientos
            cantidad(int): cantidad de asientos que se reservan
        Return:
            bool: Si se llevó a cabo la reservación o no.
        """
        destino = self.__destinos[destino - 1]
        usuario.set_destino(destino)
        for i in range(cantidad):
            for asiento in destino.get_asientos():
                if asiento.get_tipo().get_asiento() == tipo:
                    if asiento.get_status(destino.get_fechas(), fecha):
                        asiento.set_status(destino.get_fechas(), fecha)
                        usuario.reservarAsi(asiento, fecha)
                        break
                    elif asiento == destino.get_asientos()[-1]:
                        print(f'No hay asientos {tipo} disponibles\n')
                        return False
        return True
                        
    def cancelar(self, usuario:object, cantidad:int):
        """
        Método para cancelar la reservación de los asientos de un vuelo
        Params:
            usuario(object): un usuario
            cantidad(int): cantidad de asientos se cancelan
        Return:
            None.
        """
        destino = usuario.get_destino()
        copia = usuario.get_asientos().copy()
        fecha = usuario.get_fecha()
        
        if usuario.cantidad_asiento() == cantidad:
            usuario.set_destino(None)
        elif cantidad > usuario.cantidad_asiento():
            cantidad = usuario.cantidad_asiento()
            
        for i in range(cantidad):
            asiento = copia[i]
            for asiento1 in destino.get_asientos():
                if asiento1 == asiento:
                    asiento1.set_status(destino.get_fechas(),fecha)
                    print(f"Asiento: {asiento1.get_num()} cancelado\n")
            usuario.cancelarAsi(asiento)

    def resumen(self,usuario):
            """
            Método para el resumen de la reservación
            Params:
                Usuario(Objet): Un usuario
            Return:
                None.
            """
            if usuario.get_asientos() == []:
                print("No hay reservaciones\n\n")
            else:
                print(f"Resumen de reservación: \n\n{usuario}")
        
