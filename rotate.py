import cv2
import numpy
img=cv2.imread("C:/Users/Parth Khanna/Pictures/Screenshots/Screenshot (104).png",0)
cv2.resizeWindow("abc",80,50)
rows,column=img.shape
x=rows/2
y=column/2
img1=cv2.getRotationMatrix2D((x,y),90,1)
img2=cv2.warpAffine(img,img1,(column,rows))
cv2.imshow("abc",img2)
print(img.shape)
cv2.waitKey()
cv2.destroyAllWindows()

