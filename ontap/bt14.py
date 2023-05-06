import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
h=img.shape[0]
w=img.shape[1]
cv2.imshow('Anh',img)
print('Gia tri ti le giua do cao vao do rong',h/w)
cv2.waitKey(0)
cv2.destroyAllWindows()