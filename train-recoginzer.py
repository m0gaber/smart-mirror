import cv2
import os
import glob
import numpy as np


path =np.sort(glob.glob('dataset/user*.jpg'))
# recognizer = cv2.face.createEigenFaceRecognizer()
recognizer = cv2.createLBPHFaceRecognizer()

detector= cv2.CascadeClassifier('C:\Users\M_K\Desktop/face rec - Copy\Haarcascades/haarcascade_frontalface_default.xml')

# print(path)

def getImagesAndLabels(path):

	faceSamples=[]
	faceLabels=[]

	for i in path:

		img=cv2.imread(i,0)
		print(i)
		faceLabel =int(i.split('.')[1])
		faces=detector.detectMultiScale(img)
		for (x,y,w,h) in faces:
			faceSamples.append(img[y:y+h,x:x+w])
			faceLabels.append(faceLabel)


		# print(i.split('.')[1])
		# cv2.imshow('image',img)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()

	return faceSamples,faceLabels


faces,labels= getImagesAndLabels(path)
labels=np.array(labels)
labels.astype(int)
print(labels)
recognizer.train(faces,np.array(labels))
recognizer.save('training/training.yml')
