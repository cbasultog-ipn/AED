#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:55:32 2021

@author: carlosbasulto
"""
#VAMOS DE DEFINIR LA FUNCIÓN CON DATOS DE ENTRADA PILA Y TOPE
#Y NOS DEVOLVERÁ LA PILA ACTUALIZADA CON EL DATO APILADO
#Y EL NUEVO TOPE DE PILA

def apilar(pila,tope):
    valor = input("Dame un valor entero: ")
    pila.append(valor)
    tope=len(pila)
    return pila,tope

#Vamos a declar explicitamente algunas variables
tamanoPila = int(0)
tope = int(-1)
pila = []
i =int(1)

#Solicitemos el número de datos a apliar
print ("¿Cuantos datos deseas agregar a la Pila: ")
tamanoPila = int(input())

#Aprovecharemos las Listas(o arreglos) dinámicops de Python
#Vamos a apilar cada datos que nos entregue el usuario

while tamanoPila >= i:
    #Invocó, o mando llamar, la función y le paso los datos
    apilar(pila,tope)
    i =i+1

#Imprimiremos información de como se encuentra la Pila
print("El tamaño de la pila es de " + str(len(pila)) + " elementos.")
print("El índice del tope es " + str(tope))
print("El valor del tope de la pila es " +str(pila[tope]))
print (pila)

#Mostraremos la pila en pantalla, del tope a la base
#Ahora utilizaremos la estructura de control o bucle "For"
print("Vamos a imprimir la pila del topa a su base:")
#Reutilizaré la variable i
i=len(pila)-1
for n in pila:
    print(pila[i])
    i=i-1

#Observa la ventaja de usar funciones
print("¿Deseas apilar un número más?" )
decision = str(input())
#En la siguiente sentencia me convierto la entra de texto minusculas
decision = decision.lower()
while decision == "si":
    apilar(pila,tope)
    #Observa la desventaja de NO usar funciones ¿lo ves?
    i=len(pila)-1
    for n in pila:
        print(pila[i])
        i=i-1
        
    print("¿Deseas apilar un número más?")
    decision = str(input())
    decision = decision.lower()
    if decision == "no":
        decisión= "no"


print("Gracias por usar el programa.")
        
    
#Fin del programa
