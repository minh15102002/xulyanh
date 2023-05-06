import cv2
img = cv2.imread("images\\anh1.jpg")
img1 = cv2.resize(img,(320,240))
imglg = cv2.imread("images\\cayxang.jpg")
# cv2.imshow("logo",img1)
img2 = cv2.imread("images\\dau.png")
imglg1 = cv2.resize(imglg,(100,60))
imglg2 = cv2.resize(img2,(100,60))
# cv2.imshow("logo2",imglg)
# cv2.imshow("anh goc",img)
# (h,w,d)=img.shape
# print('height:{}, weith:{}, depth:{}'.format(h,w,d))
# them mau vao trong anh
# px= img[150,100]
# img1 = cv2.resize(img,(320,240))
# for i in range(120,200):
#     img1[80:160,i] = [0,0,255]
# print("pixel",px)  #img or px  
# cv2.imshow("resize: ",img1)
# tao mat na logo
img1[80:140,100:200]=imglg1
cv2.imshow("res: ",img1)
img1[50:110,160:260]=imglg2
cv2.imshow("res: ",img1)
cv2.waitKey(0)
cv2.destroyWindow()