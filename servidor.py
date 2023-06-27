import turtle #Inside_Out
import random
import socket

boton_x =-10
boton_y =-10
botonLon =50  
botonan =30

player1_x=-175
player1_y=-225
casillaOrigen=1
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.penup()
skk.goto(-200, -200)  # Posición inicial del tablero
skk.pendown()
skk.speed(60)
jugador1 = turtle.Turtle()
jugador1.color("red")
jugador1.shape("triangle")
jugador1.penup()
jugador1.speed(0)
jugador1.setposition(player1_x,player1_y)


colores = {
    "red": "rojo",
    "blue": "azul",
    "green": "verde"
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
	
    

def IniciarServidor():
	tableroInicial=wn
	skk.penup()
	skk.goto(-170, -170)  # Posición inicial del jugador
	skk.pendown()
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('192.168.0.200', 12345))
	server_socket.listen(1)
	print('Esperando conexión del cliente...')
	client_socket, client_address = server_socket.accept()
	print(f'Cliente conectado desde {client_address}')

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
					tortuga.forward(35)
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
		print(posicion)
		print(posicionDestino)
						
	
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

def click(x,y):
	global mode,casilla
	
	if boton_x<=x<=boton_x+botonLon:
		if boton_y<=y<=boton_y+botonan:

			avanzarJugador(jugador1, 12)
			

dibujarTablero()

speed=1
while True:
	skk.forward(speed)




