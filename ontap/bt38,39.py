import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
Ig=255-img
Igray=cv2.cvtColor(Ig,cv2.COLOR_BGR2GRAY)
ret,img_b=cv2.threshold(Igray,0,255,cv2.THRESH_OTSU)
Icopy=img.copy()
Icopy2=img.copy()
contours,hierarchy=cv2.findContours(img_b,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
if(len(contours)!=0):
    cv2.drawContours(Icopy, contours, -1, 255, 4)
    area=[cv2.arcLength(c,True) for c in contours]
    max_index=np.argmax(area)
    cv2.drawContours(Icopy2, contours[max_index], -1, 255, 4)
    cv2.imshow('Anh nhi phan',img_b)
    cv2.imshow('Contours cua anh',Icopy)
    cv2.imshow('Anh bai 38,39 duong con tua co chu vi lon nhat',Icopy2)
cv2.waitKey(0)
cv2.destroyAllWindows()