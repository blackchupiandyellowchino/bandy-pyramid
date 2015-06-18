# Realizar un sistema utilizando POO que permita resolver piramides numericas (el jueguito de La Capital)
# Basicamente el numero de arriba es la suma de los dos de abajo
# Ademas, debe detectarse si se puede resolver el problema o no y la base de esa piramide deben ser numeros 
# del 1 al 6 sin repetir (Nota maxima si no se toma en cuenta esta restriccion: 9)
# La piramide debe poder ser ingresada de forma incompleta
# Nota maxima si no se imprime la piramide: 8
# Nota maxima si no se toman en cuenta ejercicios que no se puedan resolver: 7
# Ejercicios con solucion unica. Si se encuentran uno o mas soluciones, faltan datos o no se puede resolver
# Objetos que colaboren con el problema
# Subir a Github papwa
# Si papwa
# Dale mamerto

#139			-> 21					-
#75 64			-> 19-20				- -
#38 37 27		-> 16-17-18				- - ->
#17 21 16 11	-> 12-13-14-15			- -	->  (-1)
#6 11 10 6 5	-> 7-8-9-10-11			- -
#1 5 6 4 2 3	-> 1-2-3-4-5-6			-


S = [1,5,6,4,2,3,6,11,10,6,5,17,21,16,11,38,37,27,75,64,139]

print " "*10, S [20]
print " "*8, S [18], "-",S[19]
print " "*6,S [15], "-", S[16], "-", S [17]
print " "*4,S [11],"-", S[12],"-", S[13], "-",S [14]
print " "*2,S[6], "-",S[7],"-", S[8],"-", S [9],"-", S[10]
print " ",S [0],"-", S[1], "-", S [2],"-", S[3],"-",S [4],"-", S[5]
