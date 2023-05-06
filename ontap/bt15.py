import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg',0)
cv2.imshow('Anh xam',img)
y=109
x=130
print('Gia tri muc xam can 5x5',img[y-2:y+2,x-2:x+2])
cv2.waitKey(0)
cv2.destroyAllWindows()