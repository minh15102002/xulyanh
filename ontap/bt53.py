import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg',0)
min_gray = np.min(img)
max_gray = np.max(img)
mean_gray = np.mean(img)
print('min',min_gray)
print('max',max_gray)
print('mean',mean_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()