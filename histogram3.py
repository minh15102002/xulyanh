import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images\\cayxang.jpg',0)
img=cv2.resize(img,(640,480))

img_equalization = cv2.equalizeHist(img)
cv2.imshow("anh goc",img)
cv2.imshow("anh equalition",img_equalization)

hist1 = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist1, color ="b")

# hist1=cv2.calcHist([img_equalization],[0],None,[256,[0,256]])
# plt.plot(hist1, color = "r")
plt.title("img histogram for blue chanel")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
