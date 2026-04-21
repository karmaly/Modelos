#Id no paramétrica
#Hay dos caminos: Desconvolución o Mínimo Error Cuadrático (MSE)

#u : entrada - y : salida - h : sistema 

#Se requiere saber cuál es el comportamiento del sistema en muestras anteriores para poder conocer el sistema en actual.
#Ojo: como se divide por la entrada esta debe ser diferente de 0 (debo interactuar con los datos para poder garantizar que esto no ocurra)

#El método de MSE evita el ruido que se puede acumular en la desconvolución. 
#p: muestras representivas. Es el número de columanas que salen de la matríz U 

import pandas as pd
import matplotlib.pyplot as ptl
import scipy.signal as signal
import numpy as np

#cargar datos

df = pd.read_csv("data.csv")
df.head() #hacer documentación
#siempre se debe hacer una inspección adecuada (graficando, muchas veces, para hacerlo más cómodo)

time = df.time
u =  df.u
y = df.y

#Inspección de datos

plt.figure(figsize=(3,3))

plt.subplot(2,1,1)
plt.plot(time, u)
plt.title("")
plt.xlabel()
plt.ylabel()
plt.grid(True)


plt.subplot(2,1,2)
plt.plot(time, y)
plt.title("")
plt.xlabel()
plt.ylabel()
plt.grid(True)

#poner el autoajuste de los subplots

plt.show()


h_desc, _ = signail.deconvolve(y, u) # el _ es el residuo y esa info no me es representativa. Siempre se pone primero la salida y luego la entrada
print(len(h_desc)) 
print(len(u))

# h_desc tiene menor longitud que la entrada
# ZERO PADDING = Agrega ceros al final de la salida. Ejem : y = [1, 1, 4, 5, 0, 0, 0] --> la cantidad de ceros depende de mi p. Como yo puedo jugar con
#este valor, en este caso es N/3

ypad = np.concatenate([y, np.zeros(round(len(u)*1/3))]) #redondeo la la divición para que no me un flotante, no puedo tener 0.5 o "media"
h, remainder = signal. deconcolve(yapad, u)

#garficar h

#revisión de la ID

y_pred_desc = signal.convolve (h, u)

#graficar este conmportamiento


# --------- AHORA PRA MSE -------


def MSE(t, y, u, p, N):
  #poner aquí el cógido de las diapos de clase del profe de teoría
