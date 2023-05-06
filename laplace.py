import cv2
import numpy as np
img_o = cv2.imread('images\\cayxang.jpg',1)
img = cv2.resize(img_o,(320,240))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# ma tran
# la bàn
kernel1 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
kernel2 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]) 
kernel3 = np.array([[1,-2,1],[-2,4,-2],[-1,-2,1]]) 
img_laplace1 = cv2.filter2D(img_gray,-1,kernel1)
img_laplace2 = cv2.filter2D(img_gray,-1,kernel2)
img_laplace3 = cv2.filter2D(img_gray,-1,kernel3)
img_laplace = img_laplace1 + img_laplace2+ img_laplace3
cv2.imshow('ori',img)
cv2.imshow('laplace1',img_laplace1)
cv2.imshow('laplace2',img_laplace2)
cv2.imshow('laplace3',img_laplace3)
cv2.imshow('laplace',img_laplace)
cv2.waitKey(0)
cv2.destroyAllWindows()