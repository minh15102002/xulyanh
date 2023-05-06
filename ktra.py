import cv2
import numpy as np
img= cv2.imread("images\\anh1.jpg")
cv2.imshow("anh goc",img)
(h,w,d)=img.shape
print("W: {} H: {} D: {}".format(h,w,d))
img_r=cv2.resize(img,(640,480))
cv2.imshow("resize",img_r)
# img_cl=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("cvt color",img_cl)
# (thread,img_thr)=cv2.threshold(img_cl,120,120,cv2.THRESH_OTSU)
# cv2.imshow("anhthread",img_thr)
# img_hsv=cv2.cvtColor(img,cv2.COLOR_HSV2BGR_FULL)
# cv2.imshow("anhhsv",img_hsv)
# b,g,r=cv2.split(img_r)
# cv2.imshow("anh b",b)
# cv2.imshow("anh g",g)
# cv2.imshow("anh r",r)
h,s,v=cv2.split(img_r)
cv2.imshow("anh h",h)
cv2.imshow("anh s",s)
cv2.imshow("anh v",v)
h=480
w=640
Igray=np.zeros((h,w),dtype=np.uint8)
Igray[:,:] = 0.2*h+0.5*s+0.3*v
cv2.imshow("anh igray",Igray)

img_mgr=cv2.merge([h, s, v])
cv2.imshow("anhmgr",img_mgr)


hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
s.fill(255)
v.fill(255)
hsv_image = cv2.merge([h, s, v])

cv2.imshow('example', hsv_image)
cv2.waitKey()
cv2.destroyWindow()