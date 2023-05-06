import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('images\\cayxang.jpg') 
img_rs= cv2.resize(img,[320,240])
cv2.imshow('anh goc',img_rs)
imghsv = cv2.cvtColor(img_rs, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(imghsv)
cv2.imshow('anh kenh s',s)
cv2.waitKey(0)
cv2.destroyAllWindows()