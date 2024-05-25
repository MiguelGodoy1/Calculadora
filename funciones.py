def suma(sumaA, sumaB):
	resultado_suma = sumaA + sumaB
	return resultado_suma
	
def resta(restaA, restaB):
	resultado_resta= restaA - restaB
	return resultado_resta
	
def multiplicacion (mult_A, mult_B):
	resultado_mult = mult_A * mult_B
	return resultado_mult

def division (div_A, div_B):
	resultado_div = div_A / div_B
	return resultado_div

def factorial (num:int)->int:
    if num == 0:
        fact = 1
    else:
        fact = num * factorial(num - 1)
        
    return fact