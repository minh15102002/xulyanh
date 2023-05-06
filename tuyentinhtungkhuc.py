import cv2
import numpy as np

def changePixelVal(img, r1, s1, r2, s2):
    if (0 <= img and img <= r1):
        return (s1 / r1)*img
    elif (r1 < img and img <= r2):
     return ((s2 - s1)/(r2 - r1)) * (img - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (img - r2) + s2
img = cv2.imread('images\\gray1.jpg')
cv2.imshow("anh goc",img)
r1, s1, r2, s2 = 70, 0, 140, 255
vec = np.vectorize(changePixelVal)
img1 = vec(img, r1, s1, r2, s2)
cv2.imshow('anh bien doi tung khuc',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()