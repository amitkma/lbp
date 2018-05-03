import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('photo_2.jpg',0)

cv2.imshow("orig", img)

##canny
img = cv2.blur(img,(2,2))
gray_seg = cv2.Canny(img, 0, 50)
cv2.imshow("cannyonoriginal", gray_seg)

#applying erosion
kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(img,kernel, iterations = 1)
cv2.imshow("erode",erosion)


##now applying canny 
gcan = cv2.Canny(erosion, 0, 50)
cv2.imshow("cannyaftererosion", gcan)
cv2.waitKey(0)
