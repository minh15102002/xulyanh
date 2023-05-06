import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('.\images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
hist1 = cv2.calcHist([h],[0],None,[256],[0,256])
plt.plot(hist1, color ="r")
hist2 = cv2.calcHist([s], [0], None, [256], [0, 256])
plt.plot(hist2, color = 'b')
hist3 = cv2.calcHist([v], [0], None, [256], [0, 256])
plt.plot(hist3, color = 'g')
plt.title("hist kenh h,s,v ")
plt.show()
hist_hsv = cv2.calcHist(img_hsv,[0],None,[256],[0,256])
plt.plot(hist_hsv)
plt.title("hist kenh hsv ")
plt.show()
hist_s = cv2.calcHist(s,[0],None,[256],[0,256])
plt.plot(hist_s)
plt.title("hist kenh s ")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()