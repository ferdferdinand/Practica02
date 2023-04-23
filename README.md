# Práctica02
## Solución práctica02 programación 
### Author: Ferd Fernando

## Clases para la reservación de una habitación en una fecha.

-------------------HOTEL------------------

+ TipoHab: Es la clase que define los 4 tipos de habitaciones que hay en el hotel dependiendo de su capacidad, y precio.

+ Habitacion: Es la clase donde se guarda la reservación del usuario en una fecha dada, contiene la información del tipo de habitación al que corresponde y sus datos de localización, es decir, el número de habitación, y el piso en que está situada.

+ Hotel: Es la clase donde se almacenan todas las habitaciones, a través de esta clase podemos hacer las reservaciones, obtener los datos de la habitación, y crear el resulmen de reserva.

+ pruebaHabitaciones: Es un script para probar las reservaciones exclusivamente de las habitaciones.

+ funciones: Es un arvchivo que contiene funciones de ayuda para las fechas de las reservaciones por habitación

## Clases para la reservación de un un asiento en una fecha de un destino.

-------------------VUELO------------------------
+ TipoAsiento: Es la clase que define los 2 tipos de asiento que tenemos para el vuelo, aquí obtenemos el porcentaje que va a aumentar en cada destino.

+ Asiento: Es la clase donde se guarda la información de la reservación que hace un usuario en una fecha dada, además contiene la información del tipo de asiento y su número de asiento.

+ Vuelo_destino: Es la case que junta los 50 asientos que tiene nuestro vuelo a un destino determinado, guarda la información del precio base del destino y calcula los precios por el tipo de asiento.
Mantiene la información de las fechas en las que el vuelo tendrá lugar.

+ Reservar_vuelos: Es la clase donde tenemos nuestros 3 vuelos disponibles, apartir de aquí se accesa a la información de cada destino y a su vez de cada asiento. Se encarga de llevar a cabo la reservación que el usuario hace y la cancelación en caso de ser necesaria.

+ pruebaVuelos: Es un script para probar las reservaciones exclusivamente de los vuelos (Esto es básicamente cómo tendrían que estar sus prácticas ya que quité la parte del hotel en la versión final que les dejé).

## Clases para guarlar la reservación de un usuario.

---------------------------Usuario---------------------------
+ Usuario: Es clase que define al usuario con su información, y las revervaciones que hace, tanto de hotel como de vuelo. Esta clase se encarga de sólo guardar la información de los asientos y habitaciones que ya han sido reservadas. Así podemos obtener un resumen de lo que ya está reservado.


## Menú de pruebas para la reservación de un un asiento y una habitación en una fecha de un destino.

--------------------------MenuReservaciones---------------------

+ ObjetosCreados: Es un script que se encarga de crear todos los objetos que vamos a utilizar en nuestra prueba. Los 4 tipos de habitaciones, las 70 habitaciones, un hotel, un usuario, los dos tipos de asientos, los 50 asientos por destino, los 3 destinos y un vuelo.

+ MenuReservaciones: Es un script donde podemos reservar los asientos de un vuelo y automáticamente se reservan las habitaciones que requerimos para el número de personas que nos acompañan. (Esta es la versión que originalmente les había pedido como práctica, realmente los cambios son muy ligeros).



