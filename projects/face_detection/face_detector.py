import cv2 
import numpy as np 
from random import randrange
# import face_recognition as fr


trained_face_data=cv2.CascadeClassifier('haarscade_frontalface_default.xml')

# img=cv2.imread('images.jpeg') 

webcam=cv2.VideoCapture(0)

while True:
    successful_frame_read,frame=webcam.read()
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img) 
    for (x,y,w,h) in face_coordinates:
           cv2.rectangle (frame,(x,y),(x+w,y+h),(0,255,0),10)


    cv2.imshow('beauty spotted',frame) 
    key =cv2.waitKey(1)

    if key==81 or key==113:
        break
print("Code Terminated")

