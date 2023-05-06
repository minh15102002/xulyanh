import cv2
import numpy as np
img_o = cv2.imread('images\\cayxang.jpg',1)
img = cv2.resize(img_o,(320,240))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# ma tran
# la bàn
kernel1 = np.array([[-1,1,1],[-1,-2,1],[-1,1,1]])
kernel2 = np.array([[1,1,1],[-1,-2,1],[-1,-1,1]]) 

img_copmpass1 = cv2.filter2D(img_gray,-1,kernel1)
img_compass2 = cv2.filter2D(img_gray,-1,kernel2)
img_compass = img_copmpass1 + img_compass2
cv2.imshow('ori',img)
cv2.imshow('compass1',img_copmpass1)
cv2.imshow('compass2',img_compass2)
cv2.imshow('compass',img_compass)
cv2.waitKey(0)
cv2.destroyAllWindows()