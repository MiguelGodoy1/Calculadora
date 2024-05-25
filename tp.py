from funciones import *

x = 0
y= 0

bandera_a = False
bandera_b = False
bandera_c = False
bandera_d = False
bandera_e = False
while True:
	opciones = input("""Menu de calculadora funcional. 
	1- Ingresar pimer operando. 
	2-Ingresar segundo operando. 
	3-Calcular todas las operaciones. 
	4-Mostrar los resultados.
	5-Salir
	""")
	if opciones == "1":
			x= int(input("Escriba su primer operando: "))
	elif opciones == "2": 
			y= int(input("Escriba su segundo operando: "))
	elif opciones == "3":
			calcular = input("""Menu de calculos 
			a- Calcular la suma 
			b-Calcular la resta 
			c-Calcular la division 
			d-Calcular la multiplicacion 
			e-Calcular el factorial\n""")
			if calcular =="a":
					bandera_a = True
			elif calcular =="b":
					bandera_b = True
			elif calcular =="c":
					bandera_c =True
			elif calcular =="d": 
					bandera_d = True
			elif calcular == "e":
					bandera_e = True
	elif opciones == "4":
			informe = input("""Informe de resultados 
			a-Resultado de la suma 
			b-Resultado de la resta 
			c-Resultado de la division 
			d-Resultado de la multiplicacion 
			e-Resultado del factorial\n""")
			if informe == "a":
					if bandera_a == True:
						print ("El resultado de la suma es ", suma(x, y))
					else:
						print ("Tiene que realizar la suma antes.")
			elif informe== "b":
					if bandera_b == True:
						print ("El resultado de la resta es ",resta(x, y))
					else :
						print ("Tiene que realizar la resta antes.")
			elif informe == "c":
					if bandera_c == True:
						print ("El resultado de la division es ",division (x, y))
					else:
						print("Tiene que realizar la division antes.")
			elif informe == "d":
						if bandera_d:
							print ("El resultado de la multiplicacion es ", multiplicacion(x, y))
						else: 
							print("Tiene que realizar la multiplicacion antes")
			elif informe == "e":
						if bandera_e == True:
							print ("El factorial del primer numero es ",factorial(x)," y del segundo es ", factorial (y))
						else:
							print("Tiene que realizar la operacion antes")
	elif opciones == "5":
		salida = input("¿Desea salir?Y/N: ")
		if salida == "Y":
			break
		elif salida == "N":
			continue