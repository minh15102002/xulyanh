import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
sobelx=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobely=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
print("Gradient theo huong x",sobelx)
print("Gradient theo huong y",sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()