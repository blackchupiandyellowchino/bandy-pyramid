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




# Objetos que colaboren con el problema

#139			->         1						
#75 64			->        2 3						
#38 37 27		->      4  5 6			
#17 21 16 11	->    7  8  9 10		
#6 11 10 6 5	->  11-12-13-14-15		
#1 5 6 4 2 3	-> 16-17-18-19-20-21



# Funcion para definir cantidad total de celdas
# n = cantidad de celdas en la ultima fila (desde arriba) = altura

# f(1) = 1
# f(n) = f(n-1) + n

# c = corrimiento de celdas donde c = {0, ..., n-1}
# valor[f(n) + c] = valor [(f(n+1) + c)] + valor [(f(n+1) + c + 1)]



# Crear 21 objetos de tipo celda (si, aspero)


# Matriz global que contiene los valores de la piramide. 
v = []

for i in range(22):
	v.append(i)

# Celdas izq -> tienen un solo padre (derecha)
# Celdas der -> tienen un solo padre (izquierda)
# Celdas hijas -> no tienen hijos
# Celdas izq hijas -> no tienen hijos y un solo padre (derecha)
# Celdas der hijas -> no tienen hijos y un solo padre (derecha)


# f(1) = padre
# f(1<n<4) + 1 = celdas izq
# f(1<n<=5) = celdas der
# f(5) + 1 = celda izq fondo
# f(5) + {2,3,4,5} = celdas fondo
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

		# Si el hijo izquierdo es f(n) + 1

		if(self.v == self.fact( self.get_high() ) + 1 ):
			return -1
		else:
			return self.pos - self.get_high()


	def set_Padre_der(self):
		self.v = (self.pos + self.get_high() + 1)

		# Si el hijo derecho es f(n)

		if(self.v == self.fact(self.get_high()+1)):
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

		if(v[self.hijo_der] != -1 and v[self.hijo_izq] != -1):

			# Si no existe a pero si b y c -> a = b + c

			if(v[self.pos]== 0 and v[self.hijo_der] != 0 and v[self.hijo_izq] != 0):
				v[self.pos] = v[self.hijo_der] + v[self.hijo_izq]

			# Si b no existe pero si a y c -> b = a - c

			elif(v[self.pos]!= 0 and v[self.hijo_der] != 0 and v[self.hijo_izq] == 0):
				v[self.hijo_izq] = v[self.pos] - v[self.hijo_der]

			# Si c no existe pero si a y b -> c = a - b

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
			return 0


# Pasadas... eeeeeeh ... 3 ?

# Si, 3. En realidad podrian ser mas, pero solo si omitimos usar las celdas padres
# Es un quilombo calcular los padres tambien, incluso innecesario sabiendo que calculamos la piramide
# desde la cima. El mambo es la cantidad de pasadas que deberia hacerse en la piramide si no usamos
# a los padres


# "La piramide la debe poder resolver un chico de 5" -> Supongo que no saben de eliminacion por Gauss
# asi que no la incluyo



# Mambo objetos: hay que crear las 21 celdas FUERA de las clases y DESPUES crear un objeto piramide
# Las funciones de calculo e impresion deben crearse dentro de la clase CELDA

# Los valores de cada celda fueron dados al principio. La piramide deberia poder calcular los valores
# faltantes e imprimirse




class Piramide(Celda):
	def __init__(self):
		self.pasadas = 0
		self.pir_calculo()
		#self.mostrar()
		#pass

	def pir_calculo(self):
		self.completed = 0
		self.completed+= Celda1.calcular()
		self.completed+= Celda2.calcular()
		self.completed+= Celda3.calcular()
		if (self.completed == 3):
			print "Piramide completa"
			return 1
		else:
			return 0
		#Celda1.calcular()
		#Celda1.calcular()
		#Celda1.calcular()




Celda1 = Celda(1,18)
Celda2 = Celda(2,8)
Celda3 = Celda(3,0)
Celda4 = Celda(4,0)
Celda5 = Celda(5,3)
Celda6 = Celda(6,2)


P = Piramide()
print v[Celda4.pos]
#print "Altura: " + str(Celda1.get_high())
#print "Padre izq: " + str(Celda1.padre_izq)
#print "Padre der: " + str(Celda1.padre_der)
#print "Hijo izq: " + str(Celda1.hijo_izq)
#print "Hijo der: " + str(Celda1.hijo_der)