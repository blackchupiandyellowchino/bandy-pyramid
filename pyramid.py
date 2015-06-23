# Realizar un sistema utilizando POO que permita resolver piramides numericas (el jueguito de La Capital)
# Basicamente el numero de arriba es la suma de los dos de abajo
# Ademas, debe detectarse si se puede resolver el problema o no y la base de esa piramide deben ser numeros 
# del 1 al 6 sin repetir (Hipoteticamente esto dejo de ser condicion base)
# La piramide debe poder ser ingresada de forma incompleta
# Nota maxima si no se imprime la piramide: 8
# Nota maxima si no se toman en cuenta ejercicios que no se puedan resolver: 7
# Ejercicios con solucion unica. Si se encuentran uno o mas soluciones, faltan datos o no se puede resolver
# Objetos que colaboren con el problema

#139			-> 21					-
#75 64			-> 19-20				- -
#38 37 27		-> 16-17-18				- - ->
#17 21 16 11	-> 12-13-14-15			- -	->  (-1)
#6 11 10 6 5	-> 7-8-9-10-11			- -
#1 5 6 4 2 3	-> 1-2-3-4-5-6			-

# No se puede usar un array para definir la piramide

# Celdas -> Filas -> Piramide (clases)