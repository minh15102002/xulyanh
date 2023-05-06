import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
Icopy=img.copy()
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img_b=cv2.threshold(img_gray,0,255,cv2.THRESH_OTSU)
contours,hirerachy=cv2.findContours(img_b,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
if(len(contours)!=0):
   area=[cv2.contourArea(c) for c in contours]
   max_index=np.argmax(area)
   max_area=cv2.contourArea(contours[max_index])
   for cnt in contours:
       area2=cv2.contourArea(cnt)
       if(area2>max_area/5.0):
         cv2.drawContours(Icopy,[cnt],-1, (0, 255, 255), 2)
         cv2.imshow('Anh bai 47',Icopy)
cv2.waitKey(0)
cv2.destroyAllWindows()