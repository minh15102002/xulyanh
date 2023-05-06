import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
cv2.imshow('Anh kenh mau H',h)
print('Muc sang trung binh kenh mau S',np.mean(s))
cv2.waitKey(0)
cv2.destroyAllWindows()