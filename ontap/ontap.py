import cv2 
import numpy as np
img = cv2.imread(".\images\\cayxang.jpg")
(h, w, d) = img.shape
print("width={}, height={}, depth={}".format(w, h, d))
imgrs=cv2.resize(img,(480,480))
cv2.imshow("anh goc",imgrs)
# 20
w = 300
h = 256
points = (w, h)
imgrsh = cv2.resize(imgrs, points, interpolation= cv2.INTER_LINEAR)
cv2.imshow("anh resize",imgrsh)
# 21
imgrs2=cv2.resize(img,(256,256))
cv2.imshow("rs",imgrs2)
# 22
edges = cv2.Canny(imgrs, 100, 300)
cv2.imshow("anh canny",edges)
# 23,24
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, img1 = cv2.threshold(img_gray, 0 , 255, cv2.THRESH_OTSU)
# cv2.imshow('img binary', img1 )
# thresh, filter_img2 = cv2.threshold(img_gray, 150 , 255, cv2.THRESH_OTSU)
kernel_averaging_5_5 = np.ones((5, 5), np.float32)/25
smooth_image_f2D_5_5 = cv2.filter2D(imgrs, -1, kernel_averaging_5_5)
cv2.imshow('img 5x5', smooth_image_f2D_5_5 )
# 25
imghsv=cv2.cvtColor(imgrs,cv2.COLOR_HSV2BGR)
h,s,v=cv2.split(imghsv)
kernel5_5 = np.ones((5, 5), np.float32)/25
smooth5_5 = cv2.filter2D(h, -1, kernel5_5)
cv2.imshow('img2 5x5', smooth5_5 )
# 26
Im = cv2.medianBlur(imghsv, 5)
cv2.imshow("loc median", Im)
# 27
x=11
y=9
print(imghsv[y-2:y+2,x-2:x+2])
# 28
# blur = cv2.blur(img,(3,3))
Imgv = cv2.medianBlur(v, 5)
cv2.imshow("loc median Iv", Imgv)
# 29
I3 = cv2.medianBlur(imghsv, 3)
imgrbg=cv2.cvtColor(I3,cv2.COLOR_RGB2BGR)
cv2.imshow("loc median i3", imgrbg)
# 30
Icanny = cv2.Canny(image=imgrs, threshold1=109, threshold2=130)
cv2.imshow('Icanny',Icanny)
# 31
Icanny = cv2.Canny(image=imgrs, threshold1=100, threshold2=120)
cv2.imshow('Icanny2',Icanny)
# 32
Icanny = cv2.Canny(image=imgrs, threshold1=160, threshold2=326)
cv2.imshow('Icanny',Icanny)
# 33
ret, Ib = cv2.threshold(img_gray, 90, 255, cv2.THRESH_OTSU)
cv2.imshow("anh nhi phan theo otsu", Ib)
# 34
thresh, I_bina= cv2.threshold(img_gray,0, 255, cv2.THRESH_OTSU)
I_copy=imgrs.copy()
contours, hierarchy = cv2.findContours(I_bina, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
area_cnt = [cv2.contourArea(cnt) for cnt in contours]
max = area_cnt[0]
for i in range(len(area_cnt)):
    if max < area_cnt[i]:
        max = area_cnt[i]
for contour in contours:
    if cv2.contourArea(contour) > (max /(5)):
        cv2.drawContours(I_copy, [contour], -1, (0, 255, 255), 3)
cv2.imshow('contours',I_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()