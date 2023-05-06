import cv2
import numpy as np

img_0 = cv2.imread('images\\barcode.jpg')
img = cv2.resize(img_0,(320,240))
img_hsv = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
cv2.imshow('img', img )
h,s,v = cv2.split(img_hsv)
cv2.imshow('anh s',s)

img_canbang = cv2.equalizeHist()
cv2.imshow('anh s can bang',img_canbang)



cv2.waitKey()
cv2.destroyAllWindows()