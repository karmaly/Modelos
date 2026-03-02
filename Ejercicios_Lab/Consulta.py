import numpy as np
import matplotlib.pyplot as plt

X = np.array([[9,1],[23, 34], [16, 28], [12,33],[5,7],[9, 4],
 [12, 34], [5, 14], [43, 6], [3, 6], [12, 9],
 [2, 30], [3, 2], [2, 4]])
# Visualización de las dos columnas de X
fig = plt.figure(figsize=(6, 3))
plt.plot(X)
plt.grid()
plt.show()