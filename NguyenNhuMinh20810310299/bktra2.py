import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('images\\cayxang.jpg') 
img_rs= cv2.resize(img,[640,480])
cv2.imshow('anh goc',img_rs)
imghsv = cv2.cvtColor(img_rs, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(imghsv)
hist1 = cv2.calcHist([h],[0],None,[256],[0,256])
plt.plot(hist1, color ="r")
hist2 = cv2.calcHist([s], [0], None, [256], [0, 256])
plt.plot(hist2, color = 'b')
hist3 = cv2.calcHist([v], [0], None, [256], [0, 256])
plt.plot(hist3, color = 'g')
plt.show()
s_equa = cv2.equalizeHist(s)
cv2.imshow('anh s can bang', s_equa)
cv2.waitKey(0)
cv2.destroyAllWindows()