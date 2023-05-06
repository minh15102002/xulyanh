import cv2
import numpy as np
img= cv2.imread("images\\cayxang.jpg")
cv2.imshow("anh goc",img)

b,g,r=cv2.split(img)
(h,w,d)=img.shape
print("W: {} H: {} D: {}".format(h,w,d))
img_neg =255-img
img_neg =255-r
cv2.imshow("anh am ban",img_neg)
cv2.imshow("anh b",b)
cv2.imshow("anh g",g)
cv2.imshow("anh r",r)


cv2.waitKey(0)
cv2.destroyAllWindows()