import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg',0)
y=9
x=11
print('Cac gia tri muc xam can 5x5',img[y-2:y+2,x-2:x+2])
cv2.waitKey(0)
cv2.destroyAllWindows()