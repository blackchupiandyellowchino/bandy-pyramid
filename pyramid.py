# Realizar un sistema utilizando POO que permita resolver piramides numericas (el jueguito de La Capital)
# Basicamente el numero de arriba es la suma de los dos de abajo
# Ademas, debe detectarse si se puede resolver el problema o no y la base de esa piramide deben ser numeros 
# del 1 al 6 sin repetir (Hipoteticamente esto dejo de ser condicion base)
# La piramide debe poder ser ingresada de forma incompleta
# Nota maxima si no se imprime la piramide: 8
# Nota maxima si no se toman en cuenta ejercicios que no se puedan resolver: 7
# Ejercicios con solucion unica. Si se encuentran uno o mas soluciones, faltan datos o no se puede resolver
# No se puede usar un array para definir la piramide

 
 
 
 
"""No usar tildes, python los toma como error de sintaxis"""
 
 


# Funcion para definir cantidad total de celdas
# n = cantidad de celdas en la ultima fila (desde arriba) = altura

# f(1) = 1
# f(n) = f(n-1) + n

 
# Libreria necesaria para cortar programa

import sys

# Matriz global que contiene los valores de la piramide

v = []
 
for i in range(22):
	v.append(i)


# f(1) = 1
# f(2) = f(1)  2 = 3
# f(3) = f(2)  3 = 6
# f(4) = f(3)  4 = 10
# f(5) = f(4)  5 = 15
# f(6) = f(5)  6 = 21
 
# Celdas izq > tienen un solo padre (derecha)
# Celdas der > tienen un solo padre (izquierda)
# Celdas hijas > no tienen hijos
# Celdas izq hijas > no tienen hijos y un solo padre (derecha)
# Celdas der hijas > no tienen hijos y un solo padre (derecha)
# f(n) = f(n1)  n
 
 
# f(1) = padre
# f(1<n<4)  1 = celdas izq
# f(1<n<=5) = celdas der
# f(5)  1 = celda izq fondo
# f(5)  {2,3,4,5} = celdas fondo
# f(6) = celda der fondo
 

class Celda:
	def __init__(self,pos,valor):
		self.pos = pos
		v[self.pos] = valor
		self.hijo_der = self.set_hijo_der()
		self.hijo_izq = self.set_hijo_izq()
		self.padre_izq = self.set_Padre_izq()
		self.padre_der = self.set_Padre_der()
		#self.hidden = True


# No se si son muy necesarias estas funciones, pero definen los padres posibles de cada celda

	def set_Padre_izq(self):
		self.v = (self.pos + self.get_high())

		# Si el hijo izquierdo es f(n)  1

		if(self.v == self.fact( self.get_high() ) + 1 ):
			return -1
		else:
			return self.pos - self.get_high()


	def set_Padre_der(self):
		self.v = (self.pos + self.get_high() + 1)

		# Si el hijo derecho es f(n)

		if(self.v == self.fact(self.get_high() + 1)):
			return -1
		else:
			return self.pos - self.get_high() + 1


# Funciones que definen los posibles hijos de cada celda, exceptuando los del piso

	def set_hijo_izq(self):
		if (self.pos >= 16 and self.pos <= 21):
			return -1
		else:
			self.v = self.pos + self.get_high()
			return self.v


	def set_hijo_der(self):
		if (self.pos >= 16 and self.pos <= 21):
			return -1
		else:
			self.v = self.pos + self.get_high() + 1
			return self.v


# Funcion que devuelve el nivel de la celda (del 1 al 6)

	def get_high(self):
		if (self.pos == 1):
			return 1
		elif(self.pos == 2 or self.pos == 3):
			return 2
		elif (self.pos >= 4 and self.pos <= 6):
			return 3
		elif(self.pos >= 7 and self.pos <= 10):
			return 4
		elif(self.pos >= 11 and self.pos <= 15):
			return 5
		else:
			return 6


# Funcion f(1) = 1; f(n) = f(n-1) + n

	def fact(self,n):
		self.n = n
		if (self.n == 1):
			return 1
		else:
			return self.n + self.fact(self.n - 1)


# Funciones exclusivas para la piramide

	def calcular(self):

		# Siendo a = pos; b y c los hijos der e izq

		# Si no existe a pero si b y c > a = b  c

		if(v[self.pos]== 0 and v[self.hijo_der] != 0 and v[self.hijo_izq] != 0):
			v[self.pos] = v[self.hijo_der] + v[self.hijo_izq]

		# Si b no existe pero si a y c > b = a  c

		elif(v[self.pos]!= 0 and v[self.hijo_der] != 0 and v[self.hijo_izq] == 0):
			v[self.hijo_izq] = v[self.pos] - v[self.hijo_der]

		# Si c no existe pero si a y b > c = a  b

		elif(v[self.pos]!= 0 and v[self.hijo_der] == 0 and v[self.hijo_izq] != 0):
			v[self.hijo_der] = v[self.pos] - v[self.hijo_izq]

			# Si existen los tres

		if(v[self.pos]!= 0 and v[self.hijo_der] != 0 and v[self.hijo_izq] != 0):
			self.correct = self.check()
			if(self.correct == 1):
				return 1

		return 0

	def check(self):
		if (v[self.pos] == v[self.hijo_der] + v[self.hijo_izq]):
			return 1
		else:
			#SALIR DEL PROGRAMA
			sys.exit("No se puede resolver la piramide.")



# "La piramide la debe poder resolver un chico de 5" > Supongo que no saben de eliminacion por Gauss
# asi que no la incluyo


# Los valores de cada celda fueron dados al principio. La piramide deberia poder calcular los valores
# faltantes e imprimirse


class Piramide(Celda):
 	def __init__(self):
		self.pasadas = 0
		self.pir_calculo()


	def pir_calculo(self):
		if(self.pasadas == 7):
			#print "No se puede"
			#SALIR DEL PROGRAMA
			sys.exit("No se puede resolver la piramide")
		self.completed = 0
		self.completed+= Celda1.calcular()
		self.completed+= Celda2.calcular()
		self.completed+= Celda3.calcular()
		self.completed+= Celda4.calcular()
		self.completed+= Celda5.calcular()
		self.completed+= Celda6.calcular()
		self.completed+= Celda7.calcular()
		self.completed+= Celda8.calcular()
		self.completed+= Celda9.calcular()
		self.completed+= Celda10.calcular()
		self.completed+= Celda11.calcular()
		self.completed+= Celda12.calcular()
		self.completed+= Celda13.calcular()
		self.completed+= Celda14.calcular()
		self.completed+= Celda15.calcular()

		if (self.completed == 15):
			print "Piramide completa"
			#imprimir()
		else:
			self.pasadas+= 1
			self.pir_calculo()


#139			>         1						
#75 64			>        2 3						
#38 37 27		>      4  5 6			
#17 21 16 11	>    7  8  9 10		
#6 11 10 6 5	>  11-12-13-14-15		
#1 5 6 4 2 3	> 16-17-18-19-20-21



Celda1 = Celda(1,139)
Celda2 = Celda(2,75)
Celda3 = Celda(3,64)
Celda4 = Celda(4,38)
Celda5 = Celda(5,37)
Celda6 = Celda(6,27)
Celda7 = Celda(7,17)
Celda8 = Celda(8,21)
Celda9 = Celda(9,16)
Celda10 = Celda(10,11)
Celda11 = Celda(11,6)
Celda12 = Celda(12,11)
Celda13 = Celda(13,10)
Celda14 = Celda(14,6)
Celda15 = Celda(15,5)
Celda16 = Celda(16,1)
Celda17 = Celda(17,5)
Celda18 = Celda(18,6)
Celda19 = Celda(19,4)
Celda20 = Celda(20,2)
Celda21 = Celda(21,3)


P = Piramide()