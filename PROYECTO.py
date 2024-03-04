
import cv2
import numpy as np

img = cv2.imread('mina.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
muestra = cv2.imread('f.png', 0)

w, h = muestra.shape[::-1]

res = cv2.matchTemplate(imgGray, muestra, cv2.TM_CCOEFF_NORMED)

umbral = 0.8
loc = np.where(res >= umbral)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255, 2))

cv2.namedWindow("RESULTADOS", cv2.WINDOW_NORMAL)
cv2.imshow("RESULTADOS", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
