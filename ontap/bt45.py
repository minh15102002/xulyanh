import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
ICanny=cv2.Canny(v,100,200)
cv2.imshow('Anh bai 45',ICanny)
cv2.waitKey(0)
cv2.destroyAllWindows()