import cv2
img=cv2.imread('.\images\\cayxang.jpg')
imgrs=cv2.resize(img,(320,320))
img_hsv=cv2.cvtColor(imgrs,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
img_s_eq=cv2.equalizeHist(s)
cv2.imshow('Anh kenh s sau can bang',img_s_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()