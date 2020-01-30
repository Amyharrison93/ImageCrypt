
#-----------------------------------------------------------------------
#      	Image Cryptogrophy v0.2
# 		Generates encryption keys from image data as seed
# 		for increased random
#		started: 28/01/2020 updated: 29/01/2020 
#		comp tested: 29/01/2020
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
intPwdLength = 32*100
strPassword = ""

fast = FastFeatureDetector_create()
orb = ORB_create()
blob = SimpleBlobDetector_create()

arryPlotX = np.zeros(254)
arryPlotY = np.zeros(254)
for i in range(0, 254):
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
	
	letter = (intSeed%254)
	#print(letter)
	
	#add letter to array 
	strPassword += str(chr(letter))
	waitKey(1)

	arryPlotX[letter] += 1
	
print(datetime.now())

plt.bar(arryPlotY, arryPlotX)
plt.show()

print(arryPlotX)

#print(strPassword)


