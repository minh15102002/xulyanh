import cv2
import numpy as np
img = cv2.imread("images\\gray1.jpg")
cv2.imshow("anh goc",img)
img_rs= cv2.resize(img,[640,480])
cv2.imshow("anh goc",img_rs)
c,e,gammar=0.5,0.01,5
img_exp=c*(255*(img_rs/255+e)**gammar)
img_exp=np.array(img_exp, dtype=np.uint8)
cv2.imshow('anh bien doi ham mu',img_exp)
cv2.waitKey(0)
cv2.destroyAllWindows()