# Realizar un sistema utilizando POO que permita resolver piramides numericas (el jueguito de La Capital)
# Basicamente el numero de arriba es la suma de los dos de abajo
# Ademas, debe detectarse si se puede resolver el problema o no y la base de esa piramide deben ser numeros 
# del 1 al 6 sin repetir (Hipoteticamente esto dejo de ser condicion base)
# La piramide debe poder ser ingresada de forma incompleta
# Nota maxima si no se imprime la piramide: 8
# Nota maxima si no se toman en cuenta ejercicios que no se puedan resolver: 7
# Ejercicios con solucion unica. Si se encuentran uno o mas soluciones, faltan datos o no se puede resolver





"""No usar tildes, python los toma como error de sintaxis"""




# Objetos que colaboren con el problema

#139			-> 1						-
#75 64			-> 2-3						- -
#38 37 27		-> 4-5-6					- - ->
#17 21 16 11	-> 7-8-9-10					- -	->  (-1)
#6 11 10 6 5	-> 11-12-13-14-15			- -
#1 5 6 4 2 3	-> 16-17-18-19-20-21		-

# No se puede usar un array para definir la piramide

# Si se podrian definir arrays por fila (supongo)

# Celdas -> (Filas?) -> Piramide (clases)



# Funcion para definir cantidad total de celdas
# n = cantidad de celdas en la ultima fila (desde arriba)

# f(1) = 1
# f(2) = f(1) + 2 = 3
# f(3) = f(2) + 3 = 6
# f(4) = f(3) + 4 = 10
# f(5) = f(4) + 5 = 15
# f(6) = f(5) + 6 = 21

# f(n) = f(n-1) + n




class Celda:
	"""Clase definida para las celdas"""
	def __init__(self):
		self.x = 1
		self.y = 1
		self.value = 0
		self.hidden = True
