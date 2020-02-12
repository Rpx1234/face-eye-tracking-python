# pip install opencv-python
import cv2
#pip install numpy
import numpy as np
# The loading of the cascade file for face tracking
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#loads in the eye cascade file for eyes
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#imports camera feed 0 is usually the normal camera feed.
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    # changes color of video to grey scale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #creates rectangle around detected items.
    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        #defines that eyes won't be found outside of a face.
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ax,ay,aw,ah) in eyes:
            # Creates the rectangle onto the video
            cv2.rectangle(roi_color, (ax, ay), (ax+aw,ay+ah), (0,255,0), 2)
    cv2.imshow('img',img)
    # allows you to escape with the esc key
    i = cv2.waitKey(30) & 0xff
    if i == 27:
        break
#after while statment breaks when you press the esc key the window will be destroyed.
cap.release()
cv2.destroyAllWindows()
