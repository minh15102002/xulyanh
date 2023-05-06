import cv2
import numpy as np



img_0 = cv2.imread('images\\cayxang.jpg',1)
img = cv2.resize(img_0,(320,240))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, img1 = cv2.threshold(img_gray, 0 , 255, cv2.THRESH_OTSU)
cv2.imshow('img binary', img1 )

Icopy = img.copy()
img2 = img.copy()
img3 = img.copy()
contours,hiearchy=cv2.findContours(img1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
if len(contours) !=0:
# ve con tour len hinh goc
    cv2.drawContours(img,contours,-1,255,3)

    # tim contour lon nhat
    areas=[cv2.contourArea(c) for c in contours]
    max_idx=np.argmax(areas)
    min_idx=np.argmin(areas)
    cnt=contours[max_idx]

    x,y,w,h=cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.drawContours(img2,contours[max_idx],-1,(0,255,255),3)
    cv2.drawContours(img3,contours[min_idx],-1,(0,255,255),3)
cv2.imshow('contours',img)
cv2.imshow('contours max',img2)
cv2.imshow('contours min',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()


