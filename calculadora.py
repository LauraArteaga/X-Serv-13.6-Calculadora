#!/usr/bin/phyton

import sys

def sumar(x, y):
    return x + y
    
def restar(x, y):
	return x - y

def multiplicar(x, y):
	return x * y

def dividir(x, y):
	return x/y 

try:
	listaArg = sys.argv
	operacion = sys.argv[1]
	num1 = int(sys.argv[2])
	num2 = int(sys.argv[3])
except ValueError:
	print
	sys.exit("No pude convertir el dato a un entero"),
		    
if __name__ == "__main__":
	
	if len(listaArg) != 4:
		print
		sys.exit("Error de uso: calculadora.py <funcion> <num1> <num2>"),
			
	if operacion == "sumar":
		suma = sumar(num1, num2)
		print str(num1) + " + " + str(num2) + " = " + str(suma),
	elif operacion == "restar":
		resta = restar(num1, num2)
		print str(num1) + " - " + str(num2) + " = " + str(resta),
	elif operacion == "multiplicar":
		multi = multiplicar(num1, num2)
		print str(num1) + " * " + str(num2) + " = " + str(multi),
	elif operacion == "dividir":
		try:
			div = dividir(num1, num2)
		except ZeroDivisionError:
			print
			sys.exit("No es posible la division por 0"),
		else:
			print str(num1) + " / " + str(num2) + " = " + str(div),
	else:
		print("Error de uso: funcion [ sumar restar multiplicar dividir ]"),
