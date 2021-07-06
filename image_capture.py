import cv2
import numpy as np

def main():

	obj = cv2.VideoCapture(0)
	count = 0
	while(1):
		
		flag, frame = obj.read()

		cv2.imshow("Photo App",frame)


		key = cv2.waitKey(1) & 0xFF

		if(key==ord('s')):

			print("Image Saved")
			count += 1
			name = "HK" + str(count) + ".jpg"
			cv2.imwrite(name,frame)

		elif(key==ord('q')):
			break
	
	obj.release()
	cv2.destroyAllWindows()

main()