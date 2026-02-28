import numpy as np
import matplotlib.pyplot as plt

#-----------------------Ejercicios con arrays-----------------------

# Ejercicio 1: Crear array 
a_vector = np.array([1,2,3])
a_matrizA = np.array([[1,2,3],[4,5,6],[7,8,9]])
a_matrizB = np.array([[90,80,70],[60,50,40],[30,20,10]])

# Ejercicio 2: Acceder a un elemnto del array. Recuerda que los indices empiezan en 0
valor_v = a_vector[1]
valor_m = a_matrizA[1,1] #primera posicion es la fila, segunda posicion es la columna


 #Operaciones con matrices
C = a_matrizA @ a_matrizB #producto matricial
D = a_matrizA * a_matrizB #producto elemento a elemento

#Info de matrices
a_matrizA.shape #dimensiones de la matriz
a_matrizA.size #cantidad de elementos en la matriz
a_matrizA.T #transpuesta de la matriz
a_matrizA + a_matrizB #suma de matrices
a_matrizA - a_matrizB #resta de matrices
E = np.max(a_matrizA) #maximo valor de la matriz
F = np.min(a_matrizA) #minimo valor de la matriz
E = np.max(a_matrizA, axis=0) #maximo valor de la matriz por columnas
F = np.min(a_matrizA, axis=1) #minimo valor de la matriz por filas


#Construccion de matrices
G = np.zeros((3,3)) #matriz de ceros
H = np.ones((3,3)) #matriz de unos
I = np.empty((3,3)) #matriz vacia (valores no definidos)
J = np.arange(0,10,2) #array con valores desde 0 hasta 10 con paso de 2
K = np.linspace(0,1,5) #array con 5 valores equiespaciados entre 0 y 1
L = a_matrizA[:,[0,2]] #selección de columnas 0 y 2 de la matriz A, es decir una submatriz

#Concatenación de matrices. Recordar que los arrays deben tener la misma dimensión en los ejes que NO se están concatenando.
M = np.concatenate((a_matrizA,a_matrizB), axis=0) #concatenacion de matrices por filas
N = np.concatenate((a_matrizA,a_matrizB), axis=1) #concatenacion de matrices por columnas

#Polinomios
p1 = np.poly1d([1, -3, 2]) #crea un polinomio de la forma x^2 - 3x + 2
p2 = np.poly1d([2, 0, -1]) #crea un polinomio de la forma 2x^2 - 1
p1e = p1(2) #evalua el polinomio en x=2
p1x = p1.r #raices del polinomio
s = p1 + p2 #suma de polinomios
m = p1 * p2 #multiplicacion de polinomios
d = p1 / p2 #division de polinomios

#-----------------------Grafica de funciones-----------------------

