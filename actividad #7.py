import math 
from math import factorial
error_esperado=0.5*10**-8*100
error_aproximado=100

num=0.85
potencia=1
valor=1
iteraciones=1
e=1


while error_aproximado >= error_esperado:
    op=(pow(num,potencia)/factorial(valor))
    e -= op
    print(e)
    iteraciones +=1
    error_aproximado = abs(((e-error_aproximado)/e)*100)
    valor +=2 
    potencia +=2
    op2 =(pow(num,potencia)/factorial(valor))
    e2= e+op2
    print(e2)
    iteraciones +=1
    error_aproximado=abs(((e2-e)/e2)*100)
    valor +=1
    potencia +=1
else:
    print("valor estimado: ", e2)
    print("error aproximado porcentual es: ", error_aproximado, "%")
    print("#iteraciones: ",iteraciones)