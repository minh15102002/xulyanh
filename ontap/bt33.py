import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg',0)
ret,img_b=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
cv2.imshow('Bai 33',img_b)
cv2.waitKey(0)
cv2.destroyAllWindows()