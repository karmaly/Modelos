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


#Construcción de matrices
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

time = np.arange(0, 10, 0.1)
y = np.sin(time)
fig = plt.figure() #se una cuando quiero un control total sobre la figura, como por ejemplo el tamaño, el fondo, etc. Si no se llama a esta función, matplotlib creará una figura automáticamente cuando se llame a la función de graficado.
plt.plot(time, y) #se usan en el argumento parámetros opcionales para personalizar la gráfica, como por ejemplo el color, el tipo de línea, el marcador, etc. Por ejemplo: plt.plot(time, y, color='red', linestyle='--', marker='o') 
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Grafica de la función seno')
plt.grid()
plt.show() #esta función es necesaria para mostrar la gráfica, si no se llama a esta función la gráfica no se mostrará. Esto le dice a la librería: "Renderiza todas las figuras pendientes y mantén la ventana abierta."

fig, axs = plt.subplots(2, 2) #se puede dividir la figura en subplots, en este caso se divide en una cuadrícula de 2 filas y 2 columnas, lo que da un total de 4 subplots. La función devuelve una figura y un array de ejes (axs) que se pueden usar para graficar en cada subplot individualmente.

axs[0,0].plot([1,2,3])
axs[0,0].set_title("Arriba izquierda")

axs[0,1].plot([3,2,1])
axs[1,0].plot([1,3,2])
axs[1,1].plot([2,1,3])

plt.tight_layout() #ajusta automáticamente los subplots para que no se superpongan entre sí, es decir, ajusta el espacio entre los subplots para que se vean mejor. Esto es especialmente útil cuando se tienen títulos, etiquetas o leyendas en los subplots que pueden superponerse si no se ajusta el diseño.
plt.show()

#También puedo usar plt.subplot() para crear subplots de forma individual, por ejemplo:
plt.subplot(3, 1, 1) #divide la figura en una cuadrícula. El primer número (3) indica el número de filas, el segundo número (1) indica el número de columnas, y el tercer número (1) indica el índice del subplot seleccionado (en este caso, el primer subplot).

#si quiero graficar señales discretas, puedo usar plt.stem() en lugar de plt.plot(), por ejemplo:

y = np.sin(time)
plt.stem(time, y) #esta función es útil para graficar señales discretas, ya que dibuja una línea vertical desde el eje x hasta el valor de y en cada punto de tiempo, con un marcador en la parte superior de la línea para indicar el valor de y. Esto hace que sea más fácil visualizar los valores discretos de la señal. Ojo con el periodo de muestreo, si el periodo es muy grande, la señal se ve muy cortada o incluso puede perder información importante. Por otro lado, si el periodo es muy pequeño, la señal se ve muy densa y puede ser difícil de interpretar.


#-----------------------Análisis de datos-----------------------

a = np.mean(a_matrizA) #media de la matriz A
a = np.mean(a_matrizA, axis=0) #media de la matriz A por columnas
a = np.mean(a_matrizA, axis=1) #media de la matriz A por filas
a = np.std(a_matrizA) #desviación estándar de la matriz A

#Vamos a ver una mierda más rara, el ajuste polinómico.

t = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
y = np.array([0.09, 0.12, 0.24, 0.27, 0.4, 0.45, 0.61, 0.67, 0.71, 0.63, 0.59])
#En este caso polyfit encuentra el polinomio que mejor se ajusta a los datos en el sentido de mínimos cuadrados. El primer argumento es el array de tiempo, el segundo argumento es el array de amplitud, y el tercer argumento es el grado del polinomio que se desea ajustar. 
p2 = np.polyfit(t, y, 2) # Ajuste polinómico de grado 2
p3 = np.polyfit(t, y, 3) # Ajuste polinómico de grado 3
# ¿Qué información se obtiene de p2 y p3? La función devuelve los coeficientes del polinomio ajustado, que se pueden usar para evaluar el polinomio en cualquier punto utilizando la función polyval.
y2_fit = np.polyval(p2, t)
y3_fit = np.polyval(p3, t)
plt.figure(figsize=(10, 3))
plt.plot(t, y, 'ok', label='Datos')
plt.plot(t, y2_fit, '--c', label='Ajuste cuadrático')
plt.plot(t, y3_fit, ':b', label='Ajuste cúbico')
plt.xlabel('Tiempo (s)')
plt.grid()
plt.legend()
