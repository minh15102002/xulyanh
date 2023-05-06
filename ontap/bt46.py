import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
Icopy=img.copy()
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img_b=cv2.threshold(img_gray,0,255,cv2.THRESH_OTSU)
contours,hirerachy=cv2.findContours(img_b,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
if(len(contours)!=0):
    cv2.drawContours(Icopy,contours,-1, 255, 4)
    cv2.imshow('Anh bai 46',Icopy)
cv2.waitKey(0)
cv2.destroyAllWindows()