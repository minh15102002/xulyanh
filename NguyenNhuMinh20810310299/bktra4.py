import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('images\\cayxang.jpg') 
img = cv2.resize(img, (320, 240))
cv2.imshow('anh goc', img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
h, s, v = cv2.split(img_hsv)
img_mean = cv2.blur(s, (5, 5))
cv2.imshow('anh loc trung binh cua so 5x5', img_mean)
cv2.waitKey(0)
cv2.destroyAllWindows()