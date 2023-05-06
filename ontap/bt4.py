import cv2 
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
h=img.shape[0]
w=img.shape[1]
Igray=np.zeros((h,w),dtype='uint8')
b,g,r=cv2.split(img)
Igray[:,:]=0.39*r+0.5*g+0.11*b
ret,img_b=cv2.threshold(Igray,0,255,cv2.THRESH_OTSU)
cv2.imshow('Anh nhi phan',img_b)
cv2.waitKey(0)
cv2.destroyAllWindows()