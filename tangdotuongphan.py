import cv2
import numpy as np
gamma = 0.7
img = cv2.imread('images\\gray1.jpg')
cv2.imshow("anh goc",img)
img_constr = np.power(img, gamma)
max_val = np.max(img_constr.ravel())
img_constr = img_constr/max_val * 255
img_constr = img_constr.astype(np.uint8)
cv2.imshow("anh bien doi tuong phan contract",img_constr)
cv2.waitKey(0)
cv2.destroyAllWindows()