import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(320, 240))

cascade = cv2.CascadeClassifier('../cascades/speed_limit_30.xml')

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	signs = cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)
    
    key = cv2.waitKey(1) & 0xFF

 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
 







