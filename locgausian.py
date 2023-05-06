import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('images\\anhnhieu.jpg')
img=cv2.resize(img,(480,480))
img_gauus=cv2.GaussianBlur(img,(9,9),0)
# cv2.imwrite('images\\anhgaus.jpg',img_gauus)
cv2.imshow('anh goc',img)
cv2.imshow('anh gaus',img_gauus)
# loc trung vi
img_median=cv2.medianBlur(img,9)
cv2.imshow('median blurring',img_median)
# loc trung binh
img_mean0=cv2.blur(img,(9,9))
cv2.imshow('anh loc tb cua so 3x3',img_mean0)
hist = cv2.calcHist([img_gauus], [0], None, [256], [0,255])
plt.plot(hist, color = 'b')
hist = cv2.calcHist([img_mean0], [0], None, [256], [0,255])
plt.plot(hist, color = 'r')
hist = cv2.calcHist([img_median], [0], None, [256], [0,255])
plt.plot(hist, color = 'g')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()