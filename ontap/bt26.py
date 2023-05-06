import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
img_loc=cv2.medianBlur(img,5)
cv2.imshow('Anh goc',img)
cv2.imshow('Anh bai 26',img_loc)
cv2.waitKey(0)
cv2.destroyAllWindows()