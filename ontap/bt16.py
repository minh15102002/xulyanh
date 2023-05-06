import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
b,g,r=cv2.split(img)
cv2.imshow('Anh kenh mau B',b)
cv2.waitKey(0)
cv2.destroyAllWindows()