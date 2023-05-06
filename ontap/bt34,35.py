import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
Igray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img_b=cv2.threshold(Igray,0,255,cv2.THRESH_OTSU)
Icopy=img.copy()
contours,hierarchy=cv2.findContours(img_b,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
if(len(contours)!=0):
    cv2.drawContours(Icopy, contours, -1, 0, 4)
    cv2.imshow('Anh nhi phan',img_b)
    cv2.imshow('Anh bai 34',Icopy)
cv2.waitKey(0)
cv2.destroyAllWindows()