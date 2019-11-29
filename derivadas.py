#!/usr/bin/env python3
#Marcos Lucas Pereira
#Teste da segunda derivada
from math import * #biblioteca contendo funções maatematicas como "raiz quadrada" 
from sympy import * #biblioteca para calculo cinetifico (ex: derivadas, integrais")
from sympy.solvers import * 
from sympy.abc import * #biblioteca de simbolos
from sympy.plotting import * #Biblioteca para plotagem, gerar grafico da função
init_printing() #parametros para imprimir as funções de maneira identica aos livros 
x, y= symbols('x y') #x e y definidos como simbolos.

entrada = (input('Digite a função desejada :')) #parametro para inserção da função

fx = diff(entrada, x) #primeira derivada em relação a x
fy = diff(entrada, y) #primeira derivada em relação a y
fxx = diff(fx,x)  #segunda derivada em relação x 
fyy = diff(fy, y) #segunda derivada em relação a y
fxy = diff(fx, y) # segunda derivada  de x em relaçlão a y 


if (fx.count(("y") or ("Y"))):
    pcx = solve(fy, x) #Resole a equação na derivada em relação a x
    val = fx.subs(x, pcx[0]) #Subistitui o valor de x, para encontrar  o valor de y
    pcy = solve(val, y) #resolve a equação em relação a y
    
else: 
    pcx = solve(fy, y) #Resole a equação na derivada em relação a x
    print ("resoltado = ", pcx)
    pcy = solve(fx, x) #resolve a equação em relação a y
    print ("pcy =",pcy, "pcx = ",pcx)


l1c1 = fxx.subs([(x, pcx[0]),(y, pcy[0])]) #encontra o primeiro valor da matriz
l2c2 = fyy.subs([(x, pcx[0]),(y, pcy[0])]) #encontra o segundo valor da matriz
l1c2l2c1 = fxy.subs([(x, pcx[0]),(y, pcy[0])]) #encontra o segundo terceiro vlor da matriz

d = l1c1*l2c2-l1c2l2c1*l1c2l2c1 #matriz Heissiana
print('Resultado = ',d ) #Resultado

if (d > 0) and (l1c1 > 0):
    print ('Minimo local')
    
elif (d > 0) and (l1c1 < 0):
    print ('Maximo local')
    
elif (d < 0):
    print ('Não é minimo local nem maximo local')
    
if (d == 0):
    print ('Ponto de sela')
