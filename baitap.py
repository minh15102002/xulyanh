import cv2
import numpy as np
img = cv2.imread("images\\cayxang.jpg")
cv2.imshow("anh goc",img)
img_hsv= cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.imshow("anh hsv",img_hsv)
h,s,v =cv2.split(img_hsv)
# (h,s,v) = img_hsv.shape
cv2.imshow("anh v",v)
cv2.waitKey()
cv2.destroyAllWindows()
