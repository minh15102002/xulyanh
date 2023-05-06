import cv2
import numpy as np

img_0 = cv2.imread('images\\cayxang.jpg')
height, width = img_0.shape[:]
cv2.imshow('anh l',img_0)
print('width:',width)
print('height:',height)
img_hsv = cv2.cvtColor(img_0,cv2.COLOR_HSV2BGR)
h,s,v = cv2.split(img_hsv)
cv2.imshow('anh kenh h',img_hsv)
# img_lhsv = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)   
# cv2.imshow('Anh goc', img )
# h,s,v = cv2.split(img_lhsv)
# cv2.imshow('anh kenh s',s)
# #caua
# img_canbang = cv2.equalizeHist(s)
# cv2.imshow('anh kenh s can bang',img_canbang)
# #caub
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img1, img_binary = cv2.threshold(img_gray,0,255, cv2.THRESH_OTSU)
# cv2.imshow('Anh Binary',img_binary)
# #cauc
# b,g,r = cv2.split(img)
# grayscale = 0.39*r + 0.5*g +0.11*b
# ig = grayscale.astype('uint8')
# cv2.imshow('anh ig ',ig)
# caud
# img_hsv = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)   
# h,s,v = cv2.split(img_hsv)
# cv2.imshow('anh kenh s',s)


cv2.waitKey()
cv2.destroyAllWindows()