import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
Icanny=cv2.Canny(img,100,200)
cv2.imshow('Canny',Icanny)
if(Icanny[109,130]==255):
    print("Điểm ảnh này là điểm biên trên ảnh biên Canny")
else:
    print("diem anh nay khong phai diem bien tren canny")
cv2.waitKey(0)
cv2.destroyAllWindows()