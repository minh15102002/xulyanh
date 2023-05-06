import cv2
import numpy as np
ig=cv2.imread(r'D:\xulyanh\ontap\imgontap.jpg')
cv2.imshow("anh goc",ig)
igr=cv2.cvtColor(ig,cv2.COLOR_BGR2GRAY)
ret,imgg=cv2.threshold(igr,0,255,cv2.THRESH_OTSU)
cv2.imshow("anh gr",imgg)
igcp=ig.copy()
igcp1=ig.copy()
contours,hierachy=cv2.findContours(imgg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
if(len(contours)!=0):
    cv2.drawContours(igcp,contours,-1,0,4)
    cv2.imshow('Anh bai  ',igcp)
    area=[cv2.contourArea(c) for c in contours]
    max_S=np.argmax(area)
    cv2.drawContours(igcp1,contours[max_S],-1,0,4)
    cv2.imshow('Anh bai 11 ',igcp1)

cv2.waitKey(0)
cv2.destroyAllWindows()