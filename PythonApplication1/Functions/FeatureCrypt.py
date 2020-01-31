#-----------------------------------------------------------------------
#      	Image feature Cryptogrophy v0.1
# 		Generates encryption keys from image data as seed
# 		for increased randomness using Features
#		inputs:
#			intLength is the length of the cryptokey, standard length is 32
#			intCamLoc is the camera to use, default is 0
#		started: 31/01/2020 
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

def ImageFeatureCrypt(intLength = 32, intCamLoc = 0):
	#initialise camera
	try:
		cam = VideoCapture(intCamLoc)
	except:
		cam = "Failed"
	
	intCount = 0
	intPwdLength = intLength
	strPassword = ""

	fast = FastFeatureDetector_create()
	orb = ORB_create()
	blob = SimpleBlobDetector_create()

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

		#ensure not null or empty
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
	
		#add letter to array 
		strPassword += str(chr(letter))
		waitKey(1)

	return strPassword



