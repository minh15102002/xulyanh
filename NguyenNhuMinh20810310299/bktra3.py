import cv2 
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('images\\cayxang.jpg') 
img_rz = cv2.resize(img,[320,240])
img_gray=cv2.cvtColor(img_rz,cv2.COLOR_BGR2GRAY)
img_hsv=cv2.cvtColor(img_rz,cv2.COLOR_BGR2HSV)
cv2.imshow("anh hsv",img_hsv)
h1,s1,v1=cv2.split(img_hsv)
cv2.imshow("anh kenh s cua anh hsv",s1)
#cau a
y, x = 50, 70
neighborhood = img_gray[y-2:y+3, x-2:x+3]
print("Mức xám trong lân cận 5x5 của điểm ảnh ({}, {}):".format(x, y))
print(neighborhood)
#cau b
neighborhood2 = img_gray[y-25:y+25, x-25:x+25]
print(neighborhood2)
img_n=img_gray[y:y+img_gray.shape[0],x:x+img_gray.shape[1]]
img_ne_equa=cv2.equalizeHist(img_n)
cv2.imshow('anh sau can bang',img_ne_equa)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()