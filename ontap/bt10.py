import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
cv2.imshow('Anh kenh mau S',s)
print('Muc sang lon nhat kenh mau V',np.max(v))
cv2.waitKey(0)
cv2.destroyAllWindows()