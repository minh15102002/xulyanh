import cv2
import numpy as np
img_o = cv2.imread('images\\cayxang.jpg',1)
img = cv2.resize(img_o,(320,240))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# ma tran
# la bàn
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]]) 

img_prewittx = cv2.filter2D(img_gray,-1,kernelx)
img_prewitty = cv2.filter2D(img_gray,-1,kernely)
img_prewitt = img_prewittx + img_prewitty
cv2.imshow('ori',img)
cv2.imshow('prewit x',img_prewittx)
cv2.imshow('prewit y',img_prewitty)
cv2.imshow('prewit xy',img_prewitt)
cv2.waitKey(0)
cv2.destroyAllWindows()