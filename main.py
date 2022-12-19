import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('mariposa.PNG', 0)

filas, columnas = np.shape(img)

img_alargada = cv.imread('mariposa.PNG', 0)
img_compresion = cv.imread('mariposa.PNG', 0)
img_desplazamiento = cv.imread('mariposa.PNG', 0)

#estos datos los obtenemos observando el histograma de la imagen orginal
minimo = 50
maximo = 100

for fila in range(filas):
    for columna in range(columnas):
        img_alargada[fila][columna] = ((img_alargada[fila][columna] - minimo)/(maximo-minimo)*(255-0))+0
        img_compresion[fila][columna] = (((80-60)/(maximo-minimo))*(img_compresion[fila][columna]-minimo))+60
        img_desplazamiento[fila][columna] = img_desplazamiento[fila][columna] + 50



#Graficas
fig, ax = plt.subplots(4, 2)

ax[0, 0].hist(img.ravel(), 256, [0, 256])

ax[0, 1].imshow(img, cmap="gray")
ax[0, 1].set_title('Mariposa Original')
ax[0, 1].axis('off')

ax[1, 0].hist(img_alargada.ravel(), 256, [0, 256])

ax[1, 1].imshow(img_alargada, cmap="gray")
ax[1, 1].set_title('Mariposa Alargada')
ax[1, 1].axis('off')

ax[2, 0].hist(img_compresion.ravel(), 256, [0, 256])

ax[2, 1].imshow(img_compresion, cmap="gray")
ax[2, 1].set_title('Mariposa Comprension')
ax[2, 1].axis('off')

ax[3, 0].hist(img_desplazamiento.ravel(), 256, [0, 256])

ax[3, 1].imshow(img_desplazamiento, cmap="gray")
ax[3, 1].set_title('Mariposa Desplazada')
ax[3, 1].axis('off')


plt.show()

cv.waitKey(0)
cv.destroyAllWindows()