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
    valor = input("Dame un valor entero: ")
    #Python ingresará los valores en el siguiente índice disponible
    pila.append(valor)
    i =i+1
    #Actualizaremos el tope ¿por qué le resto -2?
    tope = i-2

#Imprimiremos información de como se encuentra la Pila
print("El tamaño de la pila es de " + str(len(pila)) + " elementos.")
print("El índice del tope es " + str(tope))
print("El valor del tope de la pila es " +str(pila[tope]))

#Mostraremos la pila en pantalla, del tope a la base
print("Vamos a imprimir la pila del topa a su base:")
#Reutilizaré la variable i
i = tope
while i <= tope:
    print(pila[i])
    i=i-1
    if i <= -1:
        break

#Fin del programa