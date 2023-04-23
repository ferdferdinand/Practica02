"""
Funciones auxiliares para la las fechas de las reservaciones
"""

from datetime import date
from datetime import timedelta
import random as rd



#------------------------------Funciones para habitaciones-----------------------------

def habReservar(cantidad):
    """
    Calcula cuantas habitaciones hay que reservar de cada tipo

    Params:
        cantidad(int): Cantidad de personas a hospedar
    Returns:
        hab(list): Lista con la cantidad de habitaciones que se necesitan de cada tipo de habitación
    """
    personas = [4,3,2,1]
    hab = []
    aux2 = cantidad
    for persona in personas:
        aux1 = int(aux2//persona)
        aux2 %= persona
        hab.append(aux1)
    hab.reverse() #Lista con el número de habitaciones a reservar por cada tipo de habitación
    return hab


def fechas_disponibles():
    """
    Función que calcula los próximos 31 días a partir de la fecha de hoy

    Params:
        None
    Returns:
        fechas(list): lista con objetos tipo date de la paquetería datetime
    """
    fechas = []
    hoy = date.today()
    for i in range(31):
        dia = timedelta(i) # Un día, dos días etc
        fechas.append(hoy + dia)
    return fechas


def reservaciones(n):
    """
    Función que nos regresa una lista de booleanos, harán match con las fechas

    Params:
        None.
    Returns:
        reservaciones(list): Lista de booleanos
    """
    reservaciones = []
    for i in range(n):
        #Con esta parte de código podemos aleatorizar entre True o False para hacer más dinámico nuestro hotel.
        valor = rd.randrange(0,2) #valores 0 y 1 aleatorios
        #print(bool(valor)) #Los valores 0 y 1 se pueden castear a booleanos y el 0 equivale a False, 1 a True
        #Si queremos todas las fechas disponibles al crear los objetos llenamos la lista de True
        #append(True)
        reservaciones.append(bool(valor))
    return reservaciones


def encontrar(fechas,date):
    """
    Función para encontrar el índice en la lista de la fecha dada.
    En ese índice buscaremos la reservación
    Params:
        fechas(list): Lista con las objetos tipo date
        date(date): Fecha que queremos buscar
    Returns:
        indice(int): índice donde se encuentra la fecha buscada
    """
    indice = fechas.index(date)
    return indice


def encontrar2(fechas,reservaciones):
    """
    Función para encontrar únicamente con las fechas disponibles
    Params:
        fechas(list): Lista con las objetos tipo date
        reservaciones(list): Lista de con booleanos
    Returns:
        disp(list): Lista únicamente con las fechas disponibles
    """
    disp = []
    for i in range(len(fechas)):
        if reservaciones[i]: #Si es verdadero en esa posición la fecha está disponible
            disp.append(fechas[i])
    return disp


def validarFecha(fecha:str):
    """
    Validar si una fecha es correcta, para poder crear objeto tipo date
    
    Params:
        fecha(str): fecha en formato dd-mm-aaaa
    Returns:
        date: fecha como un objeto date de datetime si la fecha es válida
        str: mensaje si la fecha no es válida
    """
    #Encontramos el separador
    if fecha[:2].isdigit():
        sep = fecha[2:3]
    else:
        sep = fecha[1:2]
    #Separamos la los valores 
    fecha = fecha.split(sep)

    meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

    #Asignamos valor numérico al mes
    i = 1
    for mes in meses:
        if fecha[1] in mes:
            fecha[1] = str(i)
        elif i >= 12 and not fecha[1].isdigit():
            fecha[1] = 13
        i += 1

    #Casteamos nuestras variables a datos enteros
    dia = int(fecha[0])
    mes = int(fecha[1])
    anio = int(fecha[2])

    #En particular para años como 23, lo tomamos como 2023, para años como 70 lo tomamos como 1970
    if len(str(anio)) < 4:
        if anio < 70:
            anio += 2000
        else:
            anio += 1900

    d, m, a = False, False, False

    #Validamos que el día dado esté en su intervalo según el mes correspondiente
    if mes == 4 or mes == 6 or mes == 9 or mes ==11:
        #Para los meses de 30 días
        if dia > 0 and dia <= 30:
            d = True

    #La cantidad de días de febrero depende del año
    if mes == 2:
        #Para años bisiestos
        if anio%4 == 0:
            if dia > 0 and dia <= 29:
                d = True
        #Para los demás años
        else:
            if dia > 0 and dia <= 28:
                d = True
    #Para los meses de 31 días
    else:
        if dia > 0 and dia <= 31:
            d = True

    #Validamos que el mes esté en el intervalo [1,12]
    if mes > 0 and mes <= 12:
        m = True

    #Validamos el año
    if anio > 0:
        a = True

    #Si el día, el mes y año son correctos, la fecha es correcta
    if d and m and a :
        #Regresamos la fecha comoun objeto date de datetime
        return date(anio,mes,dia)

    #Si alguno es falso, la fecha es incorrecta
    else:
        #Regresamos str
        return "Fecha no válida"











