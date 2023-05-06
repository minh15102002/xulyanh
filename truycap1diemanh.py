import cv2
img = cv2.imread("images\\anh1.jpg")
cv2.imshow("anh goc",img)

# them mau vao trong anh
px= img[150,130]
for i in range(500):
    img[0:50,i] = [0,250,0]
print("pixel",px)  #img or px  
(h,w,d)=img.shape
print('height:{}, weith:{}, depth:{}'.format(h,w,d))
img1 = cv2.resize(img,(320,240))
cv2.imshow("resize: ",img)

# thay doi goc quay anh
img2 = cv2.transpose(img)
cv2.imshow("anh goc thay doi",img2)
cv2.waitKey(0)
cv2.destroyWindow()
