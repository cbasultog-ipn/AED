Algoritmo Pila_ApliarDatos
	// Definir variables
	definir tamanoPila como entero
	definir i como entero
	definir tope Como Entero
	
	//inicializar variables
	tope <- nulo
	i <- 1
	
	//Solicitar el tamaño de la pìla
	Escribir "Por favor ingresa el tamaño de la Pila de datos: "
	Leer tamanoPila
	
	//Definir el arreglo para la pila
	Dimension pila[tamanoPila]
	
	//Cargar los datos de la Pila
	Escribir "Vamos a cargar los datos en la pila: "
	
	Para i <- 1 hasta tamanoPila Con Paso 1 Hacer
		TextoSolicitud <- "Escribe el dato #"
		NumeroDeDato <- ConvertirATexto(i)
		Tope = tope + 1
		Escribir Concatenar(TextoSolicitud,NumeroDeDato)
		Leer pila[tope]
	FinPara
	
	//Mostrar el resultado de los datos apilados
	Escribir "La pila quedo de la siguiente forma:" 
	Mientras tope > 0 Hacer
		Escribir pila[tope]
		tope = tope -1
	Fin Mientras
	
	//finaliza el programa
FinAlgoritmo
