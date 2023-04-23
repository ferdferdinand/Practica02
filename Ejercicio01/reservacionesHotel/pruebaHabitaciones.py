from hotel import Hotel
from usuario import Usuario
from habitacion import Habitacion
from tipoHab import TipoHab

from funciones import *

#----------------------------------CREACIÓN DE OBJETOS----------------------------------
#--------------------------------4 tipos de habitaciones--------------------------------
tipo = [TipoHab(1,400),TipoHab(2,550),TipoHab(3,750),TipoHab(4,1000)]

#--------------70 habitaciones, 15 ind, 15 dos, 10 tres, 30 cuatro peronas -------------
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

#----------------------------------hotel------------------------------------------------
hotel = Hotel(habitaciones)

#----------------------------------usuario----------------------------------------------
fer = Usuario("Fernando Ortega", 21, "ferd.fernando@gmail.com", "5574938294")

fecha = None

while True:
    print("1. Ver tipos de habitaciones disponibles")
    print("2. Reservar habitación")
    print("3. Cancelar toda la reservación resevación")
    print("4. Resumen de la reservación")
    print("5. Para salir\n")
    opc = int(input("Ingrese la opción que desea consultar: "))
    print()

    if opc == 1:
        hab = hotel.tipo_habitaciones_dis()
        precio = hotel.precios()
        for i in range(len(hab)):
            print(f"{i+1}. {hab[i]} ${precio[i]}")
        print()
        
    elif opc == 2:
        #índice en en la lista de los tipos de habitaciones
        hab = int(input("Ingrese el número del tipo de habitación que desea reservar: "))
        if fecha is None:
            fecha = input("Ingrese la fecha que desea reservar reservación, el el formato dd-mm-aaaa: ")
            fecha = validarFecha(fecha)
            while type(fecha) is str or fecha < date.today():
                print("Fecha inválida")
                fecha = input("Ingrese la fecha que desea reservar reservación, el el formato dd-mm-aaaa: ")
                fecha = validarFecha(fecha)
        print()
        cap = hotel.capacidad(hab)
        hotel.reservar(cap,fecha,fer)
        print()
        
    elif opc == 3:
        hotel.cancelar(fer)

    elif opc == 4:
        hotel.resumen(fer)

    else:
        break


