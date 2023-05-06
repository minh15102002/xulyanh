import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
v_new=cv2.normalize(v,None,alpha=0,beta=255,norm_type=cv2.NORM_MINMAX)
img_new_hsv=cv2.merge((h,s,v_new))
img_rgb=cv2.cvtColor(img_new_hsv,cv2.COLOR_HSV2RGB)
cv2.imshow('Anh bai 42',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()