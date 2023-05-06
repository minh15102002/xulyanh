import cv2
import numpy as numpy
import matplotlib.pyplot as plt
img = cv2.imread('images\\cayxang.jpg',0)
img=cv2.resize(img,(640,480))
cv2.imshow('anh goc',img)
hist = cv2.calcHist([img], [0], None, [256], [0,255])
plt.plot(hist, color = 'b')
# plt.subplot(221),plt.imshow(img,"gray")
# plt.plot(img.ravel(), 256, [0,255])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()