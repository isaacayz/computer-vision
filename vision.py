import cv2
import random

img = cv2.imread('ay.jpeg')
#img = cv2.resize(img, (0,0),fx=0.2, fy=0.2)

logo = img[900:1700, 1100:2800]
img[3200:4000, 100:1800] = logo
#print(img.shape)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()