# Libreria necesaria para cortar programa

import sys

# Matriz global que contiene los valores de la piramide

v = []
 
for i in range(22):
	v.append(i)


# Variable global que usamos para que se vean prolijos los input de celdas

num = 1



class Celda:
	def __init__(self,pos):
		self.pos = pos
		global num
		v[self.pos] = int(raw_input("Ingresa valor de celda " + str(num) + ": ") )
		num+= 1
		self.hijo_der = self.set_hijo_der()
		self.hijo_izq = self.set_hijo_izq()
		self.padre_izq = self.set_Padre_izq()
		self.padre_der = self.set_Padre_der()
		#self.hidden = True


# No se si son muy necesarias estas funciones, pero definen los padres posibles de cada celda

	def set_Padre_izq(self):
		self.v = (self.pos + self.get_high())

		# Si el hijo izquierdo es f(n) + 1

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

		# Si no existe a pero si b y c > a = b + c

		if(v[self.pos]== 0 and v[self.hijo_der] != 0 and v[self.hijo_izq] != 0):
			v[self.pos] = v[self.hijo_der] + v[self.hijo_izq]

		# Si b no existe pero si a y c > b = a - c

		elif(v[self.pos]!= 0 and v[self.hijo_der] != 0 and v[self.hijo_izq] == 0):
			v[self.hijo_izq] = v[self.pos] - v[self.hijo_der]

		# Si c no existe pero si a y b > c = a - b

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
			sys.exit("No se puede resolver la piramide. Las cuentas no son correctas")



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
			sys.exit("No se puede resolver la piramide. Faltan datos")
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
			print "\n"
			print "\n"
			print "\n"
			self.imprimir()
		else:
			self.pasadas+= 1
			self.pir_calculo()

	def imprimir(self):
		print('%12s' % str(v[1]))
		print('%10s' % str(v[2]) + " " + str(v[3]))
		print('%9s' % str(v[4]) + " " + str(v[5]) + " " + str(v[6]))
		print('%8s' % str(v[7]) + " " + str(v[8]) + " " + str(v[9]) + " " + str(v[10]))
		print('%7s' % str(v[11]) + " " + str(v[12]) + " " + str(v[13]) + " " + str(v[14]) + " " + str(v[15]))
		print('%6s' % str(v[16]) + " " + str(v[17]) + " " + str(v[18]) + " " + str(v[19]) + " " + str(v[20]) + " " + str(v[21]))


#139			>         1						
#75 64			>        2 3						
#38 37 27		>      4  5 6			
#17 21 16 11	>    7  8  9 10		
#6 11 10 6 5	>  11-12-13-14-15		
#1 5 6 4 2 3	> 16-17-18-19-20-21



Celda1 = Celda(1)
Celda2 = Celda(2)
Celda3 = Celda(3)
Celda4 = Celda(4)
Celda5 = Celda(5)
Celda6 = Celda(6)
Celda7 = Celda(7)
Celda8 = Celda(8)
Celda9 = Celda(9)
Celda10 = Celda(10)
Celda11 = Celda(11)
Celda12 = Celda(12)
Celda13 = Celda(13)
Celda14 = Celda(14)
Celda15 = Celda(15)
Celda16 = Celda(16)
Celda17 = Celda(17)
Celda18 = Celda(18)
Celda19 = Celda(19)
Celda20 = Celda(20)
Celda21 = Celda(21)


P = Piramide()
