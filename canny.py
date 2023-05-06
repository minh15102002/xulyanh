import cv2
import numpy as np
img_o = cv2.imread('images\\cayxang.jpg',1)
img = cv2.resize(img_o,(320,240))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

t_lower = 50
t_upper = 150

img_canny = cv2.Canny(img_gray,t_lower,t_upper,L2gradient=True)
cv2.imshow('ori',img)
cv2.imshow('cany',img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()