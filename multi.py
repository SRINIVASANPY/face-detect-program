import cv2
facedetect = cv2.CascadeClassifier('Face.xml')
img = cv2.imread('98577420.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = facedetect.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255,),2)
    
cv2.imshow('r',img)
cv2.waitKey()
