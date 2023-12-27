#importing open cv library
import cv2
from random import randrange as r
#data load
trainedData=cv2.CascadeClassifier('Face.xml')  
#start webcam
webcam=cv2.VideoCapture(0)
while True:
    success,frame=webcam.read()
#Conversion to black and white(grayscale)
grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#detect faces
faceCoordinates=trainedData.detectMultiScale(grayimg)
for x,y,w,h in faceCoordinates:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(r(0,256),r(0,256),r(0,256)),2)
    cv2.imshow('Window',frame)
    key=cv2.waitKey(1)
    if(key==81 or key==113):
        break
webcam.release()
print('END OF PROGRAM')