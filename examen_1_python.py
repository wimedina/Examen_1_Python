# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:49:02 2021

@author: William Medina
"""

#1. En una llantera se ha establecido una promoción de las llantas marca
# Ponchadas, dicha promoción consiste en lo siguiente: Si se compran menos
# de cinco llantas el precio es de $300 cada una, de $250 si se compran de
# cinco a 10 y de $200 si se compran más de 10. Obtener la cantidad de dinero
# que una persona tiene que pagar por cada una de las llantas que compra y la
# que tiene que pagar por el total de la compra.

num_llantas = int(input('Ingrese el número de llantas a comprar: '))

if(num_llantas > 0 and num_llantas < 5):
    precio_llanta = num_llantas * 300
    print('Se debe pagar $300 por cada llanta')
    print(f'El valor total de la compra es ${precio_llanta}')
elif(num_llantas >= 5 and num_llantas <= 10):
     precio_llanta = num_llantas * 250
     print('Se debe pagar $250 por cada llanta')
     print('El valor total de la compra es ${precio_llanta}')
elif(num_llantas > 10):
     precio_llanta = num_llantas * 200
     print(f'Se debe pagar $200 por cada llanta')
     print(f'El valor total de la compra es ${precio_llanta}')

# 2. Hacer algoritmo que de el valor final por la compra de televisores. El
# descuento lo hace basado en los dos numeros finales a la cédula, si
# termina en 01 el descuento es del 10% y si termina en 25 el descuento es
# del 20%, si termina en 44 el descuento es 35% y si es 57 el 50%.

televisores = int(input('Ingrese el numero de televisores a comprar '))
precio = float(input('Ingrese el precio de cada televisor '))
subtotal = televisores * precio

cedula = input('Ingrese el número de cedula ')
ult_digitos = cedula[-2:]

if(ult_digitos == '01'):
    total = subtotal - (subtotal * 0.1)
elif(ult_digitos == '25'):
    total = subtotal - (subtotal * 0.2)
elif(ult_digitos == '44'):
    total = subtotal - (subtotal *  0.35)
elif(ult_digitos == '57'):
    total = subtotal - (subtotal * 0.5)
else:
    total  = subtotal
print(f'El valor final de la compra es ${total}')
        
        
 # 3. Una empresa de colchones ofrece descuento según la siguiente tabla
# Numero de colchones comprados % Descuento
# De 0 a menos de 3                 0%
# De 3 hasta menos de 6             20%
# De 6 hasta menos de 8             25%
# De 8 en adelante                  30%

# Determine cuanto pagará una persona que compre colchones.   

valor = float(input('Ingrese valor del colchon '))    
numero = float(input('Ingrese el número de colchones a comprar '))

if(numero >=0 and numero < 3):
    total = valor * numero
elif(numero >= 3 and numero < 6):
    subtotal = valor * numero
    total = subtotal - (subtotal * 0.2)
elif(numero >= 6 and numero < 8):
    subtotal = valor * numero
    total = subtotal - (subtotal * 0.25)
elif(numero >= 8):
    subtotal = valor * numero
    total = subtotal - (subtotal * 0.3) 

print(f'El valor a pagar por {numero} colchones es ${total}')

# 4. Una universidad desea seleccionar una muestra de estudiantes para
# realizar una encuesta. Si el número de estudiantes es menor que 20 se
# tomará el 50%, si el salón tiene entre 20 y 30 estudiantes se tomará 60%,
# si la cantidad es mayor a 30 tomará 70%. ¿Que cantidad de estudiantes
# serán seleccionados para la encuesta?.

estudiantes = int(input('Ingrese el número de estudiantes '))

if(estudiantes < 20):
    encuestados = estudiantes * 0.5
elif(estudiantes >= 20 and estudiantes <= 30):
    encuestados = estudiantes * 0.6
elif(estudiantes > 30):
    encuestados = estudiantes * 0.7

print('El numero de estudiantes que serán seleccionados \n'
      f'para la encuesta es {encuestados}')

    

