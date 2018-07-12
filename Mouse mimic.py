# import the necessary packages
#sudo modprobe bcm2835-v4l2
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import pyautogui
import time
# import pygame
# import pygame.camera
import threading

pyautogui.FAILSAFE = False
import screeninfo
# pygame.init()
# pygame.camera.init()
screen = screeninfo.get_monitors()[0]
# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (45, 120, 65)
greenUpper = (64, 255, 255)
pts = deque(maxlen=2)

vs = VideoStream(src=0).start()
# allow the camera or video file to warm up
time.sleep(2.0)
# keep looping
#clock = pygame.time.Clock()

def function(hsv):
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
		# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
# find the largest contour in the mask, then use
# it to compute the minimum enclosing circle and
# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

# only proceed if the radius meets a minimum size
#...			if radius > 10:
	# draw the circle and centroid on the frame,
	# then update the list of tracked points
#...					cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
#...					cv2.circle(frame, center, 5, (0, 0, 255), -1)

# update the points queue
	pts.appendleft(center)
# loop over the set of tracked points
	for i in range(1, len(pts)):
# if either of the tracked points are None, ignore
# them
		if pts[i - 1] is None or pts[i] is None:
			continue
			

# otherwise, compute the thickness of the line and
# draw the connecting lines
#thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
#cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
		dx = pts[i][0] - pts[i-1][0]
		dy = pts[i][1] - pts[i-1][1]
		pyautogui.moveTo((pts[i][0]-dx)*screen.width/640, (pts[i][1] - dy)*screen.height/480, 0.1,pyautogui.easeInOutQuad)

if __name__  =='__main__':
	
	while True:
	# grab the current frame
			start=time.time()
			frame = vs.read()
	#frame.vflip()
	# handle the frame from VideoCapture or VideoStream
	#frame = frame[1] if args.get("video", False) else frame

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
			if frame is None:
					break

	# resize the frame, blur it, and convert it to the HSV
	# color space
			frame = imutils.resize(frame, width=600)
			blurred = cv2.GaussianBlur(frame, (11, 11), 0)
			hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

			t = threading.Thread(target=function(hsv))
			t.daemon=True
			t.start()

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask

		#x_prev* (60+screen.width)/640, y_prev*(40 + screen.height)/480,0.1,pyautogui.easeInOutQuad
# show the frame to our screen
#...			cv2.namedWindow("Frame",cv2.WINDOW_NORMAL)
#...			cv2.moveWindow("Frame", screen.x - 1, screen.y - 1)
#...			cv2.resizeWindow("Frame",screen.width,screen.height)
#...			cv2.imshow("Frame", frame)
			#time.sleep(time.time()-start)
			# clock.tick(30)
			key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
			if key == ord("q"):
				vs.stop()
				break
			# close all windows
	cv2.destroyAllWindows()
	# pygame.quit()


	


