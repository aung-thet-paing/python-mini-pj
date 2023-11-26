import cv2
import time

vid =  cv2.VideoCapture(0)
result = True
name = int(round(time.time() * 1000))
while result:
	ret, frame = vid.read()
	cv2.imwrite(f'screenshot/{name}.jpg', frame)
	result = False
	print("Capture image")

vid.release()