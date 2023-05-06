import cv2
import numpy as np
img0=cv2.imread('.\images\\cayxang.jpg',0)
img=cv2.resize(img0,(320,360))
Icany=cv2.Canny(img,100,200)
cv2.imshow("cany",Icany)
if(img[100,300]==255):
    print('La diem tren bien')
else:
    print('Khong la diem tren bien')
cv2.waitKey(0)
cv2.destroyAllWindows()

