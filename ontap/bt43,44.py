import cv2
import numpy as np
img=cv2.imread('.\images\\cayxang.jpg')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img_hsv)
v_max=np.max(v)
v_min=np.min(v)
v_new=np.uint8((v-v_min)*(255/(v_max-v_min)))
img_new_hsv=cv2.merge((h,s,v_new))
img_rgb=cv2.cvtColor(img_new_hsv,cv2.COLOR_HSV2RGB)
cv2.imshow('Anh bai 43,44',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()