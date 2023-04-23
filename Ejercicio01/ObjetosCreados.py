#-------------------------Archivos de reservación hotel-----------------------------------
from reservacionesHotel.funciones import *
from reservacionesHotel.usuario import *
#-------------------------Archivos de reservación hotel-----------------------------------
from reservacionesHotel.tipoHab import *
from reservacionesHotel.habitacion import *
from reservacionesHotel.hotel import *

#-------------------------Archivos de reservación vuelo-----------------------------------
from tipoAsi import TipoAsiento
from asiento import Asiento
from destino import Vuelo_destino
from vuelos import Reservar_vuelos

#-----------------------------------HOTEL-------------------------------------------------

#--------------------------------4 tipos de habitaciones----------------------------------
tipo = [TipoHab(1,400),TipoHab(2,550),TipoHab(3,750),TipoHab(4,1000)]

#--------------70 habitaciones, 15 ind, 15 dos, 10 tres, 30 cuatro peronas ---------------
habitaciones = []
j = 0
k = 0
hab = 0
for i in range(70):
    # aux es el dígito que indica el piso 
    if i < 10:
        aux = "0" #planata baja piso 0, 10 habitaciones
    else:
        aux = str(i)[0] 
    j += 1
    if j == 10:
        num = aux + str(j)
        j = 0
    else:
        #Para dígitos menores a 10
        num = aux + "0" + str(j)
        
    if k == 15 and hab == 0:
        k = 0
        hab += 1
    elif k == 15 and hab == 1:
        k = 0
        hab += 1
    elif k == 10 and hab == 2:
        k = 0
        hab += 1
    k += 1
    #Lista de 70 habitaciones para el Hotel, el tipo de habitación es aleatorio
    habitaciones.append(Habitacion(tipo[hab],num))

#----------------------------------un hotel------------------------------------------------
hotel = Hotel(habitaciones)





#-----------------------------------VUELO--------------------------------------------------

#---------------------------------Dos tipos de asiento-------------------------------------
tipoAsiento = [TipoAsiento("Tradicional",0.10),TipoAsiento("VIP",0.50)]

#---------------------------------50 asientos----------------------------------------------
asientos = []
j = 0
for i in range(51):
    #-------------------30 tradicionales-----------------
    if i <= 30:
        aux = "T"
        tipo = tipoAsiento[0]
    #-------------------20 VIP-----------------
    else:
        aux = "V"
        tipo = tipoAsiento[1]

    j += 1
    if j >= 10 and j <= 30:
        num = aux + str(j)
    elif j > 30:
        j = 0
        continue
    else:
        num = aux + "0"+ str(j)

    asientos.append(Asiento(tipo,num)) #Lista con 50 asientos

#------------------------------------Tres destinos-----------------------------------------
destinos = [Vuelo_destino("New York",13989,asientos),\
            Vuelo_destino("Cancún",959,asientos),\
            Vuelo_destino("LA",6489,asientos)]

#-------------------------------------un usuario-------------------------------------------
fer = Usuario("Fernando Ortega", 21, "ferd.fernando@gmail.com", "5574938294")

#-------------------------------------un vuelo---------------------------------------------
vuelo = Reservar_vuelos(destinos)







