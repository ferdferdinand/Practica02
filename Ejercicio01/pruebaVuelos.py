
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
            
            
        case 3:
            print('-'*80,'\n','\nCancelar asientos:\n')
            cantidad = int(input('Escribe la cantidad de asientos a cancelar: '))
            vuelo.cancelar(fer, cantidad)
            
        case 4:
            print('-'*80,'\n')
            vuelo.resumen(fer)
            
        case 5:
            break
