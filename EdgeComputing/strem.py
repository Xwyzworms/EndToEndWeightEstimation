#%%
import cv2,imutils

vid = cv2.VideoCapture(0)
while True:
	img, frame = vid.read()
	frame = imutils.resize(frame, width=400) #Resizing Frame
	
	cv2.imshow("Transmitting Video", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		client_socket.close()
		break
# %%
