import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
kernel=np.ones((5,5),np.float32)/25
img_loc=cv2.filter2D(s,-1,kernel)
cv2.imshow('Anh kenh S',s)
cv2.imshow('Anh bai 25',img_loc)
cv2.waitKey(0)
cv2.destroyAllWindows()