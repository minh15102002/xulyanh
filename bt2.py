# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imread('images\\cayxang.jpg')
# img_hsv=cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
# img=cv2.resize(img,(640,480))
# cv2.imshow("anh goc",img)
# def changePixelVal(img, r1, s1, r2, s2):
#  if (0 <= img and img <= r1):
#   return (s1 / r1)*img
#  elif (r1 < img and img <= r2):
#   return ((s2 - s1)/(r2 - r1)) * (img - r1) + s1
#  else:
#   return ((255 - s2)/(255 - r2)) * (img - r2) + s2
# r1, s1, r2, s2 = 70, 0, 140, 255
# vec = np.vectorize(changePixelVal)
# img1 = vec(img, r1, s1, r2, s2)
# cv2.imshow('anh bien doi ',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('images\\cayxang.jpg')
img = cv2.resize(img, (640, 480))

img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
cv2.imshow('anh hsv', img_hsv)

h, s, v = cv2.split(img_hsv)
c = 255 / np.log(1 + np.max(v))
img_log = c * (np.log(v+1))
img_log = np.array(img_log, dtype= np.uint8)

img_new = cv2.merge((h, s, img_log))
cv2.imshow('anh hsv moi', img_new)

img_rgb = cv2.cvtColor(img_new, cv2.COLOR_BGR2RGB)
cv2.imshow('anh rgb moi', img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()