import cv2
import numpy as np

img_0 = cv2.imread('images\\cayxang.jpg',1)
img = cv2.resize(img_0,(320,240))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel=np.ones((3,3),np.uint8)
Iedge=cv2.Canny(img_gray,170,255)
cv2.imshow('img iedge',Iedge)
# noi bien
kernel1=np.ones((3,3),dtype=np.uint8)
Iclosing=cv2.morphologyEx(Iedge,cv2.MORPH_CLOSE,kernel1)
cv2.imshow('img closing',Iclosing)
# lam manh duong bien
# kernel2=np.enos((1,1),dtype=np.uint8)
# Iclosing1=cv2.erode(Iclosing,kernel2,iterations=1)
# cv2.imshow('img closing',Iclosing1)

# Idilate=cv2.dilate(Iedge,kernel,iterations=1)
# Iclosing3=cv2.dilate(Iclosing1,cv2.MORPH_CLOSE,kernel2)
# cv2.imshow('img closing',Iclosing3)
cv2.waitKey()
cv2.destroyAllWindows()