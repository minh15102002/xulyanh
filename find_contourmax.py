import cv2
import numpy as np
font=cv2.FONT_HERSHEY_COMPLEX
img_0 = cv2.imread('images\\cayxang.jpg')
img = cv2.resize(img_0,(320,240))
cv2.imshow('img binary', img )
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, img1 = cv2.threshold(img_gray, 0 , 255, cv2.THRESH_OTSU)
cv2.imshow('img binary', img1 )

Icopy = img.copy()
# img1 = img.copy()
# img2 = img.copy()
img3 = img.copy()
img4 = img.copy()
img5 = img.copy()
contours,hiearchy=cv2.findContours(img1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
if len(contours) !=0:
        cv2.drawContours(img,contours,-1,255,3)

    # tim contour lon nhat
        areas=[cv2.contourArea(c) for c in contours]
        max_idx=np.argmax(areas)
        min_idx=np.argmin(areas)
        cnt=contours[max_idx]
        x,y,w,h=cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.drawContours(img3,contours[max_idx],-1,(0,255,255),3)
        cv2.drawContours(img4,contours[min_idx],-1,(0,255,255),3)
        # 
        mask=np.zeros((img.shape[:2]),np.uint8)
        mask[y:y+h,x:x+w]=255
        masked_img=cv2.bitwise_and(img1,img1,mask=mask)
        cv2.imshow('max',masked_img)
        filter_img=cv2.blur(masked_img,(5,5))
        cv2.imshow('max1',filter_img)
        thresh, filter_img2 = cv2.threshold(filter_img, 150 , 255, cv2.THRESH_OTSU)
        cv2.imshow('max2',filter_img2)
        filter_img3=cv2.blur(filter_img2,(5,5))
        cv2.imshow('max3',filter_img3)
        thresh, filter_img4 = cv2.threshold(filter_img3, 150 , 255, cv2.THRESH_OTSU)
        cv2.imshow('max4',filter_img4)
        kernel=np.ones((5,5),np.uint8)
        erosion= cv2.dilate(filter_img4,kernel,iterations=1)
        masked_img_final=cv2.bitwise_and(img5,img5,mask=erosion)
        x=100
        y=100
        cv2.putText(masked_img_final,'text',(x,y),font,0.5,(255,0,0))
        cv2.imshow('max contour',masked_img_final)


cv2.waitKey()
cv2.destroyAllWindows()


