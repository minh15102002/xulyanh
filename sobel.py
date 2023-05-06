import cv2
import numpy as np
img_o = cv2.imread('images\\cayxang.jpg',1)
img = cv2.resize(img_o,(320,240))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_01 = cv2.imread('images\\cayxang.jpg',0)
img1 = cv2.resize(img_01,(320,240))
imgx=cv2.Sobel(img1,cv2.CV_64F,1,0,ksize=5)
imgy=cv2.Sobel(img1,cv2.CV_64F,0,1,ksize=5)
imgxy=cv2.Sobel(img1,cv2.CV_64F,1,1,ksize=5)
cv2.imshow('ori',img1)
cv2.imshow('sobel x',imgx)
cv2.imshow('sobel y',imgy)
cv2.imshow('sobel xy',imgxy)
cv2.waitKey(0)
cv2.destroyAllWindows()