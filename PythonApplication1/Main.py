
#-----------------------------------------------------------------------
#      	Image Cryptogrophy v0.2
# 		Generates encryption keys from image data as seed
# 		for increased random
#		started: 28/01/2020 updated: 29/01/2020 
#		comp tested: 29/01/2020
#		Author: AH
#-----------------------------------------------------------------------
import os
import cv2 as cv
import numpy as np
import random as rand
import statistics as stat
import matplotlib.pyplot as plt 

#initialise camera
try:
	cam = cv.VideoCapture(0)
except:
	cam = "Failed"
intCount = 0
intPwdLength = 2256
strPassword = ""

fast = cv.FastFeatureDetector_create()
orb = cv.ORB_create()
blob = cv.SimpleBlobDetector_create()

arryPlotX = np.zeros(254-32)
arryPlotY = np.zeros(254-32)
for i in range(0, 254-32):
	arryPlotY[i] = i+32

for intCount in range(0, intPwdLength):
	#collect frame
	ret, frame = cam.read()

	features = fast.detect(frame, None)

	#split channels
	Ch0 = frame[:,:, 0]
	Ch1 = frame[:,:, 1]
	Ch2 = frame[:,:, 2]

	if len(features) < 1:
		#average frames
		intCh0 = np.mean(Ch0)
		intCh1 = np.mean(Ch1)
		intCh2 = np.mean(Ch2)
	else:		
		intCh0 = len(fast.detect(Ch0, None))
		intCh1 = len(orb.detect(Ch1, None))
		intCh2 = len(blob.detect(Ch2, None))

	#initialise seed
	#				R					G					B
	intSeed = int(intCh0) << 32 | int(intCh1) << 16 | int(intCh2) << 0
	intSeed2 = int(intCh0) +		int(intCh1) +		int(intCh2)

	#print(intSeed)
	rand.seed(intSeed)

	#create random letter
	letter = rand.randint(32,(254-33))
	#print(letter)
	
	#add letter to array 
	if letter == 32:
		strPassword += str(chr(letter+1))
	else:
		strPassword += str(chr(letter))
	cv.waitKey(5)

	arryPlotX[letter] += 1

plt.plot(arryPlotX, arryPlotY)
plt.show()

print(strPassword)

