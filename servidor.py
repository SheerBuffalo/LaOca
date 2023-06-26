import turtle #Inside_Out
import random
import socket

wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.penup()
skk.goto(-200, -200)  # Posición inicial del tablero
skk.pendown()

colores = {
    "red": "rojo",
    "blue": "azul",
    "green": "verde"
}

def dibujarTablero():
	for i in range(8):
		dibujoCuadrado(55)
	skk.left(45)
	dibujoCuadrado(35)
	skk.left(45)
	for i in range(6):
		dibujoCuadrado(55)
	skk.left(45)
	dibujoCuadrado(35)
	skk.left(45)
	for i in range(9):
		dibujoCuadrado(55)
	skk.left(45)
	dibujoCuadrado(35)
	skk.left(45)
	for i in range(5):
		dibujoCuadrado(55)
	skk.left(45)
	dibujoCuadrado(35)
	skk.left(45)
	for i in range(8):
		dibujoCuadrado(55)
	skk.left(45)
	dibujoCuadrado(35)
	skk.left(45)
	for i in range(4):
		dibujoCuadrado(55)
	skk.left(45)
	dibujoCuadrado(35)
	skk.left(45)
	for i in range(7):
		dibujoCuadrado(55)
	skk.left(45)
	dibujoCuadrado(35)
	skk.left(45)
	for i in range(3):
		dibujoCuadrado(55)
	skk.left(45)
	dibujoCuadrado(35)
	skk.left(45)
	for i in range(4):
		dibujoCuadrado(55)
	skk.right(90)
	skk.fd(55)
	skk.left(90)
	skk.fillcolor(random.choice(list(colores.keys())))
	skk.begin_fill()
	for _ in range(4):
		skk.forward(100)
		skk.left(90)
	skk.end_fill()
	skk.forward(100)

def IniciarServidor():
	tableroInicial=wn
	skk.penup()
	skk.goto(-170, -170)  # Posición inicial del jugador
	skk.pendown()
	server_socket = socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('192.168.0.200', 12345))
	server_socket.listen(1)
	print('Esperando conexión del cliente...')
	client_socket, client_address = server_socket.accept()
	print(f'Cliente conectado desde {client_address}')

def dibujoCuadrado(tamano_casilla):

	skk.fillcolor(random.choice(list(colores.keys())))
	skk.begin_fill()
	for _ in range(4):
		skk.forward(tamano_casilla)
		skk.right(90)
	skk.end_fill()
	skk.forward(tamano_casilla)

dibujarTablero()
IniciarServidor()







