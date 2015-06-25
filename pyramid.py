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

#139			-> 1						-
#75 64			-> 2-3						- -
#38 37 27		-> 4-5-6					- - ->
#17 21 16 11	-> 7-8-9-10					- -	->  (-1)
#6 11 10 6 5	-> 11-12-13-14-15			- -
#1 5 6 4 2 3	-> 16-17-18-19-20-21		-



# Funcion para definir cantidad total de celdas
# n = cantidad de celdas en la ultima fila (desde arriba) = altura

# f(1) = 1
# f(n) = f(n-1) + n

# c = corrimiento de celdas donde c = {0, ..., n-1}
# valor[f(n) + c] = valor [(f(n+1) + c)] + valor [(f(n+1) + c + 1)]



# Crear 21 objetos de tipo celda (si, aspero)

# Celdas izq -> tienen un solo padre (derecha)
# Celdas der -> tienen un solo padre (izquierda)
# Celdas hijas -> no tienen hijos
# Celdas izq hijas -> no tienen hijos y un solo padre (derecha)
# Celdas der hijas -> no tienen hijos y un solo padre (derecha)


# f(1) = padre
# f(1<n<4) + 1 = celdas izq
# f(1<n<=5) = celdas der
# f(6) = celda der fondo
# f(5) + 1 = celda izq fondo
# f(5) + {2,3,4,5} = celdas fondo





#class Celda:
#	"""Clase definida para las celdas"""
#	def __init__(self):
#		self.value = 0
#		self.hijo_izq = 0
#		self.hijo_der = 0
#		#self.hidden = True
#	def set_value (self,value):
#		self.value = value
#	def set_sons (self,izq,der):
#		self.hijo_izq = izq
#		self.hijo_der = der

#cell1 = Celda()
#cell2 = Celda()
#cell2.set_value(5)
#cell3 = Celda()
#cell3.set_value(5)


class papwa:
	def __init__(self):
		self.valor = 0
	def fact(self,valor):
		self.valor = valor
		if (self.valor == 1):
			self.n = 1
			return self.n
		else:
			self.n = self.valor + self.fact(self.valor - 1)
			return self.n

hola = papwa()
print hola.fact(6)

