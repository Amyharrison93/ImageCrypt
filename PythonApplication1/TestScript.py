#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------
#      	Image Cryptogrophy v0.2
# 		Generates encryption keys from image data as seed
# 		for increased random
#		started: 28/01/2020 updated: 31/01/2020 
#		comp tested: 31/01/2020
#		Author: AH
#-----------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt 

from datetime import datetime
from cv2 import(
	FastFeatureDetector_create,
	ORB_create,
	SimpleBlobDetector_create,
	VideoCapture,
	waitKey)
#initialise camera
try:
	cam = VideoCapture(0)
except:
	cam = "Failed"
	
intCount = 0
intPwdLength = 32

strPassword = ""
strFileName = "./Results/Result{0}.png".format(datetime.now())
strFileName = strFileName.replace(":", "")
strFileName = strFileName.replace(" ", "")
print(strFileName)

fast = FastFeatureDetector_create()
orb = ORB_create()
blob = SimpleBlobDetector_create()

arryPlotX = np.zeros(126)
arryPlotY = np.zeros(126)

arryFastStdDev = np.zeros(intPwdLength)
arryOrbStdDev = np.zeros(intPwdLength)
arryBlobStdDev = np.zeros(intPwdLength)

for i in range(0, 126):
	arryPlotY[i] = i

print(datetime.now())

for intCount in range(0, intPwdLength):
	#collect frame
	ret, frame = cam.read()
	#frame = cv.resize(frame, (320, 480))
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
	
	letter = 32 + ((intSeed%126) - 32)
	#print(letter)
	
	#add letter to array 
	strPassword += str(chr(letter))
	waitKey(1)

	arryPlotX[letter] += 1
	arryFastStdDev[intCount] = intCh0
	arryOrbStdDev[intCount] = intCh1
	arryBlobStdDev[intCount] = intCh2
	
print(datetime.now())

flCh0Deviation = np.std(arryFastStdDev)
flCh1Deviation = np.std(arryOrbStdDev)
flCh2Deviation = np.std(arryBlobStdDev)

plt.bar(arryPlotY, arryPlotX)
plt.ylabel('Number of occurences')
plt.xlabel('ASCII character')
plt.title(
	"Std Deviation \n ch0: {0} \n ch1: {1} \n ch2: {2}"
	.format(flCh0Deviation, flCh1Deviation, flCh2Deviation))
plt.savefig(strFileName)
plt.show()


print(strPassword)


