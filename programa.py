#!/usr/bin/python
import sys

def calcularNumeroPrimo(numero):	
	a = numero
	contador = 0
	for i in range(1, a, 1):
		b = a % 2
		if b == 0:
			contador = contador + 1

	if contador <= 2:
		return "El numero " + str(a) + " es primo."
	else:
		return "El numero " + str(a) + " no es primo."
	

#Factorial de un numero
def calcularFactorial(numero):
	a = numero
	factorial = a
	for i in range(1, a, 1):
		factorial *= i
	
	return "El factorial de " + str(a) + " es " + str(factorial)
	
def informacion():
	a = "Saludo este es un programa hecho para la asignatura de Desarrollo de Software Libre\n"
	a += "Para selecciones una opcion del menu\n"
	a += "\t -n Ingrese \"n\" para calcular el numero primo"
	a += "\t -f Ingrese \"f\" para obtener el factorial de un numero"
	a += "Ejemplo:\n\t programa.py -n 7 "
	a += "\nNombre\t\t\tCodigo"
	a += "\nMario Ernesto Flores\t SMiS041008\n"
	return a

try:
	
	if len(sys.argv) >= 2:
		if sys.argv[1] == "-n":
			numero = int(sys.argv[2])
			print str(numero)+"es"
			print calcularNumeroPrimo(numero)
		elif sys.argv[1] == "-f":
			numero = int(sys.argv[2])
			print calcularFactorial(numero)	
		elif sys.argv[1] != "-n" and sys.argv[1] != "-f":
			print informacion()	
	else:		
		print informacion()
			
except ValueError:
	print "Hubo un error al ingresar el numero"
