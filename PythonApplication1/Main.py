
import cv2 as cv
import numpy as np
import random as rand

#initialise camera
try:
	cam = cv.VideoCapture(0)
except:
	cam = "Failed"
intCount = 0
intPwdLength = 20
strPassword = ""

for intCount in range(0, intPwdLength):
	#collect frame
	ret, frame = cam.read()

	#select channels
	Ch0Selec = rand.randint(0,200)%2
	Ch1Selec = rand.randint(0,200)%2
	Ch2Selec = rand.randint(0,200)%2

	#split channels
	Ch0 = frame[:,:, Ch0Selec]
	Ch1 = frame[:,:, Ch1Selec]
	Ch2 = frame[:,:, Ch2Selec]

	#average frames
	intCh0 = np.mean(Ch0)
	intCh1 = np.mean(Ch1)
	intCh2 = np.mean(Ch2)

	#initialise seed
	intSeed = int(intCh0) << 32 | int(intCh1) << 16 | int(intCh2) << 0
	rand.seed(intSeed)

	#create random letter
	letter = 32 + rand.randint(0,(254-32))
	
	#add letter to array 
	strPassword += str(chr(letter))
	cv.waitKey(5)

print(strPassword)