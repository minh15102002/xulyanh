import cv2
import numpy as np
# font=cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread('images\\cayxang.jpg')
imgrs = cv2.resize(img,(320,240))
# cv2.imshow('img binary', imgrs )
img_gray = cv2.cvtColor(imgrs, cv2.COLOR_BGR2GRAY)
thresh, img1 = cv2.threshold(img_gray, 0 , 255, cv2.THRESH_OTSU)
cv2.imshow('img binary', img1 )
Icopy = imgrs.copy()
img3 = imgrs.copy()
img4 = imgrs.copy()
img5 = imgrs.copy()
contours,hiearchy=cv2.findContours(img1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
if len(contours) !=0:
        cv2.drawContours(imgrs,contours,-1,255,3)
        areas=[cv2.contourArea(c) for c in contours]
        max_idx=np.argmax(areas)
        min_idx=np.argmin(areas)
        cnt=contours[max_idx]
        x,y,w,h=cv2.boundingRect(cnt)
        cv2.rectangle(imgrs,(x,y),(x+w,y+h),(0,0,255),2)
        x=15
        y=15
        dientich=cv2.contourArea(cnt)
        strdt=str(dientich)
        chuvi=cv2.arcLength(cnt,True)
        strcv=str(chuvi)
        font=cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(imgrs,strdt,(x,y),font,0.5,(255,255,255))
        cv2.putText(imgrs,strcv,(40,40),font,0.5,(255,255,255))
        cv2.imshow('puttext contour',imgrs)


cv2.waitKey()
cv2.destroyAllWindows()


