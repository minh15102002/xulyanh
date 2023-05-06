import cv2
img=cv2.imread('.\images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
cv2.imshow('Anh kenh mau S',s)
y=10
x=20
print(img_hsv[y-2:y+2,x-2:x+2])
cv2.waitKey(0)
cv2.destroyAllWindows()