import turtle #Inside_Out
import random
import socket

boton_x =-10
boton_y =-10
botonLon =50  
botonan =30

wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
wn.title("Servidor")
skk.penup()
skk.goto(-200, -200)  # Posición inicial del tablero
skk.pendown()

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
    

def IniciarServidor():
	tableroInicial=wn
	skk.penup()
	skk.goto(-170, -170)  # Posición inicial del jugador
	skk.pendown()
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('192.168.0.194', 12345))
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

def click(x,y):
	global mode
	if boton_x<=x<=boton_x+botonLon:
		if boton_y<=y<=boton_y+botonan:
			print("camara alan")

dibujarTablero()


