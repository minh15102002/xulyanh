import cv2
import numpy as np
img = cv2.imread("images\\cayxang.jpg")
cv2.imshow("anh goc",img)
c = 255 / np.log(1 + np.max(img))
img_log = c * (np.log(img + 1))
img_log = np.array(img_log, dtype = np.uint8)
cv2.imshow('anh bien doi log',img_log)

cv2.waitKey(0)
cv2.destroyAllWindows()