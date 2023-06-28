#version 5.30
#primer numero julio, segundo alan

import threading
import time
import turtle #Inside_Out
import random
import socket

boton_x =-10
boton_y =-10
botonLon =50  
botonan =30

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#wn = turtle.Screen()
#wn.bgcolor("light green")
#skk = turtle.Turtle()
#wn.title("Servidor")
#skk.penup()
#skk.goto(-200, -200)  # Posición inicial del tablero
#skk.pendown()
#skk.speed(40)

sem=threading.Semaphore(1)

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
    

def conexionServidor(servidor):
	servidor.bind(('192.168.0.194', 12345))
	servidor.listen(3)
	print('Esperando conexión del cliente...')
	client_socket1, client_address = servidor.accept()
	print(f'Cliente 1 conectado desde {client_address}')
	client_socket1.send(str(1).encode())
	client_socket2, client_address = servidor.accept()
	print(f'Cliente 2 conectado desde {client_address}')
	client_socket2.send(str(2).encode())
	client_socket3, client_address = servidor.accept()
	print(f'Cliente 3 conectado desde {client_address}')
	client_socket3.send(str(3).encode())
	
	return client_socket1, client_socket2, client_socket3

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

dataTiradas = [0,0,0] #Ultimo resultado de los dados
ordenJuego = [False, False, False] #Para verificar quien ya jugo y quien sigue
hayGanador = False #Variable de control para fin del juego

def clienteJugando(cliente, n):
	global dataTiradas, ordenJuego 
	print(f"Hola soy el hilo: ",n)
	sem.acquire() #Primera proteccion para evitar que todos jueguen a la vez
	if(ordenJuego[0]==False and n==1): #n es el cliente, o tambien, el # de jugador
		print(f"Hilo numero: ",n,"primera condcional")
		cliente.send("SI".encode()) #Envia un SI para que el cliente pueda empezar a jugar
		ordenJuego[0]=True #Activa el control que esta siendo su turno
		resultadoDadosBYTES=cliente.recv(1024) #Recibe los datos en bytes
		resultadoDados=int(resultadoDadosBYTES.decode()) #Parsea (transformar) a entero
		dataTiradas[n-1] = resultadoDados
		time.sleep(6)
		cliente.send(str(dataTiradas[1]).encode())
		time.sleep(6)
		cliente.send(str(dataTiradas[2]).encode())
		time.sleep(6)
	elif(ordenJuego[1]==False and ordenJuego[0]== True and n==2):
		cliente.send("SI".encode())
		ordenJuego[1]= True
		resultadoDadosBYTES=cliente.recv(1024)
		resultadoDados=int(resultadoDadosBYTES.decode())
		time.sleep(6)
		dataTiradas[n-1] = resultadoDados
		time.sleep(6)
		cliente.send(str(dataTiradas[0]).encode())
		time.sleep(6)
		cliente.send(str(dataTiradas[2]).encode())
		time.sleep(6)
	elif(ordenJuego[2]==False and ordenJuego[1]== True and ordenJuego[0]==True and n==3):
		cliente.send("SI".encode()) #Envia la confirmacion al cliente para que pueda comunicarse
		ordenJuego[2]= True #Activa la bandera de que ya esta jugando su turno
		resultadoDadosBYTES=cliente.recv(1024) #Espera a que el cliente le mande su resultado de los dados
		resultadoDados=int(resultadoDadosBYTES.decode())
		time.sleep(6)
		dataTiradas[n-1] = resultadoDados
		time.sleep(6)
		ordenJuego = [False for _ in range(3)] #Cuando termina su turno, vuelve a apagar las banderas porque es una nueva ronda
		cliente.send(str(dataTiradas[1]).encode())
		time.sleep(6)
		cliente.send(str(dataTiradas[0]).encode())
		time.sleep(6)
	else:
		#El cliente pregunta si le toca a cada rato, hay que enviar que no
		cliente.send("NO")
		print(f"No es tu turno Jugador:",n)
	sem.release()

###################	Seccion main	############################

cliente1, cliente2, cliente3 = conexionServidor(server_socket)
#dibujarTablero()
time.sleep(60)


while not hayGanador:
	t1 = threading.Thread(target=clienteJugando, args=(cliente1,1,))
	t2 = threading.Thread(target=clienteJugando, args=(cliente2,2,))
	t3 = threading.Thread(target=clienteJugando, args=(cliente3,3,))

	t1.start()
	t2.start()
	t3.start()
	t1.join()
	t2.join()
	t3.join()
