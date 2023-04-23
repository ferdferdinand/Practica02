class Usuario:

     def __init__(self, name:str, age: int, email:str, tel: str):
         self.__nombre = name
         self.__edad = age
         self.__correo = email
         self.__telefono = tel
         self.__habitaciones = []
         self.__fechaRes = None
         self.__asientos = []
         self.__destino = None


     def get_fecha(self):
          return self.__fechaRes
     
     ##------------------habitaciones-----------------

     def reservarHab(self,hab,fecha):
          self.__habitaciones.append(hab)
          self.__fechaRes = fecha

     def get_habitaciones(self):
          return self.__habitaciones

     def cancelar(self,hab):
          self.__habitaciones.remove(hab)

     def totalHab(self):
          total = 0
          for hab in self.__habitaciones:
               total += hab.get_tipo().get_precio()
          return total


     #-------------------Asientos-----------------

     def set_destino(self, destino:object):
        """
         Método set para el destino
         Params:
             destino(object): nuevo objeto de la clase destino
         Returns:
             None.
         """
        self.__destino = destino

     def get_destino(self):
        """
         Método get para el destino
         Params:
             None.
         Returns:
             self.__destino(Object): destino seleccionado por el usuario
         """
        return self.__destino

     def reservarAsi(self,asiento:object,fecha:object): 
          """
          Método para reservar asientos por fecha, añade los asientos a una lista
          Params:
              asiento(object): asiento que se reserva y se añade a una lista
              fecha(object): fecha de reservación
          Returns:
              None.
          """
          self.__asientos.append(asiento)
          self.__fechaRes = fecha


     def get_asientos(self):
          """
          Método get para los asientos
          Params:
              None.
          Returns:
              self.__asientos(list): lista que contiene objetos asiento 
          """
          return self.__asientos

     def cantidad_asiento(self):
        """
          Método que obtiene la cantidad de asientos que se van a reservar
          Params:
              None.
          Returns:
              len(self.__asientos)(int): numero entero de asientos 
          """
        return len(self.__asientos)

     def cancelarAsi(self,asiento:object):
          """
          Método para cancelar asientos reservados
          Params:
              asiento(object): asiento del que se desea cancelar la reservación
          Returns:
              None.
          """
          self.__asientos.remove(asiento)

     def totalAsientos(self):
          """
          Método que calcula el costo total por los asientos reservados
          Params:
              None.
          Returns:
              total(float): variable que guarda la suma del precio de los asientos reservados
          """
          total = 0
          for asiento in self.__asientos:
               tipo = asiento.get_tipo().get_asiento()
               if tipo == 'Tradicional':
                   total += self.__destino.get_precioAT()
               else:
                    total += self.__destino.get_precioAV()
          return total
     

     #-----------------------str----------------------------------------

     def __str__(self):
          habs = ""

          for hab in self.__habitaciones:
               habs += str(hab)+ "\n\n"

          asis = ""

          for asiento in self.__asientos:
               asis += str(asiento)+ "\n"
               
          return f"Reservación para el {self.__fechaRes} con destino a {self.__destino.get_destino()}\n" +\
                 "Nombre: " + self.__nombre + "\n" +\
                 "Edad: " + str(self.__edad) + "\n" +\
                 "Correo: " + self.__correo + "\n" +\
                 "Telefono: " + self.__telefono + "\n\n"+\
                 habs +\
                 "Total habitaciones: $" + format(self.totalHab(),",d") + "\n\n"+\
                 f"Asientos: \n\n{asis}" + "\n" + \
                 "Total asientos: $" + format(self.totalAsientos(),",d") + "\n\n"+\
                 "Total: $" + format(self.totalHab()+self.totalAsientos(),",d") + "\n\n"
                 
          
          
          
     

    
