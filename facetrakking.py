import cv2
from cvzone.FaceDetectionModule import FaceDetector
import pyfirmata
import numpy as np
import time



cap = cv2.VideoCapture(0)  # 0 for default camera, 1 for external camera

ws, hs = 1280, 720   # width and height of the video frame

cap.set(3, ws) # set  width ratio
cap.set(4, hs) #  set heigth ratio

if not cap.isOpened():   # check if the camera is opened
    print("Camera couldn't Access!!!") 

port = "COM8"   # change to your Arduino port

board = pyfirmata.Arduino(port)   # create an Arduino object

servo_pinX = board.get_pin('d:12:s') #pin 12 Arduino
servo_pinY = board.get_pin('d:10:s') #pin 10 Arduino
laser_pin = board.get_pin('d:11:o') #pin 11 Arduino

detector = FaceDetector()
servoPos = [90, 90] # initial servo position
servo_pinX.write(servoPos[0])  # set initial servo position

servo_pinY.write(servoPos[1]) #  set initial servo position

laser_pin.write(0)  # turn off laser

time.sleep(7) #wait for 7 seconds



while True:
    success, img = cap.read()   # read a frame from the camera

    img, bboxs = detector.findFaces(img, draw=True)   # detect faces in the frame


    if bboxs:   # if there are faces detected

        #get the coordinate
        fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
        pos = [fx, fy]
        #convert coordinat to servo degree
        servoX = np.interp(fx, [0, ws], [140, 30])
        servoY = np.interp(fy, [0, hs], [55, 125]) 
        #Make sure servo dont go beyond permissabble limits
        if servoX < 0:
            servoX = 0
        elif servoX > 180:
            servoX = 180
        if servoY < 0:
            servoY = 0
        elif servoY > 180:
            servoY = 180
        #Update servo positions
        servoPos[0] = servoX
        servoPos[1] = servoY
        laser_pin.write(1) #Turn on Laser
        


        cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)   # draw a circle around the face
        cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED) # draw a point on the center of face
        cv2.putText(img, "TARGET LOCKED", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3 )  # display "TARGET LOCKED" on the screen


    else: # IF no face is found
        cv2.putText(img, "NO TARGET", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)   # display "NO TARGET" on the screen
        servoPos = [90,90] #bring laser to center again if no face found
        laser_pin.write(0)  #turn off laser

    #give servo pos value to servo
    servo_pinX.write(servoPos[0]) 
    servo_pinY.write(servoPos[1])

    #Show image  on screen

    cv2.imshow("Image", img)
    cv2.waitKey(1)