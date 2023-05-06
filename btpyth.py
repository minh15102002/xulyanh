# tang do sang kenh vcua anh hsv bang pp giam muc xam
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
img=cv2.resize(img,(640,480))
cv2.imshow("anh goc",img)
c = 255 / np.log(1 + np.max(img))
img_log = c * (np.log(img + 1))
img_log = np.array(img_log, dtype = np.uint8)
cv2.imshow('anh bien doi',img_log)
cv2.imshow("anh hsv",img_hsv)

# cv2.imshow("anh b",b)
# cv2.imshow("anh g",g)
# cv2.imshow("anh r",r)
img_hsvb=cv2.cvtColor(img_hsv,cv2.COLOR_RGB2BGR)
b,g,r=cv2.split(img_hsvb)
cv2.imshow("anh hsv b",b)
cv2.waitKey(0)
cv2.destroyAllWindows()