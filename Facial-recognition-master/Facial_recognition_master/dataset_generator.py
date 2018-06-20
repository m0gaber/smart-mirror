
import numpy as np
import cv2
import os

import face_rec_functions



datasetPath='dataset'
if not os.path.exists(datasetPath):
	os.makedirs(datasetPath)

face_rec_functions.createFile()
name=raw_input('Enter your name:')

Id=face_rec_functions.dumpData(name)
print(Id)

count=0


detector= cv2.CascadeClassifier('haar-cascades/haarcascade_frontalcatface.xml')
cap = cv2.VideoCapture(0)

while(True):
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = detector.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

		count+=1

		cv2.imwrite(datasetPath+'/user.'+str(Id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])




	print(count)
	cv2.imshow('frame',img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	elif count>50:
		break

cap.release()
cv2.destroyAllWindows()
