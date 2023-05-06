import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('.\images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
hist_v = cv2.calcHist(v,[0],None,[256],[0,256])
plt.plot(hist_v)
plt.title("hist kenh v")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()