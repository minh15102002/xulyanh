import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
imgrz=cv2.resize(img,(256,256))
cv2.imshow("Anh bai 21,23",imgrz)
cv2.waitKey(0)
cv2.destroyAllWindows()