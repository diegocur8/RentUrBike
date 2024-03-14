
Funcion RentarBici(hora, duracion)
	Dimension bicicletas_disponibles[24]
	Para i=1 Hasta 24 Hacer
        bicicletas_disponibles[i] = 10
    FinPara
    // Verificar si hay bicicletas disponibles en esta hora
    Si bicicletas_disponibles[hora] > 0 Entonces
        bicicletas_disponibles[hora] = bicicletas_disponibles[hora] - 1
        Escribir "Ha rentado una bicicleta"
    Sino
        Escribir "Lo sentimos, no hay bicicletas disponibles en esta hora."
    FinSi
FinFuncion

Funcion CancelarReserva(hora)
	Dimension bicicletas_disponibles[24]
    // Aumentar el número de bicicletas disponibles para esta hora
    bicicletas_disponibles[hora] = bicicletas_disponibles[hora] + 1
    Escribir "Reserva cancelada. La bicicleta ha sido devuelta al sistema."
FinFuncion

Algoritmo sin_titulo
	Dimension bicicletas_disponibles[24]
    Definir decision Como Entero
    Dimension datos[6]
    decision = 0
    nombre = " "
    apellido = " "
    telefono = " "
    correo = " "
    usuario = " "
    contraseña = " "
    iniciado = Falso
    Definir duracion, hora Como Entero
    
    
    Mientras iniciado = Falso
        Escribir "Ingrese la opcion que desea hacer 1 = Registrarse | 2 = Iniciar Sesion"
        Leer decision
        Segun decision
            Caso 1:
                Escribir "Ingrese su nombre"
                Leer datos[1]
                Escribir "Ingrese su apellido"
                Leer datos[2]
                Escribir "Ingrese su numero de telefono"
                Leer datos[3]
                Escribir "Ingrese un correo electronico"
                Leer datos[4]
                Escribir "Ingrese un nombre de usuario"
                Leer datos[5]
                Escribir "Ingrese una contraseña"
                Leer datos[6]
            Caso 2:
                Escribir "Ingrese su nombre de usuario"
                Leer usuario
                Escribir "Ingrese su contraseña"
                Leer contraseña
                Si usuario == datos[5] y contraseña == datos[6] Entonces
                    Escribir "Inicio de sesion exitoso"
                    iniciado = Verdadero
                    decision = 0
                Sino
                    Escribir "Credenciales incorrectas"
                FinSi
        FinSegun
    FinMientras
	
    Mientras iniciado = Verdadero
        Escribir "Ingrese la opcion que desea hacer 1 = Ver Informacion personal | 2 = Rentar una bicicleta | 3 = Cancelar una reserva"
        Leer decision 
        Segun decision 
            Caso 1:
                Escribir "Datos personales"
                Escribir "Nombre: " datos[1]," ", datos[2]
                Escribir "Correo: " datos[4]
                Escribir "Numero de telefono: " datos[3]
                Escribir "Nombre de usuario: " datos[5]
                Escribir "Contraseña: *******"
            Caso 2:
                Escribir "A que hora desea hacer su reservacion recuerde que el horario es de 8 am a 8 pm | Ingrese la hora en formato de 24 horas"
                Leer hora
                Si hora < 8 o hora > 20 Entonces
                    Escribir "Ingrese una hora valida"
					Leer hora
                Sino
                    Escribir "Ingrese la duracion de la reservacion en horas"
                    Leer duracion
                    Si duracion < 1 Entonces
                        Escribir "Ingrese una duracion valida, la duracion debe ser igual o mayor a 1"
						Leer duracion
                    Sino
                        RentarBici(hora, duracion)
                    FinSi
                FinSi
            Caso 3:
                Escribir "A que hora desea cancelar su reserva? Ingrese la hora en formato de 24 horas"
                Leer hora
                Si hora < 8 o hora > 20 Entonces
                    Escribir "Ingrese una hora valida"
                Sino
                    CancelarReserva(hora)
                FinSi
        FinSegun
    FinMientras
FinAlgoritmo
