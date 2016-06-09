import cv2 #this will immport opencv library
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
image = cv2.imread("im1.jpg") #this will read an image from directory and we get an object of that source image called "sample.png" as image 
cv2.resize(image,(500,500))
cv2.imshow("image",image)
cv2.waitKey(0)
