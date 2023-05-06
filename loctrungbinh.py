import cv2
import numpy as np
img = cv2.imread('images\\anhnhieu.jpg')
img_mean0=cv2.blur(img,(3,3))
cv2.imshow('anh loc tb cua so 3x3',img_mean0)

s=[(3,3),(5,5),(7,7),(9,9)]
for i,k in enumerate(s):
    img_mean=cv2.blur(img,k)
    cv2.imwrite('images\\anhnhieu2.jpg',img_mean)
    cv2.imshow('anh tb (i)',img_mean)
img_mean1=cv2.blur(img,(9,9))
gama=1.8
img_constr=np.power(img_mean1,gama)
max_val=np.max(img_constr.ravel())
img_constr=img_constr/max_val*255
img_constr=img.astype(np.uint8)
cv2.imshow('anh tb 2 contrast',img_constr)
# can bang anh
# img_equ = cv2.equalizeHist(img)
# cv2.imwrite("images\\anh_equalizeHist.png",img_equ)
# cv2.imshow("Anh can bang histogram", img_equ)

cv2.waitKey(0)
cv2.destroyAllWindows()