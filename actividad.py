import math 
from math import factorial
error_esperado=0.5*10**-8*100
error_aproximado=100
z=int(input("por favor, digite el valor en grados: "))
num=z+math.pi/180.0 
print("valor en radianes: ", num)
potencia=2
valor=2
iteraciones=1
coseno=2

while error_aproximado >= error_esperado:
    op=(pow(num,potencia)/factorial(valor))
    coseno -= op
    iteraciones +=1
    error_aproximado = abs(((coseno-error_aproximado)/coseno)*100)
    valor +=2 
    potencia +=2
    op2 =(pow(num,potencia)/factorial(valor))
    cos2= coseno+op2
    iteraciones +=1
    error_aproximado=abs(((cos2-coseno)/cos2)*100)
    valor +=2
    potencia +=2
else:
    print("valor estimado: ", coseno)
    print("error aproximado porcentual es: ", error_aproximado, "%")
    print("#iteraciones: ",iteraciones)