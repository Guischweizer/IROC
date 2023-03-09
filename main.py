#!/usr/bin/env python3
import cv2

# Enable webcam
# '0' is default ID for builtin web cam
# for external web cam ID can be 1 or -1
image_capture = cv2.VideoCapture(-1)
image_capture.set(3, 640) # set width as 640
image_capture.set(4, 480) # set height as 480

# OpenCV has many pre-trained data as XML files.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

while True:
    success, img = image_capture.read() # capture frame from video
    # converting image from color to grayscale 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Getting corners around the face
    # 1.3 = scale factor, 5 = minimum neighbor can be detected
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)  

    # drawing bounding box around face
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,   0), 3)
        img = cv2.putText(img, "rosto", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2)

    # detecting eyes
    eyes = eye_cascade.detectMultiScale(img_gray)

    # drawing bounding box for eyes
    for (ex, ey, ew, eh) in eyes:
        img = cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 3)
        img = cv2.putText(img, "olho", (ex, ey-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2)
        
    # # detecting smiles
    # smiles = smile_cascade.detectMultiScale(img_gray)

    # # draw a bounding box for smile
    # for (sx, sy, sw, sh) in smiles:
    #     img = cv2.rectangle(img, (sx, sy), (sx+sw, sy+sh), (220, 20, 60), 3)

    # displaying image with bounding box
    cv2.imshow('face_detect', img)
    # loop will be broken when 'q' is pressed on the keyboard
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
image_capture.release()
cv2.destroyWindow('face_detect')