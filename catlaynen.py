import cv2
import numpy as np
img=cv2.imread('images\\cayxang.jpg',0)
img=cv2.resize(img,(640,480))
cv2.imshow("anh goc",img)
h,w=img.shape
img_gls=img.copy()
A, B =50, 150
for i in range(0,h):
 for j in range(0,w):
  if(img[i][j]>A and img[i][j]<B):
   img_gls[i][j]=255 
cv2.imshow('gray level slicing',img_gls)
cv2.waitKey(0)
cv2.destroyAllWindows()
