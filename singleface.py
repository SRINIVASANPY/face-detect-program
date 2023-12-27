#importing open cv library
import cv2 
trainedData=cv2.CascadeClassifier('Face.xml')  
#data load
img=cv2.imread('vijay-20220622092431-662.jpg') 
#choose a image
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
faceCoordinates=trainedData.detectMultiScale(grayimg) 
#detect face #[[38x, 165y, 279width 279height]]
x,y,w,h=faceCoordinates[0] 
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow('Window',img) 
#dispaly image
cv2.waitKey() 
#pause execution of the program until any key is pressed
print('END OF PROGRAM')