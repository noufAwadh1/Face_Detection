import cv2
import numpy as np
# the url to load cascade classifier files:
#https://github.com/opencv/opencv/blob/master/data/haarcascades  
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
pic=cv2.imread('index2.jpg') 
scale_factor=1.2 
while 1:
	faces=face_cascade.detectMultiScale(pic,scale_factor,5) #load detecting function 
	for(x,y,w,h) in faces: # (x,y,w,h) means the dimension of image ,width and height 
		cv2.rectangle(pic,(x,y),(x+w,y+h),(255,0,0),2)  #drowing rectangle around the face
	
	print('Number of faces found {}'.format(len(faces))) #this loop is for counting the number of faces which was detect 
	cv2.imshow('faces',pic)
	k=cv2.waitKey(30) & 0xff
	if k==2:
		break
cv2.destroyAllWindows()

	
