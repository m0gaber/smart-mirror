import cv2
import numpy as np
import os
import json

recognizer = cv2.createLBPHFaceRecognizer()


##change directories here


recognizer.load('C:\Users\M_K\Documents\GitHub\smart-mirror\Facial-recognition-master\Facial_recognition_master/training/training.yml')
detector= cv2.CascadeClassifier('C:\Users\M_K\Documents\GitHub\smart-mirror\Facial-recognition-master\Facial_recognition_master\haar-cascades\haarcascade_frontalcatface.xml')
with open('C:\Users\M_K\Documents\GitHub\smart-mirror\Facial-recognition-master\Facial_recognition_master\data.txt') as json_file:
	data = json.load(json_file)

cam =cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
text="Unknown"
while(True):
	ret,img = cam.read()

	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	faces = detector.detectMultiScale(gray,1.2,5)
#apply
	for x,y,w,h in faces:

		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

		Id,conf=recognizer.predict(gray[y:y+h,x:x+w])

		if(conf<50):

			text=data[str(Id)]
		else:
			text="Unknown"
		print("ID",Id)
		print("Conf",conf)
		cv2.putText(img,text,(x,y+h), font,1,(255,0,0))
	cv2.imshow('image',img)
	if cv2.waitKey(10) & 0xFF==ord('q') or text!="Unknown" :
		break
	# if text!="Unknown" :
	# 	break
cam.release()
print (text)
cv2.destroyAllWindows()
