import cv2
import numpy as np
import time
import os
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(1)
if cam.read()[0]==False:
	cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 


dataset = 'C:\\Users\\jikhjo\\Desktop\\dataset\\new_dataset\\'
label = int(input('Enter label: '))
num_of_images = int(input('Enter number of images that you want to be taken: '))
starting_num = int(input('Enter starting image number: '))
count_images = starting_num
is_capturing = False
if not os.path.exists(dataset+str(label)):
	os.mkdir(dataset+str(label))
while True:
	img = cam.read()[1]
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_color = img[y:y+h, x:x+w]
	if len(faces) > 0:
		face = faces[0]
		if count_images-starting_num < int(num_of_images):
			if is_capturing:
				cv2.putText(img, str(count_images-starting_num), (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 0) )
				# if rand%2 == 0:
				# 	roi_color = cv2.flip(roi_color, 1)
				cv2.imwrite(dataset+str(label)+'/'+str(label) + str('_') + str(count_images)+'.jpg', roi_color)
				count_images += 1
				time.sleep(1)
				is_capturing = False
		else:
			break
		cv2.imshow('face', roi_color)
	cv2.imshow('img', img)
	keypress = cv2.waitKey(1)
	if keypress == ord('q'):
		break
	elif keypress == ord('c'):
		is_capturing = True

	
