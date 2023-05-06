import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images\\cayxang.jpg',1)
img=cv2.resize(img,(640,480))

mask = np.zeros(img.shape[:2],np.uint8)
mask [100:300,100:400] =255
masked_img= cv2.bitwise_and(img,img,mask=mask)
hist_full=cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask=cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(221),plt.imshow(img,"gray")
plt.subplot(222),plt.imshow(mask,"gray")
plt.subplot(223),plt.imshow(masked_img,"gray")
plt.subplot(224),plt.imshow(hist_full),plt.plot(hist_mask)
# plt.xlim([0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()