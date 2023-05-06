import cv2
import numpy as np
img = cv2.imread('images\\cayxang.jpg') 
img_rs= cv2.resize(img,[640,480])
cv2.imshow('anh goc',img_rs)
# imggray= cv2.cvtColor(img_rs, cv2.COLOR_RGB2GRAY)
# cv2.imshow("anh xam",imggray)
b,g,r=cv2.split(img_rs)
# cv2.imshow("anh b",b)
# cv2.imshow("anh g",g)
# cv2.imshow("anh r",r)
h=480
w=640
Igray=np.zeros((h,w),dtype=np.uint8)
Igray[:,:] = 0.28*b+0.45*g+0.13*r
cv2.imshow("anh gray",Igray)
c,e,gammar=0.5,0.01,2
img_exp=c*(255*(img_rs/255+e)**gammar)
img_exp=np.array(img_exp, dtype=np.uint8)
cv2.imshow('anh bien doi ham mu',img_exp)
cv2.waitKey(0)
cv2.destroyAllWindows()