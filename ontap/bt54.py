import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
sobelx=cv2.Sobel(img,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)
print(sobelx)
cv2.imshow('Anh bai 54',sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()