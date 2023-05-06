import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
h=img.shape[0]
w=img.shape[1]
new_h=256
# new_w=int(new_h/h*w)
new_w=int(new_h*w/h)
img_rz=cv2.resize(img,(new_w,new_h))
cv2.imshow('Anh goc',img)
cv2.imshow('Anh moi',img_rz)
cv2.waitKey(0)
cv2.destroyAllWindows()