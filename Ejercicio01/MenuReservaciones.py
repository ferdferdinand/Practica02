
#Creamos los objetos 
from ObjetosCreados import *

fecha = None

while True:
    print("1. Ver los destinos disponibles") #mostrar destino, precio por asiento
    print("2. Reservar destino") #Ingresar destino, número de asientos, y tipo de asiento
    print("3. Cancelar asiento")
    print("4. Resumen reservación")
    print("5. Salir\n")
    op = int(input("Ingresa una opción: "))
    match op:

        case 1:
            print('-'*80,'\n','\nDestinos y fechas Disponibles:\n')
            print(vuelo.mostrar_destinos())
            
        case 2:
            print('-'*80,'\n','\nReservar vuelo:\n')
            destino = int(input('Escribe el número del destino deseado: '))
            if fecha is None:
                fecha = input("Ingrese la fecha que desea reservar reservación, el el formato dd-mm-aaaa: ")
                fecha = validarFecha(fecha)
                while type(fecha) is str or fecha < date.today() or not vuelo.fecha_disponible(destino, fecha):
                    print("Fecha inválida")
                    fecha = input("Ingrese la fecha que desea reservar reservación, el el formato dd-mm-aaaa: ")
                    fecha = validarFecha(fecha)
            tipo = input('Escribe el tipo de asiento deseado (Tradicional / VIP): ')
            cantidad = int(input('Escribe la cantidad de asientos a reservar: '))
            print()
            
            if vuelo.reservar(fer, destino, fecha, tipo, cantidad):
                print(f"Asientos {tipo} reservados\n")
                ##Si se realizó la reservación de vuelos seguimos con las habitaciones
                hab = habReservar(cantidad) #Función para saber cuántas habitaciones necesitamos de cada tipo (dentro del módulo funciones.py)
                print(f"{sum(hab)} habitaciones reservadas: \n\n")
                for cantidad in hab:
                    for i in range(cantidad):
                        cap = hab.index(cantidad)+1
                        if hab.count(cantidad) > 1:
                            hab[hab.index(cantidad)] = 0
                        hotel.reservar(cap,fecha,fer)
                
            
        case 3:
            print('-'*80,'\n','\nCancelar asientos:\n')
            cantidad = int(input('Escribe la cantidad de asientos a cancelar: '))
            restante = fer.cantidad_asiento() - cantidad
            vuelo.cancelar(fer, cantidad)
            hotel.cancelar(fer)
            #Se reservan habitaciones para el resto de personas que siguen en el vuelo
            if restante > 0:
                hab = habReservar(restante)
                print(f"{sum(hab)} habitaciones reservadas: \n\n")
                for cantidad in hab:
                    for i in range(cantidad):
                        cap = hab.index(cantidad)+1
                        if hab.count(cantidad) > 1:
                            hab[hab.index(cantidad)] = 0
                        hotel.reservar(cap,fecha,fer)
            
        case 4:
            print('-'*80,'\n')
            vuelo.resumen(fer)
            
        case 5:
            break
