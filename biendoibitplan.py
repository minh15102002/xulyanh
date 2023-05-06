import cv2
import numpy as np
img = cv2.imread('images\\cayxang.jpg',0)
img=cv2.resize(img,(640,480))
img = np.array(img)
for k in range(7):
    plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)
    res = cv2.bitwise_and(plane, img)
    img_bit_slice = (res * 255).astype(np.uint8)
    cv2.imshow(f'anh bien doi bit plan slicing {k}',img_bit_slice)
cv2.imshow('anh goc',img)
cv2.waitKey(0)
cv2.destroyAllWindows()