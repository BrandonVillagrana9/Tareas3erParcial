import random

def solucionaleatoria(tsp):
 #generamos una solucion aleatoria
 solucion = []
 ciudades = list(range(len(tsp)))#4 range regresa 0,1,2,3)
 print(ciudades)
 for i in range(len(tsp)):#vamos a recorrer 
	#vamos a escoger una ciudad aleatoria de la lista que nombramos ciudades... pero aqui debemos quitar de la lista a la ciudad que ya añadimos
	#vamos a añadir a la solucion una nueva ciudad
 	ciudadaleatoria = ciudades[random.randint(0,len(ciudades)-1)]#randind() devolver un elemento de manera aleatoria de un numero entero de cierto rango especificado randint(0,3)==0 o 1 o 2 o 3 randint(0,4)== 0 o 1 o 2 o 3 o 4
 	solucion.append(ciudadaleatoria)#añado a la solucion mi ciudad escogida de manera aleatoria
 	ciudades.remove(ciudadaleatoria)#quitar de mi lista de ciudades a elegir
 #print("Soy la solucion aleatoria")
 return(solucion)

#evaluamos la solucion
def calculalongitud(tsp,solucion):
 longitud = 0 #inicializar el valor de nuestra ruta en cero
 for i in range(len(solucion)):
 	longitud+=tsp[solucion[i-1]][solucion[i]]#a nuestra variable longitud le vamos a sumar el valor de la matriz de adyacencia (tsp), es decir, la distancia de i-1 a 1... pero lo hacemos de esta forma porque si comenzamos en cero nuestro valor que tiene i de range, python no va a tomar la posicion -1 de nuestra lista de solucion, si no que va a tomar el ultimo valor... en nuestro caso tendriamos dsitancia de 3 a 0 luego de 0 a 1 luego de 1 a 2 y de 2 a 3
 return(longitud)

#generamos a los vecinos
def generavecinos(solucion):
 vecinos=[]
 for i in range(len(solucion)):#primer for recorre cada elemento de la solucion comenzando en 0 hasta n-1
 	for j in range((i+1),len(solucion)):#segundo for recorre cada elemento de la solucion pero comenzando en i+1
 		vecino=solucion.copy()#copy es un metodo de python que realiza la copia de un elemento (generalmente se trabaja con listas)
 		vecino[i]=solucion[j]#0 1 2 3, 0 0 2 3 tomamos la posicion i del vecino y la cambiamos por la posicion j de la solucion original 
 		vecino[j]=solucion[i]#1 0 2 3 tomamos la posicion j del vecino y la cambiamos por la posiscion i de la original
 		vecinos.append(vecino)
 return(vecinos)

#aqui necesitamos evaluar a cada uno de los vecinos
def obtienemejorvecino(tsp,vecinos):
 mejorruta=calculalongitud(tsp,vecinos[0])#calculando la ruta de nuestro primer vecino (por conveniencia para la comparacion)
 mejorvecino=vecinos[0]#mi variable mejorvecino es una lista de elementos que contiene a mi vecino de la posicion 0
 for vecino in vecinos:#for i in range(vecinos):
 	rutaactual=calculalongitud(tsp,vecino)#te mando el tsp y mi vecino de la posicion i
 	if rutaactual<mejorruta:#minimizando... si nosotros quisieramos maximizar rutaactual>mejorruta
 		mejorruta = rutaactual
 		mejorvecino=vecino#vecino[i]
 return(mejorvecino,mejorruta)




#Vamos a tomar esta parte como si fuera nuestra funcion principal (main)
#generando la intancia de nuestro problema
tsp=[#necesito generar la instancia de mi problema
	[0,100,500,600],
	[100, 0, 600, 500],
	[500, 600, 0, 100],
	[600, 500, 100, 0]
]

def hillclimbing(tsp):
 solucionactual=solucionaleatoria(tsp)#generamos nuestra solucion inicial de manera aleatoria
 print("Sol inicial")
 print(solucionactual)
 valoractual=calculalongitud(tsp,solucionactual)#evaluacion de nuestra solucion inicial generada de manera aleatoria
 #generar los vecinos de mi solucion
 vecinos=generavecinos(solucionactual)
 #ahora debemos de calcular a nuestro mejor vecino y obtener su mejor ruta
 mejorvecinoobtenido,mejorrutaobtenida=obtienemejorvecino(tsp,vecinos)#return(mejorvecino,mejorruta) #obtener a nuestro mejor vecino con su ruta a partir de la solucion que generamos al inicio

 while mejorrutaobtenida < valoractual:
 	solucionactual = mejorvecinoobtenido
 	valoractual = mejorrutaobtenida
 	vecinos=generavecinos(solucionactual)
 	mejorvecinoobtenido,mejorrutaobtenida=obtienemejorvecino(tsp,vecinos)#return(mejorvecino,mejorruta) #obtener a nuestro
 #saliendo del while cuando no mejore la solucion actual
 return solucionactual, valoractual
 
print("Yo soy la mejor solucion, con mi ruta")
print(hillclimbing(tsp))#imprimo lo que me regresa mi funcion de hillclimbing



		

