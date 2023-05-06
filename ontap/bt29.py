import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
img_s_loc=cv2.medianBlur(s,5)
img_new_hsv=cv2.merge((h,img_s_loc,v))
img_rgb=cv2.cvtColor(img_new_hsv,cv2.COLOR_HSV2RGB)
cv2.imshow('Anh bai 29',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()