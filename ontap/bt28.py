import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
kernel=np.ones((3,3),np.float32)/9
img_loc=cv2.filter2D(img,-1,kernel)
cv2.imshow('Anh goc',img)
cv2.imshow('Anh bai 28',img_loc)
cv2.waitKey(0)
cv2.destroyAllWindows()