
import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('Celula4.png')
imgGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imgGris = cv2.GaussianBlur(imgGris, (9, 9), 2)

circulos = cv2.HoughCircles(imgGris, cv2.HOUGH_GRADIENT, dp=1,
                            minDist=30, param1=70, param2=30,
                            minRadius=8, maxRadius=70)

if circulos is not None:
    circulos = np.uint16(np.around(circulos))
    
    medidas_procesadas = set()  # Almacena las medidas ya procesadas

    for circulo in circulos[0, :]:
        centro = (circulo[0], circulo[1])
        radio = circulo[2]

        # Verifica si la medida ya fue procesada
        if radio not in medidas_procesadas:
            cv2.putText(imagen, str(radio) + "px", centro, cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
            medidas_procesadas.add(radio)  # Agrega la medida a las procesadas

        cv2.circle(imagen, centro, radio, (255, 255, 255), 2)

# Mostrar la imagen con Matplotlib
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Resultado')
plt.show()






