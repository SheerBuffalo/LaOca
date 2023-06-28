#version 5.30
#primer numero julio, segundo alan

import threading
import time
import turtle #Inside_Out
import random
import socket

direccionIP = '192.168.0.194'
turnoParaJugar = False #Es mi turno para jugar?
identificador="0" #Que jugador soy?
casillaOrigen=1 #En que casilla empiezo?
suma=0 #Cuanto saque en los dados?
boton_x =-10
boton_y =-10
botonLon =50  
botonan =30
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dado1=0
dado2=0
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.penup()
skk.goto(-200, -200)  # Posición inicial del tablero
skk.pendown()
skk.speed(40)
jugador=turtle.Turtle()


colores = {
    "red": "rojo",
    "blue": "azul",
    "green": "verde",
    "cyan":	"cyan",
    "yellow": "amarillo",
    "magenta": "magenta"
}

def dibujarTablero():
	numero_casilla=0
	for i in range(8):
		numero_casilla+=1
		dibujoCuadrado(55, numero_casilla)
	skk.left(45)
	numero_casilla+=1
	dibujoCuadrado(35, numero_casilla)
	skk.left(45)
	for i in range(6):
		numero_casilla+=1
		dibujoCuadrado(55, numero_casilla)
	skk.left(45)
	numero_casilla+=1
	dibujoCuadrado(35, numero_casilla)
	skk.left(45)
	for i in range(9):
		numero_casilla+=1
		dibujoCuadrado(55, numero_casilla)
	skk.left(45)
	numero_casilla+=1
	dibujoCuadrado(35, numero_casilla)
	skk.left(45)
	for i in range(5):
		numero_casilla+=1
		dibujoCuadrado(55, numero_casilla)
	skk.left(45)
	numero_casilla+=1
	dibujoCuadrado(35, numero_casilla)
	skk.left(45)
	for i in range(8):
		numero_casilla+=1
		dibujoCuadrado(55, numero_casilla)
	skk.left(45)
	numero_casilla+=1
	dibujoCuadrado(35, numero_casilla)
	skk.left(45)
	for i in range(4):
		numero_casilla+=1
		dibujoCuadrado(55, numero_casilla)
	skk.left(45)
	numero_casilla+=1
	dibujoCuadrado(35, numero_casilla)
	skk.left(45)
	for i in range(7):
		numero_casilla+=1
		dibujoCuadrado(55, numero_casilla)
	skk.left(45)
	numero_casilla+=1
	dibujoCuadrado(35, numero_casilla)
	skk.left(45)
	for i in range(3):
		numero_casilla+=1
		dibujoCuadrado(55, numero_casilla)
	skk.left(45)
	numero_casilla+=1
	dibujoCuadrado(35, numero_casilla)
	skk.left(45)
	for i in range(4):
		numero_casilla+=1
		dibujoCuadrado(55, numero_casilla)
	skk.right(90)
	skk.fd(55)
	skk.left(90)
	skk.fillcolor(random.choice(list(colores.keys())))
	skk.begin_fill()
	for _ in range(4):
		skk.forward(100)
		skk.left(90)
	skk.end_fill()
	skk.left(45)
	skk.penup()
	skk.forward(50)
	skk.write("63")
	skk.backward(50)
	skk.right(45)
	skk.pendown()
	skk.forward(100)
	draw_rect_button(skk)
	wn.onclick(click)
	turtle.done()
	
def conexionCliente(cliente, direccionIP):
	global identificador
	cliente.connect((direccionIP, 12345))
	data = cliente.recv(1024)  # recibe datos del servidor
	print('Received from server: ', data.decode())
	identificador=data.decode()
	

def dibujoCuadrado(tamano_casilla, i):

	skk.fillcolor(random.choice(list(colores.keys())))
	skk.begin_fill()
	for _ in range(4):
		skk.forward(tamano_casilla)
		skk.right(90)
	skk.end_fill()
	skk.right(45)
	skk.penup()
	skk.fd(tamano_casilla/2)
	skk.write(i)
	skk.left(180)
	skk.forward(tamano_casilla/2)
	skk.right(135)
	skk.forward(tamano_casilla)
	skk.pendown()

def draw_rect_button(pen, message = 'dado'):
    pen.penup()
    pen.begin_fill()
    pen.goto(boton_x, boton_y)
    pen.goto(boton_x + botonLon, boton_y)
    pen.goto(boton_x + botonLon, boton_y + botonan)
    pen.goto(boton_x, boton_y + botonan)
    pen.goto(boton_x, boton_y)
    pen.end_fill()
    pen.goto(boton_x + 15, boton_y + 15)
    pen.write(message, font = ('Arial', 11, 'normal'))

def click(x,y):
	global client_socket, suma, turnoParaJugar
	if boton_x<=x<=boton_x+botonLon:
		if boton_y<=y<=boton_y+botonan:
			#Si entra aqui es que se dio clic al boton
			dado1=random.randint(1,6)
			dado2=random.randint(1,6)
			print(f"Sacaste los numeros", dado1, dado2)
			suma=dado1+dado2
			if(turnoParaJugar): #Si no es su turno, no envia nada y no molesta al servidor
				client_socket.send(str(suma).encode())
				avanzarJugador(jugador, suma)
				turnoParaJugar = False


def avanzarJugador(tortuga, num_avance):
	global casillaOrigen
	retacha=False
	for i in range(num_avance):
		posicion = evaluacionPosicion(casillaOrigen)
		if(not retacha):
			posicionDestino = evaluacionPosicion(casillaOrigen+1)
			if(posicion!=posicionDestino):
				if(posicionDestino=="DIAGONAL"):
					tortuga.fd(35)
					tortuga.left(45)
					tortuga.fd(25)
				else:
					tortuga.fd(30)
					tortuga.left(45)
					tortuga.fd(35)
			elif(posicionDestino==posicion):
				tortuga.fd(55)
			casillaOrigen+=1
			if(casillaOrigen==63):
				retacha=True
		else:
			posicionDestino = evaluacionPosicion(casillaOrigen-1)
			if(posicion!=posicionDestino):
				if(posicionDestino=="DIAGONAL"):
					tortuga.backward(35)
					tortuga.right(45)
					tortuga.backward(25)
				else:
					tortuga.backward(30)
					tortuga.right(45)
					tortuga.backward(35)
			elif(posicionDestino==posicion):
				tortuga.backward(55)
			casillaOrigen-=1
		print(casillaOrigen)
	return casillaOrigen

def evaluacionPosicion(num_casilla):
	esLinea_1 = num_casilla>=0 and num_casilla<9
	if(esLinea_1):
		return "LINEA"
	esDiagonal_1 = num_casilla == 9
	if(esDiagonal_1):
		return "DIAGONAL"
	esVertical_1 = num_casilla>9 and num_casilla<16
	if(esVertical_1):
		return "VERTICAL"
	esDiagonal_2 = num_casilla==16
	if(esDiagonal_2):
		return "DIAGONAL"
	esLinea_2 = num_casilla>16 and num_casilla<26
	if(esLinea_2):
		return "LINEA"
	esDiagonal_3 = num_casilla == 26
	if(esDiagonal_3):
		return "DIAGONAL"
	esVertical_2 = num_casilla>26 and num_casilla<32
	if(esVertical_2):
		return "VERTICAL"
	esDiagonal_4 = num_casilla==32
	if(esDiagonal_4):
		return "DIAGONAL"
	esLinea_3 = num_casilla>32 and num_casilla<41
	if(esLinea_3):
		return "LINEA"
	esDiagonal_5 = num_casilla == 41
	if(esDiagonal_5):
		return "DIAGONAL"
	esVertical_3 = num_casilla>41 and num_casilla<46
	if(esVertical_3):
		return "VERTICAL"
	esDiagonal_6 = num_casilla==46
	if(esDiagonal_6):
		return "DIAGONAL"
	esLinea_4 = num_casilla>46 and num_casilla<54
	if(esLinea_4):
		return "LINEA"
	esDiagonal_7 = num_casilla == 54
	if(esDiagonal_7):
		return "DIAGONAL"
	esVertical_4 = num_casilla>54 and num_casilla<58
	if(esVertical_4):
		return "VERTICAL"
	esDiagonal_8 = num_casilla==58
	if(esDiagonal_8):
		return "DIAGONAL"
	esLinea_5 = num_casilla>58 and num_casilla<=63
	if(esLinea_5):
		return "LINEA"
	
def comunicacion_con_servidor():
	global turnoParaJugar, client_socket
	while True:
		print("Estoy escuchando :D")
		datos= client_socket.recv(1024) #Todo el rato escucho al servidor
		print("OMG recibi algo")
		if(datos.decode()=="SI"):
			turnoParaJugar=True
			print("Es mi turno para jugar")
		elif(datos.decode()=="NO"):
			turnoParaJugar=False
			print("No es mi turno para jugar")
		else:
			dadosOponenteBYTES=datos.decode()
			dadosOponente=int(dadosOponenteBYTES)
			print(f"Datos de los otros jugadores:",dadosOponente)

	
	


##########	MAIN	 ###################3

conexionCliente(client_socket, direccionIP)
if(identificador=="1"):
	jugador.color("white")
	wn.title("Cliente1")
elif(identificador=="2"):
	jugador.color("black")
	wn.title("Cliente2")
elif(identificador=="3"):
	jugador.color("brown")
	wn.title("Cliente3")
jugador.shape("triangle")
jugador.penup()
jugador.speed(0)
jugador.setposition(-175,-225)
	
hilo_socket = threading.Thread(target=comunicacion_con_servidor)

hilo_socket.start()
dibujarTablero()